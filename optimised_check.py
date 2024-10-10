def adjacent_bracket(input_str:str)->bool:
    bracket_list = ('()','{}','[]','<>')

    while any(pair in input_str for pair in bracket_list):
        for pair in bracket_list:
            input_str = input_str.replace(pair,"")

    return len(input_str) == 0

print(adjacent_bracket("(){}[]<>"))
print(adjacent_bracket("([{}])"))
print(adjacent_bracket("{[}]"))
print(adjacent_bracket("{(})"))
print(adjacent_bracket("{[(<>)]}"))