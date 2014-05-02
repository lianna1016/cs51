s = "rogerzoubelindazeng"
t = "charleszhangaidizhang"
a = " " + s
b = " " + t
m = len(a)
n = len(b)

# 2-dimensional array lev where lev[i][j] measures lev distance between
# the first i elements of s and the first j elements of t
lev = [[0 for i in range(n)] for j in range(m)]
# when one of the strings is the empty list, the lev distance is simply
# the number of additions needed to obtain the other string
for i in range(n):
	lev[0][i] = i
for j in range(m):
	lev[j][0] = j
# lev distance is the minimum out of three options, each corresponding
# to deletion, substitution and insertion
for j in range(1,m):
	for i in range(1,n):
		if a[j] == b[i]:
			sub = 0
		else:
			sub = 1
		lev[j][i] = min(lev[j][i-1]+1,lev[j-1][i]+1,lev[j-1][i-1]+sub)
# finally, find lev distance between s and t
print lev[m-1][n-1]