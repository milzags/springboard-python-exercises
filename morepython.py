chicken = {
        'name': 'Lady', 
        'breed': 'silkie',
        'total_egg_count': 12, 
        'egg_chart': {
            'M': True,
            'T': True,
            'W': True,
            'TH': True,
            'F': True,
            'S': False,
            'SU': False,
        },
        'coop_mates' : ['butters','stevie','henry'],
}

keys = chicken.keys()
print(keys) #this is not a list but it looks like one

for key in chicken.keys():
    print(key)

for value in chicken.values():
    print(value)

for pair in chicken.items():
    print(pair)

for (k,v) in chicken.items():
    print(k,'-->',v)


languages = {'ruby', 'python', 'javascript'}
type(languages) # set
# no error if duplicated elements are added, it doesn't appear 

voted_languages = ['ruby', 'python', 'JS', 'scala', 'ruby', 'python']
set(voted_languages)
# {'javascript', 'python', 'ruby', 'scala'}
