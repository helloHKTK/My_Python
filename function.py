from employee import Employee

# 全局变量,用字典存放员工信息
employee_info = {}


# 添加员工信息
def add_employee():
    em_num = input("请输入员工工号:")
    em_name = input("请输入员工姓名:")
    em_age = input("请输入员工年龄:")

    em = Employee(em_num, em_name, em_age)
    employee_info[em_num] = em  # 往字典中添加键值对
    print("恭喜！信息添加成功!")
    # print(employee_info.__len__())


# 查看员工信息
def show_employee():
    flag = False  # 标记位,用来标记是否找到对应员工编号
    em_num = input("请输入要查询的员工编号：")
    # 遍历字典的键值对
    for key, value in employee_info.items():

        if key == em_num:
            print("查找结果：\n" + "员工号:" + value.num + " 姓名:"+value.name + " 年龄:" + value.age)
            flag = True
            break

    if flag is False:
        print("没有查找到相应信息！")


# 查看所有员工信息
def show_all_employee():
    print("工号" + "  姓名" + "  年龄")
    for key, value in employee_info.items():
        print(value.num + "  " + value.name + "   " + value.age)


# 删除员工信息
def del_employee():
    flag = False  # 标记位,用来标记指定用户信息有没有被删除
    em_num = input("请输入要删除的员工编号：")
    # 遍历字典的键值对
    for key, value in employee_info.items():

        if key == em_num:
            del employee_info[em_num]  # 从字典中删除指定编号的员工信息
            flag = True
            print("删除成功！")
            break

    if flag is False:
        print("没有找到编号为" + em_num + "的员工信息！")


# 修改员工信息(实际上就是覆盖)
def update_employee():
    flag = False  # 标记位,用来标记是否找到对应员工编号
    em_num = input("请输入要修改的员工编号：")
    # 遍历字典的键值对
    for key, value in employee_info.items():

        if key == em_num:
            update_name = input("修改姓名为:")
            update_age = input("修改年龄为:")
            value.name = update_name
            value.age = update_age
            flag = True
            print("恭喜!修改成功!")
            break

    if flag is False:
        print("没有查找到相应信息！")


def main_function():
    while True:
        print("-" * 10 + "员工信息管理系统" + "-" * 10)
        print("01.添加员工信息" + "\n" +
              "02.删除员工信息" + "\n" +
              "03.修改员工信息" + "\n" +
              "04.查询员工信息" + "\n" +
              "05.查询所有员工信息" + "\n" +
              "06.退出系统" + "\n")
        num = input("请输入操作编号：")

        if num == "01":
            add_employee()
        elif num == "02":
            del_employee()
        elif num == "03":
            update_employee()
        elif num == "04":
            show_employee()
        elif num == "05":
            show_all_employee()
        elif num == "06":
            break
        else:
            print("输入有误,请检查后重新输入！！")


# 调用主函数
main_function()
