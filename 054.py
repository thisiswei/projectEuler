import doctest

#The file, 54.txt, contains one-thousand random hands dealt to two players.
#Each line of the file contains ten cards (separated by a single space): 
#the first five are Player 1's cards and the last five are Player 2's cards. 
#You can assume that all hands are valid (no invalid characters or repeated cards),
#each player's hand is in no specific order, and in each hand there is a clear winner.
#How many hands does Player 1 win?

files = file('54.txt').readlines()
hands = [h.replace('\n','') for h in files]

def result():
    dicts = {0:0, 1:0}
    for i in range(1000):
        h1, h2 = split_hand(hands[i])
        dicts[who_won(h1,h2)] +=1 
    return dicts

def split_hand(h):
    """ '8C TS KC 9H 4S 7D 2S 5D 3S AC'
    => ['8C', 'TS', 'KC', '9H', '4S']
       ['7D', '2S', '5D', '3S', 'AC'] 
    """
    h1 = h.split()
    return [h1[i] for i in range(5)], [h1[i] for i in range(5,10)]

def who_won(h1,h2):
    return h2 == max(h1,h2,key=hand_rank) 

def group(rank):
    """ [7,5,4,3,5] => [(2, 5), (1, 7), (1, 4), (1, 3)] """
    return sorted([(rank.count(r),r) for r in set(rank) ],reverse = True)

def unzip(group):
    return zip(*group)
 
def hand_rank(hand):
    """ ['8C', 'TS', 'KC', '9H', '4S'] """
    groups = group(['..23456789TJQKA'.index(r) for r,s in hand])
    count, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    points = {(4,1):7, 
              (3,2):6, 
              
              (3,1,1):3, 
              (2,2,1):2,
              (2,1,1,1):1,
              (1,1,1,1,1):0
              }
    straight = (max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5)
    flush = len(set([s for r,s in hand])) == 1 
    return max(points[count], 5*flush+4*straight),ranks


class Test:"""
>>> hands[0] 
'8C TS KC 9H 4S 7D 2S 5D 3S AC'
>>> split_hand('8C TS KC 9H 4S 7D 2S 5D 3S AC')
(['8C', 'TS', 'KC', '9H', '4S'], ['7D', '2S', '5D', '3S', 'AC'])
>>> hand_rank(['8C', 'TS', 'KC', '9H', '4S'])
(0, (13, 10, 9, 8, 4))
>>> hand_rank('4S 5S 8S 2S 4S'.split())
(5, (4, 8, 5, 2))
>>> hand_rank('5S 6H 7S 8C 9D'.split())
(4, (9, 8, 7, 6, 5))
>>> hand_rank('AH 5H 4H 3H 2H'.split())
(9, (5, 4, 3, 2, 1))
>>> hand_rank('AH KH QH JH TH'.split())
(9, (14, 13, 12, 11, 10))
>>> hand_rank('AH KH QH JH TH'.split()) > hand_rank('KH QH JH TH 9H'.split())
True
>>> unzip([(4, 5), (1, 7)]) == [(4, 1), (5, 7)]
True
>>> result()
{0: 376, 1: 624}
"""

print doctest.testmod()

    
    

