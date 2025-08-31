import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
from google import genai


newsapi = "API KEY"  # Replace with your NewsAPI key

r=sr.Recognizer()
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    


# Initialize Gemini client with your API key
client = genai.Client(api_key="API_Key") # Replace with your Gemini API key

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



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
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
        output = aiProcess(c)
        speak(output) 



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("Heard:", word)
            if "jarvis" in word.lower():
                speak("Ya, I am here")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
