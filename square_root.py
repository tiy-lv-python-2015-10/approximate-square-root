finding = True
guess = 1
user_number = int(input("Enter a postive number:"))
while finding:
    best_guess = abs(user_number - guess**2)
    if best_guess < 0.01:
        finding = False
        print("the squre root of your number is:", round(best_guess,2))
    else:
        guess = (guess + user_number/guess)/2
