def almostIncreasingSequence(sequence):
    removed = False
    length = len(sequence)
    i=0
    
    while i < len(sequence)-1:
        
        if(sequence[i]>=sequence[i+1]):
            if(removed==False):
                
                if (i+2<len(sequence) and sequence[i]<sequence[i+2] or i+1 == len(sequence)-1):
                    print("Hi")
                    del sequence[i+1]
                    
                else:
                    del sequence[i]
                    
                removed = True
                i=-1
            else:
                removed = False

        i+=1
        
    return removed