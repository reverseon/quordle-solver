from solver import predict

FILEOPENER = open("wordlist.txt","r")
WORD_LIST = FILEOPENER.readlines()
FIRST_WORD = "raise"

print("Quordle Solver")
print("--------------")
print("Instruction: ")
print("Use 0 for grey response, 1 for yellow response, and 2 for green response separated with a comma. If the box is already guessed, just click enter.")
print("Ex: GREEN GREEN GREY YELLOW GREY")
print("In: 2,2,0,1,0")

for turn in range(9):
    print(f"Turn {turn+1}")
    if turn == 0:
        alrguessed = [False for _ in range(4)]
        doneguess = [False for _ in range(4)]
        tempans = ["" for _ in range(4)]
        candidate = [FIRST_WORD]
        sol1 = WORD_LIST[:]
        sol2 = WORD_LIST[:]
        sol3 = WORD_LIST[:]
        sol4 = WORD_LIST[:]
    else:
        candidate = list(dict.fromkeys(sol1 + sol2 + sol3 + sol4))
    for i in range(4):
        if doneguess[i] and tempans[i] in candidate:
            candidate.remove(tempans[i])
    bestguess, table1, table2, table3, table4 = predict(candidate, sol1, sol2, sol3, sol4)
    print(f"BEST GUESS: {bestguess.upper()}")
    inpbuf = input("Enter response for Box 1: ")
    resp1 = (2,2,2,2,2) if inpbuf == "" else tuple([int(x) for x in inpbuf.split(",")])
    inpbuf = input("Enter response for Box 2: ")
    resp2 = (2,2,2,2,2) if inpbuf == "" else tuple([int(x) for x in inpbuf.split(",")])
    inpbuf = input("Enter response for Box 3: ")
    resp3 = (2,2,2,2,2) if inpbuf == "" else tuple([int(x) for x in inpbuf.split(",")])
    inpbuf = input("Enter response for Box 4: ")
    resp4 = (2,2,2,2,2) if inpbuf == "" else tuple([int(x) for x in inpbuf.split(",")])
    sol1 = [] if doneguess[0] else table1[resp1]
    sol2 = [] if doneguess[1] else table2[resp2]
    sol3 = [] if doneguess[2] else table3[resp3]
    sol4 = [] if doneguess[3] else table4[resp4]
    if len(sol1) == 1 and alrguessed[0] == False:
        alrguessed[0] = True
        tempans[0] = sol1[0]
    if len(sol2) == 1 and alrguessed[1] == False:
        alrguessed[1] = True
        tempans[1] = sol2[0]
    if len(sol3) == 1 and alrguessed[2] == False:
        alrguessed[2] = True
        tempans[2] = sol3[0]
    if len(sol4) == 1 and alrguessed[3] == False:
        alrguessed[3] = True
        tempans[3] = sol4[0]
    if any(alrguessed):
        for i in range(4):
            if alrguessed[i]:
                print(f"Box {i+1} answer is {tempans[i].upper()}")
    if bestguess in tempans:
        doneguess[tempans.index(bestguess)] = True
    if all(doneguess):
        print("All boxes are answered, exiting...")
        exit(0)
print("Failed to guess after 9 turns, exiting...")
