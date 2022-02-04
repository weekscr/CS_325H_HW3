def insertSort(actNum,S,F):

    for i in range(1,len(S)):
    	#take the value at i and move it backwards in the list until it is greater than the previous value
        phS=S[i]
        phF=F[i]
        phA=actNum[i]
        
        j=i-1
        while j>=0 and S[j]>phS:
        	#compare data and swap elements if needed
            S[j+1]=S[j]
            F[j+1]=F[j]
            actNum[j+1]=actNum[j]
            j-=1
        S[j+1]=phS
        F[j+1]=phF
        actNum[j+1]=phA
    return [actNum,S,F]
                



def activity(n,S,F,actNum):
    actNum,S,F = insertSort(actNum,S,F) #sort by start time

    A = [actNum[-1]]

    i = n-1
    for j in range(n-2,-1,-1): #loop through activities
        if F[j] <= S[i]:
            A.append(actNum[j])
            i = j      #if finish time of next one is less than start time of current one, schedule it 

    return A       
        

    




f = open('act.txt','r').readlines()

for i in range(len(f)):
    if len(f[i].split()) == 1:
        n = int(f[i].split()[0])
        S = []
        F = []
        actNum = []
        for j in range(i+1,i+n+1):
            actNum.append(int(f[j].split()[0]))
            S.append(int(f[j].split()[1]))
            F.append(int(f[j].split()[2]))

        A = activity(n,S,F,actNum)
        print('Maximum number of activities =',len(A))
        print(A[::-1])


"""T = int(f.pop(0))

for i in range(T):
    N = int(f.pop(0))
    P = [0]*N
    W = [0]*N
    
    for j in range(N):
        temp = f.pop(0)
        temp = temp.split()
        P[j] = int(temp[0])
        W[j] = int(temp[1])

    F = int(f.pop(0))
    M = [0]*F
    
    for j in range(F):
        M[j] = int(f.pop(0))
        
        
    print("Test Case:",i+1)
    tp,fArr = shopping(N,P,W,F,M)
    
    print("Total Price", tp)
    for i in range(F):
        print(str(i+1),end=": ")
        for j in range(len(fArr[i])-1,-1,-1):
            print(fArr[i][j],end=' ')
        print("")"""
