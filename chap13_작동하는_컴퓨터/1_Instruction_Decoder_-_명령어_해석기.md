# Instruction Decoder - 명령어 해석기

Arithmetic Engine, Registers 는 각각 Instruction 들을 가지고 있다.

이것을 선택할 수 있는 명령어 해석기(Instruction Decoder) 를 선택할 수 있도록 만든다.

즉, “전체 Instruction” 를 입력하면 Arithmetic Engine 과 Register 등의 명령어로 제어되는 부품을 선택하여 하위 명령어로 분류해주는 장치가 있어야 한다.

![Untitled](/images/1_Instruction_Decoder_-_명령어_해석기/Untitled.png)

위에서 언급한 “전체 Instruction” 의 문법은 아래와 같이 주어진다.

![Untitled](/images/1_Instruction_Decoder_-_명령어_해석기/Untitled_1.png)

## 전체 정답

![Untitled](/images/1_Instruction_Decoder_-_명령어_해석기/Untitled_2.png)

예를 들어, Instruction 에 Copy 에 해당하는 명령이 입력되면,

![Untitled](/images/1_Instruction_Decoder_-_명령어_해석기/Untitled_3.png)

Copy 가 켜진다.

![Untitled](/images/1_Instruction_Decoder_-_명령어_해석기/Untitled_4.png)