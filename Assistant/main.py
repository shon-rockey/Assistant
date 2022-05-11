import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source, None, 10)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mercury' in command:
                command = command.replace('mercury', '')
                print(command)
    except:
        pass
    return command


def run_mercury():
    command1 = take_command()
    print(command1)
    if 'play' in command1:
        song = command1.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif ('are you single' in command1) or ('do you have boyfriend' in command1):
        talk("yes")
    elif 'hello ' in command1:
        talk("Hey")
    elif 'who are you' in command1:
        talk("I am a personal assistant")
    elif 'time' in command1:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is " + time)
    elif ('who is ' in command1) or ('what is ' in command1):
        person = command1.replace("who is ", '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'theory' in command1:
        theory = command1.replace('theory', '')
        inf = wikipedia.summary(theory, 1)
        print(inf)
        talk(inf)
    elif ' movie' in command1:
        movie = command1.replace(' movie', '')
        msg = wikipedia.summary(movie, 1)
        print(msg)
        talk(msg)
    elif 'tell me a joke' in command1:
        jokes = pyjokes.get_jokes(language='en', category='chuck')
        print(jokes)
        talk(jokes)
    elif 'open notepad' in command1:
        tgd = subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        talk("opening note pad")
        talk(tgd)
    elif ('open telegram' in command1) or ('telegram' in command1):
        tg = subprocess.Popen("C:\\Users\\ACER\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        talk(tg)
    elif 'open file explorer' in command1:
        fe = subprocess.Popen("C:\\Windows\\explorer.exe")
        talk('opening file explorer')
        talk(fe)
    elif 'open videos' in command1:
        vi = subprocess.Popen(["C:\\Windows\\explorer.exe", "E:\\Videos"])
        talk(vi)

    elif 'youtube' in command1:
        yt = subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "www.youtube.com"])
        talk('opening youtube')
        talk(yt)
    elif 'open google chrome' in command1:
        glc = subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        talk('opening google chrome')
        talk(glc)


    else:
        talk("Please say the command again")


while True:
    try:
        run_mercury()
    except UnboundLocalError:
        print("no command detected! Mercury has stopped working")
        break
