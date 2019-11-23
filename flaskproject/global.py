a=2222
def test():
    global a
    a=a+2
    return a

s=test()
print(s)