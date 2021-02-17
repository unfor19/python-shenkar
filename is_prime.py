

def is_prime(num):
    counter = 0
    for i in range(1, num+1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False

# Testing
# print(is_prime(81))
# print(is_prime(13))
# print(is_prime(97))


# Targil
# תדפיס את כל המספרים עד למספר הנתון, רק אם הם ראשוניים
num = int(input("Shirly enter your num: "))

msg = ""
for i in range(2, num):
    if is_prime(i):
        msg += f"{i} "
print(msg)
