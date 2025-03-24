# Instruction Decoder - 명령어 해석기

Arithmetic Engine, Registers 는 각각 Instruction 들을 가지고 있다.

이것을 선택할 수 있는 명령어 해석기(Instruction Decoder) 를 선택할 수 있도록 만든다.

즉, “전체 Instruction” 를 입력하면 Arithmetic Engine 과 Register 등의 명령어로 제어되는 부품을 선택하여 하위 명령어로 분류해주는 장치가 있어야 한다.

![Untitled](Instruction%20Decoder%20-%20%E1%84%86%E1%85%A7%E1%86%BC%E1%84%85%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%A5%20%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%A8%E1%84%80%E1%85%B5%201bc80ae0869c8109b3affd4d629bbc23/Untitled.png)

위에서 언급한 “전체 Instruction” 의 문법은 아래와 같이 주어진다.

![Untitled](Instruction%20Decoder%20-%20%E1%84%86%E1%85%A7%E1%86%BC%E1%84%85%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%A5%20%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%A8%E1%84%80%E1%85%B5%201bc80ae0869c8109b3affd4d629bbc23/Untitled%201.png)

## 전체 정답

![Untitled](Instruction%20Decoder%20-%20%E1%84%86%E1%85%A7%E1%86%BC%E1%84%85%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%A5%20%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%A8%E1%84%80%E1%85%B5%201bc80ae0869c8109b3affd4d629bbc23/Untitled%202.png)

예를 들어, Instruction 에 Copy 에 해당하는 명령이 입력되면,

![Untitled](Instruction%20Decoder%20-%20%E1%84%86%E1%85%A7%E1%86%BC%E1%84%85%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%A5%20%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%A8%E1%84%80%E1%85%B5%201bc80ae0869c8109b3affd4d629bbc23/Untitled%203.png)

Copy 가 켜진다.

![Untitled](Instruction%20Decoder%20-%20%E1%84%86%E1%85%A7%E1%86%BC%E1%84%85%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%A5%20%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%A8%E1%84%80%E1%85%B5%201bc80ae0869c8109b3affd4d629bbc23/Untitled%204.png)