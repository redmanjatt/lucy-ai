import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lucy' in command:
                command = command.replace('lucy', '')
                print(command)
    except:
        pass
    return command


def run_lucy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'who created you' in command:
        talk('master uday duhoon created me')
    elif 'good morning' in command:
        talk('good morning master')
    elif 'hello' in command:
        talk('hello sir what would you like me to play?')
    elif 'who are you' in command:
        talk('i am lucy created by uday duhoon and i am a dog i lived for 12 years')
    elif 'sup' in command:
        talk('sup whats going on wanna play something')    
    elif 'who do you serve' in command:
        talk('i serve master uday mistress urvee duhoon and master nirbahy and i listen mostly to these three but also listen sometimes to mistress prakshi')    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('sorry master i did not get that would you kindly repeat it')


while True:
    run_lucy()
