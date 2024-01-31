def max_min(l):
    
    if len(l)==0:
        return 0
    else:
        max=l[0]
        min=l[0]

        for x in range(1,len(l)):
            if l[x]>=max:
                max=l[x]
            if l[x]<=min:
                min=l[x]
        print('The maximum number is ' ,max, ' and the minimum number is' ,min, '.')

l=[]
max_min(l)
