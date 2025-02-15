import math
def minimax(curDepth,nodeIndex,maxTurn,scores,targetDepth):
    if(curDepth==targetDepth):
        return scores[nodeIndex]
    if(maxTurn):
        return max(minimax(curDepth+1,nodeIndex*2,False,scores,targetDepth),
                   minimax(curDepth+1,nodeIndex*2+1,False,scores,targetDepth))


    else:
        return min(minimax(curDepth+1,nodeIndex*2,True,scores,targetDepth),
                   minimax(curDepth+1,nodeIndex*2+1,True,scores,targetDepth))
scores = []
x= int(input("enter total number of leaf nodes : "))
for i in range(x):
  y = int(input("Enter leaf node : "))
  scores.append(y)
targetDepth = math.log(len(scores),2)
currentdepth = int(input("enter current depth value : "))
nodeIndex = int(input("Enter node value : "))
maxTurn = True
answer = minimax(currentdepth,nodeIndex,maxTurn,scores,targetDepth)
print("The optimal value is : ",answer)
