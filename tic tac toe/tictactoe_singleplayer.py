import random
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

def compmove():
    while True:
        def lastmove():
            for i in range(0,9):
                if isempty(i)==True:
                    board[i]='O'
                    if checkwin('O')==True:
                        print('lastmov1')
                        board[i]='O'
                        return 1
                    else:
                        board[i]=' '
            for i in range(0,9):
                if isempty(i)==True:
                    board[i]='X'
                    if checkwin('X')==True:
                        print('lastmov2')
                        board[i]='O'
                        return 1
                    else:
                        board[i]=' '

        def draww():
            c=0
            for i in range(0,9):
                if board[i]=='X':
                    c=c+1
                if c==4:
                    for i in range(0,9):
                        if isempty(i)==True:
                            print('draww')
                            board[i]='O'
                            return 1
                '''else:
                    return 2'''
        def secondmov():
            c=0
            for i in range(0,9):
                if board[i]=='X':
                    c=c+1
            if c==1:
                while True:
                    x=random.randint(0,8)
                    if isempty(x)==True:     
                        print('seconmov')
                        board[x]='O'
                        return 1

        if secondmov()==1:
            break
        if lastmove()==1:
                break
        if draww()==1:
                    break
        '''elif secondmov()==2:
            if lastmove()==1:
                break
            elif lastmove()==2:
                if draww()==1:
                    break
                elif draww()==2:
                    pass
    '''





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
    compmove()
    if checkwin('O')==True:
        print('O win')
        DrawBoard()
        exit()