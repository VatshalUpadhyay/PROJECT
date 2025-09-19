# gemini_client.py

from google import genai

# Initialize the Gemini client with your API key
# Replace 'YOUR_API_KEY' with your actual API key
client = genai.Client(api_key="YOUR_API_KEY")

def ask_gemini(prompt: str) -> str:
    """
    Sends a prompt to Gemini API and returns the response text.

    Args:
        prompt (str): The question or prompt to send to Gemini

    Returns:
        str: The response text from the model
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error contacting Gemini API: {e}"

