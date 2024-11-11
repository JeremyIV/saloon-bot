import discord
from discord.ext import commands
import os
from saloon_talk import to_saloon_talk

# Check if the environment variable exists
TOKEN = os.getenv('SALOON_BOT')
if TOKEN is None:
    raise ValueError("Please set the SALOON_BOT environment variable with your bot token!")

# Set up the bot with necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
bot = commands.Bot(command_prefix='!', intents=intents)

# The channel ID for the-saloon
CAPS_CHANNEL_ID = 1305323906017792091  # The Saloon channel ID

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Ready to transform messages in the saloon!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
        
    # Only process messages in the designated channel
    if message.channel.id == CAPS_CHANNEL_ID:
        try:
            # Store the original message content and author
            original_content = message.content
            author_name = message.author.display_name
            
            # Transform the message using Claude
            transformed_message = to_saloon_talk(author_name, original_content)
            
            # Delete the original message and send the new one
            await message.delete()
            await message.channel.send(transformed_message)
            
        except Exception as e:
            print(f"Error processing message: {e}")
            # If there's an error, we could either:
            # 1. Leave the original message (by removing the delete() call)
            # 2. Send an error message to the channel
            await message.channel.send(f"*Pardner, seems like we hit a snag transformin' that message!*")
    
    # Process commands if any
    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)