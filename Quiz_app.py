total_pricemoney=0
a=0
b=4
c=0
next_question=True
user=["yash","ayush"]
password=["yash123","ayush123"]

def registration(): # THIS FUNCTION REGISTERS USER
    print("REGISTRATION PAGE:")
    uname=input("enter your username: ").lower()
    if uname in user:
        print("Username Unavailable")
        registration()
    else:
        pword=input("enter your password: ").lower()
        user.append(uname)
        password.append(pword)
        print("Registration Successfull")
        login()
    
def login():# THIS FUNCTION LOGINS USER
    print("LOGIN PAGE:")
    uname=input("enter username: ").lower()
    if uname in user:
     name_index=user.index(uname)
     pword=input("enter password: ").lower() #PASSWORD IS ASKED ONLY IF USERNAME IS CORRECT 
     if pword==password[name_index]:
         print("Login Successfull")
         while(c<7 and next_question==True):
          if(c==0):
           print("GAME START",end="\n\n")
           print("Instruction-Enter 'quit' to exit the game\n")
          question()
          answers()
          if(c==7):
           print("GAME END")
     else:
         print("Incorrect Password")
         login()
    else:
     print("user not found")
     registration()
    
def reward(answerpricemoney): #THIS FUNCTION INCREMENTS THE PRIZE MONEY
     global total_pricemoney 
     total_pricemoney =total_pricemoney + answerpricemoney 

def question(): 
    global a,b,c
    i=1
    questions=["What is the capital of India ?","What is the height of Mount Everest in metres ?","Who is the current president of India ?","Who shares the most border with India","India is the __th largest country in terms of area covered.","Bhopal gas tragedy occured in which year ?","India is a major exporter of"]
    options=["Delhi","Jabalpur","New Delhi","Pune","8849","10000","6000","15000","Pranab Mukherjee","Droupadi Murmu","Pratibha Patil","K.R. Narayanan","Bangladesh","China","Pakistan","Nepal","4","10","7","15","1980","1985","1990","1984","Petroleum proucts","Diamonds","Textile","All Of The Above"]
    print(f"Q{c+1}.",questions[c]) #THIS LINE PRINTS THE QUESTION NUMBER AND THE QUESTION
    
    for j in range(a,b):  #THIS LOOP PRINTS THE OPTIONS FOR THE GIVEN QUESTIONS
        print(f"{i}.",end="") #PRINTS THE NUMBERING OF THE OPTION 
        print(options[j])#PRINTS THE OPTION
        i=i+1
    a=b #THESR 2 LINES CHANGES THE VALUE OF a and b TO PRINT THE NEXT 4 OPTIONS FOR THE NEXT QUESTION
    b=b+4
    
def answers():
    global next_question,c
    correct_answers=["New Delhi","8849","Droupadi Murmu","Bangladesh","7","1984","All Of The Above"]
    answer_pricemoney_list=[10000,20000,50000,100000,500000,1000000,3000000]
    user_answer=input("enter your answer: ").title() #TAKES USER'S ANSWER
    if user_answer=="Quit":
        next_question=False
        print("Game Quit")
        print("You won NOTHING")
    elif(user_answer==correct_answers[c]):
        reward(answer_pricemoney_list[c])#CALLS THE reward() FUNCTION
        print("Your answer is CORRECT.")
        print(f"You have won {answer_pricemoney_list[c]} Rupees for this answer",end="\n\n")
        print(f"Your total price money is {total_pricemoney} Rupees",end="\n\n" )
        next_question=True
        c=c+1
    else:
        print("Your answer is INCORRECT.")
        print("GAME OVER!!!!")
        print(f"Your total price money is {total_pricemoney} Rupees",end="\n\n" )

        next_question=False
print("WELCOME TO THE QUIZ GAME".center(50,"*"))      
print("You are a:")
print("1. NEW USER")
print("2. EXISTING USER")
choice=input("enter your choice: ").upper()
if choice=="1" or choice=="NEW USER":
    registration()
if choice=="2" or choice=="EXISTING USER":
    login()   

    

    

     



        