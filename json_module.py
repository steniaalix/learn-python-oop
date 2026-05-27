import json

data={"name":"Steni","age":18}
json_data=json.dumps(data)
print(json_data)
print()
print(type(data))
print(type(json_data))

text='{"name":"Steni","age":18}'
python_data=json.loads(text)
print(python_data)
print(type(python_data))

data={"name":"Steni","age":18}
with open("data.json","w") as f:
    json.dump(data,f)


with open("data.json","r") as f:
    data=json.load(f)
print(data)

data={"name":"Steni","age":18}
print(json.dumps(data,indent=10))

class Student:
    def __init__(self,name):
        self.name=name
s=Student("Steni")
print(json.dumps(s.__dict__))


d={"name":"Steni","age":18,"marks":100}
print(json.dumps(d))

data='{"city":"Madurai","temp":35}'
print(json.loads(data))

emp={"Names":["Steni","Sajid","JVR"],"age":[18,18,18]}
with open("employee.json","w") as f:
    json.dump(emp,f,indent=5)

with open("employee.json","r") as f:
    data=json.load(f)

print(data)

dct='{"status":"success","data":{"name":"Steni","score":98}}'

meta_data=json.loads(dct)
print(meta_data["status"])
print(meta_data["data"]["name"])

