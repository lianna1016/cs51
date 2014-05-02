import lcs
import lev
#from sys import argv
#script, algorithm = argv
alg_fun = (raw_input("Type h for hirschberg, l for levenschtein: "))
# usage python phylotree.py algorithmname



class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, obj):
        self.children.append(obj)
    
    def add_parent(self, obj):
        self.parent = obj
    
    # this function was inspired by stack overflow http://stackoverflow.com/questions/20242479/printing-a-tree-datastructure-in-python
    def __str__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
        
    # this function was inspired by stack overflow http://stackoverflow.com/questions/20242479/printing-a-tree-datastructure-in-python
    def __repr__(self):
        return '<tree node representation>'
              
glst = []        
bacteria = ("bacteria", ['A','A','T','A'])
plant = ("plant" , ['A', 'A', 'A', 'T'])    
fish = ("fish", ['C', 'C', 'T', 'A'])
human = ("human", ['G', 'C', 'T', 'G'])


# elements must be a sorted list root, then most similar to root and so on 
# elements = [bacteria, plant, fish, human]

random_elements = [plant, fish, human, bacteria]

# creating dummy value of hirschberg so as not to get an error
#def hirschberg (el_string, second_s) :
#   x = abs(len(el_string) - len(second_s))
 #  y = x * (-1)
  # return y


def hirschberg(el_string, second_s) :
    global alg_fun
    if alg_fun == 'h':
        xl = len(lcs.hershies_rv(el_string, "@" + second_s))
        lcs.clr()
        return xl
    elif alg_fun == 'l' :
        ll = lev.lev(el_string, second_s)
        return ll
    else :
        print "Assuming levenschtein. Input: python phylotree.py h for hirschberg"
        alg_fun = 'l'
        hirschberg(el_string, second_s)
        
# take an unsorted element list and sort it
def sort_list (unsorted_lst) :
    root = unsorted_lst.pop(0)
    priority_lst = []
    # dalength = len(unsorted_lst)
    for element in unsorted_lst :
       print "srt %r %r" % (root[0],element[0])
       y = hirschberg (root[0], element[0])
       print "y"
       print y
       priority_lst.append(y)
    priority_lst, unsorted_lst = (list(x) for x in zip(*sorted(zip(priority_lst, unsorted_lst), key =lambda pair: pair[0])))
#    print "priority_lst"
#    print priority_lst
#    print "unsorted_lst"
#    print unsorted_lst
    # unsorted_lst.reverse()
    unsorted_lst.insert(0,root)
    return unsorted_lst
  
elements = sort_list(random_elements)
print "sorted list of ran el %r" % elements
# elements = sort_list (random_elements)
#print "random_elements"
#print random_elements

#INSERT UP
#insert up documentation thoughts
# node is object to be added to tree, recent is most recently added object

def insert_up (node, recent) :
    # if recent is the root
    #node = Node(nod)
    #recent = Node(recen)
# if recent.parent is None, means recent is root node, so add down from root node
    if recent.parent == None :
        # call insert down
        insert_down(node, recent)
    else:
    # so if the element is more similar to the parent node, keep calling insert up on the parent
    # compares hirschberg similarity values. Will change when hirschberg actual implemented
    # CASE similar to parent
        if hirschberg (node.data[0], recent.data[0]) < hirschberg (node.data[0], recent.parent.data[0]):  
            # else, call insert_up
            # head up tree, call parent
            insert_up(node, recent.parent)
      #      print "insert up %r %r" % (node.data, recent.parent.data)
    # CASE similar to recent
    # if the element is more similar to the recent, then call insert_down
        else :
            insert_down(node, recent)
     #       print "insert down %r %r" % (node.data, recent.data)


#INSERT DOWN
# n as node to add, baby as parent node we want to add from
def insert_down(n, baby): 
    # if we each a leaf
    if len(baby.children) == 0 : 
        # creeate new node, add node as a child to baby, make baby parent to child
        baby.add_child(n)
        n.add_parent(baby)
    # if there's one child, keep traversing
    elif len(baby.children) == 1 :
        # CASE more similar to child
        if hirschberg (n.data[0], baby.children[0].data[0]) >= hirschberg(n.data[0], baby.data[0]) :
        # go to the next child
            insert_down(n, baby.children[0])
        # CASE more similar to 
        else:
            baby.add_child(n)
            n.add_parent(baby)
    # if there's two children
    elif len(baby.children) == 2 : 
    # traverse the branch with more similarity
        if hirschberg (n.data[0],baby.children[0].data[0]) > hirschberg (n.data[0],baby.children[1].data[0]) :
            insert_down(n, baby.children[0])
        else: 
            insert_down(n, baby.children[1])

def create_tree (el = elements) :
    # insert the root
    glst.append( Node (el[0]))
    
    # insert the first child as a node
    glst.append( Node (el[1]))
    
    glst[0].add_child(glst[1])
    glst[1].add_parent(glst[0])
    
    # loop through the rest of the elements, calling insert up as necessary
    dalength = len(el)
    for x in range(2,dalength) :
       glst.append ( Node (el[x]))
       # no need to create glst[x-1] b/c should've already been created in past
       insert_up (glst[x], glst[x - 1])
       
   #    print glst[x].data     
   #    print glst[x].parent.data
       
    # print glst[x].children.data
   # print glst[0].data
    #print glst[1].data    
#f = Node(fish)
#h = Node (human)

create_tree()
print "let's hope this prints the tree"
print glst[0]

"""
print "lol"
for l in glst:
    print l.data[0]
#    print l.children
    if l.children != []:
        for ch in l.children:
            print "ch %r" % ch.data[0]
    else:
        print "no children :("
    if l.parent == None:
        print "None lol parent"
    else:
        print l.parent.data[0]
    print ""
"""    
    
 
