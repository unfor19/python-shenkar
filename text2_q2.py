def is_prime(num):
    counter = 0
    for i in range(1, num+1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def prime2dList(lst):  # [1,2,3,4,5,6,7,8,9,]
    counter = 0

    for num in lst:
        if num <= 1:
            continue
        # # using the is_prime function
        # if not is_prime(num):
        #     counter += 1

        # inline check of is_prime
        for j in range(2, num):  # כל מספר מתחלק ב1 ולכן נבדוק מ2 ועד למעלה
            if num % j == 0:
                counter = counter+1
                break  # must use break - otherwise will count more and more
    return counter


print(prime2dList(range(-20, 9)))  # -20,9
# print(prime2dList(range(-9)))
