sona = 'Virat.'
print(str(sona))
print(repr(sona))
x = 50 * 24
y = 546*234
print('x =',repr(x),'y =',repr(y))
p = 'hello, world\n'
q = repr(p)
print(q)
k=repr((x,y,('super', 'dupper')))
print(k)
    
print('{0} and {1}'.format('super', 'dupper'))
print('{1} and {0}'.format('super', 'dupper'))    

value = ('India won the WTC Final',2021)
ind = repr(value) 
print(ind)

import json
f = ["yamraj",1, 'golf', 'people']
p=json.dumps(f)
print(p)
