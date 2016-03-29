#Formulates templates of questions starting with the word "when". Tokenizes the given sentence using
#the NLTK tokenizer and then tags each token with a part of speech using the NLTK part of speech tagger.
#Gathers the subject and attributes based on the part of speech the given token is and then calls the response
#module, which will formulate a response. If the returned response is the empty string then an answer will be
#given illustrating that ArnoldFan does not know what occurred.

import nltk
import Response
from ArnoldInfo import ArnDate,ArnLocation
from MovieInfo import MovieDate
arnDate = ArnDate()
arnLoc = ArnLocation()
movieDate = MovieDate()
import random

randomAnswers = ["I don\'t know when that happened",
                 "You\'re a real wise guy asking me a question like that",
                 "Easy tough guy.I\'m not that into Arnold\'s life",
                 "I\'m tired talking to you. Why don't you do us both a favor and type 'AB' so you can talk to Arnold Bot",
                 "You need Google, not Arnold Fan"]    

def randAnswer():
    randNum = random.randint(0,len(randomAnswers)-1)
    return(randomAnswers[randNum])

def answer(sentence):
    index = sentence.index('when')+2
    text =  nltk.word_tokenize(sentence)
    #print('Question',text)
    val = nltk.pos_tag(text)
    #print('Tokens',val)
    #print(val)
    info = Response.getNextSoloTerm(val[index:],['VBN','NN'])
    if info=="":
        #print("HERE WE GO")
        return randAnswer()
    subject = info[0]
    index+=info[1]
    #print('subject',subject)
    if subject=='arnold':
        info = Response.getNextSoloTerm(val[index:],['NN'])
        if info=="":
            return randAnswer()
             #randNum = random.randint(0,len(randomAnswers)-1)
             #return(randomAnswers[randNum])
        attribute = info[0]
        index+=info[1]
        #print('ATTRIBUTE',attribute)
        form = ''
        answer = Response.buildSentence([subject,'when was',attribute,form])
        if answer=="":
            return randAnswer()
            #randNum = random.randint(0,len(randomAnswers)-1)
            #return(randomAnswers[randNum])
        return(answer)
    elif subject=='movie':
         form = ''
         #print('Form',form)
         info = Response.getMovieTitle(val[index:],['VBN','VBD'])
         if info=="":
             return randAnswer()
         title = info[0]
         index = index + info[1]
         #print('Title:',title)
         info = Response.getNextTerm(val[index:],['VBN','VBD'])
         if info=="":
             return randAnswer()
         attribute = info[0]
         index = index + info[1]
         #print('NEWcounter',counter)
         #print('Attribute:',attribute)
         answer = Response.buildSentence([subject,'when was',title,attribute,form])
         if answer=="":
             return randAnswer()
         return answer
    else:
        return randAnswer()
        #randNum = random.randint(0,len(randomAnswers)-1)
        #return(randomAnswers[randNum])
        
sentence = "when was arnold born?"
print(answer(sentence))

