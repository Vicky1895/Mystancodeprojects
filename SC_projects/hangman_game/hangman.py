"""
File: hangman.py
Name: Vicky
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    User input one character each round to guess the word.
    Players have N_TURNS chances to try and win this game.
    """
    word = "REFUND"
    # word = random_word()
    find_word = ''  # 將單字依字母數轉為'-'
    for i in range(len(word)):
        ch = word[i]
        if ch.isalpha() is True:
            find_word = find_word + '-'
    print('The word looks like: ' + find_word)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    input_ch = input('Your guess: ').upper()  # 將猜的字母轉為大寫
    if input_ch.isalpha() is False:
        print('Illegal format.')
        input_ch = input('Your guess: ').upper()
    else:
        time = N_TURNS
        while time > 0:
            if word.find(input_ch) < 0:  # 猜字未在單字中時
                time = time - 1
                find_word = replace(word, find_word, input_ch)
                print("There is no " + input_ch + "'s in the word.")
                print('The word looks like: ' + find_word)
                print('You have ' + str(time) + ' wrong guesses left.')
            else:  # 猜字在單字中時
                find_word = replace(word, find_word, input_ch)
                if find_word == word:  # 完全猜中時跳出迴圈
                    break
                else:  # 猜中時顯示出猜中字母位置
                    print('You are correct!')
                    print('The word looks like: ' + find_word)
                    print('You have ' + str(time) + ' wrong guesses left.')
            input_ch = input('Your guess: ').upper()
        if word == find_word:
            print('You are correct!')
            print('You win!!')
        else:
            print("There is no " + input_ch + "'s in the word.")
            print('You are completely hung :(')
        print('The answer is: ' + word)


def replace(word, find_word, input_ch):
    i = word.find(input_ch)
    if i < 0:
        return find_word
    else:
        ans = find_word[:i]
        ans = ans + input_ch
        ans = ans + find_word[i+len(input_ch):]
        return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
