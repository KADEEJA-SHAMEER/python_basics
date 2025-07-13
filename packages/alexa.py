import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser
import pyaudio

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.runAndWait()

def talk(text):
        engine.say(text)
        engine.runAndWait()
def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command=command.replace("alexa"," ")
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
    except Exception as e:
        print("Other error:", e)
    return command

def run_alexa():
    command = take_command()
    if command is None:
        talk("Please say the command again.")
        return

    print("Command:", command)

    if 'play' in command:
        song = command.replace('play', "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is " + time)
        print(time)

    elif 'who is' in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'send message' in command:
        talk("To whom should I send the message?")
        name = take_command()

        talk("What should I say?")
        message = take_command()

        # Replace with your contacts and numbers
        contact_dict = {
            "mom": "+918129030978",
            "dad": "+918129853093"
        }
        phone_number = contact_dict.get(name)
        if phone_number:
            # Sends message 1 minute from now
            import datetime
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute + 1

            talk(f"Sending message to {name}")
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        else:
            talk("Sorry, I don't have that contact.")

    elif 'open youtube' in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'search youtube for' in command:
        search_query = command.replace("search youtube for", "")
        talk(f"Searching YouTube for {search_query}")
        pywhatkit.playonyt(search_query)

    elif 'hello' in command:
        talk("hi .how can i help you")

    elif 'bye' in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Please say the command again.")


while True:
    run_alexa()