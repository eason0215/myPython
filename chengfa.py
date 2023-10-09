number1 = input('请输入第一个数字：')

number2 = input('请输入第二个数字：')

# Python isdigit() 方法检测字符串是否只由数字组成，只对 0 和 正数有效。

# https://www.runoob.com/python/att-string-isdigit.html

def disposeInput(str_input):

    if str_input.isdigit():

        return int(str_input)

num1 = disposeInput(number1)

num2 = disposeInput(number2)

if num1 and num2:

    print("数字的积", num2 * num1)

else:

    print('请输入大于0的数')