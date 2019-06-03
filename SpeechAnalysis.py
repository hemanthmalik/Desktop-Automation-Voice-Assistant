import speech_recognition as sr


class SpeechInput:
    def takecommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 5000
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            # print()
            query = "None"
            print("Say that again please...")
            return query
        return query
