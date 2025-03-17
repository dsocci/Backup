from random import random
from random import randint
#class will hold functions that break the syntax 
#given the required components and 
class SyntaxBreaker:

  #components is an array of all required parts of syntax
  def missing(self,components):
    string=""
    remove=random.randint(0,len(components))
    #loop should concatenate the parts but keep track of where they split 
    count=0
    #for loop to eliminate the character
    for i in range(len(components)):
      notdone=True
      if(count!=(remove)):
        temp=components[i]
        if(count+len(temp)>=remove and notdone):
          components[i][remove-count]=""
          notdone=False
        else:
          count+=len(temp)    
    return components
