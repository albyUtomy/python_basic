def reverseWords(s: str) -> str:
        str_lst = [word for word in s.split()]
        reversed_list = str_lst[::-1]
        result_string = ' '.join(reversed_list)
        return result_string

print(reverseWords("Happy Birthday to you"))