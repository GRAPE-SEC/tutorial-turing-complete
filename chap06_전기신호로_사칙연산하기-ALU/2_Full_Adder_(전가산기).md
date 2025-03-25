# Full Adder (전가산기)


👺

덧셈을 수행하는 회로, 즉 전가산기



![image.png](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/image.png)

# 여러자리 이진수 덧셈

우리가 숫자 두개를 더할 때, 이렇게 한다.

```
17 더하기 25 는,

 17
 25
---
 42

우리가 가진 숫자는 0,1,2,3,4,5,6,7,8,9 이고,
7 과 5 를 더하면,표현할 수 있는 숫자가 없다. (16진수였으면, C 여야 한다.)

그러니까 다음 자리에 1 을 올리고,
초과한 숫자인 2 가 남는다.

**이제 그 다음 자리를 계산할때는,
1 과 2 를 더하되, 바로 이전 자리의 CARRY 가 있으면, 1 을 더한다.**
```

# 전가산기(Full Adder)

전가산기는**, 여러자리의 이진수 덧셈을 할 수 있는 회로**이다.

우리가 십진수를 더할 때, 일의 자릿수를 제외한 높은 자릿수는 바로 이전에 값이 **10을 초과했는지(자리올림) 을 고려해야한다**

즉, 이진수 덧셈을 할때도 똑같다. 

- 숫자를 더한다. 이때, 이전 Carry 가 있으면 같이 더한다.

를 하려면 Carry 가 필요하다.

**즉, 반가산기를 일렬로 연결하고, 이전 자리의 반가산기의 Carry 출력을 다음 자릿수의 반가산기의 입력에 연결하면 된다.**

# 회로

마찬가지로 다출력 회로인데, 이제 **입력이 세개로 늘어났다.**

- 추가된 입력은 이전 자릿수의 Carry 이다.

![image.png](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/image%201.png)

# 직관으로 설계하기

- SUM 은 홀수의 개수를 세면 된다. Odd Number of Signal 에서 했듯, A xor B xor C 이다.
- CARRY 는 AND 한걸 다 OR 하면 된다.

# 카르노맵 쓰기

3개의 입력, 2개의 출력이므로, 3변수 카르노맵이 2개 필요하다.

### 1) SUM

![image.png](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/image%202.png)

```
[A][B]C + ABC = [A^B]C
[A]BC + A[B]C = (A^B)C

[A^B]C + (A^B)C = (A^B)^C = A^B^C
```

![image.png](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/image%203.png)

### 2) CARRY

![image.png](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/image%204.png)

![Untitled](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/Untitled.png)

![image.png](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/image%205.png)

이제 컴퓨터로 덧셈을 할 수 있게 되었다.

![image.png](/images/2_Full_Adder_(전가산기)/Full_Adder_(전가산기)%201bc80ae0869c8173b4b1ecd55fcf0c29/image%206.png)