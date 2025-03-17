from random import random
from random import randint
from datetime import datetime 
import datetime


class PrintSyntax():
  #rstr and lstr are the left and right portions 
  #expected to use a print with just 1 string
  def __init__(self):
    self.Lstr = "print(\""
    self.Rstr = "\")"
    self.phrases=["Hello World", "Hello World)(","(Hello World)"]
    self.phrases=self.phrases+["World Hello","()HelloWorld"]
    self.phrases=self.phrases+["(Hello(World))","Welcome","Welco(me","Weclome"]
    self.score=0
  def driver(self):
    self.Game()
    end=False
    while(not end):
      print("Continue? Y/N?")
      answer = input()
      if(answer == "N"):
        end=True
      elif(answer == "Y"):
        self.Game()

#creates start game prompt and replay prompt
  def Game(self):
    print("Welcome to the print syntax game")
    print("Each round you will either enter a Y or an N")
    print("If the syntax is correct you should enter a Y")
    print("If the syntax is incorrect you should enter an N")
    print("The faster your answer the more points you will receive")
    print("Once you have entered an incorrect answer the game will end")
    print("Enter a Y to begin")
    response=input()
  #user is reprompted unitl a Y is submitted 
    while(response!= "Y"):
      print("Enter a Y to begin")
      response=input()

    lost=False
    ans="N"
  #loop continues prompts until the user reaches a wrong response
    while(not lost):
      timer1=datetime.datetime.now().timestamp()
      tp=randint(0,5)
      if(tp<=2):
        ans="Y"
      else:
        ans="N"
      print(self.randstrat(tp))
      response=input()
      timer2=datetime.datetime.now().timestamp()
      if(response!=ans):
        lost=True
        print("You scored:",self.score,"points")
        self.score=0
      else:
        
        self.score=int(self.score+(7/(float(timer2)-float(timer1))))
    #function ends when the player loses 
    return self.score
  
  #selects a random phrase from phrasesarray to 
  #be added into statement as a string
  def ranphrase(self):
    return self.phrases[randint(0,8)]
  #random strategy of how to mess up code, options 0,1,2, do nothing  
  def randstrat(self,type):
    if(type<=2):
      
      return self.Lstr+self.ranphrase()+self.Rstr
    else:
      match type:
        case 3:
          return self.missing(self.ranphrase())
        case 4:
          return self.misplaced(self.ranphrase())
        case 5:
          return self.add(self.ranphrase())
    
  #removes a single component needed for the print function 
  #for a string then puts it together
  def missing(self,phrase):
    temp=list(self.Lstr)
    temp2=list(self.Rstr)
    num=randint(0,8)
    if(num>6):
      temp2[num-7]=""
    else:
      temp[num]=""
    
    temp="".join(temp)
    temp2="".join(temp2)
    final=temp+phrase+temp2
    return final
  
  #will switch any 2 components of the print function to break 
  #quotations wont switch since the result is the same 
  def misplaced(self,phrase):
    num1=randint(0,8)
    num2=randint(0,8)
    while(num2==num1 or (num2==7 and num1==6)or(num2==6 and num1==7)):
      num2=randint(0,8)
    temp=list(self.Lstr+self.Rstr)
    #flipping the values 
    temp2=temp[num1]
    temp[num1]=temp[num2]
    temp[num2]=temp2
    final=temp[:7]+list(phrase)+temp[7:]
    return "".join(final)
 
  #adds a letter somewhere to the start to break the function
  def add(self,phrase):
    temp=list(self.Lstr)
    temp2=list(self.Rstr)
    num=randint(0,6)
    temp.insert(num,chr(randint(ord('a'), ord('z'))))
    final="".join(temp+list(phrase)+temp2)
    return final