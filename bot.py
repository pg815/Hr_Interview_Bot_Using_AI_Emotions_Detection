import speech_recognition as sr  # importing speech recognition package from google api
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
from chatterbot import ChatBot
from db import Database
from testbot import get_comment
from kerasmodel import predict
from multiprocessing import Process



class Bot:

    def __init__(self):
        self.num = 1
        self.chatbot = ChatBot('MyBot')
        self.dbObj = Database()

    def bot_speaks(self,output):
        self.num += 1
        print("Bot : ", output)
        toSpeak = gTTS(text=output, lang='en-US', slow=False)
        file = str(self.num) + ".mp3"
        toSpeak.save(file)
        playsound.playsound(file, True)
        os.remove(file)

    def get_audio(self):
        r = sr.Recognizer()
        audio = ''
        with sr.Microphone() as source:
            print("Speak...")
            audio = r.listen(source, phrase_time_limit=5)
        print("Stop.")
        try:
            text = r.recognize_google(audio, language='en-US')
            print("You : ", text)
            return text
        except:
            return "None"


def ask_question():
   botObj = Bot()
   botObj.bot_speaks("Welcome to HR Interview . Please seat right back infront of your webcam.")
   botObj.bot_speaks("So lets get started.")

   Questions = botObj.dbObj.fetch_hr_questions()
   for Question in Questions:
        botObj.bot_speaks(Question[0])
        while botObj.get_audio() == "None":
            botObj.bot_speaks("Could not understand your audio, Please answer again!")
        botObj.bot_speaks(get_comment(Question[0]))
   botObj.bot_speaks("Please press q key to end interview and get your feedback")


if __name__ == "__main__":

    p1 = Process(target=ask_question)
    p1.start()
    #p2 = Process(target=predict)
    #p2.start()
    p1.join()
    #p2.join()



