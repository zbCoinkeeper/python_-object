def evaluate_f(num):
    res=[]
    for i in range(0,num+1):
        if i == 0:
            res.append(0)
        elif i<=4:
            res.append(2*res[-1]+3)
        else:
            res.append(res[-1]-1)
    return res[-1]




