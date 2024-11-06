# .2 תרגילי חזרה למבחן )רשות(:
# a. בכיתה לימוד יכולים להיכנס 30 תלמידים. יש בבית הספר 103 תלמידים
# כמה כיתות מלאות של 30 תלמידים יהיו, וכמה תלמידים ישארו בכיתה האחרונה
# כעת, בימקום ,103 קלוט את מספר התלמידים מהמשתמש והדפס כמה כיתות מלאות
# של 30 תלמידים יהיו, וכמה תלמידים ישארו בכיתה האחרונה
# רמז: השתמש בחלוקה ושארית %


students_school: int = int(input("How many students in school? "))
students_class: int = 30
fall_classes: int = students_school//students_class
last_class_students: int = students_school %students_class


print(f"classes: {fall_classes}")
print(f"Students in the last grade: {last_class_students}")


from itertools import count

# b. קלוט מספר מהמשתמש, עד אשר ייקלט מספר חוקי בין 10-99 )אם תקלט מחרוזת
# התוכנית תידע לטפל בשגיאה...(. בדוק אם ספרת האחדות גדולה מספרת העשרות,
# אם כן הפוך את המספר, אם לא, השאר את המספר כמו שהוא.
# לדוגמא -
# עבור המספר ,57 התשובה תהיה 75
# עבור המספר ,82 התשובה תהיה 82
# עבור המספר ,55 התשובה תהיה 55


while True:
    try:
        num:int  = int(input("enter number: "))
        if num < 10 or num > 99:
            break
        ahadot: int = num % 10
        asarot: int = num//10
        if ahadot > asarot:
            revers_num: int = ahadot * 10 + asarot * 1
            print(revers_num)
        else:
            print(num)
    except ValueError as e:
        print(e)

# c. הדפס את כל המספרים הראשוניים בין 1-200

list_prime: list[int] = []

for x in range(1, 200 + 1):
    if x < 1:
        continue
    else:
        if x == 1:
            continue
        elif x == 2:
            list_prime.append(x)
        elif x % 2 == 0:
            continue
        else:
            divider: int = 3
            found_divider: bool = False
            while divider <= x ** 0.5 + 1:
                if x % divider == 0:
                    found_divider = True
                    break
                divider += 2
            if not found_divider:
                list_prime.append(x)
print(list_prime)


# a b c d תשובות 4 יש אמריקאית לשאלה .d
# קלוט מהמשתמש תשובות בלולאה עד אשר ייקלט התו x( ליציאה(
# # )אם ייקלט תו אחר מאשר x d c b a, קלוט שוב(
# # בסיום הלולאה )אחרי שבחר x):
# # הדפס כמה תלמידים ענו a, כמה b, כמה c, כמה d ?
# # הדפס איזה תשובה חזרה הכי הרבה פעמים מבין d c b a ?איזה הכי פחות?


question: str = "what your MBTI type? "
answer_list: list[str] = ["A. _NT_", "B. _NF_", "C. _S_P", "D. _S_J"]
SENTINEL: str = "X"
count_list: list[int] = [0, 0, 0, 0]  #[a,b,c,d] [0,0,0,0]

while True:
    print(f"{question}\n"
          f"{answer_list[0]}\n"
          f"{answer_list[1]}\n"
          f"{answer_list[2]}\n"
          f"{answer_list[3]}")
    answer: str = input("enter your answer a/b/c/d, if exit enter x: ")
    answer = answer.upper()
    if answer == SENTINEL:
        break
    if answer == "A":
        count_list[0] += 1
    if answer == "B":
        count_list[1] += 1
    if answer == "C":
        count_list[2] += 1
    if answer == "D":
        count_list[3] += 1
    else:
        print("invalid input, try again\n")
print(f"total answer: a - {count_list[0]}\n"
      f"total answer: b - {count_list[1]}\n"
      f"total answer: c - {count_list[2]}\n"
      f"total answer: d - {count_list[3]}\n"
      f"the most answered {answer_list[count_list.index((max(count_list)))]}, times: {max(count_list)}\n"
      f"the least answered {answer_list[count_list.index((min(count_list)))]}, times: {min(count_list)}")