# https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

def step1(Sequence):          #remove all zeros from the string
  Sequence
def step2(Sequence):          #sort the sequence in descending order  
  
def step4(Sequence):          #Subtract 1 from the first N elements
  
def hh(Sequence):               #Havel-Hakimi Algorithm
    Sequence = warmup1(Sequence)
    if len(Sequence) == 0:
      return True
    Sequence = warmup2(Sequence)
    N = Sequence.pop()          #step3 starts here and ends at step4
    if N > len(Sequence):
      return False
    Sequence = step4(Sequence)
    value = hh(Sequence)
    return value
    
################################################################################################################
#main
Sequence_1 = []
value = hh(Sequence_1)
