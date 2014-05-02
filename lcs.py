s = "roger"
t = "aidig"
# len(s) = 9, len(t) = 12
m = len(t)
# includes characters at index i (in s) and index j (in t)
def lookup(s,t,i,j):
	if i == len(s) or j == len(t):
		return 0
	elif s[i] == t[j]:
		return 1 + lookup(s,t,i+1,j+1)
	else:
		return max(lookup(s,t,i+1,j),lookup(s,t,i,j+1))

# includes characters at index i (in s) and index j (in t)
def lookup_new(s,t,i,j):
	return lookup(s[:(i+1)],t[:(j+1)],0,0)

# returns height of maximum node along half-way line
def max_node(s,t,node_max,length,cur_node):
	half_idx = (len(s)-1)/2
	if cur_node < len(t):
		f = lookup(s,t,half_idx,cur_node)
		g = lookup_new(s,t,half_idx,cur_node)
		if f + g >= length:
			return max_node(s,t,cur_node,f+g,cur_node+1)
		else:
			return max_node(s,t,node_max,length,cur_node+1)
	else:
		return node_max

new_s = " " + s + " "
new_t = " " + t + " "
lst = []
def hershies(new_s,new_t,p):
	half_idx = (len(new_s)-1)/2
	n = max_node(new_s,new_t,0,0,0)
	if len(new_s) > 2:
            if n+p-1 != m:
                lst.append(n+p-1)
		# left side of divide and conquer
	    hershies(new_s[:(half_idx+1)],new_t[:(n+1)],p)
		# right side of divide and conquer
	    hershies(new_s[half_idx:],new_t[n:],n+p)

#print 
def hershies_rv(s,t):
    hershies(" "+s+" "," "+t+" ",0)
 ##   print "her rets %r %r result %r" % (s,t,list(set(lst)))
    # same as len(lst)
#    print "w set lst %r" % list(set(lst))
    return list(set(lst))
def clr () :
    lst[:] = []

g=hershies_rv(new_s,new_t)
indices = list(set(lst))
##print g
##print indices
