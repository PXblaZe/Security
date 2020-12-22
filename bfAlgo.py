from time import time


def oStream(string): print(string)

def algo(lenP = 0, startsWith = '', endsWith = ''):

    chrs = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]
    
    if lenP == 0: 
        etr = ''
        while True:
            for j in range(len(chrs)): 
                oStream(startsWith + etr + chrs[j] + endsWith)
            if etr == '' or etr == chrs[-1]*len(etr):
                etr = chrs[0]*(len(etr)+1)
            else:
                for k in range(len(etr)-1, -1, -1):
                    if etr[k] == chrs[-1]: continue
                    else:
                        etr = etr[0:k] + chrs[chrs.index(etr[k])+1] + chrs[0]*len(etr[k+1:])
                        break
    elif lenP > 0:
        r = 1
        etr = chrs[0]*(lenP-1)
        while r <= len(chrs)**lenP:
            for j in range(len(chrs)): 
                oStream(startsWith + etr + chrs[j] + endsWith)
                r+=1
            if etr == '' or etr == chrs[-1]*len(etr):
                etr = chrs[0]*(len(etr)+1)
            else:
                for k in range(len(etr)-1, -1, -1):
                    if etr[k] == chrs[-1]: continue
                    else:
                        etr = etr[0:k] + chrs[chrs.index(etr[k])+1] + chrs[0]*len(etr[k+1:])
                        break           
    else:
        np = 0
        for a in range(1,1-lenP):
            np += len(chrs)**a
        etr = chrs[-1]*(-lenP-1)
        r = 1
        while r <= np:
            for j in range(-1, -len(chrs)-1, -1): 
                oStream(startsWith + etr + chrs[j] + endsWith)
                r+=1
            if etr == chrs[0]*len(etr):
                etr = chrs[-1]*(len(etr)-1)
            else:
                for k in range(len(etr)-1, -1, -1):
                    if etr[k] == chrs[0]: continue
                    else:
                        etr = etr[0:k] + chrs[chrs.index(etr[k])-1] + chrs[-1]*len(etr[k+1:])
                        break
                        

a = time()

algo(lenP=3)
b = time()
c = str(b-a)

input(c)
