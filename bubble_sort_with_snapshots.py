def bubble(l):
    length = len(l)
    did_swap = True
    snapshots = []
    
    while did_swap:
        did_swap = False
        for i in range(length-1):            
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                did_swap = True
                print(l)
                snapshots.append(l[:])
        length -= 1
        
    print(snapshots)
    return snapshots
        
