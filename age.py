while True:
    driving = input("請問你有沒有開過車? ")
    if driving != "有"  and driving != "沒有":
        print("只能輸入 有/沒有")
    
    elif driving == "有" or driving == "沒有":
        break

age = int(input("請問你的年齡是多少? "))

if driving == "有":
    if age >= 18:
        print("恭喜你通過測驗")
    else:
        print("未滿18 是不可以開車的喔")
elif driving == "沒有":
    if age >= 18:
        print("你已經可以考駕照啦")
    else:
        print("耐心等待，再過幾年你就可以考駕照了")
    