name = input("Type your name: ")
print("Wellcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?")

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')



elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or go to back: ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer  = input("You cross the bridge and meet a stranger.Do you talk to them(Yes/No).")

        if answer == "yes":
            print("You Talk to stranger they give you Some Gold and YOU WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended and YOU LOSE.")
        else:
             print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')


else:
      print("Not a valid option. You lose.")



