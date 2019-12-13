from random import randint
print('##############################################################')

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




#Main Program
C = []
c1 = []
p1 = []
P = []
cc = list(range(1,13))
pc = list(range(1,13))
print(cc,pc)
while True:
    i = randint(1,25)
    if not i in C:
        C.append(i)
    if len(C) == 25:
        break

while True:
    i = randint(1,25)
    if not i in P:
        P.append(i)
    if len(P) == 25:
        break


def play():
    while True:
        print('####################################################################')
        print('                   |> || |\ | /-   |--|')
        print('                   |> || | \| |__\ |__|')
        print('####################################################################\n\n')
        print('Computer:--->')
        print('=============')
        dply(C,c1,rev = 1)
        print('\n\nPlayer:--->')
        print('===========')
        dply(P,p1)
        while True:
            n = int(input('\nYour turn(Enter a no. b/w 1-25): '))
            if 0<n<26:
                p1.append(n)
                c1.append(n)
                break

        while True:
            i = randint(1,25)
            if not i in c1:
                c1.append(i)
                p1.append(i)
                print('Computer\'s no.:',i)
                break

        for j in cc:
            if j == 1:
                for i in range(5):
                    c = []
                    if C[i*6] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
                
            elif j == 2:
                for i in range(5):
                    c = []
                    if C[(i+1)*4] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j == 3:
                for i in range(5):
                    c = []
                    if C[i*4] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==4:
                for i in range(1,22,5):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==5:
                for i in range(2,23,5):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==6:
                for i in range(3,24,5):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==7:
                for i in range(4,25,5):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==8:
                for i in range(5):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==9:
                for i in range(5,10):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==10:
                for i in range(10,15):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==11:
                for i in range(15,20):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
            elif j ==12:
                for i in range(20,15):
                    c = []
                    if C[i] in c1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:cc.pop(j-1)
        for j in pc:
            if j == 1:        
                for i in range(5):
                    c = []
                    if P[i*6] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
                
            elif j == 2:
                for i in range(5):
                    c = []
                    if P[(i+1)*4] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j == 3:
                for i in range(5):
                    c = []
                    if P[i*4] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==4:
                for i in range(1,22,5):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==5:
                for i in range(2,23,5):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==6:
                for i in range(3,24,5):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==7:
                for i in range(4,25,5):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==8:
                for i in range(5):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==9:
                for i in range(5,10):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==10:
                for i in range(10,15):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==11:
                for i in range(15,20):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
            elif j ==12:
                for i in range(20,15):
                    c = []
                    if P[i] in p1:c.append(1)
                    else:c.append(0)
                else:
                    if not 0 in c:pc.pop(j-1)
                            

        if len(cc) == 7:return 0
        elif len(pc) == 7:return 1

r = play()

        
