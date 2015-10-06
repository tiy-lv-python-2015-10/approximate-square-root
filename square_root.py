guess = 1
root = int(input("Enter a positive number: "))
square_root = True
while square_root:
    best_guess = root - guess**2
    if best_guess <= 0.01:
        square_root = False
        print(best_guess)
    else:
        guess = (guess + root/guess)/2
