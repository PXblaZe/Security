from random import randint
print('####################################################################')

def dply(L1, L2, hw = '*', rev = False):
    if rev:
        print('----------------')
        for i in L1:
            print('|',end="")
            if i in L2:print(str(i).rjust(2),end = '')
            else:print(hw.rjust(2),end = '')
            if not (L1.index(i)+1)%5:print('|\n----------------')
    else:
        print('----------------')
        for i in L1:
            print('|',end="")
            if i in L2:print(hw.rjust(2),end = '')
            else:print(str(i).rjust(2),end = '')
            if not (L1.index(i)+1)%5:print('|\n----------------')


def play():
    go = False
    C = []
    c1 = []
    p1 = []
    P = []
    cc = list(range(12))
    pc = list(range(12))
    while True:
        i = randint(1, 25)
        if not i in C:
            C.append(i)
        if len(C) == 25:
            break

    while True:
        i = randint(1, 25)
        if not i in P:
            P.append(i)
        if len(P) == 25:
            break
    while True:
        print('####################################################################')
        print('                   |> || |\ | /-   |--|')
        print('                   |> || | \| |__\ |__|')
        print('####################################################################\n\n')
        print('Computer:--->')
        print('=============')
        dply(C, c1, rev=1)
        print('\n\nPlayer:--->')
        print('===========')
        dply(P, p1)
        if not go:
            cd = input('Let\'s start the match!!!(Y/n): ')
            if cd.lower() == 'y':
                go = True
            elif cd.lower() == 'n':
                print('As your wish we will play later.')
                break
            else:
                pass

        if len(cc) <= 6 and len(pc) <= 6:
            return -1
        elif len(cc) <= 6:
            return 0
        elif len(pc) <= 6:
            return 1

        while True:
            n = int(input('\nYour turn(Enter a no. b/w 1-25): '))
            if 0 < n < 26:
                p1.append(n)
                c1.append(n)
                break

        while True:
            i = randint(1, 25)
            if not i in c1:
                c1.append(i)
                p1.append(i)
                print("\nComputer's no.:", i)
                break

        for j in cc:
            if j == 0:
                c = []
                for i in range(5):
                    if C[i * 6] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))

            if j == 1:
                c = []
                for i in range(5):
                    if C[(i + 1) * 4] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 2:
                c = []
                for i in range(5):
                    if C[i * 4] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 3:
                c = []
                for i in range(1, 22, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 4:
                c = []
                for i in range(2, 23, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 5:
                c = []
                for i in range(3, 24, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 6:
                c = []
                for i in range(4, 25, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 7:
                c = []
                for i in range(5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 8:
                c = []
                for i in range(5, 10):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 9:
                c = []
                for i in range(10, 15):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 10:
                c = []
                for i in range(15, 20):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j == 11:
                c = []
                for i in range(20, 15):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
        for j in pc:
            if j == 0:
                c = []
                for i in range(5):
                    if P[i * 6] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))

            if j == 1:
                c = []
                for i in range(5):
                    if P[(i + 1) * 4] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 2:
                c = []
                for i in range(5):
                    if P[i * 4] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 3:
                c = []
                for i in range(1, 22, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 4:
                c = []
                for i in range(2, 23, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 5:
                c = []
                for i in range(3, 24, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 6:
                c = []
                for i in range(4, 25, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 7:
                c = []
                for i in range(5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 8:
                c = []
                for i in range(5, 10):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 9:
                c = []
                for i in range(10, 15):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 10:
                c = []
                for i in range(15, 20):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j == 11:
                c = []
                for i in range(20, 15):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))


#Main Program
r = play()
if r == -1:print('It\'s a Draw !!!')
elif r:print('You Won !!!')
elif not r:print('You Lose !!!')
