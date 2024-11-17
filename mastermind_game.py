import random

#player1 sets a num randomly
c=1
flag=0
while(c<=2):
    num = random.randrange(1000, 10000)#5672
    print(num)
    roun=0
    count=0
    s1 = str(num)
    correct=[0]*len(s1)
    winner=[0]*2
    i=0
    #player2 guess a number
    while(True):
        n=int(input("Guess a four digit number: "))
        count=0
        if(n==num):
            if(roun==0):
                print("Great! You guessed the number in just 1 try! You're a Mastermind!")
                flag=1
                break
            else:
                print("You've become a Mastermind!")
                print("It took you only", roun+1, "tries.")
                winner[i]=roun+1
                i+=1
                c+=1
                break
        else:
            s2=str(n)
            for i in range(0, len(s1)):
                if(s1[i]==s2[i]):
                    count+=1
                    correct[i]=s1[i]
                else:
                    correct[i]=0
            print("Not quite the number. But you did get ", count, " digit(s) correct!")
            print(correct)
            roun+=1
            count=0
    if flag==1:
        break
if(winner[0]<winner[1]):
    print(winner[0], "is the winner")
elif(winner[0]==winner[1]):
    print("Game drawn!!")
else:
    print(winner[1], "is the winner")

