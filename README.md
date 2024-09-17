# ClipCraft

ClipCraft is an automated bot designed to take longer videos, cut them into short clips, and upload the results. It simplifies the process of creating and sharing bite-sized video content, and can also be accesed via Discord.
Features

    Video Splitting: Automatically splits longer videos into shorter clips.
    Custom Clip Length: Specify the duration of each clip.
    Discord Upload: Automatically uploads the generated clips.

Requirements

    Python 3.x
    moviepy for video processing
    discord.py for Discord integration

Installation

    Clone the Repository

    bash

git clone https://github.com/yourusername/clipcraft-bot.git
cd clipcraft-bot

Install Required Packages

bash

    pip install moviepy discord.py

    Set Up Discord Bot
        Create a new bot on the Discord Developer Portal.
        Copy the bot token and add it to the config.py file or specify it directly in the script.

    Configure the Bot
        Update the config.py file with your Discord bot token and other settings like the target Discord channel ID.

Usage

    Run the Bot

    bash

python clipcraft.py

Use Commands in Discord

    Once the bot is running, you can use commands in your Discord server to process and upload videos.
    Example command:

    css

        !clip video.mp4 30

        This command will split video.mp4 into 30-second clips and upload them to the configured channel.

Configuration
config.py

Create a config.py file to store your bot's configuration. For example:

python

# config.py
DISCORD_TOKEN = 'your-discord-bot-token'
CHANNEL_ID = 123456789012345678  # Replace with your target Discord channel ID

Commands

    !clip <video_path> <clip_duration>: Splits the video into clips of the specified duration and uploads them to the target Discord channel.
        video_path: Path to the video file to be processed.
        clip_duration: Duration of each clip in seconds.

Example

    Upload the video file to a specific location accessible by the bot.
    Use the !clip command in the Discord channel where the bot is present:

    css

    !clip /path/to/video.mp4 30

    The bot will split the video into 30-second clips and upload them to the configured Discord channel.

Notes

    Ensure the bot has the necessary permissions to upload files to the target Discord channel.
    Video files must be accessible to the bot; they can be stored locally or in a shared directory.