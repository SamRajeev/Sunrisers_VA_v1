import webbrowser
from PyDictionary import PyDictionary
import wikipedia
from urllib.request import urlopen as ureq
import re
import pyttsx3
import speech_recognition as sr

try:
    from googlesearch import search
except ImportError:
    print('No google')

dictionary = PyDictionary()
result = "Sorry No results"
webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

query = input("Enter your query:")
query2 = query.split(" ")
try:
    final_query = query2.index("of") + 1
except:
    pass

def speak(text):
    engine = pyttsx3.init()
    vid="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', vid)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 60)
    engine.say(text)
    engine.runAndWait()


def find_synonym():
    try:
        result = dictionary.synonym(query2[final_query])
        speak("Synonym of" + query2[final_query] + "is" + result[0] + result[1] + result[2])
    except:
        result = "Sorry No results"
        speak(result)


def find_meaning():
    try:
        result = dictionary.meaning(query2[final_query])
        speak("Meaning of" + query2[final_query] +"is" + result)
    except:
        result = "Sorry No results"
        speak(result)


def find_antonym():
    try:
        result = dictionary.antonym(query2[final_query])
        speak("Antonym of" + query2[final_query] +"is" + result[0] + result[1] + result[2])
    except:
        result = "Sorry No results"
        speak(result)


def wikipedia_fuction():
    try:
        query_final = query.replace('wikipedia search ','')
        #query_final = query_final.replace('is', '')
        result = wikipedia.summary(query_final, sentences=1)
        speak(result)
    except:
        result = "Sorry No results"
        speak(result)


def music():
    query3 = query.replace("play ", '')
    query3 = query3.replace(' ', '+')
    url = "https://www.youtube.com/results?search_query=" + query3

    uClient = ureq(url)
    page_data = uClient.read().decode()
    uClient.close()

    video_ids = re.findall(r"watch\?v=(\S{11})", page_data)
    final_url = "https://www.youtube.com/watch?v=" + video_ids[0]
    speak("Playing"+query3+"from youtube")
    webbrowser.get('chrome').open(final_url)


def open_site():
    query2 = query.replace('open ', '')
    for result in search(query2, tld='com', lang='en', num=1, stop=1, pause=2.0):
        speak("Opening" + query2)
        webbrowser.get('chrome').open(result)


def google_search():
    for result in search(query, tld='com', lang='en', num=1, stop=1, pause=2.0):
        speak("Opening site...")
        webbrowser.get('chrome').open(result)


if "synonym" in query2:
    find_synonym()

elif "meaning" in query2:
    find_meaning()

elif "antonym" in query2:
    find_antonym()

elif "wikipedia search" in query:
    wikipedia_fuction()

elif "play" in query:
    music()

elif "open" in query:
    open_site()

else:
    google_search()
