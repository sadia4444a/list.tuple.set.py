#list
courses =['history','math','english','bangla','ict']
print(len(courses))
print(courses)
print(courses[0])
print(courses[0:2])
print(courses[2:4])
print(courses[-1])


courses.append('Art')
print(courses) #last e add
courses.insert(0,'Art')
print(courses) #any position
courses2=['Art','C++']
courses.extend(courses2) #add more item from another list
print(courses)

courses.remove('math')
print(courses)

courses.pop()
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

print(courses.index('english'))

for item in courses:
    print(item)

courses=['mat','kk','sd']
for index, courses in enumerate(courses):
    print(index, courses)




num=['1','2','45','89','78']
print(min(num))
print(max(num))
num2=[2,5,7,8,9,78]
print(sum(num2))

co=['djd','dghg','yieru']
courses_str=' - '.join(co)
print(courses_str)
new_list=courses_str.split('-')
print(new_list)

#tuple-immutable and list is mutable

#mutable
list_1=['gh','yu','jk']
list_2=list_1
print(list_1)
print(list_2)

list_1[0]='hh' #mutable
print(list_2)
print(list_1)

#tuple-immutable:
tuple=('kj','eyu','weyuyu')
tuple_2=tuple

print(tuple)
print(tuple_2)
#tuple[0]='fgyu'
#print(tuple) #error immutable can't change

#set
set={'math','history'}
set2={'eng','bng'}
print(set)
print('math' in set)
print(set.intersection(set2))
print(set.difference(set2))
print(set.union(set2))

#empty list
empty_list = []
empty_list = list()

#empty tuple
empty_tuple = ()
empty_tuple = tuple()

#empty set
#empty_set={} dosn't work
empty_set = set()