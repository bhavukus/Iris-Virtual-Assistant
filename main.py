import speech_recognition as sr  # Importing the speech recognition module
import webbrowser  # Importing the webbrowser module to open web pages
import pyttsx3  # Importing the text-to-speech conversion module
import myMusic  # Importing a custom music module for song links
import requests  # Importing the requests module to make HTTP requests
import os  # Importing the os module to access environment variables

# Initialize the recognizer and speech engine
recognizer = sr.Recognizer() #created an object for the Recognizer class using the module sr
engine = pyttsx3.init() #Initializing the speech engine for tts conversion
newsapi = os.getenv("NEWS_API_KEY") # Fetching the NewsAPI key from environment variables  

# Function to process voice commands and perform actions
def processCommand(c):
    
    c = c.lower() # Convert the command to lowercase for consistency

    # Open popular websites based on voice commands
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open gmail" in c:
        webbrowser.open("https://gmail.com")

    # Play a song from the custom music library
    elif c.startswith("play"):
        song = c.split(" ")[1] # Extract the song name from the command. for example if the command is ["play", "naina"] then it will take the element from index 1 which is naina.
        link = myMusic.music[song] # Fetch the song link from the myMusic module
        if link:
            webbrowser.open(link) # Open the song link in the web browser
        else:
            speak(f"Sorry, {song} is currently not available in the library.")
        
    # Fetch and read the latest news headlines
    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()  # Parse the JSON response

            articles = data.get('articles', []) # Get the list of news articles
            for article in articles:
                speak(article['title']) # Speak the title of each article

    elif "stop listening" in c.lower():
        speak("Deactivating Iris.")
        return False  # Return False to stop the loop
    
    return True #Return True to continue listening

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait() #to wait until the text is spoken before moving ahead


# Main function to activate the virtual assistant and listen for commands
if __name__ == "__main__":
    speak("Activating Iris..") # Announce the activation of the assistant

    listening = True  # Initialize listening state

    while listening:

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source: # Use the microphone as the audio source
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) # Listen for audio input

            word = r.recognize_google(audio) # Recognize speech using Google's API
            if(word.lower() == "iris"): # Check if VA's name is taken or wake word is spoken
                speak("Yaa bro tell me?")
            with sr.Microphone() as source:
                print("Iris Activated!")
                audio = r.listen(source) # Listen for the command after activation
                command = r.recognize_google(audio) # Recognize the spoken command

                processCommand(command) # Process the recognized command
                listening = processCommand(command)  # Update listening state based on command

        except Exception as e:
            print("Error; {0}".format(e)) # Print any errors that occur during execution