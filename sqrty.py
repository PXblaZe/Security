from os.path import isfile
class Account:
    __actfile = "UsersData.act"
    def __init__(self, file: str = __actfile):
        if '.' not in file:
            self.__actfile = file + '.act'
        else:
            self.__actfile = file
    def addAct(self):
        if not isfile(self.__actfile):
            nf = open(self.__actfile, 'w')
            nf.write('log0\n')
            nf.close()
        f = open(self.__actfile, 'a')
        print('Enter the detail in the form:--->')
        fname = input('First name: ')
        lname = input('Last name: ')
        l = []
        for i in self.__getActs():
            c = i.split('')
            l.append(c[2])
        l.append('')
        usrid = ''
        while usrid in l:
            usrid = input('User Id (Must contain a non alphanumeric character): ')
            if  usrid in l:
                print('Warning: User Id already exists...\nTry a new',end=' ')
        usrpwd = input('Password: ')
        f.write(fname)
        f.write('')
        f.write(lname)
        f.write('')
        f.write(str(usrid.encode()))
        f.write('')
        f.write(str(usrpwd.encode())+'\n')
        f.close()
    def __getActs(self):
        return open(self.__actfile, 'r').readlines()[1:]
    def login(self, usrid: str, usrpwd: str):
        l = self.__getActs()
        for i in range(len(l)):
            m = l[i].split('')
            if usrid == bytes(m[2]).decode() and usrpwd == bytes(m[3][:len(m[3])-1]).decode():
                open(self.__actfile,'w').write('log'+str(i+1)+'\n')
                open(self.__actfile,'a').writelines(l)
                return True
        else:
            return False
    def islogin(self, usrid: str):
        md = self.__getActs()
        l = int(open(self.__actfile,'r').readline()[-2])
        m = md[l-1].split('')
        if bytes(m[2]).decode() == usrid:
            return True
        else:
            return False
    def logout(self, usrid: str):
        if self.islogin(usrid):
            m = self.__getActs()
            open(self.__actfile,'w').write('log0\n')
            open(self.__actfile,'a').writelines(m)
