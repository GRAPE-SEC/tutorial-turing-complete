# Bit Switch (트랜지스터)

# 정류작용(rectifying)

아주 옛날에 얘기했던, 계전기(Relay) 처럼 전기신호로 껐다켰다하는 스위치를

스위칭 소자(Switching Device) 라고 부른다.

Switching Device 는 계전기, 트랜지스터, 진공관 등이 있는데,

**논리적으로 and gate 와 동일하다. (진리표가 같음)**

다만 차이가 있는데, 전류가 흐르는 방향이 있어서 전류가 역류하지 않는다.

아래를 보면,

논리적으로는 똑같지만, AND 는 논리게이트라서 정류작용을 하지 않으므로, 오류가 발생한다.


💡

그래서 다른 Swtich 의 출력이 또다른 Switch 입력과 연결되어도 괜찮다. 



![image.png](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/image.png)

실제 현실세계에서 이렇게 전기가 무한으로 흐르는 것을 **단락(Short)** 라고 부르는데, 그러면 회로가 타버린다.

회로를 설계할 때, and 게이트의 출력을 서로 연결해야할 일이 생기는데, 그럴 때 이런 부품이 활용된다.

전기가 거꾸로 흐르지 않아서 다른 부품들이 타버리지 않고 보호된다.

이 게임에서, Switch 는 현실의 스위칭 소자를 비유한 것이고, 실제 현실에서 자주 쓰이는 스위칭소자는 트랜지스터이다.

![image.png](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/image%201.png)

# 스테이지 깨기

이 과제는 switch 와 not 으로 xor 를 만들라고 하는데,

and gate 와 not 으로 xor 를 만드는 것과 동일하게 생각하면 된다

사용할 수 있는 소자 개수에 제한이 있다. 

Switch 2개, Not 2개로 구현해야한다. 

![Untitled](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/Untitled.png)

진리표를 그려보면, and, not, or 이 필요하다.

그러나 or 이 없어서 덧셈을 못만든다.

![Untitled](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/Untitled%201.png)

근데 switch 는 전류를 순방향으로 흐르게하는 성질이 있으니 or 없이 그냥 붙여도 괜찮다.

![Untitled](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/Untitled%202.png)

# 현실의 정류작용

이건 체크벨브라는 부품인데, 물이 흐르는 파이프 안에 들어가서 물이 한쪽 방향으로만 흐르게 해준다(정류작용)

![image.png](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/image%202.png)

전기에 대해서 정류작용을 해주는 부품을 **다이오드(Diode)** 라고 부르는데,

뭔가 양자역학적인 원리로 벽을 만들어서 전기를 한쪽방향으로는 못 흐르게 가로막는다.

(몰라도 된다)

반대방향으로 너무 큰 전기를 흘려보내면 부셔지면서 걍 전기가 반대방향으로도 흐르는데, 항복현상이라고 부른다(Avalanche breakdown, Zener breakdown) 몰라도된다!

![image.png](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/image%203.png)

![image.png](/images/3_Bit_Switch_(트랜지스터)/Bit_Switch_(트랜지스터)%201bc80ae0869c81279a8ceade56e321a1/image%204.png)