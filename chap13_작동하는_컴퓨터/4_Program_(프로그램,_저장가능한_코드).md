# Program (프로그램, 저장가능한 코드)

처음 레벨에 들어가면,

instruction input 이 이제는 없다고 한다.


💡

instruction input 은 어떤 동작을 할지 선택하는 비트이다.

01 : Calculation (ALU 로 REG1 과 REG2 를 계산해서 REG3 에 넣기)

10 : Copy (레지스터들끼리 값 복사)

11 : Condition (아직 구현 안함)



![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image.png)

우리가 깼던 CALCULATIONS 에서는 Instruction 이 input 으로 주어졌다.

[CALCULATIONS - 사칙연산 계산기](CALCULATIONS%20-%20%E1%84%89%E1%85%A1%E1%84%8E%E1%85%B5%E1%86%A8%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%89%E1%85%A1%E1%86%AB%20%E1%84%80%E1%85%A8%E1%84%89%E1%85%A1%E1%86%AB%E1%84%80%E1%85%B5%201bc80ae0869c8127b875f80d9b6f0fdb.md) 

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%201.png)

이제 이 input 이 순서대로 나열되어있고, 하나 하나 순서대로 입력되는 어떤 장치인 “Program” 이라는 것으로 대체되었다.

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%202.png)

이 “Program” 부품의 하단 설명을 보면,

- input 으로 Address 를 넣으면, output 으로 출력된다.

뭔소리인지 실험해보자

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%203.png)

Byte Maker 랑 Splitter 를 달아서 테스트해보면,

- 4 를 넣으면 Program 에 적힌 4번째 숫자인 64 가 출력된다

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%204.png)

- 2를 넣으면 2번째 숫자인 177 가 출력된다.

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%205.png)

이해했다. Program 은 입력한 번지수(Address) 에 있는 Value 를 출력하는 부품이다.

# 클럭(Clock)

그러면 순서대로 하나 하나 읽으려면 어떻게 해야할까?
그렇다. 옛날에 만든 **클럭**을 달면 된다.

[COUNTER - 클럭](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021.md) 

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%206.png)

# 스테이지 깨기

그냥 PROGRAM 이라는 부품으로 바뀌었을뿐, 그냥 input 으로 했던 것 처럼 연결해주면 된다.

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%207.png)

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%208.png)

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%209.png)

# 천공카드

현대의 컴퓨터는 코드를 메모리에 저장하는데,

옛날의 컴퓨터는 이 레벨에 등장하는 Program 처럼, 

**opcode 를 순서대로 적은 종이를 읽어서 작동했다.**

[https://namu.wiki/w/천공 카드](https://namu.wiki/w/%EC%B2%9C%EA%B3%B5%20%EC%B9%B4%EB%93%9C)

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%2010.png)

![image.png](/images/4_Program_(프로그램,_저장가능한_코드)/Program_(프로그램,_저장가능한_코드)%201bc80ae0869c8157ae63c3dda2cf6dfe/image%2011.png)