# 클럭2 - ODD TICKS

입력이 0 만 있어서, 사실상 입력은 쓸모가 없다는걸 알 수 있다.

![Untitled](/images/3_클럭2_-_ODD_TICKS/Untitled.png)

### 순환하는 delay line

다음 두개의 성질을 이용하면 신기한걸 만들어 낼 수 있다.

- 0 입력에 not 을 달면 1 출력을 만들 수 있다
- delay line 은 1을 받으면 한 클락 동안 충전해놨다가 한 클락 뒤에 방전한다.

not 으로 반전되는 출력을 입력으로 입력하는 구조를 만들면, 자기가 자기를 활성화시키는 delay line 회로를 만들 수 있다.

즉, 스스로 충전되고 방전되게 함으로써 한 클락마다 깜빡깜빡 거리는(1과 0을 번갈아 출력하는) 일종의 시계를 만들 수 있다.


💡

스페이스바를 누르면 Not 부품을 회전시킬 수 있습니당



![Untitled](/images/3_클럭2_-_ODD_TICKS/Untitled_1.png)

![Untitled](/images/3_클럭2_-_ODD_TICKS/Untitled_2.png)

![Untitled](/images/3_클럭2_-_ODD_TICKS/Untitled_3.png)

# 클럭(Clock)

이 회로는 **무한히 깜빡인다.**

이것은 마치, **심장박동**과 같다.

![image.png](/images/3_클럭2_-_ODD_TICKS/image.png)