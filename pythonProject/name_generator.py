""" Generates a new name for you."""
import random


def main():
    """
    Randomly picks a first and last name
    out of the 2 tuples.
    """
    print("Welcome to the Wizard name generator")
    print("Meet your fantasy alter-ego")

    first = "Zed", "Merlin", "Oz", "Ozma", "Dorothy"
    last = ("the Magnificent", "the Enchanter",
            "of the West", "of the East", "of the North", "of the South")

    while True:
        first_name = random.choice(first)

        last_name = random.choice(last)

        print("\n\n")
        print(f"\033[1;31m{first_name} {last_name} \033[0m".center(40))
        print("\n\n")

        try_again = input("\n\nTry again? (Press ENTER or N to quit)\n")
        if try_again.lower() == "n":
            break


if __name__ == "__main__":
    main()
