maximum,minimum = int(input("enter value of alpha: ")),int(input("enter value of beta: "))
def fun_alpha_beta(depth,node,max_turn,values,alpha,beta):
    if depth==3:
        return values[node]
    if max_turn:
      best  = minimum
      for i in range(0,2):
        val = fun_alpha_beta(depth+1,node*2+i,False,values,alpha,beta)
        best = max(best,val)
        alpha = max(alpha,best)
        if beta<=alpha:
          break
      return best
    else:
      best = maximum
      for i in range(0,2):
        val = fun_alpha_beta(depth+1,node*2+i,True,values,alpha,beta)
        best = min(best,val)
        beta = min(beta,best)
        if beta<=alpha:
          break
      return best
scores = []
x= int(input("enter total number of leaf nodes : "))
for i in range(x):
  y = int(input("Enter leaf node : "))
  scores.append(y)
depth = int(input("enter depth value : "))
node = int(input("Enter node value : "))
max_turn = True
answer = fun_alpha_beta(depth,node,max_turn,scores,minimum,maximum)
print("The optimal value is : ",answer)
