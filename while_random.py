import random

n = 0
start = int(input("請輸入猜數字範圍開始值: "))
end = int(input("請輸入猜數字範圍結束值: "))
r = random.randint(start,end)

while True:
    number = int(input("請輸入 {} ~ {} 其中的一個數字: ".format(start, end)))
    n += 1
    if number == r:
        print("恭喜你猜對了!")
        break
    elif number > r :
        print("再小一點")
    elif number < r :
        print("再大一點")
    print("這是你猜的第", n, "次")

if n > 3 :
    print("總共猜了", n, "次, 智商有待加強")
else:
    print("總共猜了", n, "次, 非常聰明喔")