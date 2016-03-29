#Formulates templates of questions starting with the word "where". Tokenizes the given sentence using
#the NLTK tokenizer and then tags each token with a part of speech using the NLTK part of speech tagger.
#Gathers the subject and attributes based on the part of speech the given token is and then calls the
#response module, which will formulate a response. If the returned response is the empty string then
#an answer will be given illustrating that ArnoldFan does not know what occurred.

import nltk
import Response
from ArnoldInfo import ArnDate,ArnLocation
from MovieInfo import MovieDate
arnDate = ArnDate()
arnLoc = ArnLocation()
movieDate = MovieDate()
import random

randomAnswers = ["I don\'t where that happend at.Give me a break","That\'s a lot over my head",
                 "A couple more questions like that and I\'m going to have to get to the chopper",
                 "Your guess is as good is man"]
                 
    

def randAnswer():
    randNum = random.randint(0,len(randomAnswers)-1)
    return(randomAnswers[randNum])
    
def answer(sentence):
    index = sentence.index('where was')+2
    text =  nltk.word_tokenize(sentence)
    val = nltk.pos_tag(text)
    #print('Val',val)
    #print('Index',index)
    info = Response.getNextSoloTerm(val[index:],['VBN'])
    subject = info[0]
    index+=info[1]
    #print('Subject',subject)
    if subject=='arnold':
        info = Response.getNextSoloTerm(val[index:],['NN'])
        if info=="":
            return randAnswer()
        attribute = info[0]
        index+=info[1]
        #print('Attribute',attribute)
        form=''
        answer = Response.buildSentence([subject,'where was',attribute,form])
        if answer=="":
            return randAnswer()
        return(answer)
    elif subject=='movie':
        return('Give me a break bro. I\'m not a genie. I\'m a simple chat bot')
    else:
        return randAnswer()
        #randNum = random.randint(0,len(randomAnswers)-1)
        #return(randomAnswers[randNum])
    

