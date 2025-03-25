# 카르노맵 XOR

# SOP

우리는 AND 와 OR 을 카르노맵에서 찾을 수 있다는걸 배웠다.

- 뭉탱이는 AND 로 묶는다.
- 뭉탱이끼리 OR 로 연결한다.

그런다음 회로로 구현하면 된다.

# XOR

조금 어렵지만, 카르노맵에서 **xor 로 묶을 수도 있다.**

일단, xor 은 입력 두개가 **서로 다르면 1** 을 출력하는 회로이다.

![image.png](/images/5_카르노맵_XOR/image.png)

![image.png](/images/5_카르노맵_XOR/image_1.png)

SOP 로 묶으면,

```
[A]B + A[B]
```

이다. 이걸 외운다.

아래 두개가 OR(더하기) 로 연결되어있으면,

```
(A의 부정)(B)
(A)(B의 부정)
```

그냥

```
A xor B
```

라고 줄일 수 있다.

# XOR 의 SOP

카르노맵에선, XOR 의 형태가 두개이다.

오른쪽에서 왼쪽으로 떨어지는 대각선이거나,

![image.png](/images/5_카르노맵_XOR/image_1.png)

0 을 사이에 두고 1 이 마주보고 있다.

![image.png](/images/5_카르노맵_XOR/image_2.png)

![image.png](/images/5_카르노맵_XOR/image_3.png)

# 변수 3개를 xor 로 묶기

![image.png](/images/5_카르노맵_XOR/image_4.png)

```
<빨간색>
[A][B]C + [A]B[C]
[A](B xor C)

<파란색>
AB[C] + A[B]C
A(B xor C)

<빨간색 + 파란색>
(B xor C) 를 하나로 보면,
A xor (B xor C)
xor 은 뭘 먼저 계산하던지 상관없다(결합법칙)
A xor B xor C
```

# XNOR

xnor 는 xor 을 한번 부정한건데, 진리표가 이거다.

![image.png](/images/5_카르노맵_XOR/image_5.png)

# XNOR 의 SOP

[A]B + A[B] 가 xor 이라면, xnor은

이다.

```
AB + [A][B]
```

카르노맵에서는 대각선이 xor 과 반대로 나온다.

![image.png](/images/5_카르노맵_XOR/image_6.png)

또는 0을 한칸 띄우고 1이 마주보고 있다.

![image.png](/images/5_카르노맵_XOR/image_7.png)

# 공식 : A xor B xor C

만약 카르노맵에 AB 의 xor 과 xnor 이 같이 있고, 기준이 되는 문자 C 가 있으면,

```
[C](A xor B) + C(A xnor B)

A xnor B 는 A xor B 의 부정이므로,
A[B]+[A]B 구조이다.

그래서 A xor B xor C 이다.
```

![image.png](/images/5_카르노맵_XOR/image_8.png)