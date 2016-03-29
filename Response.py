#This module takes a template and formulates an answer based off of the answer returned by
#the ArnoldInfo module or the MovieInfo module.

from ArnoldInfo import ArnDate,ArnLocation
from MovieInfo import MovieDate
arnDate = ArnDate()
arnLoc = ArnLocation()
movieDate = MovieDate()

def getNextTerm(myTokes,myPoses):
    nextTerm = myTokes[0]
    counter = 0
    while nextTerm[1] not in myPoses:
        counter = counter+1
        #print('counter',counter)
        #print(nextTerm)
        try:
            nextTerm = myTokes[counter]
        except:
            IndexError
            return("")
    myTerm = nextTerm[0]+' '
    myPos = nextTerm[1]
    if(counter+1 < len(myTokes)):
         tempCounter = counter+1
         tempTerm = myTokes[tempCounter]
         if tempTerm[1] == myPos:
             myTerm+= tempTerm[0]+' '
             counter = tempCounter
    return([myTerm,counter+1])
    
def getMovieTitle(myTokes,myPoses):
    counter = 0
    done = 0
    nextTerm = myTokes[counter]
    title = ''
    while nextTerm[1] not in myPoses and not done:
        title+=nextTerm[0]+' '
        if counter+1 < len(myTokes):
            counter = counter+1
            nextTerm = myTokes[counter]
        else:
            done = 1
    return([title.rstrip(),counter])
        
    
def getNextSoloTerm(myTokes,myPoses):
    #print('MYTOKES',myTokes)
    nextTerm = myTokes[0]
    #print('NextTerm',nextTerm)
    counter = 0
    while nextTerm[1] not in myPoses:
        counter = counter+1
        #print('counter',counter)
        #print(nextTerm)
        try:
            nextTerm = myTokes[counter]
        except:
            IndexError
            return("")
    myTerm = nextTerm[0]
    return([myTerm,counter+1])
    
def getMovieDateInfo():
    pass

def buildSentence(terms):
    subject = terms[0]
    questType = terms[1]
    if subject=='arnold':
        att = terms[2]
        if questType=='when was':
            if terms[3] =='month':
                response = arnDate.getDateInfo(att,['month'])
            elif terms[3]=='year':
                response = arnDate.getDateInfo(att,['year'])
            elif terms[3]=='day':
                response = arnDate.getDateInfo(att,['month','day'])
            elif terms[3]=='birthday':
                response = arnDate.getDateInfo(att,['month','day'])
            elif terms[3]== 'date':
                response = arnDate.getDateInfo(att,['month','day','year'])
            elif terms[3]=='born':
                response = arnDate.getDateInfo(att,['month','day','year'])
            elif terms[3]=='':
                response = arnDate.getDateInfo(att,['month','day','year'])
            else:
                print('{} is an unknown birth form'.format(terms[3]))
        elif questType=='where was':
            att = terms[2]
            if terms[3]=='':
                response = arnLoc.getLocInfo(att,['city','country'])
            elif terms[3]=='city':
                response = arnLoc.getLocInfo(att,['city'])
            elif terms[3]=='state':
                response = arnLoc.getLocInfo(att,['state'])
            elif terms[3]=='country':
                response = arnLoc.getLocInfo(att,['country'])
        else:
            response = 'ArnoldFan only knows about where and when for Arnold'
    elif subject=='movie':
        title = terms[2]
        #print("TITLE ",title)
        att = terms[3]
        #form = terms[4]
        if questType=='when was':
            if terms[4]=='year':
                response = movieDate.getDateInfo(title,att,['year'])
            elif terms[4]=='':
                response = movieDate.getDateInfo(title,att,['year'])
                
            
        else:
            response = 'ArnoldFan only knows about when for Arnold\'s movies'
    else:
        response = '{} is a subject ArnoldFan knows nothing about'.format(subject)
    return response
   
