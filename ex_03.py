lorem = "lAmet labore eros feugait blandit ea diam erat ut in dolor"

lorem = lorem.upper()

print(lorem)

find_l_first = lorem.find('L')

find_l_last = lorem.rfind('l'.upper())

print(lorem[find_l_first:find_l_last + 1])

# if find_l >= 0:
#     print(f"""Find in position {find_l}""")
# else:
#     print("Not find")