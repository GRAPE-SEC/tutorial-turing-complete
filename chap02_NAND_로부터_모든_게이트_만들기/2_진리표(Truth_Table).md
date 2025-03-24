# 5-1. 진리표(Truth Table)

input 과 output 이 논리게이트에 따라 어떻게 나오는지를 표로 정리한걸 진리표(Truth Table, 트루쓰 테이블) 이라고 부른다.

![image.png](5-1%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%85%E1%85%B5%E1%84%91%E1%85%AD(Truth%20Table)%201bc80ae0869c81c9b3b4daae5a6d6f2d/image.png)

이 진리표는 입력되는 전기신호를  A 랑 B 라고 하고, 출력을 C 라고 했을때 어떻게 작동하는지를 표로 표시한 것이다.

![image.png](5-1%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%85%E1%85%B5%E1%84%91%E1%85%AD(Truth%20Table)%201bc80ae0869c81c9b3b4daae5a6d6f2d/image%201.png)

그동안 만든 게이트들의 진리표를 그려보면 이해가 쉬울지도?

사실 그 동안 게이트를 만든 것은 **“다른 게이트들이 모두 NAND 로 부터 만들어질 수 있다” 는걸 확인하는 실습일** 뿐이으므로 중요하지 않다.

그냥 아래의 한글을 표로 바꿨을 뿐이다.

- input 두개로 0 0 이 입력되면, output 으로 0 이 나온다~
- input 0 , input 1 이 입력되면, output 으로 1 이 나온다~
- 이하 생략…

![image.png](5-1%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%85%E1%85%B5%E1%84%91%E1%85%AD(Truth%20Table)%201bc80ae0869c81c9b3b4daae5a6d6f2d/image%202.png)

# “부정” 표기법

어떤 1 과 0 이 될 수 있는 신호를 A 라 하자.

![image.png](5-1%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%85%E1%85%B5%E1%84%91%E1%85%AD(Truth%20Table)%201bc80ae0869c81c9b3b4daae5a6d6f2d/image%203.png)

이건 A 에다가 not 을 붙인 것이다.

“A의 부정” 이라고 읽는다.

![image.png](5-1%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%85%E1%85%B5%E1%84%91%E1%85%AD(Truth%20Table)%201bc80ae0869c81c9b3b4daae5a6d6f2d/image%204.png)


💡

¬A 라고 쓰기도 하고, [A] 라고 쓰기도 하고, ~A 라고 쓰기도 하는데, 다 똑같은 뜻이다. 걍 키보드에 저 키가 없어서 그렇게 쓰는거임



그니까, A 가 1 이면, “A의부정” 은 0 이고, A 가 0 이면, “A의부정” 은 1 이다.

만약 이런 진리표가 나오면,

![image.png](5-1%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%85%E1%85%B5%E1%84%91%E1%85%AD(Truth%20Table)%201bc80ae0869c81c9b3b4daae5a6d6f2d/image%205.png)

[A] 가 1 이고, [B] 가 1 이면, [C] 는 0 이다 라는 뜻이다.

그걸 다시말하면,

- A=1
- B=0

이면,

- C=1

라는 뜻 이다. 

![image.png](5-1%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%85%E1%85%B5%E1%84%91%E1%85%AD(Truth%20Table)%201bc80ae0869c81c9b3b4daae5a6d6f2d/image%206.png)