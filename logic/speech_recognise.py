import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust mic sensitivity
            print("Listening now... Speak something!")

            audio = recognizer.listen(source, timeout=5)  # Waits 5 seconds max
            print("Processing your voice...")
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text

    except sr.RequestError:
        print("Error: Could not connect to Google API. Check your internet.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None  # Return None if an error occurs

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Run the function
command = listen()
if command:
    speak("Hi")
else:
    print("No voice input detected.")

# Run the function
command = listen()
if command:
    speak("If am also very happy. By the way, you are looking so handsome today!")
else:
    print("No voice input detected.")