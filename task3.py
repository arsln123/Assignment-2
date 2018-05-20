matrix=[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
inputM=[]
temp1=[]
tmp=[]
i=1

print ("Enter 2*2 Matrix : ")
for i in range(2):
    for j in range(2):
        strr=input("Enter value : ")
        try:
            num=int(strr)
            if i==1:
                temp1.append(num)
            else:
                tmp.append(num)
        except:
            print ("Invalid INPUT !")
            exit()
    if i==1:
        inputM.append(temp1)
    else:
        inputM.append(tmp)
    i+=1

#Functions()
def isValid(x,y):
    if(x>=0 and x<8 and y>=0 and y<8):
        return 1
    else:
        return 0


def chk(i,j):
    x1=i
    y1=j+1
    x2=i+1
    y2=j
    x3=i+1
    y3=j+1
    if isValid(x1,y1)==1 and isValid(x2,y2)==1 and isValid(x3,y3)==1:
        if matrix[x1][y1]==inputM[0][1] and matrix[x2][y2]==inputM[1][0] and matrix[x3][y3]==inputM[1][1]:
            return 1
        else:
            return 0
    else:
        return 0
    
# Match 2*2 matrix with 8*8 matrix  
var=0
for i in range(8):
    for j in range(8):
        if matrix[i][j]==inputM[0][0]:
            if chk(i,j)==1:
                print ("Given 2*2  matrix found at (",i,",",j,") --> Stratng Point")
                var=1

if var==0:
    print ("2*2 matrix not found in 8*8 matrix.")
