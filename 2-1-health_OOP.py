"""
Object Oriented Programming

This script get the age, height and weight for two groups as:

5
16 17 15 16 17
180 175 172 170 165
67 72 59 62 55
5
15 17 16 15 16
166 156 168 170 162
45 52 56 58 47
 and gives:

class A mean age: 16.2
class A mean height: 172.4
class A mean weight: 63.0
class B mean age: 15.8
class B mean height: 164.4
class B mean weight: 51.6
class with maximum mean height, then minimum weight, else print(same) : A


Author: Mojtaba Hassanzadeh
Date: March 9, 2024
"""
class Student():
    def __init__(self, label, num_Students):
        self.label = label
        self.nS = num_Students
        self.age, self.height, self.weight = self.get_students_data()

    def get_students_data(self):
        age = [int(item) for item in input(f'ages of {self.nS} students of class {self.label}:').split()]
        height = [int(item) for item in input(f'heights of {self.nS} students of class {self.label}:').split()]
        weight = [int(item) for item in input(f'weights of {self.nS} students of class {self.label}:').split()]
        return age, height, weight
    
    def calculate_average(self, data):
        return sum(data)/len(data)

class ClassComparator:
    def compare_and_print(self, ave_A, ave_B, label_A, label_B):
        if ave_A > ave_B:
            print(label_A)
        elif ave_B > ave_A:
            print(label_B)
        else:
            print('Same')

def main():
    nA = int(input('Enter No. of class A students:'))
    class_A = Student('A', nA)

    nB = int(input('Enter No. of class B students:'))
    class_B = Student('B', nB)

    comparator = ClassComparator()

    ave_age_A, ave_height_A, ave_weight_A = map(class_A.calculate_average, (class_A.age, class_A.height, class_A.weight))
    ave_age_B, ave_height_B, ave_weight_B = map(class_B.calculate_average, (class_B.age, class_B.height, class_B.weight))

    comparator.compare_and_print(ave_height_A, ave_height_B, 'A', 'B') if ave_height_A != ave_height_B else comparator.compare_and_print(ave_weight_B, ave_weight_A, 'A', 'B') if ave_weight_A != ave_weight_B else print('Same')

if __name__ == "__main__":
    main()
# 