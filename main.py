import random


def rules():
  print("+++++++++Rules++++++++++")
  print("Please type your choice in lower case.\n")
  print("Best of luck!\n")


def get_user_choice():
  choice = input("Choose rock, paper, or scissors: ")
  return choice.lower()


def get_computer_choice():
  options = ["rock", "paper", "scissors"]
  choice = random.choice(options)
  print("The computer chose:", choice)
  return choice


def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "draw"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "user"
  elif user_choice == "paper" and computer_choice == "rock":
    return "user"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "user"
  else:
    return "computer"


def play_again():
  answer = input("Do you want to play again? (y/n): \n")
  return answer.lower() == "y"


def get_login():
  while True:
    print("Default username and password is : admin")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "admin":
      return True
    else:
      print("Incorrect username or password. Please try again.")


def display_lives(user_lives):
  print(f"You have {user_lives} lives remaining.\n")


def play_game():
  if not get_login():
    return

  user_lives = 3
  computer_lives = 3

  while True:
    display_lives(user_lives)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    if winner == "draw":
      print("It's a draw! Try again.")
    elif winner == "user":
      print("You won!")
      user_lives += 1
      computer_lives -= 1
      if computer_lives == 0:
        print("Congratulations! You won the game!\n")
        break
    else:
      print("Sorry, you lost. Try again.")
      user_lives -= 1
      computer_lives += 1
      if user_lives == 0:
        print("Sorry, you lost the game.\n")
        break

    play_again_choice = play_again()
    if play_again_choice:
      continue
    else:
      print("Thanks for playing!")
      break


if __name__ == "__main__":
  rules()
  play_game()

