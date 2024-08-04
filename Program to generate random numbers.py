import random

def generate_random_numbers(count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

count = int(input("أدخل عدد الأرقام العشوائية المطلوبة: "))
lower_bound = int(input("أدخل الحد الأدنى للنطاق: "))
upper_bound = int(input("أدخل الحد الأقصى للنطاق: "))

if lower_bound > upper_bound:
    print("الحد الأدنى يجب أن يكون أقل من أو يساوي الحد الأقصى.")
else:
    numbers = generate_random_numbers(count, lower_bound, upper_bound)
    print("الأرقام العشوائية هي:", numbers)
