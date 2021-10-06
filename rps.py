import random
ai=['rock','paper','scissors']    #list for computer to pick a move
print("############## WELCOME TO ROCK PAPER SCISSORS ##############")

#game function
def main():
    q=int(input('\nChoose your move: \nrock(1),\npaper(2),\nscissors(3)\n'))
    print('\n')
    try:
        if q==1:
            pick='rock'
            print('User Picked: '+pick+'\n')
        elif q==2:
            pick='paper'
            print('User Picked: '+pick+'\n')
        elif q==3:
            pick='scissors'
            print('User Picked: '+pick+'\n')
        else:
            print('invalid input')
    except ValueError:
        print('invalid input')

    print("Computer's Turn\n")
    comp=random.choice(ai)      #computer picks a random value from the list 
    print("computer Picked: ",comp+'\n')

    #checking the result based on the moves.

    if pick=='rock' and comp=='paper':
        print('AI wins')
    elif pick=='rock' and comp=='scissors':
        print('Player wins')
    elif pick=='paper' and comp=='scissors':
        print('AI wins')
    elif pick=='paper' and comp=='rock':
        print('Player wins')
    elif pick=='scissors' and comp=='rock':
        print('AI wins')
    elif pick=='scissors' and comp=='paper':
        print('Player wins')
    else:
        print('draw')

main()


while True:
    ch=input("Play Again??(Y/N)").upper()
    if ch=='Y':
        main()
    elif ch=='N':
        break
    else:
        print('Invalid input')
