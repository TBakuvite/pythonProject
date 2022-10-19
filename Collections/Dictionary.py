my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])
prices_lookup = {'apple':2.99,'oranges':1.99,'milk':100}
print(prices_lookup['apple'])
d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3']['insideKey'])
print(d['k2'][2])
d={'key1':['a','b','c']}
mylist=d['key1']
print(mylist)
letter = mylist[0]
print(letter)
print(d['key1'][0])
d = {'k1':100,'k2':200}
d['k3']=300  #how to add a new value
print(d)
d['k1'] = 'new value'
print(d.keys())
print(d.values())
print(d.items())
print(d.pop('k1'))
print(d)