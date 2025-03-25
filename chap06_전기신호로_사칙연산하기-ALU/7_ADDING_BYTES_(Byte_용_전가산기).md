# ADDING BYTES (Byte 용 전가산기)

# Byte 전가산기

우리가 만든 Full Adder(전가산기)는 이진수(bit) 를 더할 수 있었다.

이걸 Byte 용으로 개조한다.

![Untitled](/images/7_ADDING_BYTES_(Byte_용_전가산기)/ADDING_BYTES_(Byte_용_전가산기)%201bc80ae0869c81069809e7f35a7c51f1/Untitled.png)

입출력을 관찰해보면 

- 입력은 위에서 순서대로 Carry in, Byte1, Byte2 임을 알 수 있다.
- 출력은 위에서 순서대로 Number, Carry 임을 알 수 있다.

우선 Byte 입력들을 Byte Splitter 로 쪼갠 후, 쪼개진 각 bit 를 adder 에 연결한 후,

전 adder 의 carry 를 adder 의 input 으로 연결하면 여러 자릿수를 가진 수를 더할 수 있을 것 같다.

![Untitled](/images/7_ADDING_BYTES_(Byte_용_전가산기)/ADDING_BYTES_(Byte_용_전가산기)%201bc80ae0869c81069809e7f35a7c51f1/Untitled%201.png)