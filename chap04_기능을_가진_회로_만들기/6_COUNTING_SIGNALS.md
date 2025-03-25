# COUNTING SIGNALS


👺

입력의 개수를 세는 회로를 만든다



# 비트 세기

이진수로 표현된걸 펼쳐서 output1,2,3 으로 만들자.

![image.png](/images/6_COUNTING_SIGNALS/image.png)

# 4변수 다출력 카르노맵 그리기

입력이 4개고, 출력이 3개니까, 4변수 카르노맵을 3개 그리면 된다

# 좀 더 효율적인 회로 만들기


💡

이번 챕터는 아주 똑같은 회로를 만드는 아주 다양한 방법이 있을 수 있다.

비효율적인 (논리 게이트가 많이 들어가는) 컴퓨터를 만들더라도, 괜찮다

물론 저는 카르노맵을 극한으로 써서 논리게이트를 아주 많이 줄였습니다. 이것은 저의 모범답안~



## 1) output1 카르노맵

![image.png](/images/6_COUNTING_SIGNALS/image_1.png)

![image.png](/images/6_COUNTING_SIGNALS/image_2.png)


💡

이 모양은, A xor B xor C xor D 이다.



![image.png](/images/6_COUNTING_SIGNALS/image_3.png)

## 2) Output2 카르노맵


💡

꿀팁은, output1,2,3 에서 서로 겹치는 부분이 많도록 “잘” 카르노맵을 묶으면 논리게이트를 재활용할 수 있어서 게이트 절약으로 조금 더 간단한 회로를 만들 수 있다는 점. 사실 걍 해도된다



![image.png](/images/6_COUNTING_SIGNALS/image_4.png)

![image.png](/images/6_COUNTING_SIGNALS/image_5.png)

![image.png](/images/6_COUNTING_SIGNALS/image_6.png)

```
빨간색 + 초록색은
[AB]CD + AB[CD] 이므로, AB xor CD 임
```

![image.png](/images/6_COUNTING_SIGNALS/image_7.png)

```
파란색은
[A]B + A[B] 이므로 A xor B 이다. [C]D 로 묶임
핑크색은
[A]B + A[B] 이므로 A xor B 이고, C[D] 로 묶임

[C]D C[D] 도 서로 xor 이므로,

(A xor B)[C]D + (A xor B)C[D]
= (A xor B)(C xor D)
```

즉, 파란색은 (A xor B) and (C xor D)

빨간색은 AB xor CD

![image.png](/images/6_COUNTING_SIGNALS/image_8.png)

이렇게 만들면, output1 에서 썼던 xor 을 **재활용 할 수 있다.**

![image.png](/images/6_COUNTING_SIGNALS/image_9.png)

![image.png](/images/6_COUNTING_SIGNALS/image_10.png)

이제 Desired output 4 하나만 붙이면 되시겠다

## 3) Output3 카르노맵

![image.png](/images/6_COUNTING_SIGNALS/image_11.png)

![image.png](/images/6_COUNTING_SIGNALS/image_12.png)

![image.png](/images/6_COUNTING_SIGNALS/image_13.png)

걍 A and B and C and D, 즉 ABCD 다.

output2 에서 썼던 AND 를 재활용 할 수 있다.

![image.png](/images/6_COUNTING_SIGNALS/image_14.png)

# 비하인드

열심히 종이에 써서 했다는거… 여러분도 한번 해보세요

![Untitled](/images/6_COUNTING_SIGNALS/Untitled.png)