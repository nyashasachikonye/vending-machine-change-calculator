#Title: Assignment 5: Question 3
#Description: A program to calculate the change for a vending machine
#Authour: Kuziwa Sachikonye
#Date: 30/03/2012

from __future__ import print_function

cost = int(input("Enter the cost (in cents):\n"))
cash = 0

def main(cash,cost):

    while cost > cash:

        print("Deposit a coin or note (in cents):")
        x = int(input())
        cash = cash + x
        change = cash-cost

        if change > 0:
            print("Your change is:")

            if change >= 500:
                k = int(change/500)

                print(k,"x R5")

                change = change - k*500
                
            if 500 > change >= 200:

                k = int(change/200)
                print(k,"x R2")

                change = change - k*200

            if 200 > change >= 100:

                k = int(change/100)
                print(k,"x R1")

                change = change - k*100

            if 100 > change >= 50:

                k = int(change/50)

                print(k,"x 50c")

                change = change - k*50

            if 50 > change >= 20:

                k = int(change/20)
                print(k,"x 20c")

                change = change - k*20

            if 20 > change >= 10:

                k = int(change/10)
                print(k,"x 10c")

                change = change - k*10

            if 10 > change >= 5:

                k = int(change/5)

                print(k,"x 5c")

                change = change - k*5

        #print(change)

main(cash,cost)
