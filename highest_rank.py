#Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

#Note: no empty arrays will be given. Max size 100.

#Examples
#[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
#[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
#[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3


def highest_rank(arr):
    hash_me = [0]*100
    for i in arr:
        hash_me[i] += 1
    highest_freq = max(hash_me)
    index_of_highest_freq = len(hash_me) - 1 - hash_me[::-1].index(highest_freq)
    return index_of_highest_freq
    
