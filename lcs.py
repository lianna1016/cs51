#testing
s = "roger"
t = "aidig"
m = len(t)
new_s = " " + s + " "
new_t = " " + t + " "

# global variable storage of results VERY IMPORTANT
# needs to be cleared after each use of hirschberg
lst = []

# finds largest distance from s[i],t[j] to the
# end of the two strings, distance is represented
# by the length of common subsequences between
# the two strings
def lookup(s,t,i,j):
	if i == len(s) or j == len(t):
		return 0
	elif s[i] == t[j]:
		return 1 + lookup(s,t,i+1,j+1)
	else:
		return max(lookup(s,t,i+1,j),lookup(s,t,i,j+1))

# includes characters at index i (in s) and index j (in t)
# does the same thing as lookup except from we are finding
# the the largest distance from s[0],t[0] to s[i]t[j]
def lookup_new(s,t,i,j):
	return lookup(s[:(i+1)],t[:(j+1)],0,0)

# returns height of maximum node along half-way line
def max_node(s,t,node_max,length,cur_node):
	# set the half-way line
	half_idx = (len(s)-1)/2
	# if our current node is still a letter within the string
	if cur_node < len(t):
		# check the lcs for the current node
		f = lookup(s,t,half_idx,cur_node)
		g = lookup_new(s,t,half_idx,cur_node)
		# if the lcs is greater than  or equal
		# to the stored greatest length
		if f + g >= length:
			# set the longest common subsequence
			# as the new greatest length
			# and go to the next letter in the string
			return max_node(s,t,cur_node,f+g,cur_node+1)
		else:
			# go to the next letter in the string
			return max_node(s,t,node_max,length,cur_node+1)
	else:
		# return the greatest length that we have
		return node_max


# repeatedly runs max_node 
def hershies(new_s,new_t,p):
	# the half-way line
	half_idx = (len(new_s)-1)/2
	# find the node along the half-way line where
	# the the longest common subsequence follows
	n = max_node(new_s,new_t,0,0,0)
	
	# if we aren't at the base case 
	if len(new_s) > 2:
		# don't add the values that aren't at an index
		# within the string
		if n+p-1 != m:
			lst.append(n+p-1)
		# left side of divide and conquer
		hershies(new_s[:(half_idx+1)],new_t[:(n+1)],p)
		# right side of divide and conquer
		hershies(new_s[half_idx:],new_t[n:],n+p)

# print 
def hershies_rv(s,t):
    hershies(" "+s+" "," "+t+" ",0)
    return list(set(lst))
# clear the list
def clr () :
    lst[:] = []

# testing
g=hershies_rv(new_s,new_t)
indices = list(set(lst))
# print indices to see testing results