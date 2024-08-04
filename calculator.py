def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "خطأ: القسمة على صفر غير مسموحة"

print("اختر العملية:")
print("1. جمع")
print("2. طرح")
print("3. ضرب")
print("4. قسمة")

choice = input("أدخل اختيارك (1/2/3/4): ")

num1 = float(input("أدخل الرقم الأول: "))
num2 = float(input("أدخل الرقم الثاني: "))

if choice == '1':
    print(f"النتيجة: {add(num1, num2)}")
elif choice == '2':
    print(f"النتيجة: {subtract(num1, num2)}")
elif choice == '3':
    print(f"النتيجة: {multiply(num1, num2)}")
elif choice == '4':
    print(f"النتيجة: {divide(num1, num2)}")
else:
    print("اختيار غير صحيح")
