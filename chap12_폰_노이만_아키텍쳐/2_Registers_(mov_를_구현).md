# Registers (mov 를 구현)

요구사항을 읽어보면,

레지스터끼리 복사 붙여넣기가 가능하도록 만드는 것이 목표이다.


👺

컴퓨터에서, 레지스터끼리 저장된 데이터를 복사하는 것을 이동시키다(move)를 따서 mov 라고 함



![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled.png)

- 여러개의 메모리 사이에서 복사 붙여넣기를 하려면, 어떤 메모리에서 어떤 메모리로 옮길지 지정해야한다.
- 데이터를 이미 저장하고 있는 원본 메모리를 source, 데이터를 복사할 메모리를 destination 이라고 부른다.
- source 와 destination 을 instruction byte 로 지정할 수 있어야 한다.
    - instruction byte 의 Bit 1,2,3 은 destination 을 지정한다.
    - instruction byte 의 Bit 4,5,6 은 source 을 지정한다.
    
    메모리의 위치는 아래와 같다.
    
    ![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%201.png)
    

그리고 추가적으로, 메모리끼리 데이터를 복사 붙여넣기 하는거 말고도, 메모리 외부에서 데이터가 들어왔을때 메모리의 특정 위치에 복사하거나, 메모리의 특정 위치의 데이터를 외부로 내보낼 수 있어야한다. 

- input 과 output 으로 데이터를 복사 붙여넣기 하면 된다.
- input 과 output 에 대한 instruction 도 약속되어있다. (사실 바꿔도 된다. 다만 여기서는 레벨에서 주어진걸 쓰자.)

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%202.png)

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%203.png)

## 데이터 옮기기 예시

예를 들어, 입력이 아래와 같이 주어지면,

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%204.png)

순서대로 1,2,3,4,5,6,7,8 비트이다.

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%205.png)

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%206.png)

이걸 위에 주어진 조건에 따라 해석하면,

Source, Destination, Value 로 구분해서 읽을 수 있다.

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%207.png)

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%208.png)

### step1)  instruction decoder 구현

우선, 어디에서 어디로 옮길지 (input, output, register 중에)

를 의미하는 instruction byte 를 핀으로 나누기 위해 byte splitter 와 decoder 를 연결한다.

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image.png)

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%201.png)

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%209.png)

### step2)  각 register 에 지정된 핀 연결

source 또는 destination 을 instruction 핀을 이용해 지정하므로, 이것을 각 register 의 번호에 맞게 연결한다. 위에서 부터 REG0 REG1 REG2 REG3 REG4 REG5 이다.

- 위쪽 Decoder 는 Source 이므로, 각 Register 의 Load 핀에 연결된다.
    - Register 가 Load 모드가 되면 output 핀으로 저장되어있던 데이터가 다음 tick 에 내보내기 된다.
    
    ![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%202.png)
    
    ![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%203.png)
    
    ## 잡담 : 소켓
    
    이 선을 쭉쭉 연결하는건 반복작업이라 매우 열받는다.
    
    이걸 쉽게 하기위해 소켓(Socket) 이라는게 개발되었다. 딸깍 끼기만 하면 금속끼리 연결된다
    
    ![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%204.png)
    

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%2010.png)

### step3) Register 의 input value 와 output 을 레벨의 input 과 output 과 연결

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%205.png)

![Untitled](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/Untitled%2011.png)

### step3) Instruction Code 의 INPUT 과 OUTPUT 을 decoder 에 연결

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%206.png)

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%207.png)

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%208.png)

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%209.png)

## 최종 정답

![image.png](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e/image%2010.png)