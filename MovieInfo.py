#Contains the class that stores all of the information about Arnold's movies.
#This class is utilized by ArnoldFan.

from collections import namedtuple


Movie = namedtuple('Movie',['title','released','cast'])
myTerms = ('released','mrOlympia','governor')
mySynonyms = {'released':['released','filmed','made','produced','created']}
              
              
myMovies = [Movie('terminator','1984',[]),Movie('total recall','1990',[]),
            Movie('kindergarten cop ','1990',[]),Movie('terminator 2 ','1991',[]),
            Movie('terminator 3 ','2003',[]),Movie('the expendables ','2010',[]),
            Movie('the expendables 2 ','2012',[]),Movie('the expendables 3 ','2014',[])]

#print(myMovies)

class MovieDate:
    def __init__(self):
        pass
    
    def getProperTerm(self,term):
        term = term.rstrip()
        #print('TERM',term)
        for word in mySynonyms:
            #print('WORD',word)
            #print(term in mySynonyms[word])
            #print(mySynonyms[word])
            if term in mySynonyms[word]:
                #print('DOES IT EXIST')
                return word
        return("")
        
    
    def findMovieInfo(self,title,info):
        #print("TITLEARG",title)
        for movie in myMovies:
            #print('Movie.title',movie.title)
            if title == movie.title:
                #print('MOVIE TITLE:',movie.title)
                #print("INFO",info)
                if info=="":
                    return("")
                funct = 'movie.{}'.format(info)
                #print("RIGHT?",eval(funct))
                return eval(funct)
        return ""
    
    def getDateInfo(self,title,att,form):
        term = self.getProperTerm(att)
        #print("TERMCALL",term)
        answer = self.findMovieInfo(title,term)
        if answer =="":
            return ""
        #answer =''
        #print('TERM',term)
        response = 'The movie {} was {} in {}'.format(title,term,answer)
        #for el in form:
         #   answer+= eval('dateInfo[term].{} '.format(el))
        #if(len(form)>1):
        #    response = 'Arnold was {} on {}'.format(term,answer)
        #else:
        #    response = 'Arnold was {} in {}'.format(term,answer)
        #print('SENTENCE:',response)
        return response
    

class MovieLocation:
    
    def __init__(self):
        pass
    
    def getLocInfo(self,title,attribute):
        pass
    
