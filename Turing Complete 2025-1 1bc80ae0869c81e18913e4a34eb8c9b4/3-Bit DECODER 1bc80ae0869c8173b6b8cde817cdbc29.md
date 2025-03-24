# 3-Bit DECODER

# 3 BIT Decoder

- Decoder : 부호화된 입력(Code, 용량 작음)가 입력되면 실제 데이터(Data, 용량 큼) 로 바꾼다
- 3 Bit Decoder : 이진코드를 일대일대응으로 **해당 이진수만큼의 1을 출력한다.**

# 출력(데이터)

### 데이터는 “몇번째 비트가 켜져있는지” 를 의미한다.

예시) 2번 켜짐

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image.png)

예시) 6번 켜짐

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image%201.png)

### 출력이 1개보다 많으면 안된다

그러면 ? 라고 뜬다.

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image%202.png)

# 회로 만들기


💡

우리가 만들어야하는 회로는, 

1. 입력이 1 일때와 0 일때 각각 켜지는 회로(1-bit decoder) 를 달고,
2. 각각의 경우일때 특정 비트가 켜지도록

하면 된다.



## 1) 입력이 1 일때와 0 일때 각각 켜지는 회로(1-bit decoder) 를 달기

아래와 같이, 3개의 입력을 각각 1-bit decoder 에 연결해준다.

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image%203.png)

그러면, “켜져있음” 과 “꺼져있음” 을 각각 bit 로 분리할 수 있게 된다.

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image%204.png)

이제,

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image%205.png)

사실 이렇게 not 을 써도 되긴하다.

하지만 무슨일이 일어난건지 알기 힘들긴하다.

Decoder 를 쓰는게, 설계하는 입장에서 보기 편하다.

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image%206.png)

6 출력에 대해서도 만들어보면 이러하다.

![image.png](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/image%207.png)

이제 이걸 1,2,3,4,5,6,7,8 에 대해서 만들어주면 된다

# 최종 정답

![Untitled](3-Bit%20DECODER%201bc80ae0869c8173b6b8cde817cdbc29/Untitled.png)