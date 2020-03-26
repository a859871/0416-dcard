class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender#__gender為私有屬性，不能被外部取用(對外不公開)
        self.major = new_major
        self.id = new_id
    def get_gender(self):
        """回傳private屬性"""
        return self.__gender
    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender =='F':
            self.__gender = new_gender
        else:
            print('======請傳入"M"或"F"======')
    def borrow_resources(self):
        print('someone borrow')
class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major,new_id)
    def join_class(self):
        pass
    def quit_class(self):
        pass
    def borrow_resources(self):
        print('student borrow')
class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major,new_id)
    def borrow_resources(self):
        print('professor borrow')

studentA = Student('M', '工管系', 'M10821035')#類別實體化成物件
studentB = Student('B', '經濟系', 'M10821034')
professorA = Professor('M', '資工系', 'T123456')
professorB = Professor('F', '數媒系', 'T125656')

ls = [studentA, studentB, professorA, professorB]

for item in ls:
    item.borrow_resources()
# print( studentA.__gender )#印出物件studentA的gender
studentA.set_gender('F')#呼叫物件的join_class方法
# print( studentA.__gender )
print(studentA.get_gender())
print(studentB.get_gender())
print(professorA.get_gender())
print(professorB.get_gender())
