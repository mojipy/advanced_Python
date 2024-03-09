"""
This script get the input as:
4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action

 and gives:

Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1

assigning higher ranks to the most frequently favored genres, then alphabetical order

Author: Mojtaba Hassanzadeh
Date: March 6, 2024
"""
genres = ['Horror', 'Romance', 'Comedy', 'History' , 'Adventure' , 'Action']
numb = int(input('no. of people: ') )

names = []
dic ={}

for i in range(numb):
    name, *gens = input('name and genres: ').split()
    dic[name] = gens
    names.append(name)

print(dic)

gcount = []
for genre in genres:
    gcount.append(sum([1 for name, genres in dic.items() if genre in genres]))
    # gcount.append(sum(entry.count(genre) for entry in dic.values()))
print(gcount)

data = dict(zip(genres, gcount))
sorted_data = dict(sorted(data.items(), key=lambda item: (-item[1], item[0])))


for genre, count in sorted_data.items():
    print(f"{genre} : {count}")