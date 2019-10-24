def Hangman(word):
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     o     ",
              "|    /|\    ",
              "|    / \    ",
              "|           "
              ]
    rletter = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to hangman!")
    print(board)
    while wrong < len(stages) - 1:
        print("\n")
        print("Expect a Word in the board words.")
        msg = "Word:"
        char = input(msg)
        if char in rletter:
            cind = rletter.index(char)
            board[cind] = char
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        life = 8 - e
        print(f"life:{life}")
        print("\n".join(stages[0:e]))
        if not "_" in board:
            win = True
            print("You Win!")
            break
    if win == False:
        print("Stop it! Hangman's life is already 0!")
        print(f"The answer is {rletter}")

Hangman("volcano")
