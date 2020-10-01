
def treePlanning(trees, d):
    # write your code here.
    res =[]
    lasttree =0
    for tree in trees:
        if lasttree<=0:
            lasttree =tree
        elif tree -lasttree>=d:
            lasttree =tree
        elif tree - lasttree< d:
            res.append(tree)
        print(str(tree)+'==='+str(lasttree))
    return res


ress=treePlanning([1,2,3,5,6],2)
print(ress)