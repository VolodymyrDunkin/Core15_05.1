import re

s = "I am 25 years old 34, 565"
age = re.search('\d+', s)
print(age.group())

all_ages = re.findall('\d{2}\s', s)

print(all_ages)


result_sub = re.sub(r"(\d+)", "тут має бути реклама", s)

print(result_sub)