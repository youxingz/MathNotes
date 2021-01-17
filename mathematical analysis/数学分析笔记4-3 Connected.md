## Continuity&Connectedness

### Theorem [连通函数的映射集也连通] (4.22)

$$
X\supset E_{(connetced)}\overset{f}{\to} f(E)_{connected}\subset Y
$$
If $f$ is a `continuous` mapping of a metric space $X$ into a metric space $Y$, and if $E$ is a `connected` subset of $X$, the $f(E)$ is `connected`.

**Proof.** （证明逆否命题）Assume, on the contrary, that $f(E) = A\cup B$, where $A$ and $B$ are nonempty separated subsets of $Y$. Put $G=E\cap f^{-1}(A)$, $H=E\cap f^{-1}(B)$, we need show that $G\cap \bar H$ and $\bar G\cap H$ are empty (not connected).

Then $E = G\cup H$, and neither $G$ or $H$ is empty.

Since $A\subset \bar A$ (the closure of $A$), we have $G\subset f^{-1}(A)$; the latter set is closed, since $f$ is continuous; hence $\bar G \subset f^{-1}(\bar A)$. It follows that $f(\bar G)\subset \bar A$. Since $f(H) = B$ and $\bar A \cap B$ is empty, we conclude that $\bar G \cap H$ is empty.

The same argument shows that $G\cap \bar H$ is empty. Thus $G$ and $H$ are separated. This is impossible if $E$ is connected.

### Theorem [连续实函数的介值性] (4.23)
Let $f$ be a continuous real function on the interval $[a,b]$. If $f(a)\lt f(b)$ and if $c$ is a number such that $f(a)\lt c\lt f(b)$, then there exists a point $x\in (a,b)$ such that $f(x)=c$.

**Note.** Same case for $f(a)\gt f(b)$.

**Proof.** By 【Theorem 2.47 实轴下的连通集的序的特点】, $[a,b]$ is connected; hence By 【Theorem 4.22 连通函数的映射集也连通】 shows that $f([a,b])$ is a connected subset of $\mathbb R^1$, and the assertion follows if we appeal once more to 【Theorem 2.47 实轴下的连通集的序的特点】.

### Remark (4.24)

At first glance, it might seem that 【Theorem 4.23 连续实函数的介值性】 has a converse. That is, one might think that if for any two points $x_1\lt x_2$ and for any number $c$ between $f(x_1)$ and $f(x_2)$ there is a point $x$ in $(x_1,x_2)$ such that $f(x)=c$, then $f$ must be continuous.

That this is not so may be concluede (see 【Example 4.27.d】 later).

## Discontinuities

If $x$ is a point in the domain of definition of the function $f$ at which $f$ is not continuous, we say that $f$ is `discontinuous` at $x$, or that $f$ has a `discontinuity` at $x$.

If $f$ is defined on an interval or on a segment, it is customary to divide discontinuities into two types. Before giving this classification, we have to define the `right-hand limit` and the `left-hand limit` of $f$ at $x$, which we denote by $f(x+)$ and $f(x-)$, respectively.

### Def. [左右极限] (4.25)
Let $f$ be defined on $(a,b)$. Consider any point $x$ such that $a\leq x\lt b$. We write
$$
f(x+) = q
$$
if $f(t_n)\to q$ as $n\to\infty$, for all sequences $\{t_n\}$ in $(x,b)$ such that $t_n\to x$.

To obtain the definition of $f(x-)$, for $a\lt x\leq b$, we restrict ourselves to sequences $\{t_n\}$ in $(a,x)$.

It is clear that any point $x\in (a,b)$, $\lim_{t\to x}f(t)$ exists if and only if
$$
f(x+) = f(x-) = \lim_{t\to x}f(t)
$$

（极限存在 $\Longleftrightarrow$ 左右极限都存在且等于极限值）

### Def. [两类间断点] (4.26)
Let $f$ be defined on $(a,b)$. If $f$ is discontinuous at a point $x$, and if $f(x+)$ and $f(x-)$ exist, then $f$ is said to have a `discontinuity` of the `first kind`, or a `simple discontinuity`, at $x$. Otherwise the discontinuity is said to be of the `second kind`.

（第一类间断点）There are two ways in which a function can have a simple discontinuity:
either $f(x+)\neq f(x-)$ [in which case the value $f(x)$ is immaterial], or $f(x+)=f(x-)\neq f(x)$.

（第二类间断点）For instance, the limit is not exist ($=\infty$, or other cases).

### Example (4.27)

(a) Define `Dirichlet function`
$$
f(x) =
\begin{cases}
1& x\ \text{rational},\\
0& x\ \text{irrational}.
\end{cases}
$$
Then $f$ has a `discontinuity` of the `second kind` at every point $x$, since neither $f(x+)$ nor $f(x-)$ exists.

(b) Define
$$
f(x) =
\begin{cases}
x& x\ \text{rational},\\
0& x\ \text{irrational}.
\end{cases}
$$
Then $f$ is `continuous` at $x=0$ and has a `discontinuity` of the `second kind` at every other point.

(c) Define
$$
f(x) =
\begin{cases}
x+2& -3\lt x\lt -2,\\
-x-2& -2\leq x\lt 0,\\
x+2& 0\leq x \lt 1
\end{cases}
$$
Then $f$ has a simple discontinuity at $x=0$ and is continuous at every other point of $(-3,1)$.

![Figure (c)](https://imgkr2.cn-bj.ufileos.com/96f5d1e4-5547-4ff5-9d06-dbf884ca95ff.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=ixdouj00plWXdTmJf%252FcG2Qaly6E%253D&Expires=1609163176)

(d) Define
$$
f(x) =
\begin{cases}
\sin\frac{1}{x}& x\neq 0,\\
0& x=0.
\end{cases}
$$
Since neither $f(0+)$ nor $f(0-)$ exists, $f$ has a discontinuity of the second kind at $x=0$. We have not yet shown that $\sin x$ is a continuous function. If we assume this result for the moment, 【Theorem 4.7】 implies that $f$ is continuous at every point $x\neq 0$.

![Figure (d): f(x)=sin(1/x)](https://imgkr2.cn-bj.ufileos.com/6af97ae6-ef18-4abd-8270-0ca68091c0e9.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=zlyYbT5sYWxgFigBd%252F5HNr8v2CU%253D&Expires=1609163440)

## Monotonic Functions

### Def. [单调函数] (4.28)

Let $f$ be `real` on $(a,b)$. Then $f$ is said to be `monotonically increasing` on $(a,b)$ if $a< x< y< b$ implies $f(x)\leq f(y)$. If the last inequality is reversed, we obtain the definition of a `monotonically decreasing` function. The class of monotonic functions consists of both increasing and the decreasing functions.

### Theorem [单调函数里任意点的上下极限与函数值的序关系] (4.29)

Let $f$ be monotonically increasing on $(a,b)$. then $f(x+)$ and $f(x-)$ exist at every point of $x\in (a,b)$. More precisely,
$$
\sup_{a< t< x}f(t) = f(x-) \leq f(x) \leq f(x+) = \inf_{x< t< b}f(t)
$$
Futhermore, if $a< x< y< b$, then
$$
f(x+)\leq f(y-)
$$
Analogous results evidently hold for monotonically decreasing functions.

**Proof.** 用极限的定义和单调性质（$f(x-\delta)\leq f(t)\leq f(x-) = \sup_{t\to x}f(t)$）去做，取一个左邻域 $(x-\delta, x)\ni t$ 证明 $|f(t)-\sup_{t\to x}f(t)|< \varepsilon,\ for\ t\in (x-\delta, x)$，另一半同样如此。

### Corollary (4.29)
Monotonic functions have no discontinuities of the second kind.

### Theorem [单增函数的间断点可数] (4.30)
Let $f$ be monotonic on $(a,b)$. Then the set of points of $(a,b)$ at which $f$ is discontinuous is at most countable.

**Thinking.**
直接证收集了全体单调函数的间断点的集合 $E$ 可数，是比较困难的。建立一对一的映射关系，使得 $E \leftrightarrows Rational\ Numbers$（靠单调有序的性质来建立唯一性），则可以说明 $E$ 也是可数的。

**Proof.** Suppose, for the sake of definiteness, that $f$ is increasing, and let $E$ be the set of points at which $f$ is discontinuous.

With every point $x$ of $E$ we associate a rational number $r(x)$ such that
$$
f(x-)< f(x)< f(x+)
$$
Since $x_1< x_2$ implies $f(x_1+)\leq f(x_2-)$, we see that $r(x_1)\neq r(x_2)$ if $x_1\neq x_2$.

We have thus established a $1-1$ correspondence between the set $E$ and a subset of the set of rational numbers. The latter, as we know, is countable.

### Remark (4.31)

单调函数的间断点不一定都是孤立点，事实上给定定义域内一个可数子集 $E$，这个集合甚至可以是稠密的。我们总能构造一个函数使得在 $E$ 上间断，但在定义域内除开 $E$ 上时保持连续。

## Infinite Limits and Limits at Infinity [无限极限与在无穷远点的极限]

To enable us to operate in the `extended real number system`, we shall now enlarge the scope of 【Def. 4.1】, by reformulating it in terms of neighborhoods.

For any real number $x$, we have already defined a neighborhood of $x$ to be any segment $(x-\delta, x+\delta)$.

### Def. [无穷邻域] (4.32)
For any real $c$, the set of real numbers $x$ such that $x>c$ is called a neighborhood of $+\infty$ and is written $(c,+\infty)$. Similarly, the set $(-\infty, c)$ is a neighborhood of $-\infty$.

### Def. [广义实数系中的极限] (4.33)
Let $f$ be a real function defined on $E\subset \mathbb R$. We say that
$$
f(t)\to A \ as \ t\to x
$$
where $A$ and $x$ are in the extended real number system, if for every neighborhood $U$ of $A$ there is a neighborhood $V$ of $x$ such that $V\cap E$ is not empty, and such that $f(t)\in U$ for all $t\in V\cap E$, $t\neq x$ ($t\in V\cap E \setminus \{x\}$).

### Theorem [广义实数系下函数的代数运算] (4.34)
Let $f$ and $g$ be defined on $E\subset \mathbb R$. Suppose
$$
f(t)\to A,\quad g(t)\to B \quad as\ t\to x
$$
Then

(a) $f(t)\to A^\prime$ implies $A^\prime = A$.

(b) $(f+g)(t) \to A+B$,

(c) $(fg)(t)\to AB$,

(d) $(\frac{f}{g})(t)\to \frac{A}{B}$,

provided the right members of (b), (c) and (d) are defined.

**Note.**
$\infty - \infty$, $0\cdot\infty$, $\frac{\infty}{\infty}$, $\frac{A}{0}$ are not defined.

【小亦 2020-12-27 22:35】于深圳
