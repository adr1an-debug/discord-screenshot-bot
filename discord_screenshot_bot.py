import discord
from discord.ext import commands
import pyautogui
import os

# Define intents
intents = discord.Intents.default()
intents.typing = False  # Disable typing event to reduce unnecessary events

# Discord bot setup
bot = commands.Bot(command_prefix='!', intents=intents)
discord_token = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot token
channel_id = YOUR_DISCORD_CHANNEL_ID  # Replace with your Discord channel ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    try:
        # Capture a screenshot
        screenshot_file = "screenshot.png"
        pyautogui.screenshot(screenshot_file)

        # Send the screenshot to the Discord channel
        await send_screenshot(channel_id, screenshot_file)

        # Remove the screenshot from the computer
        os.remove(screenshot_file)

    except Exception as e:
        print("An error occurred:", e)

    # Close the Discord bot connection and HTTP connection
    await bot.close()

async def send_screenshot(channel_id, file_path):
    try:
        # Log in to Discord
        bot_channel = bot.get_channel(channel_id)

        # If the channel is found
        if bot_channel:
            await bot_channel.send(file=discord.File(file_path))
        else:
            print("Channel not found.")
    except Exception as e:
        print("An error occurred while sending the screenshot:", e)

@bot.event
async def on_shutdown():
    print("Shutting down...")
    await bot.http.close()  # Close the HTTP connection

# Run the Discord bot
bot.run(discord_token)
