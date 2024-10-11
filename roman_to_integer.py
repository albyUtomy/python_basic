def roman_to_integer(input_str:str)->str:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    previous_val = 0


    for char in input_str:
        if char in roman_map:
            current_val = roman_map[char]
            
            if current_val > previous_val:
                total += current_val - 2 * previous_val
            else:
                total += current_val
            previous_val = current_val

        else:
            return "Invalid input or out of range"
    return total

print(roman_to_integer('IV'))
        