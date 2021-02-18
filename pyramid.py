# get number, print pyramid - הפוכה

def draw_pyramid(num):
    row_list = list(range(num, 0, -1))
    for row in row_list:
        msg_row = ""
        col_list = list(range(1, row+1))
        for col in col_list:
            msg_row += f"{row}"  # str(col)
        print(msg_row)


draw_pyramid(5)
