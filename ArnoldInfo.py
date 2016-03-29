#Contains the class that stores the information about Arnold's life.
#This class is utilized by ArnoldFan.

from collections import namedtuple

Date = namedtuple('Date',['month','day','year'])

myTerms = ('born','mr. olympia','governor')
mySynonyms = {'born':['birth','born','birthday','birtdate','raised'],'governor':['governor'],
              'mr. olympia':['mr. olympia','mr olympia']}

dateInfo = {'born': Date('July ','30 ','1947'),'mr. olympia': Date('','','1970'),
            'governor':Date('','','2003')}

birthday = Date('July','30','1947')
class ArnDate:
    
    def __init__(self):
        pass
   
    def getProperTerm(self,term):
        #print('Term',term)
        term = term.rstrip()
        for word in mySynonyms:
            #print('Word',word)
            #print(term in word)
            if term in mySynonyms[word]:
                return word
        return ""
        
  
    def getDateInfo(self,att,form):
        term = self.getProperTerm(att)
        #print("TERM:",term)
        #for word in mySynonyms:
            #if term in mySynonyms[word]:
                #term = word
                #break
        answer =''
        #print('TERM',term)
        for el in form:
            #print('Year?',el)
            #print('TERM',term)
        
            #print('ERROR?',dateInfo['governor'].year)
          try:
            answer+= eval('dateInfo[term].{} '.format(el))
          except:
              KeyError
              return ""
            #print("ANSWER?",answer)
        if(len(form)>1):
            response = 'Arnold was {} on {}'.format(term,answer)
        else:
            response = 'Arnold was {} in {}'.format(term,answer)
        #print('SENTENCE:',response)
        return response


Location = namedtuple('Location',['city','state','country'])   
locInfo = {'born':Location('Thal ','','Austria')}
class ArnLocation:
    
    def __init__(self):
        self.birthplace = 'Thal, Austria'
        
    
    def getProperTerm(self,term):
        #print('Term',term)
        term = term.rstrip()
        for word in mySynonyms:
            #print('Word',word)
            #print(term in word)
            if term in mySynonyms[word]:
                return word
        return ""
        
        

    def getLocInfo(self,att,form):
        term = self.getProperTerm(att)
        if term=="":
            return ""
        #for word in mySynonyms:
         #   if term in mySynonyms[word]:
         #       term = word
         #       break
        answer =''
        #print('TERM',term)
        for el in form:
            try:
                answer+= eval('locInfo[term].{} '.format(el))
            except KeyError:
                return ""
        #if(len(form)>1):
        response = 'Arnold was {} in {}'.format(term,answer)
        #else:
        #response = 'Arnold was {} in {}'.format(term,answer)
        #print('SENTENCE:',response)
        return response
        
