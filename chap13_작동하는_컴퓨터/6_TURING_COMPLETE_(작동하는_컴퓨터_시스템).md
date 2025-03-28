# TURING COMPLETE (작동하는 컴퓨터 시스템)

# Conditions 부착

이제 여기에 Conditions 를 달기만 하면 완성이다.

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%2014.png)

# Condition

우리가 Conditions 에서 만들었던 COND 부품은 이렇게 사용한다.

[Conditions - 조건분기 구현](Conditions%20-%20%E1%84%8C%E1%85%A9%E1%84%80%E1%85%A5%E1%86%AB%E1%84%87%E1%85%AE%E1%86%AB%E1%84%80%E1%85%B5%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB%201bc80ae0869c81bda41fdab62800e0e3.md) 

- 입력으로 Condition 코드와 Input 값을 넣는다.
- Condition 으로 다양한 비교를 선택할 수 있고, 그 결과가 True/False 로 Result 핀으로 출력된다

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image.png)

선택할 수 있는 Condition 코드는 아래와 같다.

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%201.png)

- 우리는 Condition Code 로 Program 에 있는 코드를 쓸거고,
- 비교할 값인 Input 으로는 REG3 에 있는 값을 써야 한다. (레벨의 요구사항임)
    - REG3 은 ALU 의 계산 결과가 저장되는 EAX 이다.

이렇게 연결하면 된다.

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%202.png)

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%203.png)

# 분기(Branch)

컴퓨터는 Conditions(조건)을 판별하여 True/False 로 알려주는 것 뿐만 아니라, 그 결과에 따라서 다른 동작을 해야한다.

```c
if(너무 더우면){
	에어컨을 켠다
}else{
	에어컨을 끈다
	}
```

이러한 “조건을 판별해서 그 결과에 따라 코드 실행을 다르게 하는 것” 을 어려운 말로 분기(Branch) 라고 부른다. (또는, 조건부 실행(Conditional Execution))

우리는 여태껏 Counter 에 따라 Address 가 1 씩 순서대로 증가하면서 순서대로 작동하는 Program 만 다뤘다.

이제, Address 가 **Conditions 에 따라 달라질 수 있게 만든다.**

# 점프(jmp)

우리의 컴퓨터에는 PROGRAM 의 Address 가 Counter 에 의해 1 씩 증가하면서 순서대로 실행시킨다.

Address 를 중간에 바꾸면, 순서대로가 아니라 Program 에 적힌 코드 어딘가로 순간이동할 수 있다.

이것을 **점프(Jump)** 라고 부른다.

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%204.png)

Program 에 달린 Counter 를 조작하면, 현재 코드를 실행중인 Address 를 바꿀 수 있다. 그럼 그곳으로 점프된다.

- Increment/Overwrite 핀을 켠 상태로,
- Overwrite Value 에 바꿀 Address 값을 넣으면 된다.

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%205.png)

점프하려면, 어디로 점프할지 지정해야한다.

이때 REG 0 에 이 값을 저장하도록 한다. (레벨 로그에 나와있음)

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%206.png)

# 분기 회로 만들기

우선 REG 0 에 저장된 값이 Counter 의 Overwrite Value 로 입력되도록 선을 연결한다.

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%207.png)

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%208.png)

이제, Increment / Overwrite 핀이 켜지면  코드가 이 값으로 점프될 것 이다.

그리고 OPCODE 가 Condition 이면서 Cond 부품이 비교한 결과가 True 일때 Increment/Overwrite 핀이 켜지도록 연결한다

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%209.png)

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%2010.png)

# 전체 정답

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%2011.png)

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%2012.png)

# Turing Complete

작동하는 컴퓨터를 완성했다!

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%2013.png)

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%2014.png)

이 컴퓨터는 Turing Complete (튜링 완전) 하다.

무슨 말이냐면, **컴퓨터이기 위한 최소한의 요건을 만족했다** 라는 뜻임

![image.png](/images/6_TURING_COMPLETE_(작동하는_컴퓨터_시스템)/TURING_COMPLETE_(작동하는_컴퓨터_시스템)%201bc80ae0869c8141acc5e7248c797fe2/image%2015.png)