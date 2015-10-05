keep_going = True
guess = 1
max_error = 0.01

while keep_going:
    try:
        num = int(input("Enter a positive number > "))
        keep_going = False
    except:
        print("Pleass enter a positive number")

root = (num - guess ** 2)

while abs(root) >= max_error:
    guess = (guess + num / guess) / 2
    root = (num - guess ** 2)

rounded = round(guess, 2)
print("The rounded square root of {} is {}".format(num, rounded))
