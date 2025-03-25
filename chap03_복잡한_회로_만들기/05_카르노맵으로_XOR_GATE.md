# 9-1. 카르노맵으로 XOR GATE

XOR 게이트는 게이트 중에서 제일 특이한 게이트인데, 이 게이트는 

이 게이트는 입력 두개가 서로 다른지 검사한다. **다르면 1 을 출력하고, 같으면 0 을 출력한다.**

진리표는 이렇다.

| input1 | input2 | output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

카르노맵을 그리면,

![image.png](/images/05_카르노맵으로_XOR_GATE/image.png)

A and [B] 와 [A] and B 를 합친 회로라는걸 알 수 있다

![image.png](/images/05_카르노맵으로_XOR_GATE/image_1.png)

![image.png](/images/05_카르노맵으로_XOR_GATE/image_2.png)

![image.png](/images/05_카르노맵으로_XOR_GATE/image_3.png)

![image.png](/images/05_카르노맵으로_XOR_GATE/image_4.png)

# 수학

지금쯤이면 다들 눈치 챘을 건데, 사실 논리 게이트는 **수학 계산과 똑같다.**

- and : + (더하기)
- or : x (곱하기)

즉, 논리 회로는 **“1 과 0 만 가지고 더하기 곱하기를 하는 것”** 이다

XOR 게이트는 

```
(A x [B]) + ([A] x B)
```

를 계산한다.

# 답

![image.png](/images/05_카르노맵으로_XOR_GATE/image.png)

![image.png](/images/05_카르노맵으로_XOR_GATE/image_1.png)

계속…