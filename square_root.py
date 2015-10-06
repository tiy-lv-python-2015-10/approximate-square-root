keep_going = True
guess = 1
max_error = 0.01


#checks user input for a positive number
while keep_going:
    try:
        num = int(input("Enter a positive number > "))
        if num < 0:
            print("That's a negative number. Try again.")
            continue
        keep_going = False
    except:
        print("Pleass enter a positive number > ")

# when root +- .01 away from 0, guess == the square root (approximately)
root = (num - guess ** 2)
count = 1

# while root +- .01 away from 0, run loop until it is
while abs(root) >= max_error:
    print("Guess #{} : {}".format(count, guess))
    guess = (guess + num / guess) / 2
    root = (num - guess ** 2)
    count += 1

#prints each guess and what number guess it is
print("Guess #{}: {}".format(count, guess))

#rounds to 2 decimal places and prints 
rounded = round(guess, 2)
print("The rounded square root of {} is {}".format(num, rounded))
