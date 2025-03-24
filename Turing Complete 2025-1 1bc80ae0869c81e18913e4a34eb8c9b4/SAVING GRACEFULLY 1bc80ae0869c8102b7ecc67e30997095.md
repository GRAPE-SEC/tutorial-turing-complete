# SAVING GRACEFULLY

## 문제 조건

Delay Line 소자는 1 tick (한 클럭)만 신호를 저장할 수 있다.

근데 어떻게 잘 만들면 **1 tick 보다 긴 시간동안 신호를 저장하게** 만들 수 있다고 한다.

그렇다. **래치(Latch)**를 만들어야한다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled.png)

만들려는 소자의 이름은 “1 bit Memory” 로, 흔히 컴퓨터 메모리라고 불리는 소자를 직접 만들어본다.

첫번째 입력 : Save : 이게 켜져있으면 값이 업데이트된다.

두번째 입력 : Save Value : 저장할 값.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%201.png)

## 동작 방식

메모리의 동작방식을 한마디로 정리하면,

“SAVE 가 enable 되어있을때만 Value 가 저장되고, 저장된 Value 는 다음 tick 에서 출력된다” 이다.

다음 그림에서,

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%202.png)

잘 보면, Save 가 켜져있을때는 Value 의 값이 그대로 다음 tick 에 출력된다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%203.png)

그러나 Save 가 꺼지면,Value 에 어떤 값이 들어오건 다음 tick 에 영향을 주지 못한다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%204.png)

다시 Save 가 켜지면, Value 값이 다음 tick 에 출력된다.

이때 주의할 점은,

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%205.png)

Value 에 1 이 저장된 상태에서 Save 가 꺼지면 “그대로 기억하고 있는 값”이 SAVE가 다시 켜질때까지 tick 에 계속 출력된다는 것이다. 

Save 에 1 이 입력되는 것은 마치 저장버튼을 누르는 것과 같다.

- 저장버튼을 계속 누르면 계속 저장이 되고, 저장버튼을 안누르면, 저장버튼을 마지막으로 눌렀을때의 값을 기억하고 있다.
- 저장버튼을 안누르면 어떤 값을 입력하던지 결과에 적용되지는 않는다.

다시 저장버튼을 누르면 다음 tick 부터 결과에 적용된다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%206.png)

# 래치 만들기

## step1 : 데이터 저장

한번 데이터가 입력되면 그 입력을 계속 머금고 있는 래치를 만든다.

이러면 1이 입력되었을 때, 그 이후 tick 에서 출력으로 1을 유지하는 회로를 만들 수 있다.

방법은 출력을 OR 게이트로 입력시켜서 이후 입력이 0으로 변해도 여전히 1을 입력되도록 만들면 된다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%207.png)

## step2 : Save off 로 래치를 끌 수 있게 만들기

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%208.png)

그러나 Save 가 꺼진 상태에서, Value 가 1 이면 원래 업데이트가 안되어야하는데 업데이트가 된다.

즉, Save:0 Value:1 일때 입력되지 않도록 해야한다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%209.png)

delay line 은 바로 전 tick 의 입력을 받는다. 래치에 저장된 신호가 없음에도 다음 tick 에 1이 출력되는 것은 Save 가 0 임에도 불구하고 래치의 입력에 1 이 들어오기 때문이다.

따라서 이걸 차단하면 된다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%2010.png)

## Step3 : Save 0 일때 Value 업데이트 막기

Save:1 Value:1 일때만 래치에 입력되도록 막으면 된다.

and 게이트를 달면 된다.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%2011.png)

그러면 성공.

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%2012.png)

# Unlock : 1 Bit Memory

이 스테이지를 완료하면 1 Bit Memory 가 해제됨

![Untitled](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/Untitled%2013.png)

![image.png](SAVING%20GRACEFULLY%201bc80ae0869c8102b7ecc67e30997095/image.png)