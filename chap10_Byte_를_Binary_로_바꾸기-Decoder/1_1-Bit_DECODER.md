# 1-Bit DECODER

# Decoder (디코더)

컴퓨터는 “디코더” 라는 장치를 이용해서 데이터를 보낼 때는 압축을 하고, 받을 때 압축을 해제한다.

압축을 해제하는 장치를 Decoder, 압축하는 장치를 Encoder 라고 부른다

디코더는 일종의 압축해제 장치이다.

실제 데이터와 일대일대응되는 부호화된 입력을 **코드(Code)** 라고 부른다.

디코더는 이 “코드” 를 데이터로 변환한다.

# 1 BIT Decoder (이진 디코더)

이진법으로 된 **코드**를 이진코드(Binary Code)라고 부른다.

코드랑 데이터는 일대일대응된다

- 0 이 입력되면 데이터 01 로 변환한다.
- 1 이 입력되면 데이터 10 로 변환한다

입력은 하나고, 출력은 두개이다.

켜지면 1, 꺼지면 0 이므로

병렬로 하나만 not 을 해서 연결하면 된다.

![Untitled](1-Bit%20DECODER%201bc80ae0869c81c1a30dd6a5e3ee488a/Untitled.png)

# 이 회로의 쓰임새

우리가 가진 입력은

- 1 (켜짐)
- 0 (꺼짐)

두개 만 표현할 수 있다

![image.png](1-Bit%20DECODER%201bc80ae0869c81c1a30dd6a5e3ee488a/image.png)

![image.png](1-Bit%20DECODER%201bc80ae0869c81c1a30dd6a5e3ee488a/image%201.png)

이 회로는 이 입력을 분리해서,

- 입력이 0 일때는 10 을 출력해라

![image.png](1-Bit%20DECODER%201bc80ae0869c81c1a30dd6a5e3ee488a/image%202.png)

- 입력이 1 이면 01 을 출력해라

![image.png](1-Bit%20DECODER%201bc80ae0869c81c1a30dd6a5e3ee488a/image%203.png)

로 바꿔준다.

이게 뭔 소용이냐고 할 수 있겠는데,

원래는 입력이 0 (꺼짐) 이면, 꺼져있을 뿐이였는데,

이 회로는 “꺼짐” 일때도, “꺼져있음” 비트가 1 이 된다.

- 내가 꺼져있음을 알리는 신호가 추가되었다고 볼 수 있다

![image.png](1-Bit%20DECODER%201bc80ae0869c81c1a30dd6a5e3ee488a/image%204.png)

이게 알쏭달쏭한 소리처럼 들릴텐데, 3-Bit Decoder 를 만들어보면 무슨 말인지 이해하게된다