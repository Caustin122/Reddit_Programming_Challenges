# https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

def step1(Sequence):          #remove all zeros from the string
    while 0 in Sequence: 
        Sequence.remove(0)
    return Sequence

def step2(Sequence):          #sort the sequence in descending order  
    Sequence.sort(reverse=True)
    return Sequence

def step4(Sequence,N):          #Subtract 1 from the first N elements
    i=0
    while i < N:
        Sequence[i] -= 1
        i+=1
    return Sequence
        
def hh(Sequence):               #Havel-Hakimi Algorithm
    Sequence = step1(Sequence)
    if len(Sequence) == 0:
        return True
    Sequence = step2(Sequence)
    N = Sequence.pop()          #step3 starts here and ends at step4
    if N > len(Sequence):       #step3 removes the first element and makes sure that the number of remaining elements is less than the number that was removed
        return False
    Sequence = step4(Sequence, N)
    value = hh(Sequence)
    return value
    
################################################################################################################
#main
Sequence_1 = [15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]
value = hh(Sequence_1)
print(value)
