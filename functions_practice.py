def hello():
    print("Hello")

def pack(a,b,c):
    return [a,b,c]

def eat_lunch(list):
    if bool(list):
        print(f"First I eat {list[0]}," + f"Next I eat {list[1]}")
    else:
        print("My lunchbox is empty!")

eat_lunch(["banana","beef"])
hello()
print(pack(1,3,5))