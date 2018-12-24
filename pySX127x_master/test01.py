c= 'Bastards'
d = len(c)
import array as arr
g = arr.array('i', [])

for h in range(d):
  g.extend([0]) 

n=-1
for x in c:
  n=n+1
  y=ord(x)
  g[n]=y
print(g)