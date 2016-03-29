#The main function from which the user is to run the entire program. The interface
#prints out an introduction and allows the user to first interact with ArnoldFan,
#the informational chatbot. At any time the user can type 'ab' to talk with ArnoldBot,
#the conversational chatbot.

import re
import whatForm
import whereForm
import whenForm
from ArnoldBot import ArnoldBot
import time
import random
arnBot = ArnoldBot()
userInput = ''
quitCommands = ['q','quit','Quit']

randomAnswers = ["I have no clue what you\'re talking about.","That question is a little out of my pay grade",
                 "You\'re killing me man. I don\'t know.","Where do you come up with these questions?",
                 "You\'re expectations are a little too high for me."]

def randAnswer():
    randNum = random.randint(0,len(randomAnswers)-1)
    return(randomAnswers[randNum])
sents = ["ArnoldFan: Hello. I Am ArnoldFan.",
      "ArnoldBot: Hello. I Am ArnoldBot",
      "Both: We are here to give you the full Arnold chat experience",
      "ArnoldBot: I\'ll talk to you like Arnold",
      "ArnoldFan: I\'ll answer your questions about Arnold\'s life and movies",
      "ArnoldBot: Anytime you want to talk to me just type (ab)",      
      "ArnoldBot: Anytime you want to quit just type (q)"]
  
for i in sents:
    alpha = len(i)
    for j in range(alpha):
        print(i[j],end='')
        time.sleep(.01)
    print()
    time.sleep(.02)
while userInput not in quitCommands:
    userInput = input('You: ').strip().lower()
    if userInput in quitCommands:
        print("Hasta la vista. Baby!!!")
    elif userInput=='ab':
        print("ArnoldFan: When you\'re tired of talking to ArnoldBot just type- bye\nGoing to get Arnold Bot. I\'ll be baack!!\n")
        arnBot.talk()
    elif re.match('^(what).*$',userInput):
        print('ArnoldFan: {}'.format(whatForm.answer(userInput)))
    elif re.match('^(when).*$',userInput):
        print('ArnoldFan: {}'.format(whenForm.answer(userInput)))
    elif re.match('^(where was).*$',userInput):
        print('ArnoldFan: {}'.format(whereForm.answer(userInput)))
    else:
        print("ArnoldFan: {}".format(randAnswer()))
        
       
        
