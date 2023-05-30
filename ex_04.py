lorem = "     lAmet labore eros    \n    feugait blandit    \n     ea diam erat ut\n    in dolor"

split_data = lorem.split("\n")

split_data_clear = [i.strip() for i in split_data]

print(split_data)
print(split_data_clear)

print(":".join(split_data_clear[:1]))

print(split_data_clear[0])
print(split_data_clear[:1])

print(lorem[10:30])