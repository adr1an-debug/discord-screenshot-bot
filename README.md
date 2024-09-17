# Discord Screenshot Bot
![image](https://github.com/user-attachments/assets/f0d2e401-3b8d-4906-aad4-07b6ce8bbb66)

This Python script is a Discord bot that captures a screenshot of your screen and sends it to a specified Discord channel.

## Requirements

- Python 3.7+
- `discord.py`
- `pyautogui`

To install the required packages, use the following command:

```bash
pip install discord.py pyautogui
```

## Configuration

1. Replace the placeholders in the script with your Discord bot token and the target channel ID.
```
discord_token = 'YOUR_DISCORD_BOT_TOKEN'
channel_id = YOUR_DISCORD_CHANNEL_ID
```

2. Save the script as `discord_screenshot_bot.py.`

## Usage

`python discord_screenshot_bot.py`

The bot will:

1. Log in to Discord.
2. Capture a screenshot of your screen.
3. Send the screenshot to the specified Discord channel.
4. Delete the screenshot from your local machine.
5. Shut down the bot.

## License
This project is licensed under the MIT License.
