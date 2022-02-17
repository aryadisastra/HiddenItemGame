x = 4 #posisi vertical
y = 1 #posisi horizontal

play    =  True 
posisi  =  "X" #posisi player
jalan   =  "." #jalan untuk dilalui
item    =  "$" #hidden item

board = [["#" for a in range(8)] for b in range(6)] #deklarasi board
#penempatan rintangan, player, item dan jalan
board[x][y] = posisi
board[1][1] = jalan
board[1][2] = jalan
board[1][3] = jalan
board[1][4] = jalan
board[1][5] = jalan
board[1][6] = jalan
board[2][1] = jalan
board[2][5] = jalan
board[2][6] = item
board[3][1] = jalan
board[3][2] = jalan
board[3][3] = jalan
board[3][5] = jalan
board[4][3] = jalan
board[4][4] = jalan
board[4][5] = jalan
board[4][6] = jalan

print('"X" : Posisi Anda')
print('"#" : Rintangan (Jika Terkena Akan Kalah)')
print('"." : Jalan Yang Bisa Dilalui')
print('"$" : Hidden Item')
print('')

while play == True :
    for i in board:
        print(''.join(i))

    print('Petunjuk :')
    print('Atas  : W')
    print('Bawah : S')
    print('Kiri  : A')
    print('Kanan : D')

    navigasi = input('Masukan Pilihan : ')
    if navigasi.lower() == 'w' : #bergerak ke atas
        board[x][y] = '.'
        x -= 1
        if board[x][y] == '#':
            board[x][y] = '#'
            print('Kamu Kalah')
            play = False
        elif board[x][y] == '$':
             board[x][y] = '$'
             print('Kamu Menang Selamat')
             play = False
        else : board[x][y] = 'X'
    elif navigasi.lower() == 's' : #bergerak ke atas
        board[x][y] = '.'
        x += 1
        if board[x][y] == '#':
            board[x][y] = '#'
            print('Kamu Kalah')
            play = False
        elif board[x][y] == '$':
             board[x][y] = '$'
             print('Kamu Menang Selamat')
             play = False
        else : board[x][y] = 'X'
    elif navigasi.lower() == 'a' : #bergerak ke atas
        board[x][y] = '.'
        y -= 1
        if board[x][y] == '#':
            board[x][y] = '#'
            print('Kamu Kalah')
            play = False
        elif board[x][y] == '$':
             board[x][y] = '$'
             print('Kamu Menang Selamat')
             play = False
        else : board[x][y] = 'X'
    elif navigasi.lower() == 'd' : #bergerak ke atas
        board[x][y] = '.'
        y += 1
        if board[x][y] == '#':
            board[x][y] = '#'
            print('Kamu Kalah')
            play = False
        elif board[x][y] == '$':
             board[x][y] = '$'
             print('Kamu Menang Selamat')
             play = False
        else : board[x][y] = 'X'