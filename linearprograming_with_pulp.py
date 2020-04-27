import pulp as p 
import numpy as np
import ast

print("-----------------------------------------------------------")
print("\nNote:Format string is matrix and solve the problem with MINIMIZE.\n")
print("-----------------------------------------------------------")
objective=input('objective(minimize)=')
matrixList=ast.literal_eval(objective);
obj=np.array(matrixList).reshape(1,len(matrixList))
subject=input('Subject to(<=)=')
sub=ast.literal_eval(subject)
sub= np.array(sub)
if(1==1):
    #create variable >=0
    problem=p.LpProblem("Simplex method:",p.LpMinimize)
    
    toantu=sub[:,-1]
    toantu=toantu.reshape(sub.shape[0],1)
    sub=sub[:,0:-1]
    
    #name=[f"x{i}" for i in obj[0,:]]
    index=0
    name=[]
    for i in obj[0,:]:
        index+=1
        name.append(f"X{index}")
    
    variable=[]
    for temp in name:
        variable.append(temp)
        variable[-1]=p.LpVariable(temp,lowBound=0)
    variable=np.array(variable).reshape(len(variable),1)
    #-----
    
    problem+=obj.dot(variable)[0][0]
    #-----
    sub=sub.dot(variable)
    for i in range(0,sub.shape[0]):
        problem+=sub[i,0]<=toantu[i,0]
     
   
    print(problem)
    problem.solve()
    for i in variable[:,0]:
        print(f'{i}={p.value(i)}')
    print(f'Min={p.value(problem.objective)}')
    

else:
    print("Error.")




 
