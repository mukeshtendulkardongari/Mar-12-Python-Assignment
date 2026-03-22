# upper(),lower(),title(),capitalize()

# 1. upper()

str1="Manjunadh"
res=""
for i in str1:
    if ord(i)>=97 and ord(i)<=122:
        res+=chr(ord(i)-32)
    else:
        res+=i

print(res)

# output:
# MANJUNADH

# 2. lower()

str1="MaNJUNADH"
res=""
for i in str1:
    if ord(i)>=65 and ord(i)<=90:
        res+=chr(ord(i)+32)
    else:
        res+=i

print(res)

# output:
# manjunadh

# 3. capitalize()

str1="manjUnaDh"

res=""
for i in range(len(str1)):
    ch=str1[i]
    if i==0:
        if 'a'<= ch <='z':
            res+=chr(ord(ch)-32)
        else:
            res+=ch
    else:
        if 'A'<= ch <='Z':
            res+=chr(ord(ch)+32)
        else:
            res+=ch
print(res)

# output:
# Manjunadh

# 4. title()


def my_title(s):
    result=""
    new_word=True

    for ch in s:
        if ch.isalpha():
            if new_word:
                result+=ch.upper()
                new_word=False
            else:
                result+=ch.lower()
        else:
            result+=ch
            new_word=True

    return result

s="my name is manju, i am 21 years old"
print(my_title(s))

# output:
# My Name Is Manju, I Am 21 Years Old