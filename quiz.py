print("Welcome to my Quiz Game \n Interesting Game to play")
player = input("Do you want to play the game? \n")
if player.lower() !='yes' :
    print("Good Bye")
    quit()

name_player = input("Enter your name: ")
print("Let's start the game :)",name_player)

def cricket():
    score = 0
    answer = input("who is the captain of india right now?\n")
    if answer.lower() == 'rohit sharma':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("Which team won the 2024 t20 world cup?\n")
    if answer.lower() == 'india':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("which team won the 2024 ODI world cup?\n")
    if answer.lower() == 'australia':
        print("Correct")
        score += 1
    else:
        print("wrong")
    answer = input("which team won the 2024 ipl trophy?\n")
    if answer.lower() == 'kolkata knight riders':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("which women's team won the 2024 ipl trophy?\n")
    if answer.lower() == 'royal challenge bangalore':
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("You got the" + str(score) + "correct answers")
    print("You got the" + str((score / 5) * 100) + "correct answers")
def computer():
    score = 0
    answer = input("what is CPU stands for?\n")
    if answer.lower() == 'central processing unit':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("What is GPU stands for?\n")
    if answer.lower() == 'graphical processing unit':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("Mouse is an input device or output device?\n")
    if answer.lower() == 'input device':
        print("Correct")
        score += 1
    else:
        print("wrong")
    answer = input("what is ROM stands for?\n")
    if answer.lower() == 'read only memory':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("what is RAM stands for?\n")
    if answer.lower() == 'random access memory':
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("You got the" + str(score) + "correct answers")
    print("You got the" + str((score / 5) * 100) + "correct answers")
def politics():
    score = 0
    answer = input("who is the cm of AP in 2019 ?\n")
    if answer.lower() == 'ys jagan mohan reddy':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("Who is the pm of india in 2024 ?\n")
    if answer.lower() == 'narendra modi':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("who elected as three times of india prime minister?\n")
    if answer.lower() == 'narendra modi':
        print("Correct")
        score += 1
    else:
        print("wrong")
    answer = input("who is the cm of uttarpradesh ?\n")
    if answer.lower() == 'yogi adhityanadh':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("who is the president of india?\n")
    if answer.lower() == 'murmu':
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("You got the" + str(score) + "correct answers")
    print("You got the" + str((score / 5) * 100) + "correct answers")
def film():
    score = 0
    answer = input("who is the hero in BHAHUBALI ?\n")
    if answer.lower() == 'prabhas':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("Who is the director for kalki 2898 ?\n")
    if answer.lower() == 'nag ashwin':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("which actor named as first PAN india star in tollywood ?\n")
    if answer.lower() == 'prabhas':
        print("Correct")
        score += 1
    else:
        print("wrong")
    answer = input("who plays a role of ashwadhama in KALKI 2898?\n")
    if answer.lower() == 'amitabh bachan':
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answer = input("who is the best comedian in telugu industry ?\n")
    if answer.lower() == 'brahmanandham':
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("You got the" + str(score) + "correct answers")
    print("You got the" + str((score / 5) * 100) + "correct answers")


while True:
  print("A. cricket")
  print("B. computer")
  print("C. politics")
  print("D. film")
  print("E. Exit")
  choice =input("enter your choice: ")
  if choice == "a" or choice == "A":
      print("cricket")
      cricket()
  elif choice == "b" or choice == "B":
      print("computer")
      computer()
  elif choice == "c" or choice == "C":
      print("politics")
      politics()
  elif choice == "d" or choice == "D":
      print("food")
      film()
  elif choice == "e" or choice == "E":
      print("quit")
      quit()

