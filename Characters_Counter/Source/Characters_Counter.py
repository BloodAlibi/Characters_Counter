import time

#-----------

def Introduction():
  print("Welcome to Characters Counter. You will be able to count the number of characters of the sentence you provide.\nFor example, the program will return 5 for \"Hello!\", with 1x\"h\", 1x\"e\", 2x\"l\", 1x\"o\" and 1x\"!\".")

def Counter():
  word1 = " is "
  word2 = " character "
  count = 0
  letters = {}
  sentenceinput = input("\n--------------------------\nEnter below your sentence.\n>>>\t")
  for character in sentenceinput:
    char = character.lower()
    count += 1
    if not char in letters:
      letters[char] = 0
    letters[char] += 1
    if count > 1:
      word1 = " are "
      word2 = " characters "
  print("\n* There" + word1 + str(count) + word2 + "in the sentence you provided :")
  for letter,number in letters.items():
    if letter.isspace():
      print("\t[Space] : " + str(number))
    else:
      print("\t" + str(letter) + " : " + str(number))

#-----------

Introduction()
time.sleep(1)
while True:
  Counter()
  time.sleep(2)