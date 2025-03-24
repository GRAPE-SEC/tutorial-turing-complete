# COUNTER - 클럭

## 문제 조건

1 tick 마다 1 씩 증가하는 회로를 만들면 된다. **즉, 시계다.**

그니까 이걸 만들면 된다.

![image.png](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/image.png)

컴퓨터에서는 시계를 **클럭(clock)** 이라고 부른다.

클럭수가 높으면 컴퓨터가 빠르게 작동한다.

단. 1 tick 을 카운트하는 것 말고도 값을 Overwrite 하는 기능도 있어야 된다고 한다.

예를 들어, 1초부터 34초까지 세는 도중에 120 으로 Overwrite 하면, 그다음 tick 은 121 부터 세게 하도록 만들어야한다. 

![image.png](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/image%201.png)


💡

타이머도 “시간 세팅” 기능으로 현재시간을 바꿀 수 있는 기능이 있다. 그 기능을 만들어야됨



즉, 회로적으로 Counter 모드와 Overwrite 모드 두가지 모드가 있고, 다른 동작을 해야한다.

- Couter 모드에서는 1 tick 이 지날때마다 Output 이 1 씩 증가한다.
- Overwrite 모드에서는 입력 Value 를 Counter 에 덮어씌운다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled.png)

## 레퍼런스

[https://turingcomplete.wiki/wiki/Level/Counter](https://turingcomplete.wiki/wiki/Level/Counter)

[https://www.youtube.com/watch?v=3BDBeXz2hs8&list=PL53_yYWrgleF7NkNaTgyNTPi5hQ75beX9&index=2](https://www.youtube.com/watch?v=3BDBeXz2hs8&list=PL53_yYWrgleF7NkNaTgyNTPi5hQ75beX9&index=2)

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%201.png)

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%202.png)

# 설계

- 숫자를 카운트한다는 것은 더하기 1 을 한다는 것이다. 따라서 Adder 가 필요하다.
- 또한, 기존 숫자를 기억했다가 거기에 1을 더해야한다. 기억을 해야하므로 Register 가 필요하다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%203.png)

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%204.png)

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%205.png)

## 항상 Save 하고 Load 하는 Register

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%206.png)

테스트해보면, 잘 작동한다. 아래 사진을 보면, 항상 기억하는 (Save 와 Load 핀의 입력이 항상 1) Register 를 만들고, Byte 값을 입력하면, 

> 를 눌러서 tick 을 증가시켜도 입력한 값(41)을 계속 유지한다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%207.png)

이제 이 “항상 기억하는 Register” 의 출력값을 1을 더한다음 다시 저장하는 회로를 만든다.

ADD 는 두개의 Byte 를 더한다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%203.png)

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%208.png)

ON 은 1bit 입력이므로 1을 더한다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%209.png)

그냥 길다란 8 bit Maker 를 써도 되긴 하다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2010.png)

암튼 이걸 “항상 기억하는 Register” 에 붙인다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2011.png)

테스트해보면 Overwrite 모드가 활성화되는 Tick 2 전까지 잘 작동한다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2012.png)

## Overwrite 구현

이제 Overwrite 모드가 활성화되면 입력 Value 를 레지스터에 저장하도록 하면 된다.

근데 레지스터의 Value 핀(세번째) 는 이미 ADD 의 출력에 연결되어있다.

선택 bit 에 따라 두가지 입력을 선택하려면 Mux 를 쓰면 된다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2013.png)

Overwrite 모드이면 입력이 1이 되어, Mux 의 Select 핀이 1이 되고,

Mux 가 Input2 인 Value 입력을 선택해서 Register 에 연결해준다. (Add 1 은 끊어진다.)

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2014.png)

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2015.png)

# 최종 정답

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2016.png)

완료하면 “Counter” 부품을 얻는다.

![Untitled](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/Untitled%2017.png)

# 클럭(Clock)

클럭은 컴퓨터에서 심장과 같은데,

순서대로 작동해야하는 신호들을 딱딱 박자를 맞춰준다. (어려운 말로, 동기화(Sync) 라고 한다)

![image.png](%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A82%20-%20ODD%20TICKS%201bc80ae0869c819e8553f117ae25315a/image.png)

# 오버클럭

일반적으로, 컴퓨터 제조사들은 컴퓨터가 안정적이고 오래 오래 오류 없이 동작하게 하기 위해서, 클럭이 CPU 성능보다 느린 속도로 작동하도록 설정 해놓는다.

그런데, 설정을 바꿔서 이 클럭의 속도를 높일 수 있는데 이걸 **오버클럭(Over-Clock)** 이라고 부른다.

![image.png](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/image%202.png)

그러면 컴퓨터가 한계를 넘어서 빨라지는데, 대신 수명이 줄어들 수 있다.

또한, CPU 가 과열되어서, 냉각장치가 추가로 필요해질 수도 있다.

*마치 원피스에 등장하는 기어세컨드 같다.

![image.png](COUNTER%20-%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A5%E1%86%A8%201bc80ae0869c8100a90ac9d08d5e1021/image%203.png)