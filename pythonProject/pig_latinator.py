"""This code will turn any entered text into pig latin"""


def main():
    """
    This function will check if the first work is a vowel.
    If the condition is met, 'ay' is added to the end.
    Then it will check if the second letter is a vowel.
    If it's true, the first letter is moved to the end with 'ay'
    Otherwise, it will move the first two consonants to
    the end with 'ay'.
    """
    print("\nWelcome to the pig latinator")
    print("urntay anyhay entencesay intoway atinlay")

    vowels = ("a", "e", "i", "o", "u", "y")

    while True:
        raw_input = input("\n\ntype in a sentence (N to quit)\n")
        if raw_input.lower() == "n":
            break
        split_input = raw_input.split()
        output = ""
        for word in split_input:
            if word.startswith(vowels):
                vowel_word = word + "nay "
                output = output + vowel_word
            elif word[1:].startswith(vowels):
                consonant_word = word[1:] + word[0] + "ay "
                output = output + consonant_word
            else:
                cluster_word = word[2:] + word[0:2] + "ay "
                output = output + cluster_word
        print(output)


if __name__ == "__main__":
    main()
