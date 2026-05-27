import os
'''
print(os.getcwd())


os.chdir(r" ")
print(os.getcwd()) 

os.chdir(r"")
print(os.listdir())



os.mkdir("example")

print(os.listdir())


os.makedirs(
    "Project",
    exist_ok=True
)

print(os.listdir())


os.rmdir("Project")
print(os.listdir())


os.remove("sample.txt")
print(os.listdir())


list_dir=os.listdir(r"")

print("List of directories before creating a file:")
print(list_dir)

with open("sample.txt","w") as f:
    pass

print("list of dirs after creating a file:")
print(os.listdir(r""))


os.rename("sample.txt","meow.txt")
print(os.listdir())


with open("sample.txt","w") as f:
    pass

print(os.path.exists('samples.txt'))

print(os.path.isfile(r"path"))


print(os.path.isdir(r"path"))

print(os.path.getsize("library1.py"))



print(os.environ.get(r"path"))


os.environ[r"path"]="123"
print(os.environ.get(r"path"))


print(os.environ.get(r"path"))

for folder , _ , files in os.walk("sample"):
    for file in files:
        if file.endswith(".txt"):
            print(file)
            print(os.path.join(folder,file))
        print()
    print()
    print()

print(os.getcwd())
print(os.listdir())

os.makedirs("Projects/Python",exist_ok=True)
os.makedirs("Projects/AI",exist_ok=True)
os.makedirs("Projects/Web",exist_ok=True)

for folder , _,files in os.walk("."):
    for file in files:
        if file.endswith(".py") or file.endswith(".txt"):
            print(file)


for folder , _,files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(folder,file))
            print()

fo=0
fi=0
for folders , _ ,files in os.walk("sample"):
    fo+=1
    fi+=len(files)

print(f"Total folders: {fo}")
print(f"Total files: {fi}")

size=0
large=None
for folder , _,files in os.walk("."):
    for file in files:
        if os.path.getsize(os.path.join(folder,file))>size:
            size = os.path.getsize(os.path.join(folder,file))
            large=file

print(f"The largest file is : {large}")
print(f"It's size is : {size/(1024*1024):.2f}MB")

print(os.environ.get("PATH"))
print(os.environ.get("USERNAME"))
print(os.environ.get("HOME"))

with open("backup_log.txt","w") as f:
    for folder,_,files in os.walk("."):
        for file in files:
            f.write(file + "\n")

'''

