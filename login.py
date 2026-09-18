# 注册账户板块
while True:
    username = input("请输入您的用户名，不可以少于两位，多于五位")
    if 2 <= len(username) <= 5:
        print("用户名已注册")
        break
    else:
        print("注册用户名失败")
        continue

while True:
    password = int(input("请输入您的密码，不可少于六位，多于十二位"))
    if 6 <= len(password) <= 12:
        print("密码已注册")
        break
    else:
        print("注册密码失败")
        continue

# 登录账户板块
MAX_WRONG_COUNT = 3
wrong_count = 0
while MAX_WRONG_COUNT != wrong_count:
    already_login = False
    login_username = input("请输入登录用户名")
    login_password = int(input("请输入登录密码"))
    if username == login_username and password == login_password:
        print("登录成功!")
        already_login = True
    else:
        print("登录失败")
        wrong_count += 1
        continue
if already_login == True:
    print("登录已结束")
elif already_login == False:
    print("登录失败,程序结束")