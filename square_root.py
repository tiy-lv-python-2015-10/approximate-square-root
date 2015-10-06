guess = 1
user_num = int(input("Enter a positive number?"))  # input from user
square_root = True

while square_root:
  best_guess = abs(user_num - guess ** 2)
  if best_guess <= 0.01:
    square_root = False
    print(best_guess)
  else:
    guess = abs((guess + user_num/guess)//2)
