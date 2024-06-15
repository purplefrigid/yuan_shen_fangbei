
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
print("初始值: ", a, b, c, d)
def x():
    global a, b
    a = 1 if a == 5 else a + 1
    b = 1 if b == 5 else b + 1

def y():
    global a, b, c
    a = 1 if a == 5 else a + 1
    b = 1 if b == 5 else b + 1
    c = 1 if c == 5 else c + 1

def z():
    global b, c, d
    b = 1 if b == 5 else b + 1
    c = 1 if c == 5 else c + 1
    d = 1 if d == 5 else d + 1

def t():
    global c, d
    c = 1 if c == 5 else c + 1
    d = 1 if d == 5 else d + 1

# 初始化变量和操作序列
sequence = []

# 查找操作顺序
while (a, b, c, d) != (4, 4, 4, 4):
    if a != 4:
        if b != 4:
            x()
            sequence.append('x')
        elif c != 4:
            y()
            sequence.append('y')
        else:
            z()
            sequence.append('z')
    elif b != 4:
        if c != 4:
            z()
            sequence.append('z')
        else:
            t()
            sequence.append('t')
    elif c != 4:
        if d != 4:
            t()
            sequence.append('t')
        else:
            y()
            sequence.append('y')
    elif d != 4:
        t()
        sequence.append('t')
print("操作顺序: ", sequence)
print("最终值: ", a, b, c, d)
