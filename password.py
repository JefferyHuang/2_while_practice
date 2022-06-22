a = 0                             
while a < 3 :
    a = a + 1
    password = input("請輸入密碼: ")
    if password == "a123456":
        print("登入成功!")
        break
    else:
        print("密碼錯誤")
        if 3-a > 0 :
            print("還有", 3-a, "次機會")
        else:
            print("請聯繫客服")

