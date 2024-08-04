def add_note():
    note = input("أدخل الملاحظة: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("تم حفظ الملاحظة.")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        for index, note in enumerate(notes, 1):
            print(f"{index}. {note.strip()}")
    except FileNotFoundError:
        print("لا توجد ملاحظات بعد.")

print("اختر العملية:")
print("1. إضافة ملاحظة")
print("2. عرض الملاحظات")

choice = input("أدخل اختيارك (1/2): ")

if choice == '1':
    add_note()
elif choice == '2':
    view_notes()
else:
    print("اختيار غير صحيح")
