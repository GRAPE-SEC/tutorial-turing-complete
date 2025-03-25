# ARITHMETIC ENGINE

# Arithmetic Engine (산술 연산기)


💡

Logic Engine 은 OR, NAND, AND 같은 논리게이트를 “코드” 로 선택할 수 있게 해주는 회로이다.

Arithmetic Engine 은 더하기 빼기도 선택할 수 있는 기능을 추가한 것이다.



즉, Logic Engine 에 Full Adder 를 합친거다.

[Logic Engine - 연산 선택기](Logic%20Engine%20-%20%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%89%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A2%E1%86%A8%E1%84%80%E1%85%B5%201bc80ae0869c81dc8102f2dd3a15a07e.md) 

[Full Adder (전가산기)](Full%20Adder%20(%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%80%E1%85%A1%E1%84%89%E1%85%A1%E1%86%AB%E1%84%80%E1%85%B5)%201bc80ae0869c8173b4b1ecd55fcf0c29.md) 

문제 조건은 다음과 같다.

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled.png)

Instruction 입력을 클릭해서 데이터를 바꿔보면 각 숫자에 대응되는 명령어가 표시된다.

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_1.png)

OR, NAND, NOR, AND, ADD, SUB 이 6개의 논리 연산을 하는 회로를 만들고, Instruction 입력에 따라 이 회로가 동작하도록 하면 될 것 같다.

## 명령어 해석기 만들기

이진수 입력을 자릿수에 따라 분해하려면 Decoder 를 사용한다.

입력이 6개이므로, 2^3 보다 작다. 그러므로 3 Bit decoder 를 사용하면 된다.

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_2.png)

3bit 범위인 0~7 까지 데이터를 Decode 할 수 있다.

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_3.png)

## OR, NAND, NOR, AND, ADD, SUB 연산 구현하기

OR, NAND, NOR, AND 의 논리게이트를 선을 자르지 않고, “코드” 로 선택할 수 있도록, 전부 가져다가 놓는다.

“코드” 를 압축해제하기 위해서 3-Bit-Decoder 를 단다.

[3-Bit DECODER](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29.md) 

![image.png](/images/1_ARITHMETIC_ENGINE/image.png)

우선 논리연산들인 OR, NAND, NOR, AND 를 먼저 구현한다.

- 주의) bit 용 논리소자가 아니라, Byte 용을 써야한다.

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_4.png)

ADD 와 SUB 를 구현한다.

- SUB 는 그냥 첫번째 입력에 NEG 을 넣어서 음수로 만들면 된다.
    - NEG 는 2의보수법(2’s complement) 로 음수로 바꾸는 소자이다.
    - 폰 노이만 센세 덕분에, 전가산기 만으로 뺄셈을 만들 수 있다. 그냥 음수를 더하면 된다
    - [2’s Complement(2의 보수법)](2%E2%80%99s%20Complement(2%E1%84%8B%E1%85%B4%20%E1%84%87%E1%85%A9%E1%84%89%E1%85%AE%E1%84%87%E1%85%A5%E1%86%B8)%201bc80ae0869c8153a420c4e352ddd215.md)

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_5.png)

이제 이걸 8 Bit Switch 로 Decode 된 Instruction 에 따라 선택하면 된다.

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_6.png)

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_7.png)

# 최종 정답

![Untitled](/images/1_ARITHMETIC_ENGINE/Untitled_8.png)