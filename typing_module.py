'''
name: str=1
print(name)


def add(a: int, b: int)-> int:
    return  a+b

print(add('a','b'))


height: float=6

print(height)

def greet(name: str,age:int)->str:
    return f"{name} is {age}"

print(greet("Steni",18))


from typing import List
marks: List[int]=[90,80,"z"]
print(marks)

from typing import Dict
point: Dict[str,int]={"math":90,"Science":97}
print(point)

from typing import Tuple

points:Tuple[int,int]=(1,2,3)
print(points)


from typing import Set

nums:Set[int]={1,2,3}
print(nums)

from typing import Optional

name: Optional[str]="Steni"
print(name)

from typing import Union
x:Union[int,float]=3.3
print(x)

from typing import TypedDict

class Student(TypedDict):
    name:str
    age:int
    
student=Student(name="steni")
print(student)
print(student["name"])

square=lambda x: x*x
print(square(2))


is_even=lambda x: x%2==0
print(is_even(5))

students = [
    ("Steni", 90),
    ("Alex", 70),
    ("Bob", 95)
]
students.sort(key=lambda x:x[1])
print(students)


nums=[1,2,3,3,4]

result=map( lambda x:x*2,nums)
print(list(result))

names=["Steni","aalix"]
upper=map(lambda x:x.upper(),names)
print(list(upper))

words=["cat","elephant"]

length=map(lambda x:len(x),words)
print(list(length))
'''

nums=[1,2,3,45,5]
print(list(x*2 for x in nums))