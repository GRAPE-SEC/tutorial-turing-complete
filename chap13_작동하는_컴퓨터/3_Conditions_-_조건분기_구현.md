# Conditions - 조건분기 구현


👺

컴퓨터라고 불리려면, 논리회로가 if else 같이 특정 조건을 검사하고 어떤 코드를 실행하고 어떤 코드를 실행하지 않을지 판단하는 기능을 가지고 있어야 한다.



Conditions 는 “조건” 이라는 뜻이다.

컴퓨터가 “만약~ 라면” 라는 동작을 처리할 수 있게 해준다.

C언어나 Python 의 if 문이나 for문을 내부적으로 처리할 때 쓰인다.

![Untitled](/images/3_Conditions_-_조건분기_구현/Untitled.png)

회로에는 두개의 Input 이 있다.

- Input2 는 Byte 숫자가 입력된다.
- Input1 은 아래의 3 Bit 짜리 Code 중 하나인데,
    - 000 이면 Input2 의 숫자와 상관없이 항상 Output 으로 1 을 출력한다.
    - 001 이면 Input2 의 숫자가 0 과 같으면 Output 으로 1을 출력한다. 다르면 0을 출력한다.
    - 010 이면 Input2 의 숫자가 0 보다 작으면 Output 으로 1을 출력한다. 크거나 같으면 0을 출력한다.
    - 011 이면 Input2 의 숫자가 0 보다 작거나 같으면 Output으로 1을 출력한다. 크면 0을 출력한다
    - 100 이면 Input2 의 숫자와 상관없이 항상 Output 으로 0을 출력한다.
    - 101 이면 Input2 의 숫가 0 이 아니면 Output 으로 1을 출력한다. 0 이면 0을 출력한다.
    - 110 이면 Input2 의 숫자가 0 보다 크거나 같으면 Output 으로 1을 출력한다. 작으면 0을 출력한다.
    - 111 이면 Input2 의 숫자가 0보다 크면 Output 으로 1을 출력한다. 작거나 같으면 0을 출력한다.

![Untitled](/images/3_Conditions_-_조건분기_구현/Untitled_1.png)


💡

위에 있는 Level Log 버튼을 누르면 다시 볼 수 있다.



![image.png](/images/3_Conditions_-_조건분기_구현/image.png)

![Untitled](/images/3_Conditions_-_조건분기_구현/Untitled_2.png)

# 개어려운거 아님?

사실 복잡해보이지만, 그렇지 않다

이거 만족시키는 회로 만들고,

![image.png](/images/3_Conditions_-_조건분기_구현/image_1.png)

이거 만족시키는 회로 그 위에다가 만들고,

![image.png](/images/3_Conditions_-_조건분기_구현/image_2.png)

이거 만족시키는 회로 만들고

![image.png](/images/3_Conditions_-_조건분기_구현/image_3.png)

쭉… 해서, 마지막까지 그 위에다가 만들면 된다

![image.png](/images/3_Conditions_-_조건분기_구현/image_4.png)

**즉, 모든 행을 삼행시마냥 각각 만들고 합치면 된다.**

(즉, 다출력 카르노맵을 사용하면 되겠다)

![image.png](/images/3_Conditions_-_조건분기_구현/image_5.png)

# byte splitter 달기

우선 입력이 byte로 들어오니까, 이걸 쪼개서 bit 로 만들어주기 위해 byte splitter 를 단다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_6.png)

# 0 인지 판별하기

어떤 Byte 가 0 인지 판단하는 것은 쉽다.

그냥 다 더해서 0이여야만 0 이다. 하나라도 1이 있으면, 0 이 아니다.

즉, 전부 다 더해서(OR) 0 이면 0 이다.

0 인지 판단하는 Bit Code 는 아래 두개이다.

- Bit Code : 001
- Bit Code : 101

![image.png](/images/3_Conditions_-_조건분기_구현/image_7.png)

그니까 이렇게 다 OR 로 연결한다음 저놈을 이제 **isZero** 라는 하나의 bit 로 생각하자.

![image.png](/images/3_Conditions_-_조건분기_구현/image_8.png)

![image.png](/images/3_Conditions_-_조건분기_구현/image_9.png)

Input 을 클릭해서 값을 바꿔보면 테스트해볼 수 있는데, 1 이 하나라도 있어서 0 이 아니면 **isZero bit** 가 켜진다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_10.png)

근데 모든 숫자중에, 0 은 한개인데 0이 아닌 숫자는 아주 많다. 그래서, isZero 를 한번 뒤집어서 is not Zero(0 아님?) 으로 하는게 회로가 더 간단해진다. (삽질이지만, 궁금하면 직접 해봐도 좋다. 일단 난 해봄)

![image.png](/images/3_Conditions_-_조건분기_구현/image_11.png)

OR 에 not 을 붙인건 NOR 니까, NOR로 바꿔서 논리게이트를 하나 아낄 수 있다. 다 돈이니까…

![image.png](/images/3_Conditions_-_조건분기_구현/image_12.png)

# 음수 양수 판별하기


💡

**복습 : 음수, 양수, 2의 보수(2’s complement)**

앞에서, 컴퓨터는 음수를 표현할 때 이렇게 한다고 했다.

1. 부호가 있는거 (signed) 로 읽을지, 부호가 없는거 (unsigned) 로 읽을지 정한다.
    - 부호가 없다고 하면 항상 양수임. 음수는 못표현 한다.
2. **부호가 있을때(signed) 제일 큰 자릿수를 나머지 자릿수 다 더한거에서 뺀 값으로 정한다.**

이 방법은 2의 보수법(2’s complement) 라고 부르고, 거의 모든 컴퓨터는 음수를 이렇게 계산함 ㅇㅇ

이진수는, **나머지 자릿수를 다 더한 것도 맨 끝자리 하나보다 작다**

뭔 소리냐면, 1111 은 네자리 수중에 제일 크고, 10000 은 다섯자리 수중에 제일 작다.

 **그런데 1111 에 딱 1을 더하면 10000 이 된다.**

1111 = 8+4+2+1 = 15, 10000 = 16

즉, 2의 보수법에서, 어떤 수가 음수인지 볼려면 **제일 큰 비트가 1 인지 보면 된다**. 그러면 무조건 음수다.

예를 들어, 10110 은 **계산해볼 필요 없이 음수**이다. 그냥 맨 앞에 있는 비트가 마이너스 기호라고 생각해도 무방한 것 이다.

그래서 맨 왼쪽에 있는 비트를 **짱중요비트(MSB, Most Significant Bit)** 라고 함. (*진짜임)



### signed unsigned 바꾸기

암튼 어떤 숫자를 부호가 있는(signed) 로 볼수도있고, 부호가 없는(unsigned) 로 볼 수도 있다.

Turing Complete 에서는 +255 라고 된 버튼을 누르면 모드가 바뀐다.

- -1 이라고 써있으면 signed 모드이다.
- +255 라고 써있으면 unsigned 모드이다.

클릭해서 -1  로 바꿔준다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_13.png)

![image.png](/images/3_Conditions_-_조건분기_구현/image_14.png)

Input 에 있는 알맹이들을 클릭하면, 숫자를 바꿀 수 있는데,

잘 보면 제일 큰 비트(MSB) 가 1 (초록색) 이면 무조건 음수다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_15.png)

즉, 어떤 수가 0보다 작은지 큰지는 그냥 **맨 왼쪽 비트(MSB)** 만 보면 된다는거다

그니까 맨 왼쪽 bit 인 128번 bit 와 연결된 라인만 쏙 빼서 이제 얘를 **isNeg(음수임?)** 이라는 bit 로 부르기로 한다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_16.png)

순서가 이상하니 뒤집자

Byte Splitter 를 선택한 뒤, 스페이스바를 누르면 회전한다

![image.png](/images/3_Conditions_-_조건분기_구현/image_17.png)

이렇게 하면 Tick 과 Level Log 에 있는 Bit code 와 순서를 맞출 수 있다. 거꾸로 볼라면 불편하니깐

![image.png](/images/3_Conditions_-_조건분기_구현/image_18.png)

잘 보면, 위 아래가 대칭임을 알 수 있다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_19.png)

그래서 이제 우리의 목표가 반으로 줄어들었다.

 ??? 안에 있는 회로를 만들기만 하면 된다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_20.png)

# 카르노맵

|  | Bit Code (2) | Bit Code (1) | isnot Zero | is Pos | Out |
| --- | --- | --- | --- | --- | --- |
| 항상 0 | 0 | 0 | x | x | 0 |
| A=0 | 0 | 1 | 0 | 0 | 1 |
| A<0 | 1 | 0 | 1 | 0 | 1 |
| A≤0 (음수일때) | 1 | 1 | 0 | 0 | 1 |
| A≤0 (0일때) | 1 | 1 | 1 | 0 | 1 |

![image.png](/images/3_Conditions_-_조건분기_구현/image_21.png)

왼쪽놈 만들고 오른쪽놈 만든다음 OR 로 만들어서 더해주면 된다.

순서대로 조합하면,

![image.png](/images/3_Conditions_-_조건분기_구현/image_22.png)

![image.png](/images/3_Conditions_-_조건분기_구현/image_23.png)

![image.png](/images/3_Conditions_-_조건분기_구현/image_24.png)

![image.png](/images/3_Conditions_-_조건분기_구현/image_25.png)

이제 이 두개를 더해주면 된다

![image.png](/images/3_Conditions_-_조건분기_구현/image_26.png)

그러면 성공이다.

![image.png](/images/3_Conditions_-_조건분기_구현/image_27.png)


💡

이제 컴퓨터에서 0 인지 아닌지 알고싶거나, 0 보다 큰지 아닌지 알고 싶다면, 이 회로에 넣어보면 된다.

- Bit code 에 원하는 모드를 넣고, ( 예를들어, 0 인지 아닌지 검사하고 싶다면 001 을 넣는다)
- Input 에 판별을 원하는 값을 넣으면 된다.


우리는 이미 덧셈 뺄셈을 구현했다.


💡

덧셈 : 전가산기(full-adder) 를 만들었음. 여러자릿수의 byte 를 더할 수 있음

뺄셈 : 전가산기에 2의 보수법(2’s complement)로 표현된 음수를 넣어서 더하면 됨



이 두개를 합치면 **모든 숫자의 대소 비교를 할 수 있다.**


💡

엥? 어떻게요?
어떤 숫자 A 와 B 의 대소를 비교하고 싶다면,

- A 랑 B 를 뺀다
- **0 보다 큰지 검사한다,**


이 두개를 합치면 **모든 숫자가 같은지 아닌지 검사할 수 있다.**


💡

엥? 어떻게요?
어떤 숫자 A 와 B 의 대소를 비교하고 싶다면,

- A 랑 B 를 뺀다
- **0 인지 검사한다**


Python, Java, C언어에서 문자열을 비교하는 것은 사실 CPU 에서 이렇게 작동한다.


💡

문자들을 각각 ASCII 코드(문자마다 대응되는 약속된 숫자)로 바꾼다

ASCII 코드는 숫자니까 숫자끼리 비교 가능

- 숫자끼리 뺀다
- 0 인지 아닌지 검사한다

이걸 텍스트의 모든 문자에 대해 수행하고, 모두 0이 아니면 같다고 판정한다. 만일 하나라도 다르면 다르다고 판정한다.



문자열을 비교하는 코딩은 사실 기계어로 이렇게 생겼다

```bash
cmp al, bl         ; Compare the two bytes
jne .not_equal     ; If they are not equal, jump to .not_equal
test al, al        ; Check if we reached the end of the string (null terminator)
je .equal          ; If we have reached the null terminator, strings are equal
inc rdi            ; Move to the next character in string1
inc rsi            ; Move to the next character in string2
mov al, [rdi]      ; Load the next byte of string1 into AL
mov bl, [rsi]      ; Load the next byte of string2 into BL
jmp .loop          ; Repeat the loop
```

이걸 16진수로 표현하면,

```
38 C3 (cmp al, bl)
75 05
84 C0
74 03
48 FF C7
48 FF C6
8A 07
8A 1E
EB F3
```

이걸 전기신호로 바꾸면,

```
0011 1000 1100 0011 (전기 안흐름, 안흐름, 흐름, 흐름 ...
0111 0101 0000 0101
1000 0100 1100 0000
0111 0100 0000 0011
0100 1000 1111 1111 1100 0111
0100 1000 1111 1111 1100 0110
1000 1010 0000 0111
1000 1010 0001 1110
1110 1011 1111 0011
```

이 된다.

이제 슬슬 작동하는 컴퓨터에 다가가고 있다는 사실…