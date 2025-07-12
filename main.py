import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import musicLibrary
import requests
import os
import google.generativeai as genai

# Set your API key
os.environ["YOUR_GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"
genai.configure(api_key=os.environ["YOUR_GEMINI_API_KEY"])



def ask_gemini(prompt_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content([prompt_text])
        print(f"[Gemini raw response]: {response}")
        return response.text
    except Exception as e:
        print(f"[Gemini error] {e}")
        return "Sorry, I couldn't get an answer right now."


recognizer = sr.Recognizer()
# newsapi = "YOUR_NEWSAPI_KEY_HERE"  # Replace with your actual NewsAPI key


def speak(text):
    print(f"[Speaking]: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen(timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        audio = recognizer.listen(
            source, timeout=timeout, phrase_time_limit=phrase_time_limit
        )
    return recognizer.recognize_google(audio)


def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif command.startswith("play"):
        song = command[5:].strip().lower()
        print(f"Looking for song: '{song}'")
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't know the song {song}.")
    elif "news" in command.lower():
        speak("Fetching the latest news headlines for you.")
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={"newsapi"}"
        )

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            headlines = [article["title"] for article in articles[:5]]
            news_summary = "Here are the top 5 headlines. " + ". ".join(headlines)
            speak(news_summary)
        else:
            speak("Sorry, I couldn't fetch the news right now.")

        return

    else:
        speak("Let me think about that...")
        ai_reply = ask_gemini(command)
        speak(ai_reply)


if __name__ == "__main__":
    speak("Initializing Phoenix")
    print("Listening...")  # Only once at start!

    while True:
        try:
            heard = listen(timeout=5, phrase_time_limit=3)
            print(f"Heard: {heard}")

            if "phoenix" in heard.lower():
                speak("Phoenix Unleashed...")
                print("Phoenix Active...")

                while True:
                    try:
                        command = listen()
                        print(f"Command: {command}")

                        if (
                            "stop" in command.lower()
                            or "sleep" in command.lower()
                            or "bye" in command.lower()
                        ):
                            speak("Okay, shutting down. Goodbye.")
                            exit()  # or use sys.exit() if you prefer

                        processCommand(command)

                    except sr.WaitTimeoutError:
                        print("Timeout in active mode: Nothing heard.")
                    except sr.UnknownValueError:
                        print("Could not understand command.")
                    except Exception as e:
                        print(f"Error in active mode: {e}")

        except sr.WaitTimeoutError:
            print("Timeout: Nothing heard.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except Exception as e:
            print(f"Error: {e}")
