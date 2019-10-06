import math;

def int2BinaryConv(d,binary):
    binaryList=[];
    print(binary)
    
    for i in range(0,d):
        if binary%2==1:
            binaryList.append(1);
        else:
            binaryList.append(0);
        binary=int(binary/2);
    binaryList.reverse()    
    return binaryList
    
    


with open('sample.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
for x in content:
    str=x.strip()
    splitter=str.split()
    NoOfRatio=splitter[0]
    ratioColon=splitter[1]
    ratioList=ratioColon.split(':')

    # Research .. Ratio to Binary array C

    sum=16;
    d=int(math.log2(sum));
    C=[]
    for i in ratioList:
        C.append(int2BinaryConv(d,int(i)))
    A=[]
    
    print("\n")
    for i in C:
        tempA=[]
        for j in range(0,d-1):
            tempA.append(i[j] & i[d-1])
        A.append(tempA);
    print(A);
    evenSum=0
    isLastColPair=1
    while isLastColPair!=d:
        for i in A:
            evenSum=evenSum+i[d-isLastColPair]
        if evenSum==0 || evenSum==1:
            isLastColPair=isLastColPair+1;
        else:
            break;
        
    
    if evenSum%2==0:
        pair1=-1
        pair2=-1
        for i in range(0,NoOfRatio)
            if A[i][d-1]==1:
                if pair1==-1:
                    pair1=i
                else:
                    pair2=i
            if pair1!=-1 && pair2 !=-1:
                # graph viz m add krdo pair1 and pair2 node ko
                pair1=-1
                pair2=-1
                C[pair1][d-1]=0;
                C[pair2][d-1]=0;
                
                    
                

    else :
        



        
