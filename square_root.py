#cesar marroquin
#assignment 1
guess = 1
epsilon = .01
marginOfError = True
iteration = 0
notNum = True
while notNum:
    try:
       #val = int(user_input)
       user_input = int(input("Please Enter a positive number: "))
       notNum = False
    except ValueError:
       print("That's not a number!")

if user_input == 0:
    print("The square root of 0 is: 0")
elif user_input < 0:
    user_input = user_input * -1
    realpart = user_input**(1/2)
    imaginary = complex(realpart, 1)
    print(imaginary)
else:
    while marginOfError:
        best_guess = abs((guess * guess) - user_input)
        iteration += 1
        if best_guess < 0.01:
            marginOfError = False
            print("The square root of", user_input , "is", round(guess, 2))
        else:
            guess = abs((guess + user_input / guess) / 2)
            print("guess number", iteration ,"is: ",guess)
