def is_uppercase(string):
    for i in string:
        if 65 <= ord(i) <= 90:
            return True
        if 97 <= ord(i) <= 122:
            return False

user_input = input("Введіть рядок для перевірки: ")
if is_uppercase(user_input):
        print("True")
else:
        print("False")
