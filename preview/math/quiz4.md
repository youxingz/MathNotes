Quiz 4

1. Calculate Truth Table:（20）

  | $p$ | $q$ | $p\lor q$ | $p\land q$ | $\sim p$ | $\sim p \lor q$ | $\sim p \lor (q \land p)$ | $\sim p\to q$ | $p\to (p\lor q)$|
  |-----|-----|-----------|-----------|----|---|---|--|--|
  | F   |  F  |F |F|F |F | T | F | T
  | F   |  T  |T |F|F |T | T | T | T
  | T   |  F  |T |F|T |F | F | T | T
  | T   |  T  |T |T|T |F | T | T | T
  
2. Calculate Truth Table:（30）
     
  | $p$ | $q$ | $r$ | $p\lor q \lor r$ | $p\land q\land r$ | $\sim (p\land r)$ | $\sim p \lor q\land r$ | $~(p\lor r)\to p$|
  |-----|-----|-----|-----------|-------|---|--|--|
  |T|T|T| T | T |F|T|T
  |T|T|F| T | F |T|F|T
  |T|F|T| T | F |F|F|T
  |T|F|F| T | F |T|F|T
  |F|T|T| T | F |T|T|T
  |F|T|F| T | F |T|T|F
  |F|F|T| T | F |T|T|T
  |F|F|F| F | F |T|T|F
  
3. 将“对于任意的$x$属于集合$X$，存在$y$属于$X$，使得$y$小于等于$x$，则称$y$为$X$中的最小元”翻译为符号语言：（5）
   $\forall x\in X, \exists y\in X, s.t. y\leq x$, we say that $y$ is the minimal value of $X$.
4. 将“$\forall a\in A, \exists b \in \Z, s.t. a=2b$，我们称集合$A$为偶数集”，翻译为自然语言。（其中$s.t.$为“使得”，$\Z$为整数集）（5）
   对于任意的$a$属于$A$，存在$b$属于$A$，使得$a=2b$，我们称...
5. 请用自然语言构造一个悖论 $A$：（5）
   
6. 请用自然语言构造一个含有两个命题的悖论 $A, B$：（5）

7. 请问$(a\to b \land c)\land (c\to a)$ 与 $(a\land b\land c)\lor(\sim a\land\sim c)$ 是等价的吗？请用真值表解释原因。（10）

8. 化简：（20）
   1. $(a \land b)\land(a \lor b)$  => $a\land b$
   2. $(a \land b)\land \sim(a \lor b)$ => $False$
   3. $\sim(a \land b)\land \sim(a \lor b)$ => $\sim a\land \sim b$
   4. $(a \to b)\land \sim(a \lor b)$ => $\sim a\land \sim b$
   5. $(a \to b)\land \sim(\sim a \to \sim b)$ => $\sim a\land b$
   6. $\sim(\sim b \lor\sim a)\to a$ => $True$

