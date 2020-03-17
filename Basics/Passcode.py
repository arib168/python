''' This is a program for mimicking the behavior of simple mobile passcode. The program include usage of
time library, variable, a function, looping construct, string concatenation, break statement, if conditional statement'''

import time     # importing time library for timer
lock = 2580     # Store password
i = 5

def stimer(j):
    while(j>=0):
                print(j,end=' ')
                time.sleep(0.1)
                j=j-1

while(i>=0):
    guess = int(input('Enter your password'))
    if guess == lock:
        print('Access Granted')
        break
    else:
        if(i == 0):
            print(" Chances Over. Wait for 10 seconds")
            stimer(10)
            i =5
        else:
            print(" Wrong Password. You have " +str(i)+"chances remaining")
            i=i-1
