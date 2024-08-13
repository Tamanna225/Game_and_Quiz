import mysql.connector
mydb = mysql.connector.connect(host="localhost", user = "root", passwd="#t@m@nn@")                 #Sql Conectivity
mycursor = mydb.cursor()

from turtle import *
def q():                                                                              #Function for a quiz
    global mycursor
    mycursor.execute("Use quiz")
    quiz = input("Do you want to play quiz:")
    if quiz == "yes":
        print("what is red in colour and easy to it?")
        print("a. Bannana","b. Apple","c. Orange",sep="\n")
        A1 = input("Your answer:")
        o = "1"
        c1 = "b"
        if A1 == "b":
            print("correct")
            score = 1
        else:
            print("incorrect")
            score = 0
        mycursor.execute("Insert Into Score VALUES(%s,%s,%s,%s)",(o,A1,c1,score))
        print("what color are bannanas?")
        print("a. green","b. red","c. yellow",sep="\n")
        Ar = input("Your answer:")
        t= "2"
        c2 = "c"
        if Ar == "c":
            print("correct")
            score = score + 1
        else:
            print("incorrect")
            score = score
        mycursor.execute("Insert Into Score VALUES(%s,%s,%s,%s)",(t,Ar,c2,score))
        print("what color are oranges?")
        print("a. orange","b. blue","c. purple",sep="\n")
        Af = input("Your answer:")
        th="3"
        c3="a"
        if Af == "a":
            print("correct")
            score = score + 1
        else:
            print("incorrect")
            score = score
        print("Your score is:")    
        print(score)
        mycursor.execute("Insert Into Score VALUES(%s,%s,%s,%s)",(th,Af,c3,score))
        Column = ("Question Number","Your Choice","Correct Answer","Marks Obtained")
        print(Column)
        mycursor.execute("SELECT * FROM Score")
        results = mycursor.fetchall()
        for x in results:
            print(x)
        mydb.commit()
        input("press ENTER to EXIT")
    elif quiz == "no":
           input("press ENTER to EXIT")
    else:
         print("please answer in yes or no")
         q()
         
def qut():                                              #what to do
    que = input("what do you want to do?\n 1.Want to play a game\n 2.Want to take a quiz\n")
    
    if que == ("1"or"WANT TO PLAY A GAME"):                                 #to play snake game
        ID =input("Enter your identification number:\n")
        global mycursor
        mycursor.execute("USE Game")
        from random import randrange
        from freegames import square, vector

        food = vector(0, 0)
        snake = [vector(10, 0)]
        aim = vector(0, -10)

        def change(x, y):
            "Change snake direction."
            aim.x = x
            aim.y = y

        def inside(head):
            "Return True if head inside boundaries."
            return -370 < head.x < 360 and -300 < head.y < 290

        def move():
            "Move snake forward one segment."
            head = snake[-1].copy()
            head.move(aim)

            if not inside(head) or head in snake:
                square(head.x, head.y, 9, 'red')
                update()
                return

            snake.append(head)
 
            if head == food:
                print('Snake:', len(snake))
                food.x = randrange(-15, 15) * 10
                food.y = randrange(-15, 15) * 10
            else:
                snake.pop(0)

            clear()

            for body in snake:
                square(body.x, body.y, 9, 'green')

            square(food.x, food.y, 9, 'red')
            update()
            ontimer(move, 100)


        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: change(10, 0), 'Right')
        onkey(lambda: change(-10, 0), 'Left')
        onkey(lambda: change(0, 10), 'Up')
        onkey(lambda: change(0, -10), 'Down')
        move()
        done()
        sn = len(snake)
        snakes = str(snake)
        info = ("Identification Number","Your Score","You Collected Food At")
        print(info)
        mycursor.execute("Insert Into Score VALUES(%s,%s,%s)",(ID,sn,snakes))
        mycursor.execute("SELECT * FROM Score")
        result = mycursor.fetchall()
        for a in result:
            print(a)
        print("YOUR FINAL SCORE",sn)
    elif que == ("2"or"WANT TO TAKE A QUIZ"):
        q()
    else:
        print("Enter valid answer")
        qut()   
name = input("Hlo, What is your name:\n")                         #greeting
print("Hello! "+name)

def pas():                                                        #password
    password = input("Please enter password:\n")
    if password == "writerpf":
        print("Your password is correct")
        qut()    
    elif password == "satpf":
         print("Your password is correct")                 #you can ony take quiz with this password
         q()
    elif password == "Iamyourboss":                              #password for boss
         print("Welcome! Boss")
         boss = input("what you want me to do?\n")
         if boss == "WANT TO SEE THE CODE":                        #to introspect code
              ad = input("Enter additional passcode to access program: ")
              if ad == "qwerasdf":
                  print("you have entered correct password")
                  print("this program is related to the source code of this program. ")
                  ex = input("we want your identification: ")
                  if ex == "tamanna who made this":
                      n = open("project.py","r")
                      print(n.read())
                  else:
                      print("Wrong identification")
              else:
                  print("Wrong passcode entered") 
         else:
            print("Only available things are")
            qut()
    else:
        print("your password is incorrect\n","Please try again")
        pas()
pas()   
