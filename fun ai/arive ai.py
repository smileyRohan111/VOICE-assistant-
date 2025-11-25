# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am arive Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohantanty200@gmail.com', 'your-password')
    server.sendmail('rohantanty200@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")
            
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            
        elif 'open valorent' in query:
            webbrowser.open("valorent.com")
        
        elif 'open fortnite' in query:
            webbrowser.open("fortnite.com")
            
        elif 'open replit' in query:
            webbrowser.open("replit.com")
            
        elif 'cancel browser' in query:
            speak("Closing all browser windows.")
            os.system("taskkill /im chrome.exe /f")
            os.system("taskkill /im msedge.exe /f")
            os.system("taskkill /im firefox.exe /f")
            webbrowser.open("gmail.com")
            
        elif 'open notepad' in query:
            notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(notepadPath)
            
        elif 'open command prompt' in query:
            os.system("start cmd")
            
        elif 'open camera' in query:
            os.system("start microsoft.windows.camera:")
            
        elif 'take a screenshot' in query:
            speak("Taking a screenshot")
            os.system("start snippingtool.exe")
            
        elif 'open vlc' in query:
            vlcPath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPath)
            
        elif 'open file explorer' in query:
            os.startfile("explorer")
            
        elif 'open control panel' in query:
            os.system("start control panel")
            
        elif 'open settings' in query:
            os.system("start ms-settings:")
            
        elif 'open task manager' in query:
            os.system("start taskmgr")
            
        elif 'open paint' in query:
            os.system("start mspaint")
        elif 'open calculator' in query:
            os.system("start calc")
            
        elif 'open word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)
            
        elif 'open excel' in query:
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excelPath)
            
        elif 'open power point' in query:
            powerPointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(powerPointPath)
        
        elif 'open pdf' in query:
            pdfPath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(pdfPath)
        
        # elif 'open vs code' in query:
        #     codePath = "C:\Users\subha\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        #     os.startfile(codePath)
            
        elif 'open telegram' in query:
            telegramPath = "C:\\Users\\\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telegramPath)
        
        elif 'open discord' in query:
            discordPath = "C:\\Users\\Haris\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe"
            os.startfile(discordPath)
            
        
        elif'open vmware' in query:
            vmwarePath = "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"
            os.startfile(vmwarePath)
            
        elif'open chrome'in query:
            chromepath ="C:\Program Files\Google\Chrome\Application"
            os.startfile(chromepath)
            
         
        elif 'open music' in query:
            music_dir = '/home/haris/Music'
            # music_dir = ''
            try:
                songs = os.listdir(music_dir)
            except FileNotFoundError:
                speak("Sorry, I couldn't find the music directory. Please check the path.")
                print("Error: Music directory not found.")
                continue
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\--\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to rohan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rohantanty@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry rohan  bhai  I am not able to send this email")  
            else:
                speak("Sorry, I didn't understand that. Could you please repeat?") 
                print("Sorry, I didn't understand that. Could you please repeat?")
     
        if 'exit' in query:
            speak("Goodbye! Have a great day!")
            break
              
           