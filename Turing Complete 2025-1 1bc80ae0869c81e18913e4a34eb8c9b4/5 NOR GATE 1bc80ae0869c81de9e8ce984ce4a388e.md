# 5. NOR GATE

NOR 게이트를 만들어보자.

![image.png](5%20NOR%20GATE%201bc80ae0869c81de9e8ce984ce4a388e/image.png)

Nor 도 Nand 와 마찬가지로, Nor 만으로 나머지 게이트들을 몽땅 만들 수 있다


💡

Nor, Nand 게이트는 나머지 다른 논리게이트를 모두 만들어낼 수 있어서, “범용 논리게이트(Universal Gate) 라고 불린다. 

</aside>

OR 게이트는 Not 게이트를 NAND 의 input 으로 집어넣어서 만들 수 있다.

진리표를 그려보면, 

### NAND

| input 1 | input 2 | output |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

우리는 이런 회로를 만들어야 된다

### NOR

| input 1 | input 2 | output |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

# nand 의 output

| nand 의 output |
| --- |
| 1 |
| 1 |
| 1 |
| 0 |

output 의 모양을 만들려면, 우선, 

- 모든 input output 을 위아래로 뒤집는다

| output (위아래 뒤집힘) |
| --- |
| 0 |
| 1 |
| 1 |
| 1 |
- 각각을 부정한다

| output (부정됨) |
| --- |
| 1 |
| 0 |
| 0 |
| 0 |

라는걸 알 수 있다.

# 위아래 뒤집기

진리표의 위아래를 뒤집으려면 A 와 B 에 Not 을 달아주면 된다.

![image.png](5%20NOR%20GATE%201bc80ae0869c81de9e8ce984ce4a388e/image%201.png)

# 각각을 부정하기

모든 값을 반대로 청개구리처럼 말하게 하면 된다.

![image.png](5%20NOR%20GATE%201bc80ae0869c81de9e8ce984ce4a388e/image%202.png)

# 성공

![image.png](5%20NOR%20GATE%201bc80ae0869c81de9e8ce984ce4a388e/image%203.png)