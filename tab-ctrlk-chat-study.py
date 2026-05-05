# a = 10
# b = 20
# c = a + b
# print(c)
# d = a - b
# print(d)
# e = a * b
# print(e)
# f = a / b
# print(f)

# while True:
#     var = input("请输入一个变量：")
#     try:
#         # 尝试转换为浮点数，判断是否为数字类型
#         num = float(var)
#         if num > 0:
#             print("这个数字是正数")
#         elif num < 0:
#             print("这个数字是负数")
#         else:
#             print("这个数字是0")
#         break
#     except ValueError:
#         print("输入的不是数字类型，请重新输入。")

    
# even_numbers = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         # 把i放进一个列表
#         # 首先需要先定义一个列表容器，可以在循环外定义
#         # 但由于插入点在循环内部，假设外部定义了列表 even_numbers
#         even_numbers.append(i)
# print(even_numbers)


# def jisuanarea1(banjing):
#     #banjing = input("请输入圆的半径：")
#     banjing = float(banjing)
#     def jisuanarea(banjing):
#         area = 3.14 * banjing * banjing
#         return area
#     print(jisuanarea(banjing))

# jisuanarea1(5)



while True:
    name = input("请输入你的名字：")
    age = input("请输入你的年龄：")
    # 判断name是否为字符串 & age是否为数字
    # input() 默认返回str，所以只需判断age能否转换为数字即可
    if name.strip() == "":
        print("名字不能为空，请重新输入。")
        continue
    try:
        age_int = int(age)
    except ValueError:
        print("年龄必须为数字，请重新输入。")
        continue
    # 通过检查，退出循环
    break

# age = age_int  # 替换原 age 值为 int 型

# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
age = int(age)
if age >= 18:
    print(f"{name} 你已经成年了")
else:
    print(f"{name} 你还没有成年")
print("欢迎光临")

#checkout本地master分支




