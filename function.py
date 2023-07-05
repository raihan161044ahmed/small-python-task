def even_odd(x, y, string_input):
    if x <= y:
        if string_input == "even":
            for i in range(x, y+1):
                if i % 2 == 0:
                    print(i)
        elif string_input == "odd":
            for i in range(x, y+1):
                if i % 2 != 0:
                    print(i)
    else:
        if string_input == "even":
            for i in range(x, y-1, -1):
                if i % 2 == 0:
                    print(i)
        elif string_input == "odd":
            for i in range(x, y-1, -1):
                if i % 2 != 0:
                    print(i)


