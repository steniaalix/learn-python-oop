import random
'''
class Dice:
    def roll(self):
        return random.randint(1,6)

d=Dice()
print(d.roll())


deck=["A","k","Q",1,2,3,4,5,6,7,8,9,10]
random.shuffle(deck)
print(random.choices(deck,k=3))



std=["Steni","Sajid","JVR","Keerthi"]
print(random.choice(std))
print(random.choices(std,k=3))



lst=[1,2,3,4,5,6,7,8,'a','s','d','f','g','h','j',"k","!","@","+","%","^"]
password=random.choices(lst,k=7)
print(password)

'''

play='yes'
while play=='yes':
    n=int(input("Enter number 1-7:"))
    a=random.randint(1,7)
    if n==a:
        print("YOu won the game")
        exit()
    print("you lost")
    print(f"The computer gussed {a}")
    play=input("Do you want to continue?(yes/no)").lower()