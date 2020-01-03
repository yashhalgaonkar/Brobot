#=========Importing Required Packages==================
import pyttsx3
import webbrowser
from googlesearch import *
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha 
import os
import sys
import calendar
import time
from selenium import webdriver
from tkinter import *
from tkinter import messagebox
import playsound
#==============Initailize the driver==============================
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('E4PPJ3-LG2QJYW5UW')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

#====================Defining some useful fuctions=====================

def speak(audio):
    #print('Called speak')
    """Function to make BroBot speak."""
    print('BroBot: ' + audio)
    E2['text'] = audio
    engine.say(audio)
    engine.runAndWait()
#-----------------------------------------------------------------------
def greetMe():
    """Function to greet the user."""
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        engine.say('Good Morning!')

    if currentH >= 12 and currentH < 18:
        engine.say('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        engine.say('Good Evening!')
    engine.say('Hello Sir, I am your digital assistant Brobot. How can I help you?')
    engine.runAndWait()
#-------------------------------------------------------------------------
def myCommand():
    #print('called my command')
    """Function to take the command from the user. """  
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        #print("Listening...")
        #E2['text'] = 'Listening...'
        print('listening...')
        engine.say('Listening...')
        engine.runAndWait()
        r.pause_threshold =  0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        engine.say('Sorry sir! I didn\'t get that! Try typing the command.')
        engine.runAndWait()
        query = str(input('Command: '))
    E1['text'] = query
    return query
#----------------------------------------------------------------------------
""" Function to send mail """
def send_email(): 
    speak('Who is the recipient? ')
    recipient = myCommand()

    if 'me' in recipient:
        try:
            speak('What should I say? ')
            content = myCommand()
        
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("Your_Username", 'Your_Password')
            server.sendmail('Your_Username', "Recipient_Username", content)
            server.close()
            speak('Email sent!')

        except:
            speak('Sorry Sir! I am unable to send your message at this moment!')
#-----------------------------------------------------------------------------------
def search_google(query):
    """ Search google"""
    #chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)
#---------------------------------------------------------------------------------
def whatsapp():
    driver = webdriver.Chrome(executable_path=r'C:\Users\yashh\OneDrive\Desktop\Brobot\chromedriver_win32\chromedriver.exe')
    speak('Please scan the QR code-')
    driver.get('https://web.whatsapp.com/')
    speak('To whom do you want to send message- ')
    name = myCommand()
    name = name.title()
    speak(random.choice(['What should I say to '+name+'?','What is your message?']))
    msg = myCommand()
    speak('Okay!\nPress any button after scanning QR code.')
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(1):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()   
#------------------------------------------------------------------------
def birthday():
    """ Function that tells user if today is a birthday."""
    birthdays = open('BirthdayFile.txt', 'r') 
    today = time.strftime('%m/%d') 
    bday = False
    for line in birthdays:
        date,name = line.split('-')
        if today==date:
            print(name,'has their Birthday today.')
            bday = True
    if bday:
        print('Wish them well!!')
    else:
        print('There are no bdays today.')

#--------------------------------------------------------------------------
def facebook():
    """ Function that enables user to send Facebook messages"""

    ###### Future Scope #######



#----------------------------------------------------------------------------------
def set_reminder():
    """Function to set reminder"""





########## Future Scope ################





    

#=====================Initializing commom conversation topic function================
def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return true"""
    for word in sentence.split():
        if word.lower() in greeting_keys:
            return True
    else:
        return False
#------------------------------------------------------------------------
def check_for_abuse(sentence):
    """ If any of the words in users input was a abuse, return true"""
    for word in sentence.split():
        if word.lower() in abuse_keys:
            return True
    return False
#-----------------------------------------------------------------------------
def check_for_praise(sentence):
    """If any word in user input is a praise, return true"""
    if sentence in grateful_keys:
        return True
    for word in sentence.split():
        if word.lower() in grateful_keys:
            return True
    return False  
#-----------------------------------------------------------------------
def take_notes():
    ''' Take notes from the user and save it in a file.'''
    note = open('notes.txt','a+')
    note.write(str(time.ctime)+'\n')
    speak('Tell your note-')
    user_note = myCommand()
    note.write(user_note+'\n')
    note.close()
#-----------------------------------------------------------------------
def show_notes():
    '''To show user its notes.'''
    note = open('notes.txt')
    
    for line in note:
        print(line,end='')
    note.close()
#-----------------------------------------------------------------------
def clear_notes():
    """ To clear all the notes"""
    notes = open('notes.txt','w')
    notes.close()
    speak('Done!')
#-----------------------------------------------------------------------
def take_budget():
    """ To take budget from the user and save it in a file."""


    ######   FUTURE SCOPE   #######


    
#---------------------------------------------------------------------
def show_budget():
    """ To show saved budget to the user."""


    ######   FUTURE SCOPE   #######


#--------------------------------------------------------------------
def clear_budget():
    """ To clear all existing budget"""

    
    
    ######   FUTURE SCOPE   #######

    
    
#-------------------------------------------------------------------------
def i_do():
    speak('I am BroBot and I am a college project for my makers. I can do almost everything!!')
    #speak('Here is a list of some of the interesting things I can do-\n')
    speak('Read news for you, Open websites, Play music, Search for person on Wikipedia, Solve simple maths')
    speak('Search Google, Take Notes and many more interesting things.')
    #time.sleep(3)
    speak('And if I am not able to do any of these, I can always say sorry :-)')
    speak('I dont like to brag, but I am really smart!! You can try me.')


#========================Main Function===========================================
def nextCommand():
    print('called next command')
    query = myCommand()
    if query=='Nahi Mila':
        print('query not found')
    print('query found')
    query = query.lower()
        

    if 'what can you do' in query or 'what are your features' in query or 'what are you' in query or 'what do you do' in query or 'tell me something about yourself' in query:
        i_do()

    elif check_for_greeting(query):
        speak(random.choice(greeting_res))

    elif check_for_praise(query):
        speak(random.choice(grateful_res))

    elif check_for_abuse(query):
        speak(random.choice(abuse_res))
        speak(random.choice(['Whatever, I am still smarter than you.','I am still better than you.']))
#-------------------------------------------------------------------------------------------------------
    elif 'take notes' in query or 'take a note' in query or 'note down' in query:
        take_notes()

    elif 'clear notes' in query:
        clear_notes()

    elif 'show notes' in query:
        show_notes()

    elif 'budget' in query:
        take_budget()
#---------------------------------------------------------------------------------------------

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        speak(results)

    elif 'check  birthday' in query or 'today\'s birthdays' in query:
        birthday()
            
    elif 'search' in query and 'google' in query:
        query = query.replace('google','')
        query = query.replace('search','')
        query = query.replace('on','')
        speak('Searching '+query.title()+' on Google')
        search_google(query)

    elif 'open youtube' in query:
        speak('okay')
        webbrowser.open('www.youtube.com')

    elif 'open google' in query:
        speak('okay')
        webbrowser.open('www.google.co.in')

    elif 'open gmail' in query:
        speak('okay')
        webbrowser.open('www.gmail.com')

    elif 'open stackoverflow' in query:
        speak('okay')
        webbrowser.open('www.stackoverflow.com')

    elif 'open geeksforgeeks' in query:
        speak('okay')
        webbrowser.open('www.geeksforgeeks.com')

    elif 'open quora' in query:
        speak('okay')
        webbrowser.open('www.quora.com')
            
    elif 'open facebook' in query:
        speak('okay')
        webbrowser.open('www.facebook.com')

    elif 'open twitter' in query:
        speak('okay')
        webbrowser.open('www.twitter.com')

    elif 'send whatsapp message' in query:
        speak('okay')
        whatsapp()

    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))

    elif 'what\'s the time' in query or 'what time is it' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'calendar' in query:
        speak('Here is the calendar: ')
        print(calendar.month(2019,5))

    elif 'email' in query or 'send email' in query:
        send_email()   ################ Under Beta-Testing ####################
                       

    elif 'nothing' in query or 'abort' in query or 'stop' in query or 'quit' in query:
        speak('okay')
        speak(random.choice(['Bye Sir, have a good day.','Bye Sir, Hope you liked me!','Bye Sir, See you soon.']))
        sys.exit()
           
    elif 'hello' in query:
        speak('Hello Sir')

    elif 'bye' in query:
        speak('Bye Sir, have a good day.')
        sys.exit()
                                    
    elif 'play music' in query:
        os.system(r'C:\User\yashh\Music\The Chainsmokers & Coldplay - Something Just Like This (Lyric) (192  kbps).mp3')
       
                  
        speak('Okay, here is your music! Enjoy!')
            

    else:
        query = query
        speak('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                speak(random.choice(['According to me- ','I think- ']))      
                #Wolfaralpha 
                speak(results)
                    
            except:
                results = wikipedia.summary(query, sentences=2)
                #speak('Got it.')
                speak('According to WIKIPEDIA- ')
                speak(results)
        
        except:
            speak(random.choice(['I can\'t find what you are looking for. Please search it yourself on Google.']))
            webbrowser.open('www.google.com')
    time.sleep(1)

#==============Initializing word dictionary=============================

greeting_keys = ["hello", "hi", "greetings", "sup", "what's up",]
greeting_res = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

abuse_keys = ['dumb','bad','slow','irritating','fat','moron','ugly','idiot']
abuse_res = ['I am a bot and you hurt my feelings.',
             'I am a bot but that doesn\'t mean I dont have feelings.',
             'I am not powered by AI but that doesn\'t mean I dont have feelings.',
             'You hurt my feelings :-(']

grateful_keys  = ['thank you','thanks','good job','well done','great job','awesome','cool','killer','good']
grateful_res = ['Glad you liked it. :-)','All credit to my makers. :-)',
                'Dont thank me, thank Python. :-)',
                'Just doing my thing. :-)'                
                'Dont thank me, thank my makers. :-)',
                'Today, my maker\'s will be proud of me. ']

#=======================GUI=======================================
root = Tk()
root.geometry('900x800')
root.wm_title("BroBot- Your Digital Assistant")
root.config(bg="#3867d6")

w = Label(root,
          text="BroBot",
          padx=(100),
          fg = "#f7f1e3")
w.pack()
w.config(font=("Purisa" ,44, "bold"), bg = "#3867d6")

w1 = Label(root,
           text="Your Digital Assistant",
           padx=(100),
           pady=(0),
           fg = "black")

w1.config(font=("Lobster", 20, "italic"), bg = "#3867d6")
w1.pack()

L1 = Label(root,
           text="User - ",
           font = ("black", 15, "bold"),
           width = (10),
           height = (2),
           bg = "#f1c40f",
           relief = "sunken")
L1.pack(pady=(50)) 
E1 = Label(root,
           width = (80),
           height = (6),
           text='') 
E1.pack(pady=(0))

L2 = Label(root,
           text="BroBot - ",
           font = ("black", 15, "bold"),
           width = (10),
           height = (2),
           bg = "#f1c40f",
           relief = "sunken") 
L2.pack( pady= (50))
E2 = Label(root,
           width = (80),
           height = (6),
           text='Hi sir! I am your digital assistant Brobot. What can I do for you?') 
E2.pack()

def helloCallBack(): 
   speak('Bye sir! Have a nice day! I hope you miss me.')
   sys.exit()

C = Button(root,
           text='Give Command',
           command = nextCommand,
           font = (40),
           width = (20),
           relief = 'raised',
           bg = '#f1c40f')
C.pack(pady = (30))

B = Button(root,
           text = "Exit",
           command = helloCallBack,
           font = (40),
           width = (10),
           relief = "raised",
           bg= "#f1c40f",
           cursor = "circle") 
B.pack(side = BOTTOM, pady=(30))

greetMe()
    
root.mainloop()

##################################    END    #######################################################        
