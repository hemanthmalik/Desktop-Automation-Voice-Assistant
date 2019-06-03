import pyttsx3
import Feedback
import datetime


class Speaker:
    def speak(self, audio):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        # print(voices[0].id)
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

    def wishMe(self):
        obj1 = Feedback.Speaker()
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            obj1.speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            obj1.speak("Good Afternoon!")

        else:
            obj1.speak("Good Evening!")

        obj1.speak("I am David, Please tell me how may I help you")

