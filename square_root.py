guess = 1
running = True

user_number = int(input("pick a number: "))

while running:
    best_guess = abs(user_number - guess**2)
    if best_guess <= 0.01:
        running = False
        rounded = round(best_guess, 2)
        print("You have found apprx. square-root: ", rounded)
    else:
         guess = (guess + user_number/guess) / 2
