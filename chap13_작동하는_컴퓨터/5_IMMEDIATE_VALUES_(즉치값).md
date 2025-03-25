# IMMEDIATE VALUES (즉치값)

CALCULATIONS 레벨에서는 레벨에서 직접 레지스터에 값을 바꿔주었다.

이것을 외부에서 직접 OPCODE 를 이용해서 하도록 수정해보자.

[CALCULATIONS - 사칙연산 계산기](CALCULATIONS%20-%20%E1%84%89%E1%85%A1%E1%84%8E%E1%85%B5%E1%86%A8%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%89%E1%85%A1%E1%86%AB%20%E1%84%80%E1%85%A8%E1%84%89%E1%85%A1%E1%86%AB%E1%84%80%E1%85%B5%201bc80ae0869c8127b875f80d9b6f0fdb.md) 

# immediate value(즉치값)

직접 레지스터에 어떤 값을 저장하도록 하는 명령을 즉치(immediate) 라고 한다.

그러한 값을 immeidate value(즉치값) 이라고 한다.

# 레벨 로그

OPCODE 로는 맨 앞의 두개의 비트가 00 이면 immeidate mode(즉치 모드) 라고 한다.

- immediate value 로 값을 세팅할 수 있는 레지스터는 **REG0 으로 정해져있다.**
- 다른 레지스터들(REG1 ,REG2, REG3 등) 에 값을 설정하려면, **REG0 를 한번 거쳐서 가야한다**
    - REG0 로 우선 즉치모드로 값을 저장한다음, COPY 모드로 REG0 에서 다른 레지스터로 옮겨야한다

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image.png)

# REG0 와 연결된 회로 수정

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%201.png)

OR 을 사이에 넣고,

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%202.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%203.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%204.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%205.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%206.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%207.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%208.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%209.png)

그러나 아직 REG0 에 immediate value 가 저장이 안되는데,

그 이유는 OPCODE 가 COPY 가 아닐때는 DEC 이 비활성화 되도록 되어있어서, 레지스터의 SAVE 핀이 켜지지 않기 때문이다.

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%2010.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%2011.png)

그러니까 OPCODE 가 IMMEDIATE 일때도 SAVE 핀이 켜지도록 OR 을 달아준다

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%2012.png)

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%2013.png)

# 전체 정답

![image.png](/images/5_IMMEDIATE_VALUES_(즉치값)/IMMEDIATE_VALUES_(즉치값)%201bc80ae0869c81a49503f46769b2835d/image%2014.png)