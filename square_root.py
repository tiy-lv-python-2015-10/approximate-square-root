guess = 1
user_num = int(input("Enter a positive number? "))  # input from user
square_root = True

while square_root:
  best_guess = abs(user_num - guess **2)  # if the user num is < 0, the nuers is sqrted
  if best_guess < 0.01:
    square_root = False             # to make the loop stop
    print("The square root of",user_num,"is",guess)
  else:
    guess = round((guess + user_num/guess)/2)  # // to minimize the decimal
    print("guess another number")
