# Task 8.2



# Defining Main

def main():
    raw_mark = float(input("What mark did you get in your test? We will tell you how you've done. Good Luck!" '\n'))
    print(Classification(raw_mark))

# Defining Classification
def Classification(score):
    if score >= 0 and score < 40:
        return ("Unfortunatly this score classifies as a fail!")
    elif score >= 40 and score < 50:
        return ("This score classifies as Third")
    elif score >= 50 and score < 60:
        return ("This score classifies as 2(ii)")
    elif score >= 60 and score < 70:
        return ("This score classifies as 2(i)")
    elif score >= 70 and score <= 100:
        return ("Congratulations, this score classifies as First!")
    else:
        return("Sorry this mark isn't possible!")

main()

