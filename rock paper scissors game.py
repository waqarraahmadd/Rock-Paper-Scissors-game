import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
image = [rock, paper, scissors]

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if human >=3:
  print("You've entered an invalid number, you lose")
else:
  computer = random.randint(0,2)
  
  print(image[human])
  
  print(f"Computer chose {image[computer]}")  
  
  if human == 0 and computer == 1:
    print("You lose")
  elif human == 0 and computer == 2:
    print("You Win")
  elif human == 1 and computer == 0:
    print("You Win")
  elif human == 1 and computer == 2:
    print("You Loose")
  elif human == 2 and computer == 0:
    print("You lose")
  elif human == 2 and computer == 1:
    print("You Win")
  else:
    print("Draw")