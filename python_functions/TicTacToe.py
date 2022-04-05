board =[' ' for x in range(10)]

def insertLettre(lettre, pos):
    board[pos] = lettre

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |  |')
    print('  '+board[1]+'| '+board[2]+'| '+board[3])
    print('   |  |')
    print('----------')
    print('   |  |')
    print('  '+board[4]+'| '+board[5]+'| '+board[6])
    print('   |  |')
    print('----------')
    print('   |  |')
    print('  '+board[7]+'| '+board[8]+'| '+board[9])
    print('   |  |')

def isWinner(board,lettre):
    return (board[7] == lettre and board[8]==lettre and board[9] ==lettre) or (board[4] == lettre and board[5]==lettre and board[6] ==lettre) or (board[1] == lettre and board[2]==lettre and board[3] ==lettre) or (board[1] == lettre and board[4]==lettre and board[7] ==lettre) or (board[2] == lettre and board[5]==lettre and board[8] ==lettre) or (board[3] == lettre and board[6]==lettre and board[9] ==lettre) or (board[1] == lettre and board[5]==lettre and board[9] ==lettre) or (board[3] == lettre and board[5]==lettre and board[7] ==lettre)

def playerMove():
    run = True
    while run:
        move = int(input('Please select a position to place an \'X\' (1-9): '))
        try:
            if move >0 and move<10:
                if spaceIsFree(move):
                    run = False
                    insertLettre('X',move)
                print('Sorry, this space is occupied!')
            print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen)>0:
        move = selectRandom(cornerOpen)
        return move
    if  5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move = selectRandom(edgesOpen)
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    return True

def main():
    print('Welcome to Tic Tac Toe!!')
    printBoard(board)
    while not(isBoardFull(board)):
        if isWinner(board,'O'):
            print('Sorry O\'s won the time!')
            break
        playerMove()
        printBoard(board)
        if isWinner(board,'X'):
            print('X\'s won the time! Good Job!')
            break
        move = compMove()
        if move ==0:
            print('Tie Game!')
        else:
            insertLettre('O',move)
            print('Computer placed an \'O\' in position ', move , ' :')
            printBoard(board)
    if isBoardFull(board):
        print('Tie Game!')

main()
