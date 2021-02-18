def func(string):
    if type(string) != str:
        return
    my_words = string.split(" ")
    new_words = []
    for word in my_words:
        new_words.append(word[::-1])
    return " ".join(new_words)  # "מפריד".join(רשימה)


print(func("willy wonka"))
