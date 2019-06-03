import Feedback
import SpeechAnalysis
import wikipedia
import os
import SystemAutomation
import wolframalpha
import random
import webbrowser


class Test:
    client = wolframalpha.Client('634LX2-LYYPLU7W44')

    if __name__ == "__main__":
        obj = SpeechAnalysis.SpeechInput()
        obj1 = Feedback.Speaker()
        objf = SystemAutomation.AutomateBrowser()
        obj1.wishMe()

        while True:
            query = obj.takecommand().lower()
            if query == "None":
                continue
            # print(query)
            # obj1.speak(query)
            if "goodbye" in query:
                obj1.speak("Have a nice day, Sir!")
                break

            elif "wikipedia" in query:
                obj1.speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                obj1.speak("According to Wikipedia")
                print(results)
                obj1.speak(results)

            elif "open file browser" in query:
                filePath = "C:\\Users\\HemantMalik"
                os.startfile(filePath)

            elif "open torrent" in query:
                filepath = "C:\\Program Files\\qBittorrent\\qbittorrent.exe"
                os.startfile(filepath)

            elif 'send email' in query:
                try:
                    obj1.speak("What should I say?")
                    content = obj.takecommand()
                    to = query.split(" ")
                    to = to[-1]
                    objf = SystemAutomation.AutomateBrowser(to, content)
                    objf.sendEmail()
                    obj1.speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    obj1.speak("Sorry Sir, I am not able to send this email")

            elif "open google" in query or "open Chrome" in query:
                webbrowser.open("google.com")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif "open website" in query or "open a website" in query:
                obj1.speak("Which website would you like to open?")
                website = obj.takecommand()
                if website != "None":
                    webbrowser.open(website+".com")

                else:
                    obj1.speak("Website unrecognizable, Please enter a valid website.")

            elif "login to my facebook" in query:
                obj1.speak("Please, tell me your secret passkey.")
                passkey = obj.takecommand().lower()
                if "1234" in passkey:
                    try:
                        objf.facebookLogin()
                    except:
                        obj1.speak("Login Failed, Please try again.")
                else:
                    obj1.speak("Invalid Passkey entered please try again!")

            elif "send whatsapp message" in query:
                obj1.speak("To whom do you want to send message?")
                to = obj.takecommand()
                # print(to)
                if to != "None":
                    obj1.speak("What should i say?")
                    message = obj.takecommand()
                    # print(message)
                    if message != "None":
                        objf = SystemAutomation.AutomateBrowser(to, message)
                        objf.whatsappMess()
                    else:
                        obj1.speak("Sorry Sir!, I am unable to send an empty message.")
                else:
                    obj1.speak("Unable to identify receiver.")

            elif "who are you" in query or "what is your name" in query:
                obj1.speak("I am David, Your Desktop voice assistant")

            elif "watch movie" in query or "play movie" in query or "open movie" in query or "start movie" in query:
                filepath = r"D:\\The Shawshank Redemption (1994) 720p BrRip x264 [Dual Audio] [Hindi-English].mkv"
                os.startfile(filepath)

            elif 'play music' in query or "open music" in query or "listen music" in query or "start music" in query:
                music_dir = r'D:\Hemant\Enrique Iglesias Discography (iTunes-Rip) [theLEAK]\Studio Albums\7 (UK Version)'
                songs = os.listdir(music_dir)
                # print(songs, sep="\n")
                song = random.randrange(16)
                os.startfile(os.path.join(music_dir, songs[song]))

            elif "google search" in query or "search google" in query or "search on google" in query:
                obj1.speak("What do you want me to search.")
                searchcontent = obj.takecommand()
                objf = SystemAutomation.AutomateBrowser("", searchcontent)
                try:
                    objf.googlesearch()
                except:
                    obj1.speak("Unable to proceed with google search. Sir!")

            elif "youtube search" in query or "search youtube" in query or "search on youtube" in query:
                obj1.speak("What do you want me to search.")
                searchcontent = obj.takecommand()
                objf = SystemAutomation.AutomateBrowser("", searchcontent)
                try:
                    objf.youtubesearch()
                except:
                    obj1.speak("Unable to proceed with Youtube search, Sir!")

            else:
                try:
                    if query != "none":
                        # print(query)
                        res = client.query(query)
                        output = next(res.results).text
                        print(output)
                        obj1.speak(output)
                except:
                    obj1.speak("Sorry, I am unable to answer this question, Sir! Do You want me to search it on google")
                    dosearch = obj.takecommand()
                    if "yes" in dosearch:
                        objf = SystemAutomation.AutomateBrowser("", query)
                        objf.googlesearch()

