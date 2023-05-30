def custom_split(text: str, split_symbol: str = "") -> list:
    result = []
    temp_str = ''
    for i in text:
        if i == split_symbol:
            result.append(temp_str)
            temp_str = ''
            continue
        temp_str += i
    
    return result

lorem = "     lAmet labore eros    \n    feugait blandit    \n     ea diam erat ut\n    in dolor"

print(custom_split(lorem, "\n"))

print(len("\n"))