import pymysql.cursors
import cryptography

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='',  #Enter your mysql username
                             password='',  #Enter your mysql password
                             database='QuizApp',
                             )

def registration():#THIS FUNCTION REGISTERS USER AND STORES THEIR DATA IN THE DATABASE
    print("\nREGISTRATION PAGE:")
    with connection.cursor() as cursor:
        uname=input("enter your username: ").lower()
        sql="select User_id from user_details"
        cursor.execute(sql)
        users=cursor.fetchall()
        while (f"{uname}",) in users:
            print("Username unavailable")
            uname=input("enter your username: ").lower()    
        pword=input("enter your password: ").lower()
        name=input("Enter your name:").title()
        enroll=input("Enter your enrollment number:").upper()
        branch=input("Enter your Branch:").upper()
        sql1="insert into user_details(User_id,Name,Enroll_no,Branch) values(%s,%s,%s,%s)"
        val=(uname,name,enroll,branch)
        cursor.execute(sql1,val)
        connection.commit()
        sql2="insert into login_details(User_id,Password) values(%s,%s)"
        val2=(uname,pword)
        cursor.execute(sql2,val2)
        connection.commit()
        print("Registration Successfull")
        login()

def login():#THIS FUNCTION LOGINS USER AND UPDATES THE LOGIN STATUS
    with connection.cursor() as cursor:
        print("LOGIN PAGE:")
        uname=input("enter your username: ").lower()
        sql="select User_id from login_details"
        cursor.execute(sql)
        users=cursor.fetchall()
        if (f"{uname}",)  in users:
            pword=input("enter your password: ").lower()
            sql1="select Password from login_details where User_id=%s"
            val=(uname)
            cursor.execute(sql1,val)
            password=cursor.fetchone()
            while (pword!=password[0]):
                print("Incorrect Password")
                pword=input("enter your password: ").lower()   
            if (pword==password[0]):
                print("Login Successfull")
                sql2=f"update Status set login_status=1 where login_status=0"
                sql3="update Status set logged_user=%s where logged_user='None'"
                val1=(uname)
                cursor.execute(sql2)
                cursor.execute(sql3,val1)
                connection.commit()
                
                menu()
        else:
            print("Unregistered User")
            registration()            
def game():#THIS FUNCTION IS THE QUIZ GAME
    global c,reward,score
    reward=0
    with connection.cursor() as cursor:
            next_question=True
            while(next_question==True and c<=7):
                if(c==1):
                    print("\nGAME START",end="\n\n")
                    print("Instructions:")
                    print("1.Enter answers in text not serial.no .")
                    print("2.Enter 'quit' to exit the quiz.\n")
                o=1
                sql = f"SELECT * FROM Quiz where que_no={c}"
                cursor.execute(sql)
                que = cursor.fetchone()
                sql1 = f"SELECT * FROM options where que_no={c}"
                cursor.execute(sql1)
                print(f"Q{que[0]}. {que[1]}")
                while o<=4:
                    opt = cursor.fetchone()
                    print(f"{opt[0]}. {opt[1]}")
                    o=o+1
                c=c+1
                answer=input("Enter your choice:").title()
                if answer=="Quit":
                 next_question=False
                 print("GAME OVER!!!!")
                 
                elif answer==que[2]:
                    print("\nCorrect Answer")
                    print(f"You won {que[3]} points for this answer\n")
                    score=c-1
                    reward=reward+que[3]
                else:
                    print("\nIncorrect Answer")
                    print("GAME OVER!!!!")
                    next_question=False
                if(c==8):
                    print("GAME END")        
            input("\nPress ENTER to return to MENU:")
            menu()
            
def show_profile():#THIS FUNCTION FETCH USER DETAILS FROM THE DATABASE AND DISPLAYS THEM
    with connection.cursor() as cursor:
        sql1="select logged_user from status"
        cursor.execute(sql1)
        result=cursor.fetchone()
        logged_user=result[0]
        
        sql2="select * from User_details where User_id=%s"
        val=(logged_user)
        cursor.execute(sql2,val)
        result=cursor.fetchone()
    
        print()
        print("USER INFORMATION\n")
        print(f"Username: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"Enrollment Number: {result[2]}")
        print(f"Branch: {result[3]}")
        input("\nPress ENTER to return to MENU:")
        menu()
        
def show_result():#THIS FUNCTIONS DISPLAYS RESULT
    global c,score,reward
    print("\nRESULT:\n")
    print(f"Questions correctly answered by the user: {score}")
    print(f"Total points won by the user: {reward}")
    print()
    input("Press Enter to go back to MENU:")
    menu()
 
def logout():#THIS FUNCTION LOGOUT USER AND UPDATES LOGIN STATUS
     with connection.cursor() as cursor:
            sql2=f"update Status set login_status=0"
            sql3="update Status set logged_user='None'"
            cursor.execute(sql2)
            cursor.execute(sql3)
            connection.commit()
            print("Logged Out Successfully")
            
def menu():#THIS FUNCTION SHOWS THE MENU OF WHEN A USER IS ALREADY LOGGED IN
    global c,reward
    c=1
    print("MENU".center(20,"*"))
    print()
    print("1.Attempt Quiz")
    print("2.Show Profile")
    print("3.Show Result")
    print("4.Logout")
    action=input("Enter your choice: ").title()
    if action=="Attempt Quiz" or action=="1":
        game()
    elif action=="Show Profile" or action=="2":
        show_profile() 
    elif action=="Show Result" or action=="3":
        show_result()
    elif action=="Logout" or action=="4":
        logout()
    else:
        print("Invalid Input")
        
def menu2():#THIS FUNCTIONS SHOWS THE MENU OF WHEN NO USER IS ALREADY LOGGED IN
    print("Select User Type:")
    print("1. NEW USER")
    print("2. EXISTING USER")
    choice=input("enter your choice: ").upper()
    if choice=="1" or choice=="NEW USER":
        registration()
    if choice=="2" or choice=="EXISTING USER":
        login()

c=1
reward=0
score=0
print("WELCOME TO THE QUIZ GAME".center(50,"_"))
print()
with connection.cursor() as cursor:
    sql1=f"select login_status from status"  #THIS CODE CHECKS IF A USER IS ALREADY LOGGED IN OR NOT
    cursor.execute(sql1)
    result=cursor.fetchone()
if(result[0]==1):
    menu()
else:
    menu2()

            

