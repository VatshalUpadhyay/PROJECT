import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
from google import genai
import sys, logging

newsapi = "API KEY"  # Replace with your NewsAPI key

r=sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen(timeout=None, phrase_time_limit=None):
    """Listen and return recognized text, returns empty string if not recognized."""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.energy_threshold = 300
        r.dynamic_energy_threshold = False
        print("Listening...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            command = r.recognize_google(audio, language="en-in")
            print("User said:", command)
            return command.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            speak(f"Network error: {e}")
            return ""

# Initialize Gemini client with your API key
client = genai.Client(api_key="API KEY") # Replace with your Gemini API key

def aiProcess(command: str) -> str:
    """
    Sends a command to Gemini API and returns the response text.
    
    Args:
        command (str): The user query or instruction.
        
    Returns:
        str: The response from the Gemini model.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=command
        )
        return response.text
    except Exception as e:
        return f"Error contacting Gemini API: {e}"



def processCommand(command):
        
    if "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")

    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("This song is not in your playlist.")

    elif "Search" in command.lower() or "search" in command.lower():
        speak("What you looking for")    
        topic = listen()                                            # topic input
        webbrowser.open(f"https://www.google.com/search?q={topic}")
        speak(f"Here is what I found for {topic}")


    elif "exit" in command or "quit" in command or "stop listening" in command:
        speak("Going offline. Goodbye!")
        sys.exit(0)


    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
             # Extract the articles
            articles = data.get('articles', [])
            if not articles:
                speak("Sorry, I could not find any news at the moment.")
            else:
             for article in articles:  # Limit to 5 headlines
                speak(article['title'])
                time.sleep(0.5)
    
    else:
        # Let Gemini handle the request
        output = aiProcess(command)
        speak(output) 



def main():
    speak("Activating Jarvis...")

    while True:
        # ---- WAKE WORD MODE ----
        print("Listening for wake word...")
        word = listen(timeout=None, phrase_time_limit=None)  # Wait indefinitely
        if "jarvis" in word:  # accepts both names
            speak("Yes, I am here.")
            
            # ---- ACTIVE MODE ----
            while True:
                command = listen(timeout=None, phrase_time_limit=None)
                if command:
                    processCommand(command)

if __name__ == "__main__":
    main()
