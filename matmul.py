# coding: utf-8
x = rand(3, 3)
y = rand(3, 3)
multiplicands = []
for i in range(3):
    for j in range(3):
        multiplicands.append((x[i], y[j]))
        
multiplicands = []
for i in range(3):
    for j in range(3):
        multiplicands.append((x[i], y[:, j]))
        
len(multiplcands)
len(multiplicands)
dotter = lambda x: np.dot(*x)
dotmap = map(dotter, multiplicands)
list(dotmap)
np.array(list(dotmap)).reshape(3, 3)
list(dotmap)
dotmap = map(dotter, multiplicands)
np.array(list(dotmap)).reshape(3, 3)
np.dot(x, y)
