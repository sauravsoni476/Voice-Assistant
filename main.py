import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from random import shuffle
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
#engine.say("I am your Basanti")
#engine.say("What can I do for you")
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "basanti" in command:
                command = command.replace('basanti', '')
                print(command)
    except:
        pass
    return command

def run_basanti():
    flag = 'bye bye'
    while flag:
        command = take_command()
        print(command)
        if "play" in command:
            song = command.replace('play','')
            talk("playing" + song)
            pywhatkit.playonyt(song)
        elif 'open google' in command:
            talk('opening google')
            webbrowser.open('www.google.com')
        elif 'open instagram' in command:
            talk('yeah opening instagram')
            webbrowser.open('www.instagram.com')
        elif 'open whatsapp' in command:
            talk('opening whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        elif 'open flipkart' in command:
            talk('opning Flipkart')
            webbrowser.open("https://www.flipkart.com/")
        elif 'open amazon' in command:
            talk('opning amazon')
            webbrowser.open("https://www.amazon.in/")
        elif 'time' in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            talk('Current Time is'+time)
        elif 'find' in command:
            peron = command.replace('what', '')
            info = wikipedia.summary(peron,1)
            print(info)
            talk(info)
        elif 'date' in command:
            print('Sorry I have a headache')
            talk('Sorry I have a headache')
        elif 'are you single' in command:
            talk('I am in a relation')
        elif 'who are you' in command:
            talk('Hello \n I am basanti \n developed by Saurav soni\n How can i help you' )
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'Hello' in command:
            talk('Hello sir How can i help you')
        elif 'jor se bolo' in command:
            talk('jai  maataa  di ')
        elif 'i love you' in command:
            talk("I am a machine\n i don't have any feelings")
        elif 'chalti hai kya' in command:
            talk('apni shakal dekhi hai\nchichora kahi ka')
        elif 'how are you' in command:
            lists = ['Hello i am good\nand you?',"i am good \n tell me how can i help you","i am good \n i am waiting your command"]
            shuffle(lists)
            list1 = lists[0]
            talk(list1)
        elif 'bye bye' in command:
            talk('thank you \n bye bye')
            flag = False
        elif 'i am good' or 'i am also good' in command:
            talk('Great\n so how can i help you')
        else:
            talk('please say the command again')
run_basanti()