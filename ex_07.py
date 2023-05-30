text = "{} Test {} {} {}"

print(text.format("this", 
                  "and this", 
                  "more this", 
                  "end more this"))

text1 = "{:#d}".format(10)

print(text1)

for num in range(20):
    print("{n:03d}||||{n:#x}|{n:>10o}|{n:<10b}".format(n=num))
    
    
print("pi {:0.3}".format(113.1415))

