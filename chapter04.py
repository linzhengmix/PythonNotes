


def mergeList(list):
    newlist = []
    for i in  range(len(list)-1):
        newlist.append(list[i]+', ')
    newlist.append('and '+list[-1])
    newlist = "".join(newlist)
    # print newlist
    return newlist

spam = ['apple','bananas','tofu','cats']
# print ", ".join(spam)
# print mergeList(spam)


grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.', '.', '.', '.', '.']]

def picTrans(list):
    for i in range(len(list)):
        print i
        for j in range(len(list[i])):
            print list[i][j],

picTrans(grid)
