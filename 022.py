"""
file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. 
So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?"""


LETTERS = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def scores():
    names = readnames('names.txt')
    return sum(name_score(name, i) for (i, name) in enumerate(names, 1))

def readnames(filename):
    nlists = file(filename).read().split(',')
    return sorted(nlists)

def name_score(name, i):
    '"ABBEY"'
    name = name[1:-1]
    return sum(LETTERS.index(w) for w in name) * i



