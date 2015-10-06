guess = 1
root = int(input("Enter a positive number: "))
keep_going = True

while keep_going:
    differance = abs(root - guess**2)
    if differance < 0.01:
        keep_going = False
        print(round(guess, 2))
    else:
        guess = (guess + root/guess)/2
