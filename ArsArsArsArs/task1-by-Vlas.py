def isnumber(string: str):
    return string.isnumeric()


def nonumber_error(inp: str):
    print("You have entered not a row of digits, dummy!")


def working(inp: str):
    inp2 = inp.replace(inp[0], "", 1)
    inp3 = inp2.replace(inp2[0], "", 1)
    inp4 = inp3.replace(inp3[0], "", 1)
    print(inp4)


condiditions = {"False": nonumber_error, "True": working}

inp = input("Enter a row of digits: ")
result_isnumber = isnumber(inp)
result_conditions = condiditions[str(result_isnumber)]
result_conditions(inp)
