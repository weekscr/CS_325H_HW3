def days(n,X,d):
    pos = 0
    stop = 0
    days = 0

    while(pos<X[n-1]):
        for i in range(stop,n):
            if X[i]>pos+d:
                if i == stop:
                    return "impossible"
                else:
                    pos = X[i-1]
                    stop = i-1
                    days = days+1

    return days 

n = 5
X = [100,300,700,800,900]
d = 400

print(days(n,X,d))
