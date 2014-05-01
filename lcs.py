t = "pinea"
s = "palech"

# finds longest common subsequence of suffixes
def lookup(s,t,i,j):
	if i == len(s) or j == len(t):
		return 0
	elif s[i] == t[j]:
		return 1 + lookup(s,t,i+1,j+1)
	else: 
		return max(lookup(s,t,i+1,j),lookup(s,t,i,j+1))

# # finds longest common subsequence of prefixes
def lookup_new(s,t,i,j):
	return lookup(s[:(i+1)],t[:(j+1)],0,0)

# s, t are our two input strings, node_max keeps track of the node that
# yields the current maximum LCS length, length keeps track of the 
# maximum LCS length, cur_node is a counter that traverses from 0 to 
# len(t)-1
def max_node(s,t,node_max,length,cur_node):
	if cur_node < len(t):
		f = lookup(s,t,len(s)/2,cur_node)
		g = lookup_new(s,t,len(s)/2,cur_node)
		if f + g >= length:
			return max_node(s,t,cur_node,f+g,cur_node+1)
		else:
			return max_node(s,t,node_max,length,cur_node+1)
	else:
		return node_max

# list that we want to store list of row numbers in
lst = []
def hershies(s,t,p):
	n = max_node(s,t,0,0,0)
	if n != 0:
		lst.append(n+p)
		hershies(s[:len(s)/2],t[:n],0)
		hershies(s[len(s)/2:],t[n:],n+p)

# want to find list of unique integers in lst
# hershies(s,"@" + t,0)

def hershies_rv(s, t) :
    hershies(s,t,0)
    print "s"
    print s
    print "t"
    print t
    print "lst"
    print lst    
    return len(lst)
    
def clr ():
    lst[:] = []

# print len(lst)
# similarity_value = len(lst)
# print similarity_value
# print lst
