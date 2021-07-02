def bunch(ar):
    max=0
    i=0
    
    while(i<len(ar)):
        temp=ar[i]
        tempc=0
        j=0
        while(j<len(ar)):
           
           if(ar[j]==temp):
               tempc=tempc+1
           j=j+1
        if(tempc>max):
           max=tempc
        i=i+1
    
    return max


arr=[1, 2, 2, 3, 4,4, 4,4]
print(bunch(arr))
