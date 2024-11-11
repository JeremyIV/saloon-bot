import os
import anthropic
from anthropic import Anthropic
from saloon_characters import get_or_create_character

def to_saloon_talk(username: str, comment: str) -> str:
    # Get API key from environment
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("Please set ANTHROPIC_API_KEY environment variable")
    
    # Get or create character for this user
    character_name, character_desc = get_or_create_character(username)
    
    # Initialize Anthropic client
    client = Anthropic(api_key=api_key)
    
    # Craft the prompt
    prompt = f"""Transform this message into Wild West saloon speech for a specific character.

    Character: {character_name}
    Character Description: {character_desc}
    
    Original message: {comment}
    
    Rules:
    - KEEP THE RESPONSE SIMILAR IN LENGTH TO THE ORIGINAL.
    - The transformed message should not be more than 50% longer than the original.
    - Match the character's personality as described
    - Use at most one Western interjection
    - Focus on the message's meaning first, character's style second
    - No need for action descriptions
    - Don't include the character name in the response
    
    Respond with ONLY the transformed message."""
    
    # Call Claude
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    # Extract the text and prepend the character name
    transformed_text = message.content[0].text
    return f"**{character_name}:** {transformed_text}"

# Example usage
if __name__ == "__main__":
    # Test the function
    test_message = "Hey everyone, I'm going to get some lunch. Anyone want to join?"
    result = to_saloon_talk("JohnDoe", test_message)
    print(result)