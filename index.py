#QUIZ Game
import time
player_name=str(input("Enter your name: "))
subject= str(input('''enter the name of subject on which you want to attend Quiz
English\t\tGK\tScience''').upper())
sc=0
if(subject=="ENGLISH"):
    print("You have selected English")
    ques1=str(input('''This is __ apple. 
    Option 'A': the  Option 'B': an   Option 'C': a   Select the Correct option and write the option apha''').capitalize())
    if(ques1=="B"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")        
    ques2=str(input('''We agreed___ help. 
    Option 'A': to  Option 'B': and   Option 'C': a   Select the Correct option and write the option apha''').capitalize())
    if(ques2=="A"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")
    ques3=str(input('''I have no____  cash left. 
    Option 'A': much  Option 'B': and   Option 'C': more   Select the Correct option and write the option apha''').capitalize())
    if(ques3=="C"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")    
elif(subject=="GK"):
    print("You have selected GK")
    ques1gk=str(input('''Prime Minister of Pakistan is
    Option 'A': Imran K  Option 'B': Shehbaz S   Option 'C': Maryam N  Select the Correct option and write the option apha''').capitalize())
    if(ques1gk=="B"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")        
    ques2gk=str(input('''Capital of Pakistan is ___ . 
    Option 'A': Islamabad  Option 'B':Karachi  Option 'C': Lahore   Select the Correct option and write the option apha''').capitalize())
    if(ques2gk=="A"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")
    ques3gk=str(input('''COAS is____. 
    Option 'A': Gen Asim  Option 'B': Gen Bajwa   Option 'C': Gen ABC   Select the Correct option and write the option apha''').capitalize())
    if(ques3gk=="C"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")  
else:
    print("You have selected Science")
    ques1sc=str(input('''metal is a good conductor of ____. 
    Option 'A': electricty  Option 'B': water   Option 'C': MINERAL   Select the Correct option and write the option apha''').capitalize())
    if(ques1sc=="A"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")        
    ques2sc=str(input('''Formula of water is __. 
    Option 'A': H20  Option 'B': CO2  Option 'C': HHCO   Select the Correct option and write the option apha''').capitalize())
    if(ques2sc=="A"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!")
    ques3sc=str(input('''___ revolve around the sun. 
    Option 'A': car  Option 'B': moon   Option 'C': earth   Select the Correct option and write the option apha''').capitalize())
    if(ques3sc=="C"):
            print("Correct")
            sc+=1
    else:
        print("You are wrong!") 
print("Congratulations! You have successully completed the quiz")        
# score=int(input("How many of these you got right? Be HONEST Please I am good enough to count your score sadly!!: "))
time.sleep(5)
print(f"your final score is {sc}, THANKS FOR ATTENDING, {player_name}")