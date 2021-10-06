import random

#Difficulty level 

def easy():                   
    f=open('hard.text','r')
    read=f.read()
    o=[]
    for i in read.split('\n'):
        o.append(i)
    word= random.choice(o)
    return word

def medium():
    f=open('intermediate.text','r')
    read=f.read()
    k=[]
    for i in read.split('\n'):
        k.append(i)
    word= random.choice(k)
    return word

def hard():
    f=open('easy.text','r')
    read=f.read()
    l=[]
    for i in read.split('\n'):
        l.append(i)
    word= random.choice(l)
    return word


def game(word):                 #Main function for games working
    ans=' _'*len(word)
    guess=6
    completed=False
    guessed_letters=[]
    guessed_words=[]
    print("############## WELCOME TO HANGMAN ##############")
    print('guesses left: '+str(guess),"\n")
    print(hang[guess])
    print(ans)
    print('\n')
    
    while not completed and guess>0:                    #if the user guesses a word
        x=input("\nenter your guess.").lower()
        if len(x)>1 and x.isalpha():
            if x==word:
                print("you win")
                break
            elif x in guessed_words:
                print('you already guessed ',+x)
            elif x!=word:
                print(x, "is not the word")
                guess-=1
                print("guesses left: ", str(guess))
                guessed_words.append(x)
            
                
        elif len(x)==1 and x.isalpha():             #if the user guesses a letter
            if x in guessed_letters:
                print('you already guessed ',x)
            elif x not in word:
                print(x, "is not in the word")
                guess-=1
                guessed_letters.append(x)

            else:
                print(x,"is in the word.")
                guessed_letters.append(x)
                wordl=ans.split()
                fill=[i for i, letter in enumerate(word) if letter == x]   #To fill in the blanks 
                for j in fill:
                    wordl[j]=x
                ans="  ".join(wordl)
                if "_" not in ans.split():            
                    break
        
                    
                
                

        else:
            print('Inavalid input')

        print(hang[guess])
        print('guesses left: '+str(guess))
        print(ans)
        print('\n')
    if completed:
        print("Congrats you found the word "+word)
    else:
        print('Sorry you lost the word was '+word+'\n Better Luck Next Time')


def main():      #loop to keep the game running
    try:
        q=int(input("Choose Difficulty: \neasy(1),\nintermediate(2),\nhard(3)\n"))
        if q==1:
            word=easy()
        elif q==2:
            word=medium()
        elif q==3:
            word=hard()
        else:
            print('invalid input')
    except ValueError:
        print('invalid input')
    game(word)
    while True:
        ch=input('Play Again(Y/N)').upper()
        if ch=='Y':
            try:
                    
                q=int(input("Choose Difficulty: \neasy(1),\nintermediate(2),\nhard(3)\n"))
                if q==1:
                    word=easy()
                elif q==2:
                    word=medium()
                elif q==3:
                    word=hard()
                else:
                    print('invalid input')
            except ValueError:
                print('invalid input')
            game(word)
        elif ch=='N':
            print("Thanks For Playing!!!")
            break
        else:
            print("invalid input")

# Hangman image 
hang= [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

main()
