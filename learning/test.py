import re


def increment_string(strng):
    if not strng:
        return '1'
    regular_digit = re.findall(r'\d+', strng)
    regular_alpha = re.findall(r'[a-zA-Z]+[^0-9]', strng)
    if not regular_digit:
        strng += '1'
        return strng
    if not regular_alpha:
        strng = str(int(strng) + 1)
        return strng

    result_strng = '0' * (len(regular_digit[0]) - len(str(int(regular_digit[0])+1))) \
                   + str(int(regular_digit[0])+1)
    return regular_alpha[0] + result_strng

print(increment_string('010'))
print(int('0042'))
