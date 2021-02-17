
my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for inner_list in my_list:
    msg = ""
    for item in inner_list:
        msg += f"{item} "
    msg = msg.strip()  # trim spaces (left and right)
    print(msg)

    # required output
    # 1 2 3
    # 4 5 6
    # 7 8 9
