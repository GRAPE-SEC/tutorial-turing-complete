# CALCULATIONS - 사칙연산 계산기

내가 만든 Arithmetic Engine 과 Registers 를 서로 연동하는 레벨이다.

(실제로 내가 만든 Registers 회로가 자동으로 불러와진다…)

여기서 만든 회로가 불러와진다.

[Registers (mov 를 구현)](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e.md) 

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled.png)

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_1.png)

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_2.png)

그리고, REG 1, REG2 를 ALU 의 input 으로 하고, 결과를 REG3 에 저장해야한다.

### 레지스터 번호

위에서 부터 순서대로 Reg0, Reg1, Reg2, Reg3, Reg4, Reg5 이다.

Reg1 와 Reg2 의 값을 더한 값을 Reg3 에 저장하도록 바꾸는 것이 목표이다


💡

이 스테이지에서는 게임에서 직접 Register 에 값을 수정한다.

Input 을 Register 에 저장하는 명령을 구현하는 것을 IMMEDIATE VALUE 에서 다룬다. (바로 다음 스테이지)



![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image.png)


💡

실제 컴퓨터에서 return value 를 register esi, edi, eax 레지스터에 저장하는 것을 구현하는 것이다.



# Step1) Registers

아래에서 만든게 그대로 불러와진다.

[Registers (mov 를 구현)](Registers%20(mov%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB)%201bc80ae0869c8147a9b7ebd8c331e39e.md) 

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_1.png)

## Step2) COPY 핀으로 Registers 토글할 수 있게 하기

Registers 는 COPY 와 관련된 회로이므로,

COPY instruction 이 아니면 명령이 수행되지 않아야 한다.

따라서 Decoder 의 Disable 핀을 끄도록 연결한다.

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_3.png)

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_4.png)

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_5.png)

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_2.png)

## Step3) ALU 장착

이제 여기에 ALU 를 조립한다.

ALU 는 CUSTOM 폴더에 들어있다.

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_6.png)

INPUTS 의 Instruction 이 ALU 의 Instruction 으로 입력되어야하고,

ALU 의 Output 은 OUTPUTS 로 출력되어야한다

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_3.png)

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_4.png)

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_5.png)

그리고 OPCODE 가 CALCULATION 일때만 출력으로 연산결과가 출력되어야한다

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_6.png)

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_7.png)

그리고 Instuction 이 CALCULATION 일때만 동작해야하므로, 

CALCULATION 이 on 일때만 출력에 연결한다.

- Switch 를 이용하면 된다.


💡

CALCULATION 이외의 다른 동작을 할 때도, ALU 는 계산을 하고 있다. 다만, 다른 동작(IMMEDIATE, COPY, CONDITION) 을 수행할 때는 계산결과가 저장되지 않는다



![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_7.png)

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_8.png)

## 참고) Register Plus

CALCULATIONS 레벨에 등장하는 Register 는 하나의 핀이 더 추가되어있는 특수한 Register 이다.(스테이지 시작할 때 말해준다)


💡

레지스터가 저장하고 있는 전기신호(맴도는 갇힌 전기) 를 내보내는 핀이 추가되어있다

(아니 이럴거면 Register 만들때 그냥 만들게 시키지…)



![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_9.png)

기존의 8 Bit Register

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_8.png)

CACULATION 에 등장하는 8 Bit Register

- Always output 이라는 핀이 추가로 있다.

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_9.png)

기존의  Register 는  Save 핀이 on 일때 값을 저장하고, Load 핀이 on 일때만 다음 tick 에 값을 output 으로 내보낸다.

아래는 SAVING BYTES 인데, Load OFF 일때는 레벨의 OUTPUT 이 Not enable 된다.

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_10.png)

따라서 추측컨데, CALCULATIONS 레벨에 등장하는 특수한 레지스터는 아래와 같은 회로를 가지고 있을 것이다.

Load 핀과 상관없이 항상 저장된 값을 다음 tick 에 Load 하는 “Always Output” 핀을 만들 수 있다.

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_11.png)


💡

왜 처음에 Register 설계할때 이 핀을 추가해놓지 않고 나중에 뒷북을 치는건가?



TMI 인데, 실제로, 구버전의 turing complete 에는 이 회로를 custom circuit 으로 직접 만들어서 썼어야 됐었던 듯 하다. (아래 링크는 과거 어떤 유저가 올린 질문으로, 이를 뒷받침하는 증거이다)

[https://steamcommunity.com/app/1444480/discussions/0/3266806084906733653/](https://steamcommunity.com/app/1444480/discussions/0/3266806084906733653/)

그러나 turing complete 개발자들이 생각하기에 좀 힘들것같다고 생각해서 특수한 register 를 준 것 같다. **(좀 짜친다)**

## Step4) ALU 연산을 저장할 Register 연결하기

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_10.png)

- ALU 의 출력

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_11.png)

실제로 이런 레지스터를 rax 또는 eax 라고 부른다. (ALU 의 a 와 같은 a, accumalator 의 약자이다)

# Step5) ALU 에 계산할 Register 두개 연결하기

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_12.png)

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_13.png)

# 전체 정답

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_14.png)

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_12.png)

좀 더 예쁘게 만드려면 이렇게 만들어도 된다

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_15.png)

# 버스(bus)

컴퓨터의 주요 부품들을 서로 연결해주는 와이어들을 버스(Bus)라고 부른다.

이 버스를 타고 데이터와 제어신호(OPCODE) 가 오고 간다.

참고로, 저 혼자만 특이하게 OR 로 연결되어 산술연산장치(Accumulator Logic Unit, ALU) 의 결과를 저장하는 레지스터를 현대 컴퓨터에서안 EAX (Enhanced Accumulator Register) 라고 부른다. 

EAX 의 A 는 Accumulator 이다.

이 스테이지를 깨고 나면, 기존의 8 bit Register 에 Always Output 핀이 추가된 RegistePlus 부품을 얻는다.

![Untitled](/images/2_CALCULATIONS_-_사칙연산_계산기/Untitled_13.png)

컴공과나 전전과에 오면 자주 보게 되는 이런 그림이 있는데, **우리가 방금 직접 손으로 만들었다.**

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_16.png)

![image.png](/images/2_CALCULATIONS_-_사칙연산_계산기/image_17.png)

# EAX 와 C언어

실제로 C언어 코드를 컴파일한 후, 바이너리 에디터로 뜯어보거나 디스어셈블하면

```c
int main() {
    return 0;
}
```

이 코드가

```c
main:
    xor     eax, eax ;
    ret      
```

로 컴파일됨을 알 수 있다.

return 0 는 연산의 최종 결과가 0 라는 의미이다.

따라서 이 0 이라는 값은 **eax 레지스터를 통해 다른 곳으로 전달된다.**