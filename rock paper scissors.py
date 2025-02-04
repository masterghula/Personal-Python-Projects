import random
# Scissors>Paper>Rock
check="Y"
while check=="Y":
    user=int(input("Choose one:\n1 for rock, 2 for paper, 3 for scissors\n"))
    bot=random.randint(1,3)
    dict={1:"rock",2:"paper",3:"scissors"}
    print(dict[user]+" vs "+dict[bot])
    if user==bot:
        print("Draw")
    elif (user==1 and bot==3) or (user==3 and bot==2) or (user==2 and bot==1):
        print("You win")
    else:
        print("You lose")
    check=input("Do you want to play again?\nY/N\n").upper()
# rock paper        l
# rock rock         d
# rock scissor      w
# paper rock        w
# paper paper       d
# paper scisor      l
# scissor rock      l
# scissor paper     w
# scissor scissor   d