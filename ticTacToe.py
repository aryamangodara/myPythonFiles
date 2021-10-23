arr = ['1','2','3','4','5','6','7','8','9']

def drawBoard():
    print(arr[0] +" | " + arr[1]+" | "+arr[2])
    print("----------")
    print(arr[3] +" | " + arr[4]+" | "+arr[5])
    print("----------")
    print(arr[6] +" | " + arr[7]+" | "+arr[8])


drawBoard()

def markBoard(player, positon):
    char = 'O'
    if (player==1):
        char='X'
    arr[positon-1]=char

count=0
while (True):
    count+=1
    if (count%2==0):
        player = 2
    else:
        player = 1

    position = input("Player 1 enter the positon")