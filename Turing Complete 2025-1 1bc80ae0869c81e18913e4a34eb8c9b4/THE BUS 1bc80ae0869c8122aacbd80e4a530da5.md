# THE BUS

Bit Switch 와 동일하게, 어떤 조건(세모모양)으로 어떤 입력을 출력과 연결할지 선택하는 회로를 만들면 된다.

참고:  [Bit Switch (트랜지스터)](Bit%20Switch%20(%E1%84%90%E1%85%B3%E1%84%85%E1%85%A2%E1%86%AB%E1%84%8C%E1%85%B5%E1%84%89%E1%85%B3%E1%84%90%E1%85%A5)%201bc80ae0869c81279a8ceade56e321a1.md) 

조건입력을 두개로 나눠서 하나에만 NOT 을 붙여서 byte switch 에 연결한다.

각 byte switch 는 사이에 병렬로 연결한다. (어차피 두개의 입력이 동시에 활성화 되는 경우의 수는 없다)

![Untitled](THE%20BUS%201bc80ae0869c8122aacbd80e4a530da5/Untitled.png)

# 정류작용

사실, 논리적으로는 SWC 를 AND 게이트로 바꿔도 상관없다.

하지만, 가운데 연결통로로 전기가 거꾸로 흘러서 문제가 생긴다.

![image.png](THE%20BUS%201bc80ae0869c8122aacbd80e4a530da5/image.png)