def findSingle(A, ar_size): 
    for i in range(ar_size): 
        count = 0
        for j in range(ar_size):  
            if(A[i] == A[j]): 
                count += 1
        if(count == 1): 
            return A[i] 
    return -1
ar = [2, 3, 5, 4, 5, 3, 4] 
n = len(ar)  
print("Element occurring once is",findSingle(ar,n))
