import os
from anthropic import Anthropic
from typing import Dict, Tuple

# In-memory storage of characters
character_store: Dict[str, Tuple[str, str]] = {}

def make_character(username: str) -> Tuple[str, str]:
    """Generate a Wild West character based on a username."""
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("Please set ANTHROPIC_API_KEY environment variable")
    
    client = Anthropic(api_key=api_key)
    
    prompt = f"""Create a colorful Wild West saloon character inspired by the username: {username}

    Rules for the character:
    - Should have a memorable, era-appropriate nickname
    - Can optionally incorporate elements from the username if it fits naturally
    - Should be the kind of character you'd find in a saloon
    - Create a brief description focusing on their personality and role in the saloon
    
    Respond in this exact format (no other text):
    NAME: [character name]
    DESC: [one-sentence character description]"""
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        temperature=1.0,  # High temperature for creative names
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    # Parse the response
    response = message.content[0].text
    name_line = [line for line in response.split('\n') if line.startswith('NAME:')][0]
    desc_line = [line for line in response.split('\n') if line.startswith('DESC:')][0]
    
    character_name = name_line.replace('NAME:', '').strip()
    character_desc = desc_line.replace('DESC:', '').strip()
    
    return character_name, character_desc

def get_or_create_character(username: str) -> Tuple[str, str]:
    """Get existing character or create new one for username."""
    if username not in character_store:
        character_store[username] = make_character(username)
    return character_store[username]

# For debugging/testing
if __name__ == "__main__":
    test_usernames = ["CowboyJohn", "DragonSlayer99", "Alice_Wonder"]
    for username in test_usernames:
        name, desc = make_character(username)
        print(f"\nUsername: {username}")
        print(f"Character: {name}")
        print(f"Description: {desc}")