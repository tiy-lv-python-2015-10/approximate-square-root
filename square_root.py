guess = 1
running = True

user_number = int(input("pick a number: "))

while running:
    best_guess = abs(user_number - guess**2)
    if best_guess <= 0.01:
        running = False
        print("You have found apprx. square-root: ", best_guess)
        
    else:
         guess = (guess + user_number/guess) / 2
