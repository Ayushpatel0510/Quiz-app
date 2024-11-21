total_pricemoney=0
a=0
b=4
c=0
next_question=True
    
def show_profile():
  with open("registration_details.txt","r")as show:
    pf=show.readlines()
  profile=[]
  for str in pf:
    str1=str.replace("\n","")
    profile.append(str1)              #THIS FUNCTION FETCH THE USERS'S DETAILS -> FORMATS THEM -> STORES THEM IN A LIST -> DISPLAYS THEM
  profile_index=profile.index(f"Username-{logged_user}")
  print("User Details:\n")
  for num in range(profile_index,profile_index+5):
   print(profile[num])
  print()
  input("Press Enter to go back to MENU ")
  menu()
        
def attempt_quiz():
    while(c<7 and next_question==True):
        if(c==0):
         print("\nGAME START",end="\n\n")
         print("Instructions:")
         print("1.Enter answers in text not serial.no .")
         print("2.Enter 'quit' to exit the quiz.\n")
        question()
        answers()
        if(c==7):
         print("\nGAME END\n")
    menu()
         
def show_result():#THIS FUNCTIONS DISPLAYS RESULT
    print("\nRESULT:\n")
    print(f"Questions correctly answered by the user: {c}")
    print(f"Total amount won by the user: {total_pricemoney}")
    print()
    input("Press Enter to go back to MENU ")
    menu()
            
def logout():
    with open("logs.txt","w") as logs:
        logs.write(f"login_status=False\n")
        logs.write(f"logged_user=None")
    print("Logged Out Successfully")

def registration(): # THIS FUNCTION TAKES THE USER'S DETAILS AND STORES THEM IN FILES 
    print("REGISTRATION PAGE:")
    uname=input("enter your username: ").lower()
    pword=input("enter your password: ").lower()
    name=input("Enter your name:").title()
    enroll=input("Enter your enrollment number:").upper()
    branch=input("Enter your Branch:").upper()
    with open("registration_details.txt","a") as reg:
        reg.write(f"\nUsername-{uname}\n")   
        reg.write(f"Password-{pword}\n")   
        reg.write(f"Name-{name}\n")   
        reg.write(f"Enrollment_no-{enroll}\n")   
        reg.write(f"Branch-{branch}")
        
    with open("login_details.txt","a") as log:
        log.write(f"Username-{uname}\n")   
        log.write(f"Password-{pword}\n")
        
    print("Registration Successfull")
    login()
    
def login():# THIS FUNCTION LOGINS USER
    with open("login_details.txt","r") as log:
            cred=log.readlines()
    credential=[]
    user=[]
    password=[]
    
    for str in cred:
        x=str.split("-")
        un_pass=x[1].replace("\n","")   #THIS LOOP FORMATS AND STORES THE USERNAME AND PASSWORD IN A SINGLE LIST
        credential.append(un_pass)
        
    for index in range(0,len(credential)):
        if index%2==0:
            user.append(credential[index])    #THIS LOOP STORES USERNAME AND PASSWORD IN DIFFERENT LIST 
        else:
            password.append(credential[index])
            
    print("LOGIN PAGE:")
    uname=input("enter username: ").lower()
    if uname in user:
     name_index=user.index(uname)
     pword=input("enter password: ").lower() #PASSWORD IS ASKED ONLY IF USERNAME IS CORRECT 
     if pword==password[name_index]:
         print("Login Successfull\n")
        
         with open("logs.txt","w") as logs:
             logs.write(f"login_status=True\n") #THIS BLOCK UPDATES THE LOGS FILE
             logs.write(f"logged_user={uname}")
             
         menu()
         
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
    
    with open("questions.txt","r") as ques:
        q=ques.readlines()
    questions=[]                     #THIS BLOCK FETCH QUESTIONS FROM THE FILE AND STORE THEM IN A LIST
    for question in q:
        qu=question.replace("\n","")
        questions.append(qu) 

    with open("options.txt","r") as opt:
        o=opt.readlines()
    options=[]
    for option in o:                  #THIS BLOCK FETCH OPTIONS FROM THE FILE AND STORE THEM IN A LIST
        x=option.replace("\n","")
        options.append(x)
        
    print(f"Q{c+1}.",questions[c]) #THIS LINE PRINTS THE QUESTION NUMBER AND THE QUESTION
    
    for j in range(a,b):  #THIS LOOP PRINTS THE OPTIONS FOR THE GIVEN QUESTIONS
        print(f"{i}.",end="") #PRINTS THE NUMBERING OF THE OPTION 
        print(options[j])#PRINTS THE OPTION
        i=i+1
    a=b #THESR 2 LINES CHANGES THE VALUE OF a and b TO PRINT THE NEXT 4 OPTIONS FOR THE NEXT QUESTION
    b=b+4
    
def answers():
    global next_question,c
    answer_pricemoney_list=[10000,20000,50000,100000,500000,1000000,3000000]
    
    with open("answers.txt","r") as ans:
        a=ans.readlines()
    correct_answers=[]              #THIS BLOCK OF CODE FETCH NSWERS FROM THE TEXT FILE AND STORES THEM IN A LIST
    for answer in a:
        x=answer.replace("\n","")
        correct_answers.append(x)
  
    user_answer=input("enter your answer: ").title() #TAKES USER'S ANSWER
    if user_answer=="Quit":
        menu()
    elif(user_answer==correct_answers[c]):
        reward(answer_pricemoney_list[c])#CALLS THE reward() FUNCTION
        print("Your answer is CORRECT.")
        print(f"You have won {answer_pricemoney_list[c]} Rupees for this answer",end="\n\n")
        next_question=True
        c=c+1
    else:
        print("Your answer is INCORRECT.")
        print("GAME OVER!!!!")
        next_question=False
        menu()

def menu():#THIS FUNCTION SHOWS THE MENU OF WHEN A USER IS ALREADY LOGGED IN
    print("MENU".center(20,"*"))
    print()
    print("1.Attempt Quiz")
    print("2.Show Profile")
    print("3.Show Result")
    print("4.Logout")
    action=input("Enter your choice: ").title()
    if action=="Attempt Quiz" or action=="1":
        attempt_quiz()
    if action=="Show Profile" or action=="2":
        show_profile() 
    if action=="Show Result" or action=="3":
        show_result()
    if action=="Logout" or action=="4":
        logout()
        
def menu2():#THIS FUNCTIONS SHOWS THE MENU OF WHEN NO USER IS ALREADY LOGGED IN
    print("Select User Type:")
    print("1. NEW USER")
    print("2. EXISTING USER")
    choice=input("enter your choice: ").upper()
    if choice=="1" or choice=="NEW USER":
        registration()
    if choice=="2" or choice=="EXISTING USER":
        login()
        
print("WELCOME TO THE QUIZ GAME".center(50,"_"))
print()
with open("logs.txt","r")as logs:
    l=logs.readlines()
logs=[]
login_status=l[0].split("=")[1].replace("\n","")
logged_user=l[1].split("=")[1]
if(login_status=="True"):
    menu()
else:
    menu2()

   

    

    

     



        