# LITTLE BOX - 롬(ROM)

[https://www.reddit.com/r/TuringComplete/comments/18oetwh/little_box_solution/](https://www.reddit.com/r/TuringComplete/comments/18oetwh/little_box_solution/)

이 스테이지에서는 “메모리 주소” 라는 개념이 나온다.

메모리는 이전에 만들었던 “Save 또는 Load 가 입력되어, Save 모드일대 입력된 값을 저장하고, Load 모드일때 저장된 값을 내보내는 부품” 이다.

메모리에 번호를 붙여서 어떤 메모리에 저장할지 지정하고, 저장하면 해당 메모리에 데이터를 저장한다(Latch로 전기를 맴돌게 만드는 것이다)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled.png)

아래 부품은 Output 인데,

두개의 핀 중 하나는 데이터핀이고 하나는 Output Enable 핀이다.

- Output Enable 에 0 이 입력되면 데이터핀으로 입력된 데이터를 저장한다.
- Output Enable 이 1 이 입력되면 데이터핀으로 저장된 데이터를 내보낸다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%201.png)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%202.png)

## step1 : 하나의 메모리에 대해 구현해보기

우선 하나의 메모리에 대해 잘 작동하도록 만들어본다.

- Save/Load input 을 각각 8bit Register 의 Save Load 핀에 연결한다.
- Value 입력을 8bit Register 의 Value 핀에 연결한다.

주소 입력 (A OR B 와 0 OR 1) 은 연결되어있지 않으므로, 여러개의 Register 중 하나를 선택할 수는 없다. 하나의 Register 에 대해서만 정상작동한다.

이때, Register 가 Load 일때, 문제에서 주어진 Output 부품에서 해당 데이터를 다시 문제에서 주어진 Input 으로 거꾸로 보내야한다. 따라서 load 입력을 Output 부품에도 연결한다(핑크색)

즉, 아래와 같이 연결한다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%203.png)

실행시켜보면,

Tick 0 에서

- 245 라는 데이터가 입력으로 들어온다.
- Register 의 Value 로 데이터가 입력된다.
- Save 핀이 Enable 되어, Register 에 245 가 저장
    - 저장된 것은 “다음 Tick 에 Load 입력이 1이라면 Register 에서 출력될 것이다.”

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%204.png)

다음 Tick 인 Tick 1 으로 이동하면

Load 핀이 활성화되어(핑크색)

- Register 가 Load 모드가 되어 데이터(245)를 내보낸다.
- Output 소자에서 저장되었던 데이터(245)가 출력된다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%205.png)

## 여러개의 메모리에 대해 구현해보기

step1 을 실행해보면, tick 10 전까지는 잘 작동하는데 tick10 에서 오류가 난다는 것을 관찰할 수 있다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%206.png)

왜 tick 10 전까지는 잘 작동하는걸까 관찰해보면,

Save 와 Load 하는 메모리가 동일하다는 특징이 있다.

예를 들어, tick4 에서는 메모리 A1 에 Save 하고 tick5에서 A1 을 읽는다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%207.png)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%208.png)

그러나 tick10 에서는 tick9 에서 B1 에 저장한 것을 tick10 에서 load 하므로 메모리 하나로는 만족시킬수없다.

## 메모리 주소로 메모리를 선택할 수 있게 만들기

주소 선택 입력의 입력에 따른 메모리 선택의 모든 경우의수는 다음과 같다.

00 : A0

01 : A1

10 : B0

11 : BB

nor 게이트, and 게이트, not 게이트를 활용해서 각각의 경우 출력을 내보내는 회로를 만든다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%209.png)

그리고 각 레지스터의 Value 에 데이터를 연결한다.

- 데이터 입력은 선택하지 않아도 된다. 왜냐하면 어차피 Save 나 Load 모드를 안켜면 데이터가 레지스터에 안저장되니까, Save, Load 로 레지스터를 구분하면 된다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2010.png)

그러고 나면, Save 인지 Load 인지에 따라 각 레지스터가 선택되어 작동하도록 연결한다.

예를 들어, 메모리주소 01 을 선택하면 두번째 줄의 AND 게이트가 활성화 되고 레지스터가 선택된다. 그리고나면 Save 인지 Load 인지에 따라 선택된 레지스터의 동작이 달라진다.

- 레지스터의 Load 핀(첫번째 입력핀)은 레지스터 선택 게이트에 연결하면 된다. 다른 레지스터의 Load 핀은 활성화되지 않는다.
- 레지스터의 Save 핀 의 경우, AND 게이트로 Save 입력과 레지스터 선택 게이트를 묶어야한다.
    - 그렇지 않으면 Save 입력이 1 이 입력되면 모든 레지스터에 동일한 값이 저장될 것이기 때문이다.
    - 구글에서 찾은 자료에서는 and 가 아니라 switch 를 썼다. 근데 and와 switch 는 논리적으로는 똑같다. (이사람은 switch가 크기가 더 작아서 쓴 것 같다.)
        - [https://www.reddit.com/r/TuringComplete/comments/18oetwh/little_box_solution/](https://www.reddit.com/r/TuringComplete/comments/18oetwh/little_box_solution/)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2011.png)

# 최종 정답

논리적으로는 쉬운데, 칸이 좁아서(…그래서 little box 인거같다.) 조정에 노가다가 필요했다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2012.png)

## 사실 이 소자는….

이건 사실 컴퓨터의 메모리인 RAM 의 미니 버전이다.

8 bit Register 를 4개 이어 붙였으므로, 1 byte x 4 = 4 byte

즉, 4 byte RAM 이다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2013.png)

## 현실의 RAM

Windows 를 사용하고 있다면, Ctrl Alt Del → 작업관리자 → 성능 에 들어가서, 현재 메모리(RAM) 상태를 확인할 수 있다.

![image.png](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/image.png)

메모리 크기가 16GB(기가바이트) 이므로,

이 컴퓨터에는, 이 **“LITTLE BOX” (4 byte)** 가 **17179869184 개** 장착되어있다. (1024  x 1024 x 1024)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2012.png)

2024년 기준으로 현실의 컴퓨터에는 16 GB(기가바이트) 정도의 RAM 이 장착된다.

(쿠팡에 판다)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2014.png)

노트북 뒷판을 열면 RAM 이 장착되어있는 것을 확인할 수 있다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2015.png)

16 GB 는 졸라 큰건데, 16 GB = 10000000000 byte 이다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2016.png)

실제 RAM을 현미경으로 보면,

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2017.png)

아래와 같이 생겼다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2018.png)

Turing Complete 로 표현해보면 대충 이런 느낌이지 않을까…

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2019.png)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2020.png)

 2023년 9월 12일에 출시된 아이폰15 에는 6GB 의 RAM 이 장착되어있다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2021.png)

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2022.png)

하이닉스나 삼성전자 같은 회사의 메모리 사업부에서는 이 RAM 을 만들어서 먹고산다.

![Untitled](LITTLE%20BOX%20-%20%E1%84%85%E1%85%A9%E1%86%B7(ROM)%201bc80ae0869c81b597d6f7f7b052f842/Untitled%2023.png)