square = int(input("Enter a positive number"))
y = 1
counter = 0
square_root = True
while square_root:
    guess = abs(square - y**2)
    counter += 1
    if guess <= 0.01:
        square_root = False
    else:
        y = (y + square/y)/2
    print(counter, "{0:.2f}".format(y))

print("The square root of", square, "is {0:.2f}" .format(y))
