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
#for user
choice = [rock, paper, scissors]
user_choice = int(input("Enter your choice (0 for stone, 1 for paper, and 2 for scissors): "))
if user_choice >= 0 and user_choice <= 2:
    print(choice[user_choice])

#for computer
computer_choice = random.randint(0, 2)
print("The computer chose: ")
print(choice[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!!")
elif computer_choice > user_choice:
    print("You lose!!")
elif user_choice > computer_choice:
    print("You win!!")
elif user_choice == computer_choice:
    print("Its a draw!!")


