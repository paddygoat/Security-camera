import array as arr
import numpy as np

c= 'Hello World'
g = arr.array('i',[])
n=-1

for h in range(len(c)):
  g.extend([0]) 
for x in c:
  n = n+1
  y = ord(x)
  g[n] = y
print(g)

j = np.array(g).tolist()

c= 'Hello World'
g = arr.array('i',[])
n=-1

#for h in range(len(c)):
  #g.extend([0]) 
for x in c:
  g.extend([0])
  n = n+1
  y = ord(x)
  g[n] = y
print(g)