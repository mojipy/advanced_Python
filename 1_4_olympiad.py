"""
This script get the input as:
4
m.hosSein.python
f.miNa.C
m.aHMad.C++
f.Sara.java

 and gives:

f Mina C
f Sara java
m Ahmad C++
m Hossein python


Author: Mojtaba Hassanzadeh
Date: March 9, 2024
"""

numb = int(input('no. of people: ') )

dic ={}

for i in range(numb):
    data = input('sex name language: ').split('.')
    dic[data[1].lower().capitalize()] = {'sex':data[0].lower(), 'Language':data[2]}

# print(dic)
sorted_dic = dict(sorted(dic.items(), key = lambda x: (x[1]['sex'], x[0])))
# print(sorted_dic)
print([f"{value['sex']} {key} {value['Language']}" for key, value in sorted_dic.items()])
print("\n".join([f"{value['sex']} {key} {value['Language']}" for key, value in sorted_dic.items()]))
