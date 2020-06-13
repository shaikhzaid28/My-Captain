list1=[9,8,7,]
list2=[1,2,3,]
mytuple=("C","C++","Java","PHP")
myDict={"C":"Easy","C++":"Moderate","Java":"Advanced",}
#assigning elements to different list
list1.append(6)
list2.append(4)
print("Elements in list1 are :",list1,)
print("Elements in list2 are :",list2,)
#accessing a element from a tuple
print(mytuple[2])
#dict
print("Programing languages in dictionarie is :",myDict)
del myDict["Java"]
#after deleting java from the dict
print("Programing languages in dictionarie is :",myDict)