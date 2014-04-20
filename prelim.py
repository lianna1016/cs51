Class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

bacteria = ("bacteria", ['A','A','T','A'])
plant = ("plant" , ['A', 'A', 'A', 'T'])    
fish = ("fish", ['C', 'C', 'T', 'A'])
human = ("human", ['G', 'C', 'T', 'G'])
                                    
elements = [bacteria, plant, fish, human]

for theelement in elements :
    print theelement
   
def create_tree (el = elements) :
    b = Node (el[0])
    p = Node (el[1])
    b.add_child(p)
    print b.children
#f = Node(fish)
#h = Node (human)
create_tree()
#INSERT UP
#INSERT DOWN
#if len(b.children) == 0 : 
# create new node, add as child
#if len(b.children) == 1 :
# go to the next child
#if len(b.children) == 2 : 
# compare similarities between node we want to create and 2 children
# traverse the branch with more similarity
