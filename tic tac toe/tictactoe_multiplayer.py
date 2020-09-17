board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']   
def DrawBoard():    
    print(" %c | %c | %c " % (board[0],board[1],board[2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[3],board[4],board[5]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[6],board[7],board[8]))    
    print("   |   |   ") 

def diogn(cha):
    if (board[0]==cha and board[4]==cha and board[8]==cha) or ( board[2]==cha and board[4]==cha and board[6]==cha):
        return True
def coln(cha):
    if (board[0]==cha and board[3]==cha and board[6]==cha) or (board[1]==cha and board[4]==cha and board[7]==cha) or (board[2]==cha and board[5]==cha and board[8]==cha):
        return True
def rows(cha):
    if (board[0]==cha and board[1]==cha and board[2]==cha) or (board[3]==cha and board[4]==cha and board[5]==cha) or (board[6]==cha and board[7]==cha and board[8]==cha):
        return True

def checkwin(cha):
    if diogn(cha)==True or coln(cha)==True or rows(cha)==True:
        return True
def isempty(mov):
    if board[mov]==' ':
        return True
    else:
        return False
while True:
    DrawBoard()
    while True:
        mov=input("X's move: ")
        try:
            mov=int(mov)-1
            if isempty(mov)==True:
                board[mov]='X'
                break
        except:
            pass
    DrawBoard()
    if checkwin('X')==True:
        print('X win')
        exit()
    while True:
        mov=input("O's move: ")
        try:
            mov=int(mov)-1
            if isempty(mov)==True:
                board[mov]='O'
                break

        except:
            pass
    if checkwin('O')==True:
        print('O win')
        exit()
    