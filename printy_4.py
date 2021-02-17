

def lst4(list1):
    lst = []
    if len(list1) > 4 or len(list1) < 4:  # אם יש יותר מארבע איברים או פחות מ4 איברים
        print("you need exzactly 4")
    else:
        for item in list1:  # ניקח ברשימ את כל הספרות שהסכום שלהפ גדול מ9
            num = item  # בוא נשמור את המספר המקורי מהרשימה המקורית המגניבה
            sum_digits_of_num = 0
            while num > 0:
                digit = num % 10  # ימנית
                sum_digits_of_num += digit
                num = num // 10

                if sum_digits_of_num > 9:
                    lst.append(item)
                    break
            # this also works
            # if sum_digits_of_num > 9:
            #    lst.append(item)

        print(lst)


lst4([1, 29, 3, 78])
