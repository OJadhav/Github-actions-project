
nums = [11, 21, 33, 21, 11, 21, 55, 66, 22, 11]

uniq = []

for n in nums:
    if n not in uniq:
        uniq.append(n)
        
print(uniq)