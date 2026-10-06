input_value = input()
input_value_list = list(input_value)
for number, letter in enumerate(input_value_list):
    if ord(letter) >= 65 and ord(letter) <= 90:
        letter = chr(ord(letter) + 32)
        input_value_list[number] = letter

str_input_value = ''.join(input_value_list)

print(str_input_value)



