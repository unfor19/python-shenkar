# כל מספר שאני נתקל בו, הוא גיל
# הדפס את כל הגילים - מספרים
# מהו ממוצע הגילים באובייקט המורכב

def shir_recurse(obj, my_list):
    # רק אחד קורה לכל הרצה
    if type(obj) == int:
        my_list.append(obj)
    elif type(obj) == dict:
        if "age" in obj:
            shir_recurse(obj["age"], my_list)
    elif type(obj) == list:
        for item in obj:
            shir_recurse(item, my_list)

    return my_list


my_object = [
    [
        2,
        3,
        6,
        {"age": 14}
    ],
    {
        "age": 23,
        "name": "meir"
    },
    33,
    [
        45,
        80,
        {"name": "shir"},
        [99, 101, 131, [192, 188]]
    ]
]

# getting all the ages in the same list
age_list = shir_recurse(my_object, [])
print(age_list)

# calculation logic
if age_list:  # if true, yaani has items
    sum_ages = sum(age_list)
    len_ages = len(age_list)
    avg_ages = round(sum_ages / len_ages, 2)
    msg = f"Number of items: {len_ages}\nAvg ages: {avg_ages}"
    print(msg)
