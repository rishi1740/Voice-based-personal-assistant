import psutil,wikipedia
import subprocess,os,webbrowser
from time import ctime
import speech,platform,nltk


def speak(string):
    speech.speak(string)
def recordAudio():
    data=speech.recordAudio()
    return data
def read(string):
    speech.read(string)
def write():
    data=speech.write()
    return data

def cpustatus():
    os, name, version, _, _, _ = platform.uname()
    version = version.split('-')[0]
    cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory()[2]
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    response = "I am currently running on %s version %s. " % (os, version)
    response += "This system is named %s and has %s CPU cores. " \
        % (name, cores)
    response += "Current CPU utilization is %s percent. " % cpu_percent
    response += "Current memory utilization is %s percent. " % memory_percent
    response += "Current disk utilization is %s percent. " % disk_percent
    speak(response)
    

def playsong():   #open video
    speak("which video you want to play ?")
    content=os.listdir("F:\Videos")
    x=content.index(content[-1])
    for i in range(0,x+1):
        string=content[i]
        print("{}. {}".format(i+1,string[:50]))
    a=recordAudio()
    a=("{}.mp4".format(a))
    if a in content:
        try:
            speak('ok sir playing {} '.format(a))
            subprocess.Popen('F:\Videos{}'.format(a),shell=True)
        except:
            speak("Video not present")

def shutdown():
    speak("Do you want to shut down your Computer")
    data=recordAudio()
    if "yes" in data:
        subprocess.call(["shutdown", "/s"])
    if "no" in data:
        speak("ok")


        
def wiki():
    speak("what do you want to search?")
    a=recordAudio()
    speak((wikipedia.summary(a, sentences=2)))

    

def directory():
    content=os.listdir(r"f:\Videos")
    x=content.index(content[-1])
    for i in range(0,x+1):
        string=content[i]
        print("{}. {}".format(i+1,string[:50]))
    




def writefile():  #open notepad
    speak("By which name do you want to save the file?")
    a=recordAudio()
    speak("Say something to Write in file!")
    data=write()
    file = open("{}.txt".format(a),'a')
    file.write(data)
    file.close()


def readfile():
    speak("which file do you want to open?")
    a=recordAudio()
    file = open("{}.txt".format(a),'r')
    read(file.read())
    file.close()
    
    

def clsvlc():
    for process in (process for process in psutil.process_iter() if process.name()=="vlc.exe"):
        process.kill()


def clsnotepad():
    for process in (process for process in psutil.process_iter() if process.name()=="notepad.exe"):
        process.kill()


def clsbrowser():
    for process in (process for process in psutil.process_iter() if process.name()=="chrome.exe"):
        process.kill()


def close():
    speak("Which program do you want to close?")
    a=recordAudio()
    for process in (process for process in psutil.process_iter() if process.name()==a+".exe"):
        process.kill()


def search():   #web search
    speak("what you want to search")
    a=recordAudio()
    return webbrowser.open('https://www.google.co.in/search?q='+a)

 

wikipedia=["search wikipedia"]
welcome=["hello","hi"]
play=["play video","play","play song","play music"]
newfile=["create file"]
readfile=["read file"]
question=["how are you","who are you"]
searchweb=["search", "google"]
time=["what is the time","time"]
reply=["hello","hi"]
end=["exit program","exit"]
display=["display log file","log file"]
shutdownpc=["shutdown the computer"]
folders=["show files","show directory"]
closeprogram=["close vlc","close google chrome","close program","close notepad"]
status=["status"]


def jarvis(data):
    first=data.split(" ")
    if first[0]=="locate" or first[0]=="location":
        import location
        return location.loco(first[1])
    if (first[0]=="play" or first[0]=="search") and first[1]=="youtube":
        del(first[0])
        del(first[0])
        a="+".join(first)
        b=" ".join(first)
        import urllib.request
        import urllib.parse
        import re

        query_string = urllib.parse.urlencode({"search_query" : a})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        print("playing:"+a)
        return webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
    if first[0]=="google" or first[0]=="search":
        del(first[0])
        a="+".join(first)
        return webbrowser.open('https://www.google.co.in/search?q='+a)
    if first[0]=="connect":
        del(first[0])
        a="".join(first)
        return webbrowser.open(a+".com")
    if first[0]=="who":
        del(first[0])
        a="".join(first)
        from wikiapi import WikiApi
        wiki = WikiApi()
        wiki = WikiApi({ 'locale' : 'en'})
        results = wiki.find(a)
        article = wiki.get_article(results[0])
        print(article.summary)
        return webbrowser.open(article.image)
    
    while(1):
        if data in wikipedia:
            wiki()
            break
        if data in status:
            cpustatus()
            break
        if data in welcome:
            speak("hi there")
            break
        if data in play:
            speak("ok sir")
            playsong()
            break
        if data in newfile:
            writefile()
            break
        if data in readfile:
            readfile()
            break
        if data in searchweb:
            speak("ok sir")
            search()
            break
        if data in time:
            speak(ctime())
            break
        if "close notepad" in data:
            clsnotepad()
            break
        if "close video" in data:
            clsvlc()
            break
        if "close browser" in data:
            clsbrowser()
            break
        if data in display:
            log.display()
            break
        if data in end:
            com="close"
            return com
            break
        if data in shutdownpc:
            shutdown()
            break
        if data in folders:
            directory()
            break
        if data in closeprogram:
            close()
            break
        else:
            print("I don't understand the command!! Try again")
            break
# initialization
if __name__=="__main__":
    print("initializing")
    run=1
    try:
        speak("Ask me Anything")
        while (run):
            data = recordAudio()
            #data=input("command:")
            data=nltk.processing(data)
            com=jarvis(data)
            if com=="close":
                run=0
    except:
        print("Error occured during program Exection")
        print("Possibility:\n1.Internet is not working.Please connect to Internet")
        print("2.Error in Code\n3.Manual Intruption")
    finally:
        print("Thank you")
