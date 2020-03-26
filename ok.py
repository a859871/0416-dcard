# def add(a, b):
#     return a+b
# x=1
# y=4
# result=add(x,y)
# print (result)
# str='Hello,World!'
# x=10
# y=2.0
# boolean=True
# none=None
# print(type(str))
# print(type(x))
# print(type(y))
# print(type(boolean))
# print(type(none))
# x = 3
# str_x = str(x)
# print(str(x))
# float_x = float(x)
# x=3.4
# int_x = int(x)
# x=2
# y=5
# z=x+y
# print(z)
# print(x+y)
# print(x-y)
# print(x*y+15/2)
# print(y/x)
# print(y%x)
# mathScores=[60,70,10,20,81,63,4]#序列打法
# mathScores[2]
# print(mathScores[2])
# mathScores[1:6]
# print(mathScores[1:6])
# print(mathScores[6])
# print(mathScores[-1])
# print(mathScores[:5])
# print(mathScores[5:])
# print(len(mathScores))
# print(sum(mathScores))
# print(max(mathScores))
# print(min(mathScores))
# print(sum(mathScores)/len(mathScores))
#
#
# mathScores2 = []
# print(mathScores2)
# mathScores2.append(60)
# print(mathScores2)
# mathScores2.append(70)
# mathScores2.append(50)
# mathScores2.append(40)
# mathScores2.insert(2,30)
# mathScores2[1] = 55
# print(mathScores2)
# mathScores2.pop()#丟掉最後一個值
# mathScores2.pop(1)
# print(mathScores2)
# print(33 in mathScores2)
# print(55 in mathScores2)
# print(55 not in mathScores2)
# mathScores2.append(70)
# mathScores2.append(40)
# print(mathScores2)
# print(mathScores2.count(70))
# print(mathScores2.count(40))
# print(mathScores2.index(70))
# print(mathScores)
# print(mathScores2)
# print(mathScores+mathScores2)
# print(sorted(mathScores2, reverse=True))
#
# ls =[[1,2,3],[4,5,6]]
# print(ls[0])
# print(ls[1][1])
# print(ls[0][1])
# grates=[[5,14,7],[23,36,28],[88,90,92]]
# print(grates[2])
# print(sum(grates[0])/len(grates[0]))
# print(sum(grates[1])/len(grates[1]))
# print(sum(grates[2])/len(grates[2]))
# grates.append([94,90,96])
# print(grates)
# grates[0][1]=20
# print(grates)
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 3, 4, 5, 6)
# print(tuple1)
# print(tuple2)
# tuple3 = ()
# print(tuple3)
# print(tuple1[3])
# tuple1.index(4)
# print(tuple1.index(4))
# print(tuple1.count(3))
# tuple1[2] = 10
# print(tuple1+tuple2)
# print(sorted(tuple1))
# print(sorted(tuple1, reverse=False))
# tuple1 = (88, 12, 20)
# x, y, z = tuple1
# print(x)
# print(y)
# print(z)
# gratesTuple = ([5, 14, 7], [23, 36, 28], [88, 80, 92])
# print(gratesTuple)
# print(gratesTuple[2])
# print(sum(gratesTuple[0])/len(gratesTuple[0]))
# print(sum(gratesTuple[1])/len(gratesTuple[1]))
# print(sum(gratesTuple[2])/len(gratesTuple[2]))

# family = {
#     "dad": "Homer",
#     "mom": "Yaling",
#     "son": "Bart",
#     "daghter": "Lisa",
# }
# print(family["dad"])
# print(family["mom"])
# print(family.get("dog"))
# # print(family["dog"])
# print("dog" in family)
# print(family.keys())
# print(family.values())
# print(family.items())
# print(family)
# for item in family:
#     print(item)
# for item in family.items():
#     print(item)
# family = {}
# print(family)
# family["cousin"] = "Max"
# print(family)
# family["cousin"] = "Eric"
# print(family)
# family.update({
#     "uncle": "Martin",
#     "aunt" : "May"
# })
# print(family)
# del family["uncle"]
# print(family)
# family.pop("cousin")
# print(family)
# gradesDict = {
#     "chinese": [5,14,7],
#     "english": [23,36,28],
#     "math": [88,80,92],
# }
# print(gradesDict["math"])
# print(sum(gradesDict["chinese"])/len(gradesDict["chinese"]))
# print(sum(gradesDict["english"])/len(gradesDict["english"]))
# print(sum(gradesDict["math"])/len(gradesDict["math"]))
# gradesDict.update({
#     "science": [94,90,96]
# })
# print(gradesDict)

# fruits = {
#     "apple",
#     "banana",
#     "guava",
#     "guava"
# }
# fruits1 = {
#     "strawberry",
#     "papaya",
#     "banana"
# }
# print(fruits | fruits1)
# print(fruits & fruits1)
# print(fruits - fruits1)
# print(fruits)
# fruits.add("watermelon")
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# fruits.discard("apple")
# print(fruits)
# fruits.remove("watermelon")
# print(fruits)
# fruits.discard("watermelon")
# print(fruits)
# fruits.clear()
# print(fruits)
# print(sorted(fruits))
# print(sorted(fruits, reverse = True))
#
# allStudents = {
#     "John",
#     "Eva",
#     "Jill",
#     "Eric",
#     "Andy",
#     "Albert",
#     "Polina",
#     "Kristin",
#     "Angela"
# }
# danceClub = {
#     "John",
#     "Eva",
#     "Jill",
#     "Eric",
#     "Andy"
# }
# guitarClub = {
#     "Andy",
#     "Eric",
#     "Albert",
#     "Polina",
#     "Kristin"
# }
# print(danceClub & guitarClub)
# print(danceClub - guitarClub)
# print(allStudents-(danceClub|guitarClub))
# X = 70
# if X >= 60:
#     print("及格")
#     X = X + 10
# else:
#     print("被當")



