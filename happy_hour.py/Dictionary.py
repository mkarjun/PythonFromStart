
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

print(states.get('NY','not found'))
print(states.get('OG','not found'))

arjun = {'Name':'Arjun','Height':'180'}
aparna = {'Name':'Aparna','Height':'165'}
shafeeq = {'Name':'Shafeeq','Height':'170'}

name=[arjun,aparna,shafeeq]
print(name)

for person in name :
    print(person.get('Name') + " : " ,person.get('Height'))