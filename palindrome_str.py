def isPalindrome(s: str) -> bool:
    new_str = s.replace(" ","")
    new_str = "".join(char for char in new_str if char.isalnum())
    new_str = new_str.lower()

    if new_str[::] == new_str[::-1]:
        print("True")
    else:
        print("False")
        
isPalindrome("A man, a plan, a canal: Panama")