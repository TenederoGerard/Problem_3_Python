import numpy as np

def bestfit(r):
    
    for n in range(len(r)):
        
        w = np.polyfit(r[:,0],r[:,1],n)
        e = np.polyval(w, r[:,0])
        o = np.linalg.norm(r[:,1] - e)
        l = [n,o]

        if n==0:
            y = l

        elif y[1] >= l[1]:
            z = l[0]
            
    c = np.polyfit(r[:,0],r[:,1],z)

    print('Coefficients: ',c)    

rows = int(input("Enter number of rows: ")) 
columns = 2    

print("Enter the data points:")
data_points = list(map(int, input().split()))  
F = np.array(data_points).reshape(rows, columns)

print("Coefficients:")
bestfit(F)