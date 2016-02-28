import sys

def create_stench(filename):
    #print 'rohan'
    fp = open(filename, 'a')
    #fp.write('#rohan')

    rohan = '(if %s (and %s))'
    str2 = '(if %s (and %s %s))\n'
    str3 = '(if %s (and %s %s %s))\n'
    str4 = '(if %s (and %s %s %s %s))\n'
    monster = ''
    options = {2: str2, 3: str3, 4: str4}
    fp.write('#create stench in adjacent squares given a monster\n')
    for i in range(1, 5):
        for j in range(1, 5):
            #if (i==1 and j==1) or (i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2):
            #    continue
            stench = []
            monster = 'M_'+`i`+'_'+`j`
            if j-1>0:
                stench.append('S_'+`i`+'_'+`(j-1)`)
            if i+1<5:
               stench.append('S_'+`(i+1)`+'_'+`j`)
            if j+1<5:
               stench.append('S_'+`i`+'_'+`(j+1)`)
            if i-1>0:
                stench.append('S_'+`(i-1)`+'_'+`j`)
            if len(stench) == 2:
                #print str2 %(monster,stench[0],stench[1])
                s1 = str2 %(monster,stench[0],stench[1])
                fp.writelines(s1)
            if len(stench) == 3:
                #print str3 %(monster,stench[0],stench[1],stench[2])
                s3 = str3 %(monster,stench[0],stench[1],stench[2])
                fp.writelines(s3)
            if len(stench) == 4:
                #print str4 %(monster,stench[0],stench[1],stench[2],stench[3])
                s4 = str4 %(monster,stench[0],stench[1],stench[2],stench[3])
                fp.writelines(s4)

            #temp = options[len(stench)]
            #print temp
            #print temp %(monster,tuple(stench))
            #for i in range(len(stench)):
            #    print temp %(monster, stench[i])
            #print rohan %(monster,tuple(stench))


    fp.close()

def create_breeze(filename):
    #print 'rohan'
    fp = open(filename, 'a')
    #fp.write('#rohan')

    rohan = '(if %s (and %s))'
    str2 = '(if %s (and %s %s))\n'
    str3 = '(if %s (and %s %s %s))\n'
    str4 = '(if %s (and %s %s %s %s))\n'
    #monster = ''
    options = {2: str2, 3: str3, 4: str4}

    fp.write('#create breeze in adjacent squares given a pit\n')

    for i in range(1, 5):
        for j in range(1, 5):
            #if (i==1 and j==1) or (i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2):
            #    continue
            breeze = []
            pit = 'P_'+`i`+'_'+`j`
            if j-1>0:
                breeze.append('B_'+`i`+'_'+`(j-1)`)
            if i+1<5:
               breeze.append('B_'+`(i+1)`+'_'+`j`)
            if j+1<5:
               breeze.append('B_'+`i`+'_'+`(j+1)`)
            if i-1>0:
                breeze.append('B_'+`(i-1)`+'_'+`j`)
            if len(breeze) == 2:
                #print str2 %(pit,breeze[0],breeze[1])
                s1 = str2 %(pit,breeze[0],breeze[1])
                fp.writelines(s1)
            if len(breeze) == 3:
                #print str3 %(pit,breeze[0],breeze[1],breeze[2])
                s3 = str3 %(pit,breeze[0],breeze[1],breeze[2])
                fp.writelines(s3)
            if len(breeze) == 4:
                #print str4 %(pit,breeze[0],breeze[1],breeze[2],breeze[3])
                s4 = str4 %(pit,breeze[0],breeze[1],breeze[2],breeze[3])
                fp.writelines(s4)

def create_monster(filename):
    #print 'rohan'
    fp = open(filename, 'a')
    #fp.write('#rohan')

    rohan = '(if %s (or %s))'
    str2 = '(if %s (or %s %s))\n'
    str3 = '(if %s (or %s %s %s))\n'
    str4 = '(if %s (or %s %s %s %s))\n'
    #monster = ''
    #options = {2: str2, 3: str3, 4: str4}
    fp.write('#create monster in adjacent squares given a stench\n')
    for i in range(1, 5):
        for j in range(1, 5):
            monster = []
            stench = 'S_'+`i`+'_'+`j`
            if j-1>0:
                monster.append('M_'+`i`+'_'+`(j-1)`)
            if i+1<5:
               monster.append('M_'+`(i+1)`+'_'+`j`)
            if j+1<5:
               monster.append('M_'+`i`+'_'+`(j+1)`)
            if i-1>0:
                monster.append('M_'+`(i-1)`+'_'+`j`)
            if len(monster) == 2:
                #print str2 %(stench,monster[0],monster[1])
                s1 = str2 %(stench,monster[0],monster[1])
                fp.writelines(s1)
            if len(monster) == 3:
                #print str3 %(stench,monster[0],monster[1],monster[2])
                s3 = str3 %(stench,monster[0],monster[1],monster[2])
                fp.writelines(s3)
            if len(monster) == 4:
                #print str4 %(stench,monster[0],monster[1],monster[2],monster[3])
                s4 = str4 %(stench,monster[0],monster[1],monster[2],monster[3])
                fp.writelines(s4)

def create_pit(filename):
    #print 'rohan'
    fp = open(filename, 'a')
    #fp.write('#rohan')

    rohan = '(if %s (or %s))'
    str2 = '(if %s (or %s %s))\n'
    str3 = '(if %s (or %s %s %s))\n'
    str4 = '(if %s (or %s %s %s %s))\n'
    #monster = ''
    #options = {2: str2, 3: str3, 4: str4}
    fp.write('#create breeze in adjacent squares given a pit\n')
    for i in range(1, 5):
        for j in range(1, 5):
            pit = []
            breeze = 'B_'+`i`+'_'+`j`
            if j-1>0:
                pit.append('P_'+`i`+'_'+`(j-1)`)
            if i+1<5:
               pit.append('P_'+`(i+1)`+'_'+`j`)
            if j+1<5:
               pit.append('P_'+`i`+'_'+`(j+1)`)
            if i-1>0:
                pit.append('P_'+`(i-1)`+'_'+`j`)
            if len(pit) == 2:
                #print str2 %(breeze,pit[0],pit[1])
                s1 = str2 %(breeze,pit[0],pit[1])
                fp.writelines(s1)
            if len(pit) == 3:
                #print str3 %(breeze,pit[0],pit[1],pit[2])
                s3 = str3 %(breeze,pit[0],pit[1],pit[2])
                fp.writelines(s3)
            if len(pit) == 4:
                #print str4 %(breeze,pit[0],pit[1],pit[2],pit[3])
                s4 = str4 %(breeze,pit[0],pit[1],pit[2],pit[3])
                fp.writelines(s4)

def no_monsters_pits(filename):
    fp = open(filename,'a')
    rule = '(not %s)\n'
    fp.write('#rule 6: no monsters and pits in  (1,1), (1,2), (2,1), (2,2)\n')
    for i in range(1,3):
        for j in range(1,3):
            m = rule %('M_'+`i`+'_'+`j`)
            p = rule %('P_'+`i`+'_'+`j`)
            fp.write(m)
            fp.write(p)
    fp.close()

def rule_five(filename):
    s = '(xor %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s)\n'
    monsters = []
    fp = open(filename,'a')
    fp.write('#rule five: there is one and only one monster\n')
    for i in range(1,5):
        for j in range(1,5):
            monsters.append('M_'+`i`+'_'+`j`)
    temp = s %(monsters[0],monsters[1],monsters[2],monsters[3],monsters[4],monsters[5],monsters[6],monsters[7]
               ,monsters[8],monsters[9],monsters[10],monsters[11],monsters[12],monsters[13],monsters[14],monsters[15])
    #print temp
    fp.write(temp)
    fp.close()

def rohan(filename):
    s = '(not %s and not %s and not %s and not %s)\n'

    fp = open(filename)
    i = 2
    for j in range(1,4):
        list = []
        list.append('M_'+`i`+'_'+`j`)
        list.append('P_'+`i`+'_'+`j`)
        temp = s %(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7])
    fp.write(temp)
    fp.close()

def create_additional_info():
    fp = open('rohan_add.txt','w')
    for i in range(1,5):
        for j in range(1,5):
            fp.write('(not M_'+`i`+'_'+`j`+')\n')
            fp.write('(not P_'+`i`+'_'+`j`+')\n')
            fp.write('(not B_'+`i`+'_'+`j`+')\n')
            fp.write('(not S_'+`i`+'_'+`j`+')\n')


    fp.close()

def main(argv):
    #print argv[1]
    create_stench(argv[1])
    create_monster(argv[1])
    create_breeze(argv[1])
    create_pit(argv[1])
    rule_five(argv[1])
    no_monsters_pits(argv[1])
    #create_additional_info()

if __name__ == '__main__':
    main(sys.argv)