# Python study

## 변수와 연산자
```python
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
```

## 숫자 처리함수
```python


# 숫자 처리 함수
print(abs(-5)); # 5
print(pow(4, 2)); # 4^2 = 4*4 = 16
print(max(5, 12)); # 최대값 출력
print(min(5, 12)); # 최소값 출력
print(round(3.14)); # 반올림, 3
print(round(4.99)); # 반올림 5

from math import * # 계산 라이브러리 호출
print(floor(4.99)); # 내림, 4, JavaScript : Math.floor();
print(ceil(3.14)); # 올림, 4
print(sqrt(16)) # 제곱근, 4

```

## 랜던 함수
```python

# 랜덤 함수
from random import * # 랜던 함수 라이브러리 호춣
print(random()) # 0.0 ~ 1.0 미만의 임의의 난수 값을 생성, JacaScript : Math.random();
print(random() * 10); # 0.0 ~ 10.0 미만의 임의의 난수 값을 생성
print(int(random() * 10)); # 소숫점 제외
print(int(random() * 10) + 1); # 1부터 10 미만의 수
print(int(random() * 45) + 1); # 1 ~ 45 이하의 수 생성
print(randrange(1, 46)); # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)); # 1 ~ 45 이하의 임의의 값 생성

#
print(randint(4, 28));
offDate = randint(4, 28);
print("오프라인 모임 날짜는 매월" + str(offDate) + "입니다.");
print("오프라인 모임 날짜는 매월", offDate, "입니다.");
```

## 문자열 출력
```python
# 문자열 츌력
sentence = 'Im a boy';
print(sentence);
sentence2 = "Python is easy";
print(sentence2);
sentence3 = """
Im a boy
You are girl
Python is Easy
"""
print(sentence3)
```

## 슬라이싱
```python
# 슬라이싱
juminNum = "160321-1234567";
print("성별 : " + juminNum[7]); # 1
print("생년", juminNum[0:2], "년생");
print("월" + juminNum[2:4] + "월");
print("생년월일" + juminNum[0:6]);
print("뒷자리" + juminNum[7:]); # 앞에서 7번째부터 끝까지
print("뒷자리" + juminNum[-7:]); # 맨뒤에서 7번째부터 끝까지)
```


## 문자열 처리함수
```python
# 문자열 처리함수
python = "Python is Amazing";
print(python.lower()); # 소문자로 출력
print(python.upper()); # 대문자로 출력
print(python[0].isupper()); # 첫번째 문자가 대문자인가? => True
print(len(python)); # python 문자열의 자릿수, JavaScript : python.length;
print(python.replace("Python", "Java")); # 원하는 값을 덮어쓰기(바꾸기), Java is Amazing
index = python.index("n"); # python 문자열에서 "n" 글자가 몇번째 있는지 출력
print(index); # 5
index = python.index("n", index +1); # 앞에서 찾은 index 값에서 1자리 뒤에서부터 "n" 이 몇번째 인지 찾기
print(index);

print(python.find("Java")); # -1 출력
# print(python.index("Java")); # 오류 출력
print(python.count("n")); # python 문자열에서 "n" 이 몇개인지 출력, 2
```