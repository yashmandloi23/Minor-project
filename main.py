# Import required libraries
import speech_recognition as sr
import os
import webbrowser
import datetime
import google.generativeai as genai  # Replace openai with google.generativeai

# Set up Gemini API
GEMINI_API_KEY = "your-gemini-api-key-here"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')  # Use Gemini Pro model

def say(text):
    os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry, I couldn't understand what you said."

# Function to use Gemini API instead of OpenAI
def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return "I encountered an error while processing your request."

if __name__ == '__main__':
    print('Welcome to Jarvis AI')
    say("Hello, I am Jarvis AI. How can I help you today?")
    
    while True:
        print("Listening...")
        query = takeCommand()
        
        # Basic commands can be handled directly
        if "open youtube" in query.lower():
            say("Opening YouTube")
            webbrowser.open("https://youtube.com")
        elif "open google" in query.lower():
            say("Opening Google")
            webbrowser.open("https://google.com")
        elif "what's the time" in query.lower() or "what is the time" in query.lower():
            time = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {time}")
        elif "exit" in query.lower() or "quit" in query.lower():
            say("Goodbye!")
            break
        # For all other queries, use Gemini AI
        else:
            response = generate_response(query)
            print(response)
            say(response)