#Formulates templates of questions starting with the word "what". Tokenizes the given sentence using
#the NLTK tokenizer and then tags each token with a part of speech using the NLTK part of speech tagger.
#Gathers the subject and attributes based on the part of speech the given token is and then calls the response
#module, which will formulate a response. If the returned response is the empty string then an answer will be
#given illustrating that ArnoldFan does not know what occurred.

import nltk
import re
import Response
from ArnoldInfo import ArnDate,ArnLocation
from MovieInfo import MovieDate
arnDate = ArnDate()
arnLoc = ArnLocation()
movieDate = MovieDate()
import random


randomAnswers = ["I don\'t know what the hell you\'re talking about",
                 "Whoa. That question went way over my head",
                 "No clue kid. You\'re being kind of weird if you ask me.",
                 "Your guess is as good as mine",
                 "Good one. Go Google it.", "No idea"]
def randAnswer():
    randNum = random.randint(0,len(randomAnswers)-1)
    return(randomAnswers[randNum])
    
def answer(sent):
    #print(sent)
    sent = sent.lower()
    locTerms = ['city','country''province']
    dateTerms = ['month','year','day','date']
    curiousTerms = ['is','was']
    if re.match('^(what).*$',sent):
        tokes= nltk.pos_tag(nltk.word_tokenize(sent))
        if tokes[1][0] in dateTerms:
            #print('we\'re in the date object')
            counter = 2
            info = Response.getNextSoloTerm(tokes[counter:],['VBN','NN'])
            if info=="":
                return randAnswer()
            subject = info[0]
            counter = counter+info[1]
            #print('Subject:',subject)
            if subject =='movie':
                form = tokes[1][0]
                #print('Form',form)
                info = Response.getMovieTitle(tokes[counter:],['VBN','VBD'])
                if info=="":
                    return randAnswer()
                title = info[0]
                counter = counter + info[1]
                #print('Title:',title)
                info = Response.getNextTerm(tokes[counter:],['VBN','VBD'])
                if info=="":
                    return randAnswer()
                attribute = info[0]
                counter = counter + info[1]
                #print('NEWcounter',counter)
                #print('Attribute:',attribute)
                answer = Response.buildSentence([subject,'when was',title,attribute,form])
                if answer=="":
                    return randAnswer()
                return answer
            elif subject=='arnold':
                form = tokes[1][0]
                #print('Form:',form)
                info = Response.getNextTerm(tokes[counter:],['NN','NNP'])
                if info=="":
                    return randAnswer()
                attribute = info[0]
                counter = counter + info[1]
                #print('Attribute:',attribute)
                #print('OBJECT:\nSubject: {}\nQuestType: when\nAttribute: {}\nForm: {}'.format(subject,attribute,form))
                answer = Response.buildSentence([subject,'when was',attribute,form])
                if answer=="":
                     return randAnswer()
                return answer
        elif tokes[1][0] in locTerms:
            #print('we\'re in the location object')
            counter = 2
            info = Response.getNextSoloTerm(tokes[counter:],['VBN','NN'])
            if info=="":
                return randAnswer()
            subject = info[0]
            counter = counter+info[1]
            #print('Subject:',subject)
            if subject=='arnold':
                form = tokes[1][0]
                #print('Form:',form)
                info = Response.getNextTerm(tokes[counter:],['NN','NNP'])
                if info=="":
                    return randAnswer()
                attribute = info[0]
                counter = counter + info[1]
                #print('Attribute:',attribute)
                return Response.buildSentence([subject,'where was',attribute,form])
        elif tokes[1][0] in curiousTerms:
            return randAnswer()
            #randNum = random.randint(0,len(randomAnswers))
            #return(randomAnswers[randNum])
        else:
            return randAnswer()
            #randNum = random.randint(0,len(randomAnswers)-1)
            #return(randomAnswers[randNum])
        
#for i in range(0,10):
#print('Question:',sentence[0])
#doWork(sentence[0])
