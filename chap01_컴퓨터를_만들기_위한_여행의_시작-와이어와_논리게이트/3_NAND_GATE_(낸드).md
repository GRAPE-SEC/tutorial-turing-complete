# 2. NAND GATE (낸드)

다음 스테이지는 NAND GATE 입니다

NAND 는 논리회로 또는 논리 게이트(Logic Gate) 라는 특수한 부품입니다.

어려운 말이 나와버렸는데, 사실 어려운 말은 아니고요

전기가 흐르는 것과 안흐르는 것을 1 과 0 으로 구분했을때, 

1 이나 0 을 입력하면 조건에 따라서 1 이 나오거나 0 이 나오거나가 결정되어있는 부품을 논리 게이트라고 부릅니다.

논리게이트로 들어가는 와이어를 **입력(input)**, 나가는 와이어를 **출력(output)** 이라고 부릅니다.

NAND 게이트는 Input 을 두개 입력받아서, 둘 다 1 일때만 0을 출력하는 논리 게이트입니다.

AND 는 “둘 다” 뭐 이런 뜻인데, NAND 는 Not AND 라는 뜻입니다.


💡

나는 햄버거와 피자 둘다 좋아한다 (I love Burger and I love Pizza)



표로 그려보면 이런거죠


💡

그림을 그려준 안아름(4기) 님께 감사를 드립니다. 2024-09-10



![NAND 회로표.jpg](/images/2_NAND_GATE_(낸드)/nand_circuit.jpg)

아니 근데 왜 AND 안배웠는데 NAND 배우냐는 생각이 들 수 있는데,

NAND 를 조합해서 AND 를 만들 수 있지만, AND 로는 NAND 를 못만듭니다. 네 상위호환이라는것이죠.

우주의 신비입니다.

사실, Not 과 AND 를 합친게 NAND 여서 그렇습니다.

강한 부정은 강한 긍정이라는 말이 있죠

![image.png](/images/2_NAND_GATE_(낸드)/image.png)

Not 을 두번하면 Not 없는것도 표현할 수 있지만, Not 이 없는걸로는 Not 을 만들어낼 수 없다는것이죠

나중에 AND 가 나오니까 몰라도 됩니다

![image.png](/images/2_NAND_GATE_(낸드)/image_1.png)

왼쪽에 있는 버튼을 클릭해서 Input 의 전기를 바꿀수 있습니다

초록색은 전기흐름(1) 이고, 빨간색은 전기안흐름(0) 입니다

초록색일 때는 와이어에 전기가 슝슝 지나가는걸 볼 수 있습니다.

그 결과는 시뮬레이션에 표시되는데, 잘 보면 Input 두개가 둘다 1 일때만  Output 이 0 이 되는것을 확인할 수 있습니다. 나머진 다 Output 이 1 이고요

![image.png](/images/2_NAND_GATE_(낸드)/image_2.png)

그 답을 쓰면 이 스테이지는 통과입니다

![image.png](/images/2_NAND_GATE_(낸드)/image_3.png)

## 실제 세상의 논리 게이트

물리현상을 이용하면 논리 게이트를 만들 수 있는 경우가 많습니다

도미노로도 만들 수 있다고 하는군요 (고전역학)

[https://www.youtube.com/watch?v=w6E7aQnA4Ws](https://www.youtube.com/watch?v=w6E7aQnA4Ws)

물로도 만들 수 있습니다.

입력 두개에 물이 흐르면 밖으로 물이 안흐르고, 하나라도 물이 안흐르면 물이 빠져나가는 물 NAND 게이트를 만들 수 있습니다

[https://www.youtube.com/watch?v=IxXaizglscw](https://www.youtube.com/watch?v=IxXaizglscw)

## 계전기( 또는 릴레이, Relay)


💡

**참고**
[https://www.relaiscomputer.nl/index.php/elements](https://www.relaiscomputer.nl/index.php/elements)



어 근데 물이나 도미노로는 전기를 input 과 output 으로 사용할 수 없습니다. 

아주 옛날의 최초의 컴퓨터들은 **계전기** 라고 불리는 부품을 사용했다고 전해집니다

계전기가 뭐냐면 이렇게 생긴 작은 부품입니다. 손가락이랑 같이 찍힌 사진을 구하는것이 힘들었죠

![image.png](/images/2_NAND_GATE_(낸드)/image_4.png)

안에 뜯어보면 이렇게 생겼는데요

![image.png](/images/2_NAND_GATE_(낸드)/image_5.png)

![image.png](/images/2_NAND_GATE_(낸드)/image_6.png)

중학교 과학시간에 배운 전자석입니다.

복잡하게 생겼지만 걍 기능은 단순합니다.

전자석은 전기가 흐르면 자석이 되어서 쇠를 당기고, 전기가 안흐르면 쇠를 안당기는 걍 쇠가 됩니다.

![image.png](/images/2_NAND_GATE_(낸드)/image_7.png)

잘 보면 Coil, 즉 구리선으로 빙빙 두른 쇳덩어리가 안에 들어가 있는걸 볼 수있죠 

![image.png](/images/2_NAND_GATE_(낸드)/image_8.png)

계전기는 전자석으로 쇠를 당기고 끊는 일종의 “전기로 작동하는 전기 스위치” 입니다.

뭔말이냐면,

스위치는 인간이 손가락으로 눌러서 전기를 켜고 끊을 수 있습니다

삑~

![image.png](/images/2_NAND_GATE_(낸드)/image_9.png)

계전기는 이 손가락을 전기로 조종할 수 있게 바꾼것입니다.

전자석의 전기를 껐다 켜서 쇠를 움직이는것이지요

![image.png](/images/2_NAND_GATE_(낸드)/image_10.png)

그림으로 표현하면 이건데요

![image.png](/images/2_NAND_GATE_(낸드)/image_11.png)

가운데가 딸깍 딸깍 움직일 수 있게 되어있어서 전자석이 쇠를 당기면 전기가 연결되고, 전자석이 자석이 아니면 다시 스프링으로 되돌아가면서 전기가 끊어집니다 

![image.png](/images/2_NAND_GATE_(낸드)/image_12.png)

저 그림에서 작대기에는 모두 실제로 전기를 연결해야합니다

![image.png](/images/2_NAND_GATE_(낸드)/image_13.png)

PCB 에 연결하면 이렇게 생겼죠

![image.png](/images/2_NAND_GATE_(낸드)/image_14.png)

이 릴레이를 아래와 같이 연결하면 전기로 작동하는 NAND 논리 게이트를 만들 수 있다는 사실을 아주 옛날 사람들이 알아냈습니다.

![image.png](/images/2_NAND_GATE_(낸드)/image_15.png)

## 발전

요즘 컴퓨터는 계전기를 안쓰고 **반도체**를 씁니다. 중간에 잠깐 진공관을 썼었던 적도 있었는데 옛날얘기고요

릴레이는 이런 성질을 가지고 있습니다.

- 전기가 들어가고 나가는 Input Ouput 이 있음
- 그걸 컨트롤하는 3번째 전기 입력이 있음(계전기에서는 전자석)

어 근데 전자석으로 만드니까, 이런 문제가 있었습니다.

- 시간이 갈 수록 자석이 약해짐
- 딸깍거리는 쇠붙이 (전기를 켜고 끄는) 애가 오래되면 부셔짐

그래서 사람들이 (과학자들이) 이런 생각을 했습니다.


💡

어 아니 걍 전기를 껐다 켰다 할 수 있는 무언가로 대체하면 되는거 아니냐?



이것 저것 테스트해보다가 결국 찾아냈고요 제일 싸고 제일 만들기 쉽고 그런걸 계속 찾아서 현재는 

**금속 산화막 반도체 전계효과 트랜지스터** (MOSFET) 라는걸 쓰고요 몰라도 됩니다. 그냥


💡

아 그냥 짱좋은 전자석이구나



그런겁니다

계전기랑 똑같이 작동하지만, 양자역학으로 전기를 껐다 끄는거죠(우리는 몰라도 됩니다 하이닉스랑 삼성이 만들어줄거니까)

그림으로는 이렇게 그리는데요

![image.png](/images/2_NAND_GATE_(낸드)/image_16.png)

이렇게 생겼습니다 실제로는

![image.png](/images/2_NAND_GATE_(낸드)/image_17.png)

어려워 보이지만 걍

- 베이스 = 전자석 역할, 전기 켜고 끔
- 컬렉터 = 전기 들어가는거. input
- 이미터 = 전기 나가는거. output

![image.png](/images/2_NAND_GATE_(낸드)/image_18.png)

걍 계전기랑 똑같다는걸 알수있습니다. 

이건 사실 컴퓨터를 만들기 위한 부품이였습니다. 동작은 걍 전자석이랑 똑같고요.

이걸 중학교 과학쌤이 알려줬다면 중학교 과학시간에 더 재밌게 배울 수 있을텐데 아쉽군요

# CPU

컴퓨터에 들어가는 칩을 CPU 라고 부르는데, 2024년에 나오는 최신 CPU 에는 논리게이트가 수십억개 들어있습니다.

![image.png](/images/2_NAND_GATE_(낸드)/image_19.png)

우리가 만들 컴퓨터에도 논리게이트가 한 100개 이상은 들어갈 예정입니다.

![image.png](/images/2_NAND_GATE_(낸드)/image_20.png)

최신 컴퓨터랑은 쨉도 안되긴 하는군요

하지만 속도만 빨라졌을 뿐 원리는 논리 게이트 100개짜리 컴퓨터건 수십억개 컴퓨터건 똑같습니다.

# 스테이지 깨면 부품을 얻는다

앞으로 한 스테이지를 깰 때마다 그 스테이지에서 만든 부품을 가져와서 쓸 수 있게 됩니다.

만든걸 또 만들면 귀찮으니까 게임에서 기능으로 제공하는 것이지요

![image.png](/images/2_NAND_GATE_(낸드)/image_21.png)

계속…