#gets functions from phylotree
import phylotree
from sys import argv
#get text file names
script, namefile, dnafile = argv

#opens files, gets info and creates list from them into mainlist
f = open(namefile, "r")
namelist = f.readlines()
namelist = [s.strip('\n') for s in namelist]
g = open(dnafile, "r")
dnalist = g.readlines()
dnalist = [r.strip('\n') for r in dnalist]
mainlist = zip(namelist, dnalist)

#creates tree for mainlist elements, gets results
phylotree.clr_glst()
phylotree.create_tree(mainlist)
dalst = phylotree.get_glst()
mainstr = phylotree.str_dalst(mainlist)

#prints tree
print "tree of %r" % mainstr
print dalst[0]

#closes text files
g.close()
f.close()
