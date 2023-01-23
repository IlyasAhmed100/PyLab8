# Task 8.3


# Import
from random import randint

def main():
    print(printRandomJoke())

def printRandomJoke():
    joke1 = ("Why was the scarecrow good at his job?" '\n' "Because he was outstanding in his field")
    joke2 = ("What has a neck and cannot swallow" '\n' "A bottle")
    joke3 = ("What has eyes and cannot see?" '\n' "A needle")
    chosen_joke = randint(1,3)
    if printRandomJoke == 1:
        return joke1
    elif printRandomJoke == 2:
        return joke2
    else:
        return joke3

main()    
