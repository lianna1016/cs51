class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = []

    def add_child(self, obj):
        self.children.append(obj)
    
    def add_parent(self, obj):
        self.parent.append(obj)
              
        
bacteria = ("bacteria", ['A','A','T','A'])
plant = ("plant" , ['A', 'A', 'A', 'T'])    
fish = ("fish", ['C', 'C', 'T', 'A'])
human = ("human", ['G', 'C', 'T', 'G'])

elements = [bacteria, plant, fish, human]



for theelement in elements :
    print theelement
# creating dummy value of hirschberg so as not to get an error
def hirschberg (el_string, second_s) :
    len(el_string) 



#INSERT UP
#insert up documentation thoughts
# node is object to be added to tree, recent is most recently added object

def insert_up (node, recent) :
    # if recent is the root
# if recent.parent is None, means recent is root node, so add down from root node
    if False :
    #recent.parent == [] :
        # call insert down
        insert_down(node, recent)
    else:
    # so if the element is more similar to the parent node, keep calling insert up on the parent
    # compares hirschberg similarity values. Will change when hirschberg actual implemented
    # node[0] as name, node[1]as genome/DNA sequence
    # recent[0] as last added node's name, recent.parent[0] as the name of the node's parent
    
    # CASE similar to parent
        if hirschberg (node[0],recent[0]) < hirschberg (node[0],recent.parent[0]):  
            # else, call insert_up
            # head up tree, call parent
            insert_up(node, recent.parent)
    # CASE similar to recent
    # if the element is more similar to the recent, then call insert_down
        else :
            insert_down(node, recent)


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
        if hirschberg (n[0], baby.children[0]) >= hirschberg(node[0], baby) :
        # go to the next child
            insert_down(n, baby.children[0])
        # CASE more similar to 
        else:
            baby.add_child(n)
            n.add_parent(baby)
    # if there's two children
    elif len(baby.children) == 2 : 
    # traverse the branch with more similarity
        if hirschberg (node[0],baby.children[0]) > hirschberg (node[0],baby.children[1]) :
            insert_down(n, baby.children[0])
        else: 
            insert_down(n, baby,children[1])
def create_tree (el = elements) :
    # insert the root
    b = Node (el[0])
    # insert the first child as a node
    p = Node (el[1])
    b.add_child(p)
    p.add_parent(b)
    
    # loop through the rest of the elements, calling insert up as necessary
    dalength = len(el)
    for x in range(2,dalength) :
       insert_up (el[x],el[x - 1])
    
#f = Node(fish)
#h = Node (human)
create_tree()

