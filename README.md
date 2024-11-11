# 🤠 The Saloon Bot

A Discord bot that transforms your server channel into an old-timey Western saloon. Every user gets their own persistent Wild West character, and all messages are automatically transformed into period-appropriate saloon talk using Claude AI.

## Features

- 🎭 **Automatic Character Creation**: Each user gets a unique Wild West persona generated just for them
- 🗣️ **Message Transformation**: All messages are automatically transformed into saloon-appropriate speech
- 🎪 **Persistent Characters**: Users keep their saloon character across messages
- 🎯 **Channel-Specific**: Only operates in the designated saloon channel

## Setup

### Prerequisites

- Python 3.11+
- A Discord bot token
- An Anthropic API key

### Installation

1. Clone the repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
export SALOON_BOT='your-discord-bot-token'
export ANTHROPIC_API_KEY='your-anthropic-api-key'
```
On Windows, use `set` instead of `export`.

### Configuration

1. Create a Discord bot in the [Discord Developer Portal](https://discord.com/developers/applications)
2. Enable the "Message Content Intent" in your bot's settings
3. Invite the bot to your server with appropriate permissions (read messages, send messages, manage messages)
4. Update the `CAPS_CHANNEL_ID` in bot.py with your desired saloon channel ID

## Running the Bot

```bash
python saloon_bot.py
```

## Commands

- `!setcapschannel` - (Admin only) Sets the current channel as the saloon

## Example

Original message:
> "Hey everyone, I'm new here!"

Transformed message:
> **Wild-Eyed Wyatt:** Gather 'round, folks! Just rode into this here saloon with tales that'd curl yer whiskers!

## License

MIT

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- Built with Discord.py and Claude AI
- Inspired by the classic Western saloons of yore