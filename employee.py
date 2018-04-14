class Employee:
    # 公有属性
    num = ''
    name = ''
    age = ''
    # 私有属性
    wage = 0

    # 构造函数(创建类的对象的时候自动被创建)
    def __init__(self, num_01, name_01, age_01):
        self.num = num_01
        self.name = name_01
        self.age = age_01

    # 析构函数
    # def __del__(self):
    #     print("员工"+self.name+"的信息已被销毁！")