# SAVING BYTES

### Output 부품에 관한 설명

Output enable 핀이 켜져있을 때만 ,Output Value 에 채점기가 원하는 신호가 입력되어야한다.

(논리적으로는 AND 인 셈이다)

![image.png](/images/3_SAVING_BYTES/image.png)

![image.png](/images/3_SAVING_BYTES/image_1.png)

![image.png](/images/3_SAVING_BYTES/image_2.png)

## 설계

그냥 각 데이터 핀을 byte 로 분할하고 save value 핀에 연결한다.

enable 핀을 각 1bit memory 에 연결해준다.

![Untitled](/images/3_SAVING_BYTES/Untitled.png)

이 레벨을 완료하면, 8 Bit Register 부품이 언락되어 사용할 수 있게 된다.

![Untitled](/images/3_SAVING_BYTES/Untitled_1.png)

아까 만들었던대로, 

- 첫번째 핀은 Load 모드를 켜고 끈다.
- 두번째 핀은 Save 모드를 켜고 끈다.
- Load 와 Save 모드는 동시에 Enable 될 수도 있다.

![Untitled](/images/3_SAVING_BYTES/Untitled_2.png)

이것을 Sandbox 에서 테스트해보면,

- SAVE 가 Enable 되어있으므로 0 tick 에서 input value 가 바로 Register 에 저장된다.
- LOAD 가 Enable 되어있으나, 다음 tick 인 1 tick 과 관련이 있으므로, 현재 tick 에서는 아무 역할도 하지 않는다.

![Untitled](/images/3_SAVING_BYTES/Untitled_3.png)

다음 tick 인 tick 1 이 되면 저장되어있던 Value 가 output 으로 출력된다.

![Untitled](/images/3_SAVING_BYTES/Untitled_4.png)

끝