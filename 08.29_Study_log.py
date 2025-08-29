#format 함수 연습

#정수
print("{}".format(52))
print("저는 {}살 이고요. 몸무게는 {}kg 입니다.".format(23,61))
print("{:d}".format(52))
print("{:5d}".format(52))
print("{:05d}".format(52))
print("{:+5d}".format(52))
print("{:+5d}".format(-52))
print("{:=+10d}".format(52))
print("{:=+10d}".format(-52))
format("{:=+010d}".format(52))

#실수
print("{:15f}".format(52.273))
print("{:+15f}".format(52.273))
print("{:015f}".format(52.273))
print("{:+015.3f}".format(52.273))
print("{:+015.2f}".format(52.273))

#general, e
print("{:+015g}".format(52.273))
print("{:+015e}".format(0.000012))


#upper, lower
a = "Hello My name is Jim"

a = a.upper()
print(a)

a = a.lower()
print(a)

#strip
a = """
    안녕하세요
    저는 미국에서 온 Jim이라고 합니다.

"""

print(a.rstrip())
print(a.lstrip())
print(a.strip())

#isOO
print("Hello033".isalnum())
print("Hello".isalpha())
print("0310".isdecimal())
print("0310".isdigit())
print("    ".isspace())
print("hello my name is".islower())
print("HELLO MY NAME IS".isupper())


#find & rfind
print("안녕안녕하세요".find("안녕"))
print("안녕안녕하세요".rfind("안녕"))


#in
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

#split
print("10 20 30 40 50".split())
print("10,20,30,40,50".split())