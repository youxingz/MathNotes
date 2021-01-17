# 数学分析【定义定理整理】

## [Metric Space](https://www.amazon.com/Principles-Mathematical-Analysis-International-Mathematics/dp/007054235X "数学分析 Rudin 版第三版")

### Def. [赋距空间 Metric Space] (2.15)
  A set $X$, whose elements we shall call `points`, is said to be a `metric space` if with any two points $p$ and $q$ of $X$ there is associated a real number $d(p, q)$, called the distance from $p$ to $q$, such that:
  
  a) 【非负性】 $d(p, q) > 0$ if  $p\neq q$; $d(p,q)=0$;
  
  b) 【对称性】 $d(p,q)=d(q,p)$;
  
  c) 【三角不等式】 $d(p,q)\leq d(p,r)+d(r,q)$, for any $r\in X$.
  
  Any function with these three properties is called a `distance function`, or a `metric`.
  
### Def. [凸性 Convex] (2.17)
  If $\boldsymbol{x}\in \mathbb{R}^k$ and $r>0$, the open (or closed) ball $B$ with center at $\boldsymbol{x}$ and radius $r$ is defined to be the set of all $\boldsymbol{y}\in \mathbb{R}^k$ such that $|\boldsymbol{y}-\boldsymbol{x}< r|$ (or $|\boldsymbol{x}-\boldsymbol{y}< r|$) (remark: $d(\boldsymbol{x},\boldsymbol{y})< r$).

  We call a set $E \subset \mathbb{R}^k$ convex if
$$
\lambda\boldsymbol{x} + (1-\lambda)\boldsymbol{y} \in E
$$
  whenever $\boldsymbol{x} \in E, \boldsymbol{y}\in E$, and $0<\lambda<1$.
  
  #### Example: Balls are convex
  For any points $\boldsymbol{z},\boldsymbol{y}\in B_r(\boldsymbol{x})$, we hava
$$
\begin{aligned}
& |\lambda \boldsymbol{y} + (1-\lambda) \boldsymbol{z} - \boldsymbol{x}| \\
&= |\lambda \boldsymbol{y} + (1-\lambda) \boldsymbol{z} -(1 - (1 - \lambda))\boldsymbol{x}|\\
&\leq \lambda |\boldsymbol{y} - \boldsymbol{x}| + (1-\lambda)|\boldsymbol{z}-\boldsymbol{x}| \\
&< \lambda r + (1-\lambda)r \\
&= r \end{aligned}
$$
  
  (Remark: The same proof applies to `closed ball` by `k-cells`)
  
### Def. [重要概念 Some Important Concepts] (2.18)
Let $X$ be a `metric space`. All `points` and `sets` mentioned below are understood to be elements and subsets of $X$.

(a) 【邻域】 A `neighborhood` of $p$ is a set $N_r(p)$ consisting of all $q$ such that $d(p,1)< r$, for some $r>0$. The number $r$ is called the `radius` of $N_r(p)$.

(b) 【极限点】 A `point` $p$ is a `limit point` of the set $E$ if *every* neighborhood of $p$ contains a point $q\neq p$ such that $q\in E$

(c) 【孤立点】 If $p\in E$ and $p$ is not a limit point of $E$, then $p$ is called an `isolated point` of $E$. 

(d) 【闭集】 $E$ is `closed` if every limit point of $E$ is a point of $E$.

(e) 【内点】 A point $p$ is an `interior point` of $E$ if there is a neighborhood $N$ of $p$ such that $N\subset E$

(f) 【开集】 $E$ is `open` if every point of $E$ is an interior point of $E$

(g) 【补集】 The `complement` of $E$ (denoted by $E^c$) is the set of all points $p\in X$ such that $p\notin E$.

(h) 【完全集】 $E$ is `perfect` if $E$ is closed and if every point of $E$ is a limit point of $E$.

(i) 【有界性】 $E$ is `bounded` if there is a *real number* $M$ and a point $q\in X$ such that $d(p,q)< M$ for all $p\in E$ 

(j) 【稠密性】 $E$ is `dense` in $X$ if every point of $X$ is a limit point of $E$, or a point of $E$ (or both).

(Remark: $\mathbb{R}^1$ neighborhoods are `segments（区间）`, $\mathbb{R}^2$ neighborhoods are `interiors of circles（圆面）`.)

### Theorem [邻域是开集] (2.19)
**Every neighborhood is an open set.**

**Thinking.** 任取开球内一点，利用三角不等式，证明以这一点为心的开球在大开球内。

**Proof.** Consider a neighborhood $E=N_r(p)$, and let $q$ be any point of $E$. Then there is a postive real number $h$ such that
$$
d(p,q)= r-h
$$
For all points $s$ such that $d(q,s)< h$, we have then
$$
\begin{aligned}
d(p,s)
&\leq d(p,q)+d(q,s) \\
&< r-h+h \\
&=r
\end{aligned}
$$
so that $s\in E$. Thus $q$ is an interior point of $E$.

### Theorem [极限点的集的内点含有无限个点] (2.20)

**If $p$ is a `limit point` of a set $E$, then every `neighborhood` of $p$ contains infinitely many points of $E$.**

**Thinking.** （反证法）任取集合内一点的邻域，假设邻域只包含有限个点，则邻域内的更小的邻域会有 $r>0$ 的尽头，无法让 $r\rightarrow 0$。

**Proof.** Suppose there is a neighborhood $N$ of $p$ which contains only a finite number of points of $E$. Let $q_1, q_2, ... , q_n $ be those points of $N\cap E$, which are distinct from $p$, and put
$$
r=\min_{1\leq m \leq n}d(p, q_m)
$$

The minimum of a **finite** set of positive numbers is clearly positive, so that $r>0$.
The neighborhood $N_r(p)$ contains **no** point $q$ of $E$ such that $q\neq p$, so that $p$ is not a limit point of $E$. This contradiction establishes the theorem.

### Corollary (2.20)
**A *finite* point set has no limit points.**

**Thinking.** 总能找到一个更小的 $r$ 使得 $N_r(p)$ 不包含 $E$ 内任何极限点。

### Theorem [德摩根定律 de Morgan's Law] (2.22)

Let $\{E_\alpha\}$ be a (finite or infinite) collection of sets $E_\alpha$. Then
$$
(\bigcup_{\alpha}E_\alpha)^c = \bigcap_\alpha (E_\alpha^c)
$$

**Thinking.** 用基本的选择方法进行证明，任取左边集合内一点，证明属于右边；任取右边集合内一点，证明属于左边。

**Proof.** Let $A$ and $B$ be the left and right members of such equation. If $x\in A$, then $x\notin \bigcup_{\alpha} E_\alpha$, hence $x \notin E_\alpha$ for any $\alpha$, hence $x\in E_\alpha^c$ for every $\alpha$, so that $x\in \bigcap_{\alpha} E_\alpha^c$. Thus $A\subset B$.

Conversely, if $x\in B$, then $x\in E_\alpha^c$ for every $\alpha$, hence $x\notin E_\alpha$ for any $\alpha$, hence $x\notin \bigcup_\alpha E_\alpha$, so that $x\in (\bigcup_\alpha E_\alpha)^c$. Thus $B\subset A$.

It follows that $A=B$.

### Theorem [开集的补集是闭集] (2.23)

**A set $E$ is `open` if and only if its `complement` is `closed`.**

**Thinking.**

必要性：假设集合的补集是闭集，任选集合内一点，根据开闭集的定义证明 “这一点所生成的邻域”（证明了这是内点）不在该集合的补集中，则必在该集合中，则该集合为开集。

充分性：另一方面假设集合是开集，任选一个集合的补集的极限点，证明这个极限点不在集合中，则这个点必在补集中，所以极限点都在补集中，补集闭。

**Proof.**

First, suppose $E^c$ is closed. Choose $x\in E$. Then $x\notin E^c$, and $x$ is not a limit point of $E^c$ (Because $E^c$ is closed). Hence there exists a neighborhood $N(x)$ of $X$ such that $E^c \cap N(x)$ is empty, that is, $N(x)\subset E$. Thus $x$ is an interior point of $E$, and $E$ is open.

（简述：Suppose $E^c$ is closed, we will show that every point in $E$ is interior point. Choose $x\in E$, then $x\notin E^c$, that means $x$ is not limit point of $E^c$. Thus $[N(x)\subsetneq E^c]\Rightarrow [N(x) \subset E] \Rightarrow$ $[x$ is interior point of $E\ ]$ $\Rightarrow$ $[E$ is open$]$.）

Next, suppose $E$ is open. Let $x$ be a limit point of $E^c$. Then every neighborhood of $x$ contains a point of $E^c$, so that $x$ is not an interior point of $E$. Since $E$ is open, this means that $x\in E^c$.

（简述：Suppose $E$ is open, we will show that every point in $E^c$ is limit point of $E^c$. Choose $x\in (E^c)^\prime$, then $[N(x) \subset (E^c)^\prime] \Rightarrow [N(x) \subsetneq E]$, then $x$ is not an interior point of $E$. But $E$ is open, so $[x\notin E]\Rightarrow [x\in E^c]$, so $[\ $every limit point is in $E^c]\Rightarrow [E^c$ is closed$\ ]$.）

It follows that $E^c$ is closed.

### Corollary (2.23)

**A set $E$ is `closed` if and only if its `complement` is `open`.**

**Thinking.** 思路同上 【 *Theorem [开集的补集是闭集] (2.23)* 】


### Theorem [有限交并原则] (2.24)

有限开的交为开，有限闭的并为闭；无限开的并为开，无限闭的交为闭

(a) For any collection $\{G_\alpha\}$ of `open sets`, $\bigcup_\alpha G_\alpha$ is `open`.

(b) For any collection $F_\alpha$ of closed sets, $\bigcap_\alpha F_\alpha$ is closed.

(c) For any finite collection $G_1, G_2, ... , G_n$ of open sets, $\bigcap_{i=1}^n G_i$ is open.

(d) For any finite collection $F_1, F_2, ..., F_n$ of closed sets, $\bigcup_{i=1}^n F_i$ is closed.

**Thinking.** 根据【Theorem 2.22, 2.23】很容易证明 (a), (b)。针对 (c), (d)，因为指标有限，所以可以对邻域半径取得 `min(...)` 函数的有效值，从而得出最小邻域存在的结论，即开。（注意：若指标无限，则开集的无限交可能为一个点，闭集的无限并也可能为一个点）。

**Proof.** (c) Let $H = \bigcap_{i=1}^n G_i$. For any $x\in H$, there exist neighborhoods $N_i$ of $x$ with radii $r_i$, such that $N_i \subset G_i (i = 1, ..., n)$. Put
$$
r=min(r_1, r_2, ..., r_n)
$$
then $N_r(x)\subset G_i$ for $i = 1,2,...,n$, so that $[N_r(x)\subset H] \Rightarrow [H$ is open $]$.

(d) By taking complements, (d) follows from (c):
$$
(\bigcup_{i=1}^n F_i)^c = \bigcap_{i=1}^n (F_i^c)
$$

#### Example [开的无限交可以为一个点]

$\mathbb{R}^1$ case, let $G_n$ be segment $(-\frac{1}{n}, \frac{1}{n})$, $n=1,2,3,...$. then $G_n$ is open in $\mathbb{R}^1$.
Put $G=\bigcap_{n=1}^\infty G_n$, then $G$ consists of a single point (at $x = 0$) and it is not open in $\mathbb{R}^1$


### Def. [闭包] (2.26)

If $X$ is a metric space, if $E \in X$, and if $E^\prime$ denotes the set of all limit points of $E$ in $X$, then the `closure` of $E$ is the set $\bar{E} = E\cup E^\prime$.

### Theorem [闭包特点] (2.27)

If $X$ is a metric space and $E\subset X$, then

(a) 【闭性】$\bar{E}$ is closed,

(b) 【闭集的闭包是自身】$E = \bar{E}$ if and only if $E$ is closed,

(c) 【包含性】$\bar{E} \subset F$ for every closed set $F\subset X$ such that $E\subset F$.

By (a) and (c), $\bar{E}$ is the smallest closed subset of $X$ that contains $E$.

**Thinking.**

(a) 集合 $\bar{E}$ 外任取一点，既不是 $E$ 的极限点也不是 $E$ 的孤立点，则该点的邻域在 $\bar{E}^c$ 中，即 $\bar{E}^c$ 集合开，则 $\bar{E}$ 闭。

(b) 根据闭集和闭包的定义走。

(c) 利用闭集的定义（所有点都是极限点则闭）得出推导关系 $E$ 的极限点也必然在闭集 $F$ 中。

**Proof.** 

(a) Choose $p\in X$ and $p\notin \bar{E}$ (then $p \in \bar{E}^c$) then $p$ is neither a point of $E$ nor a limit point of $E$. Hence $[N(p)\subsetneq \bar{E}] \Rightarrow [N(p)\subset \bar{E}^c]$, then $\bar{E}^c$ is open, so the complement of $\bar{E}^c$ (which is $\bar{E}$) is closed.

(b) "$\Rightarrow$": if $E=\bar{E}$, (a) implies this.

"$\Leftarrow$": If $E$ is closed, then $E^\prime \subset E$, hence $\bar{E} = E$ (By Def. 2.26, $\bar{E} = E \cup E^\prime = E$)

(c) If $F$ is closed and $F \supset E$, then $F\supset F^\prime$, so we have $F^\prime = F \supset E^\prime$, thus $F\supset \bar{E}$. （$E$ 的极限点也必然在闭集 $F$ 中）

### Theorem [ $\mathbb{R}^1$ 中集合的上确界] (2.28)
**Let $E$ be a `nonempty set` of *real numbers* which is bounded above. Let $y=supE$. Then $y\in\bar{E}$. Hence $y\in E$ if $E$ is closed.**

**Thinking.** 这是在说集合的上确界要么在集合内，要么在集合外，但都必在其闭包内。分这两种情况讨论一下即可。

**Proof.** If $y\in E$ then $y\in \bar{E}$, prove done. Else if $y\notin E$, for every $h>0$ there exists a point $x\in E$ such that $y-h< x< y$, for otherwise $y-h$ would be an upper bound of $E$. Thus $N_{>h}(y)\ni x$, that means $y$ is a limit point of $E$. Hence $y\in \bar{E}$.

### Remark [开闭的相对性] (2.29)

一个集合是开/闭的，是相对其对应的父集合而言，相对不同的父集合可能是开也可能是闭也可能是半开半闭。（讨论 $E\subset Y \subset X$，则可能存在 $E$ is open relative to $Y$ but closed relative to $X$）

### Theorem [降临定理] (2.30)

**Suppose $Y\subset X$. A subset $E$ of $Y$ is `open relative to` $Y$ if and only if $E=Y\cap G$ for some open subset $G$ of $X$.**

描述简述：$E \subset_{open}  Y\subset X$ $\Longleftrightarrow$ $E=Y\cap G,\ G\subset_{open} X$

**Thinking.** 

充分性：构造这一的开集 $G$ 满足题意即可。

必要性：还是根据充分性的构造，如下图所示。

**Proof.**

"$\Rightarrow$": Suppose $E$ is open relative to $Y$, We will show that $E \subset G\cap Y$ and $G\cap Y \subset E$.

Choose $p\in E,\ q\in Y$, there is a postive number $r_p$ such that $d(p,q)< r_p$. Let $V_p = \{q\ |\ d(p,q)< r_p, q\in X\}$, and define
$$
G=\bigcup_{p\in E}V_p
$$
Then $G$ is an open subset of $X$ (By Theorem 2.19 and 2.24).

Since $p\in V_p$ for all $p\in E$, so that $E\subset G\cap Y$.

Also, we have $V_p \cap Y \subset E$ for all $p\in E$, so that $G\cap Y\subset E$. Thus $E=G\cap Y$.

"$\Leftarrow$": If $G$ is open in $X$ and $E=G\cap Y$, then every $p\in E$ has neighborhood $V_p\subset G$. Then $V_p \cap Y\subset E$, so that $E$ is open relative to $Y$.

![我的天哪，我终于画了一个图](https://imgkr2.cn-bj.ufileos.com/3fb3e4db-eb84-4b35-94c1-f6044b4d9af3.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=Oi6YctmcC%252BcwTGw2A0tjUjSD06A%253D&Expires=1608659824)


【小亦 2020-12-22 01:58】于深圳

