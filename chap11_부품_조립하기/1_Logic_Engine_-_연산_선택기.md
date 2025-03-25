# Logic Engine - 연산 선택기

# Logic Engine


💡

그 동안

or, nand, and 같은 논리게이트를 사용했다.

다른 논리게이트를 사용하려면, 선을 끊은다음 다른 논리게이트를 연결해야했다.

어떤 논리게이트를 사용할지 “코드” 로 선택할 수 있게 만들 수 없을까?



or, nand, and 를 선택해서 연산해주는 계산기를 만들면 된다.

각 연산자에 대응되는 코드가 있다. (or=00, nand=01, and=11)

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled.png)

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_1.png)

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_2.png)

사용할 수 있는 8bit logic 부품이 or 과 not 만 있으니, 모든 논리연산을 or 과 not 으로 변환해야한다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_3.png)

우선 or 는 or 부품이 있으니까 그냥 쓰면 된다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_4.png)

# nand 구현

nand 를 구현하려면, nand 소자가 없으므로, 논리식을 부울대수로 정리해서 변환해보자.

OR 을 두고 NAND 로 바꾸려면,

(AB)’ = A’+B’

**[AB]=[A]+[B]**
(이 표기법은 steam solution 의 표기법이다.)

즉, not 끼리 or 를 하면 nand 출력을 만들 수 있다.

Tick 탭을 이용하여 테스트해보면 nand 출력이 제대로 나오는걸 확인할 수 있다.

(nand 는 입력이 1,1 일때만 0 출력)

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_5.png)

# and 구현

and 는

AB = [[A]+[B]]

즉 아래와 같이 구성하면 된다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_6.png)

nor 는 

[A+B]

00 일때만 1 이 나오면 된다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_7.png)

이제 각 연산을 선택할 수 있게 선택기 입력을 구현하면 된다.

4개의 회로를 각각 구현해도 되지만, 잘 보면 겹치는 부분이 많다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_8.png)

# Input Selector(Mux)

전에 만들었던 “멀티플렉서” 를 활용할 때가 왔다.

(INPUT SELECTOR 스테이지에서 얻은 부품이다)

[INPUT SELECTOR(MUX)](INPUT%20SELECTOR(MUX)%201bc80ae0869c81408a6cd30831cf76c6.md) 

선택기(MUX) 를 앞에 달면 **선택**에 따라 **입력**을 전환할 수 있다.

![image.png](/images/1_Logic_Engine_-_연산_선택기/image.png)

예를 들어, ON OFF 를 붙여서 테스트해보면,

MUX 의 선택 입력이 1 이면 아랫쪽 입력을 출력으로 내보낸다.

선택 입력이 0 이면 위쪽 입력을 출력으로 내보낸다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_9.png)

OFF 를 달거나, 아무것도 안달면 선택입력에 0 이 들어가면서 윗쪽 입력을 출력으로 연결한다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_10.png)

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_11.png)

## or 와 mux 연결

일단 OR 는 선택입력이 00 일때이므로, 기본적으로 mux 선택이 모두 0 인 회로에 연결한다.

아무것도 안 입력하면 이 흐름을 따라가서 or 이 연산될 것이다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_12.png)

## nand 와 mux 연결

**[AB]=[A]+[B]**

선택입력이 01 일때 nand 연산을 수행하면 된다.

not 입력을 달고 mux 신호가 1일때만 수행하도록 연결한다.

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_13.png)

## nor 와 mux 연결

선택입력이 10 일때는 nor 연산되도록 한다.

[A+B]

![Untitled](/images/1_Logic_Engine_-_연산_선택기/Untitled_14.png)

## and 와 mux 연결

and 는

AB = [[A]+[B]]