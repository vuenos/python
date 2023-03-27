print(5);
print(-3.14);
print(8+8);
print(6*6);
print(3*(5+8));
print("파이썬");
print("파이 "*9);
print(5 > 10);
print(5 < 10);
print(not True);

# variable
name = "Jintae kim";
age = 24;
age = 17; # 변수값 재할당
is_adult = age >= 18;

print("My name is " + name + ", age is" + str(age) + " - " + str(is_adult)); # 
print("My name is", name, "age is",age, "-", is_adult);

# Operator
print(2**3); # 2^3 = 8
print(10%3); # 나머지 구하기 1
print(10//3); # 나눈 몫의값 3

print(10 > 3); # True
print(4 >= 7); # False

print(3 == 3); # True
print(4 == 7); # False
print(3 + 4 == 7); # True

print(1 != 3); # True, 값이 다름을 판별
print(not (1 != 3)); # False, not 뒤의 결과의 반대를 출력

print((3 > 0) and (3 < 5)); # True, and 연산자 : 앞뒤의 값이 모두 만족할때 True
print((3 > 0) & (3 < 5)); # True 위와 동일

print((3 > 0) or (3 > 5)); # True, 앞 뒤의 값 중 한개만 만족해도 True
print((3 > 0) | (3 > 5)); # True, 위와 동일

cal1 = 2 + 3 * 4;
print(cal1); # 14 

cal1 = cal1 + 3;
print(cal1); # 17
cal1 += 2; # cal1 = cal1 + 2 와 동일
print(cal1); # 19
cal1 *= 2; # cal1 = cal1 * 2 와 동일
print(cal1); # 38