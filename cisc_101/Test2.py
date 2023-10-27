
bingo=bingo=[[[1],[2],[3]],
       [[4],[5],[6]],
       [[7],[8],[9]]]

while True:

    yes = input()
    if bingo[0][0] == "SEEN" and bingo[0][1] == "SEEN" and bingo[0][2] == "SEEN" or \
            bingo[1][0] == "SEEN" and bingo[1][1] == "SEEN" and bingo[1][2] == "SEEN" or \
            bingo[2][0] == "SEEN" and bingo[2][1] == "SEEN" and bingo[2][2] == "SEEN" or \
            bingo[0][0] == "SEEN" and bingo[0][2] == "SEEN" and bingo[2][2] == "SEEN" "SEEN" and bingo[2][0] == "SEEN":

        print(*bingo,sep="\n")
        print("you win")
        break

    elif yes == "y":
        card = [9]
        print(bingo[2][2])
        print("YOUR CARD IS:"+str(card))

        for t in range(len(bingo)):
            for i in range(len(bingo[t])):
                if card == bingo[t][i]:
                    bingo[t][i] = "SEEN"



    elif yes != "y":
        break

