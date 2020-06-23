"""
Feedback paramaters:
Illegal move = -99
Mated in x = -40/x
Normal moves = positional advantage/disadvantage change from chess.com
Mate in x = +40/x
Take king = +99

Current problems:
The system needs to check 224 individual moves, not every piece to every spot. Phrase()
needs to be rewritten to account for this.

Future problems:
AI is always white using this system.
"""
inputs = [[]]
labels = [[]]
row = ["1", "2", "3", "4", "5", "6", "7", "8"]
column = ["a", "b", "c", "d", "e", "f", "g", "h"]
color = ["White", "Black"]
initial = []
def pieceswitch(n):
    switcher = {
        0: "Rook A",
        1: "Knight A",
        2: "Black Bishop",
        3: "Queen",
        4: "King",
        5: "White Bishop",
        6: "Knight B",
        7: "Rook B"
    }
    return  switcher.get(n, "ERROR")
def idtopiece(n):
    if (n > 8):
        return "Pawn " + column[n-8]
    else :
        return pieceswitch(n)
def fetchnumber(nrow, ncolumn, pieceid, ncolor):
    a = ((int(nrow) - 1) * 128)
    a += (column.index(ncolumn) * 16)
    a += (piece.index(idtopiece(pieceid)) * 2)
    if ncolor == "Black":
        a += 1
    return a
def phrase(n):
    print_phrase = ""
    black = 0
    i = 0
    while n > 128:
        n -= 128
        i += 1
    ii = 0
    while n > 16:
        n -= 16
        ii += 1
    iii = 0
    while n > 2:
        n -= 2
        iii = 0
    if n == 1:
        black = 0
    print_phrase = color[black] + " " + piece[iii] + " to " + column[ii] + row[i]
    return print_phrase
for x in range(1024):
    initial.append(0)
initial[fetchnumber("1", "a", "RookA", "White")] = 1
initial[fetchnumber("1", "b", "KnightA", "White")] = 1
initial[fetchnumber("1", "c", "Bishop", "White")] = 1
initial[fetchnumber("1", "d", "Queen", "White")] = 1
initial[fetchnumber("1", "e", "King", "White")] = 1
initial[fetchnumber("1", "f", "Bishop", "White")] = 1
initial[fetchnumber("1", "g", "KnightB", "White")] = 1
initial[fetchnumber("1", "h", "RookB", "White")] = 1
initial[fetchnumber("2", "a", "Pawn", "White")] = 1
initial[fetchnumber("2", "b", "Pawn", "White")] = 1
initial[fetchnumber("2", "c", "Pawn", "White")] = 1
initial[fetchnumber("2", "d", "Pawn", "White")] = 1
initial[fetchnumber("2", "e", "Pawn", "White")] = 1
initial[fetchnumber("2", "f", "Pawn", "White")] = 1
initial[fetchnumber("2", "g", "Pawn", "White")] = 1
initial[fetchnumber("2", "h", "Pawn", "White")] = 1
initial[fetchnumber("8", "a", "Rook", "Black")] = 1
initial[fetchnumber("8", "b", "Knight", "Black")] = 1
initial[fetchnumber("8", "c", "Bishop", "Black")] = 1
initial[fetchnumber("8", "d", "Queen", "Black")] = 1
initial[fetchnumber("8", "e", "King", "Black")] = 1
initial[fetchnumber("8", "f", "Bishop", "Black")] = 1
initial[fetchnumber("8", "g", "Knight", "Black")] = 1
initial[fetchnumber("8", "h", "Rook", "Black")] = 1
initial[fetchnumber("7", "a", "Pawn", "Black")] = 1
initial[fetchnumber("7", "b", "Pawn", "Black")] = 1
initial[fetchnumber("7", "c", "Pawn", "Black")] = 1
initial[fetchnumber("7", "d", "Pawn", "Black")] = 1
initial[fetchnumber("7", "e", "Pawn", "Black")] = 1
initial[fetchnumber("7", "f", "Pawn", "Black")] = 1
initial[fetchnumber("7", "g", "Pawn", "Black")] = 1
initial[fetchnumber("7", "h", "Pawn", "Black")] = 1
for x in range(1024):
    inputs[0].append(initial[x])
for x in range(1024):
    print(phrase(x))
    #continue this core loop