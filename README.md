cs51
====

Our cs51 phylogenetic tree project

Developers: The Zzzz's
Aidi Zhang
Belinda Zeng
Charles Zhang
Roger Zou

Instructions to Run Code:

    We coded everything in python, so all that is needed to run is to type “python phylotree.py” into the command line. A prompt will appear on the command line, and type h if you want to use hirschberg or l to use levenshtein. 

Files:
phylotree.py
    invariant: the phylogenetic tree takes a list.  (the function itself deals with a list that is sorted with respect to similarity to the root, but luckily, phylotree.py takes care of this invariant by sorting the list.)
lcs.py
    invariant: for the function hershies within this file, the length of the first input string must be greater than the length of the second input string, unless they are the same, in which case, does not matter
lev.py
    invariant: the function lev takes in 2 string inputs


