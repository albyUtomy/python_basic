def stack_bracket_validation(input_str:str)->bool:
    bracket_map ={'}':'{', ')':'(', ']':'[','>':'<'}
    stack = []


    for char in input_str:
        if char in bracket_map:
            top_element = stack.pop() if stack else ""

            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(stack_bracket_validation("[{}()]"))
print(stack_bracket_validation("[]()"))
print(stack_bracket_validation("{[}]"))