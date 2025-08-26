# 기본 print
print("Hello World!","Me Either!")

# 줄바꿈
print()



# 자료
print(type("안녕하세요!"))
print(type(3))
print(type(3.3))
print(type(True))

# "", ''
# Syntax Error
# print(""안녕하세요"라고 합니다")
print('"안녕하세요"라고 합니다.')
print("\"안녕하세요\"라고 합니다.")

#Escape Character \t
print("이름\t나이\t성별")
print("엄태호\t23\t남자")

#Escape Character \n, \\
print("내 이름\n\\엄태호\\")



#연산자
#문자열 연결 연산자
print("안녕"+"하세요")

#문자열 반복 연산자
print(3*"안녕하세요 ")

#문자 선택 연산자
print("안녕하세요"[2])

#문자열 범위 선택 연산자
print("안녕하세요"[:3])

#Index Error
#print("안녕하세요"[10])

#문자열 길이
print(len("안녕하세요"))



#숫자형
print(3 + ( 2 + 4 ) / 6 * 2 )
print( 7 // 2)
print(7 % 2)
print( 7 ** 2)



#변수
pi = 3.141592

#복합 대입 연산자
pi += 1
print(pi)

pi -= 1
print(pi)

pi //= 2
print(pi)

pi %= 2
print(pi)

#input 함수
a = input("값을 입력하세요 : ")
a = int(a)
print(a,type(a))

a = float(a)
print(a,type(a))

a =str(a)
print(a,type(a))

#Value Error
