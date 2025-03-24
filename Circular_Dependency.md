# Circular Dependency

Circular Dependency(순환 의존성) 이란,

- 전기신호가 무한히 회로 안을 돌게 되는 것

이다.

Circular Dependency 는 **어떤 회로의 출력이 똑같은 회로의 입력으로 들어갈때** 발생한다. 

우리가 지금껏 만든 회로에서는 Circular Dependency 가 있는 상황이 없었으며, 그런 회로가 필요하지도 않았다.

그래서, 게임 상에서 Circular Dependency 를 만들면 오류가 발생한다.

이 스테이지의 요구사항은, 일부러 이 오류를 범하면 된다

아무 논리 게이트나 가져와서, 출력을 입력으로 연결하면 이 스테이지가 성공한다.

![image.png](Circular%20Dependency%201bc80ae0869c81e2bf73e243a82808a9/image.png)

![image.png](Circular%20Dependency%201bc80ae0869c81e2bf73e243a82808a9/image%201.png)