# 3. NOT GATE

![image.png](3%20NOT%20GATE%201bc80ae0869c81ef82b2c1b321c9bbe2/image.png)

앞으로도 계속 Desired output 과 Current output 이 아래에 표시될 건데요

Current ouput 은 현재 내가 와이어로 연결한 것의 ouput 이 표시되는 것이고,

Desired output 은 현재 스테이지를 깨기 위한 목표입니다.

즉,


💡

와이어 연결을 수정해서 스테이지가 요구하는 Desired output 만들기 

</aside>

를 하는 것이 이 게임의 목표입니다.

그걸 순서대로 깨다 보면 컴퓨터가 완성되는 것이죠

# NOT GATE

NOT 게이트는 input 이 1 이면 output 이 0 이고, 

input 이 0 이면 output 이 1 이 되게 하는 게이트입니다.

논리 게이트들을 종류별로 만드는 것이 일단 목표인데요, 앞으로 만들 다른 논리 게이트는 이렇습니다.

- AND
- NOT
- OR
- XOR

사실 복잡해 보이지만 그냥 청기 백기 게임을 전기로 할 수 있는 기계일 뿐입니다.


💡

청기 올리고 백기 올리지마 청기 올리지말고 백기 올리지마

</aside>

걍 그런겁니다. 컴퓨터는 단순하죠

NOT 게이트는 input 1 과 input 2 가 똑같도록 같은 선에 연결하면 됩니다.

강줄기를 두갈래로 나누면 두 강줄기에 물이 흐르는 것 처럼,

전기도 마찬가지로 선이 두갈래로 나뉘면 두 선에 전기가 흐릅니다. 중학교 과학시간에 배우는거죠

전기가 줄어들지 않냐고요? 맞습니다. 근데 컴퓨터 만들때 얼마나 전기를 나뉘어 먹힐지 계산하고 설계하기 때문에 괜찮습니다.

![image.png](3%20NOT%20GATE%201bc80ae0869c81ef82b2c1b321c9bbe2/image%201.png)

input 을 쪼개서 input 1 과 input 2 에 집어넣으면 스테이지 클리어입니다.

![image.png](3%20NOT%20GATE%201bc80ae0869c81ef82b2c1b321c9bbe2/image.png)

## 회로 테스트하기

꺽쇠 버튼을 누르거나 F5 를 누르면 Input 을 바꿔가며 테스트할 수 있습니다.

아래 패널에 있는 Input 이 순서대로 전기신호로 입력되고, Current output 에 결과가 표시됩니다

![image.png](3%20NOT%20GATE%201bc80ae0869c81ef82b2c1b321c9bbe2/image%202.png)

Desired output 과 Current output 이 일치하면 통과되고, Level Complete 가 표시됩니다.

![image.png](3%20NOT%20GATE%201bc80ae0869c81ef82b2c1b321c9bbe2/image%203.png)

또한 NOT 게이트를 만들었으니, 다음 스테이지부터는 NAND 로 부터 만들지 않고 직접 사용할 수 있게 되었습니다.

![image.png](3%20NOT%20GATE%201bc80ae0869c81ef82b2c1b321c9bbe2/image%204.png)

Onwards 를 누르면 다음 스테이지로 이동합니다.

# NAND 게이트의 신비로운 성질

과학자들과 수학자들은 NAND 게이트가 여러개 있으면 그거끼리 잘 연결해서 다른 논리 게이트 들을 모두 만들 수 있다는 매우 놀라운 사실을 발견했습니다.

즉, NAND 게이트만 있으면 다른 게이트를 따로 만들 필요가 없습니다.

NAND 끼리 연결해서 만들 수 있는거죠 몹시 신기합니다

앞으로 모든 논리 게이트를 NAND 로 만들거나, NAND 로 만든 다른 게이트로 만듭니다.

NAND 로 만든 게이트는 NAND 로 되어있으니 전체를 NAND 로 만든거나 다름 없죠


💡

네 그렇습니다… 컴퓨터는 온통 NAND 입니다

</aside>

계속…