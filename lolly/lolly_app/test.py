# def format_integer(number, thousand_separator='.'):
#     def reverse(string):
#         string = "".join(reversed(string))
#         return string

#     s = reverse(str(number))
#     count = 0
#     result = ''
#     for char in s:
#         count = count + 1
#         if count % 3 == 0:
#             if len(s) == count:
#                 result = char + result
#             else:
#                 result = thousand_separator + char + result
#         else:
#             result = char + result
#     return result

# num = input('enter the num')
# print(format_integer(num))


# file = open('blind_test_gpt-j.exc', 'r')
# read_data = file.read()
# per_word = read_data.split()

# print('Total Words:', len(per_word))



from babel.numbers import format_decimal
value = input('enter the number')
print(format_decimal(value, locale='en_US'))