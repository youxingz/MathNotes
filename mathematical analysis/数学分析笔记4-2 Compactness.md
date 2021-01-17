## Comtinuity and Compactness

### Def. [函数的界] (4.13)
A mapping $\mathbf f$ pf a set $E$ into $\mathbb R^k$ is said to be `bounded` if there is a real number $M$ such that $\mathbf f(x)\leq M$ for all $x\in E$.

### Theorem [紧集上连续函数映入的集合为紧集] (4.14)
Suppose $f$ is a `continuous mapping` of a `compact` metric space $X$ into a metric space $Y$. Then $f(X)$ is `compact`.

**Thingking.** 证明紧性就是寻找至少存在一组开覆盖包含这个集合。根据连续映射可将开集映射为开集，则将有限个开集映射后的集合依然可以作为开覆盖来包含值域，则值域紧。

此处为了证明开集映射后依然为开集，用了【Theorem 4.8 连续函数的逆映射函数】来说明开的逆映射为开，从而构造出这个开覆盖。

即：$K\subset X$，有：
$$
\begin{aligned}
&K\subseteq f^{-1}(f(K)) \subseteq f^{-1}(\bigcup_{\alpha\in I} V_\alpha) = \bigcup_{\alpha\in I}f^{-1}(V_\alpha)\\
&\Rightarrow
f(K) \subseteq \bigcup_{\alpha\in I} V_\alpha
\end{aligned}
$$

其中易知 $V_\alpha$ 为开，$\alpha$ 为有限个，故形成一组有限开覆盖使得 $f(K)$ 紧。

**Proof.** Let $\{V_\alpha\}$ be an open cover of $f(X)$. Since $f$ is continuous, 【Theorem 4.8 连续函数的逆映射函数】 shows that each of the sets $f^{-1}(V)$ is open. Since $X$ is compact, there are finitely many indices, say $\alpha_1,...,\alpha_n$, such that
$$
X\subset f^{-1}(V_{\alpha_1}) \cup\dotsb \cup f^{-1}(V_{\alpha_n})
$$
Since $f(f^{-1}(E))\supset E$ for every $E\subset Y$, this equation implies that
$$
f(X) \subset V_{\alpha_1} \cup\dotsb\cup V_{\alpha_n}
$$
Thus, $f(X)$ is compact. This completes the proof.

**Note.** We have used the relation $f(f^{-1}(E))\supset E$, valid for $E\subset Y$. If $E\subset X$, then $f^{-1}(f(E))\supset E$; equality need not hold in either case.

### Theorem [连续函数把紧集映射到欧式空间为有界闭集] (4.15)
If $\mathbf f$ is a `continuous` mapping of a `compact` metric space $X$ into $R^k$, then $\mathbf f(X)$ is `closed` and `bounded`. Thus, $\mathbf f$ is `bounded`.

**Note.** This proof follows from 【Theorem 2.41 海涅博雷尔定理 Heine Borel】. The result is particularly important when $f$ is real:

### Theorem [紧集上的连续实函数有上下确界] (4.16)

Suppose $f$ is `continuous` `real` function on a `compact` metric space $X$, and
$$
M=\sup_{p\in X}f(p), \quad m=\inf_{p\in X}f(p)
$$
Then there exist points $p,q\in X$, such that $f(p)=M$ and $f(q)=m$.

（我们之后一般会用字母 $M,m$ 分别表示函数的上限和下限）

The notation above means that $M$ is the `least upper bound` of the set of all numbers $f(p)$, where $p$ ranges over $X$, and that $m$ is the `greatest lower bound` of this set of numbers.

该定理可等价叙述为：
There exist points $p,q\in X$ such that $f(q)\leq f(x)\leq f(p)$ for all $x\in X$. (That is, $f$ attains its maximum at $p$ and its minimum at $q$.)

**Proof.** By 【Theorem 4.15 连续函数把紧集映射到欧式空间为有界闭集】, $f(X)$ is a closed and bounded set of real numbers; hence $f(X)$ contains
$$
M=\sup f(X)\quad \text{and} \quad m=\inf f(X)
$$
by 【Theorem 2.28 $\mathbb R^1$ 中集合必有上下确界】.

### Theorem [紧集上的 $1-1$ 连续函数的逆函数也连续] (4.17)
Suppose $f$ is a `continuous` $1-1$ mapping of a `compact` metric space $X$ onto a `metric` space $Y$. Then the inverse mapping $f^{-1}$ definned on $Y$ by
$$
f^{-1}(f(x)) = x\quad x\in X
$$
is a `continuous` mapping of $Y$ onto $X$.

**Thinking.** 思路：根据【Theorem 4.8 函数连续当且仅当其逆函数将开集映入开集】，我们只需要证明 $f^{-1}$ 的逆 $f$ 将所有的开集 $V$ 映入开集即可。
$$
\begin{aligned}
&V\ open \\
\Longrightarrow &V^c\ closed \\
\overset{on\ compact}{\Longrightarrow} &V^c\ is\ compact\ in\ X \\
\overset{on\ compact}{\Longrightarrow} &f(V^c)\ is\ compact\ in\ Y \\
\Longrightarrow &f(V^c)\ is\ closed\ in\ Y \\
\Longrightarrow &f(V)\ is\ open\ in\ Y
\end{aligned}
$$

**Proof.** Apply 【Theorem 4.8 连续函数的逆映射函数把开集映入开集】 to $f^{-1}$ inplace of $f$, we see that it suffices to prove that $f(V)$ is an open set in $Y$ for every open set $V$ in $X$. Fix such a set $V$.

The complement $V^c$ of $V$ is closed in $X$, hence compact (【Theorem 2.35 紧集的闭子集为紧集】); hence $f(V^c)$ is a compact subset of $Y$ (【Theorem 4.14 紧集上连续函数映入的集合为紧集】). and so is closed in $Y$ (【Thoerem 2.34 紧集必然是闭集】). Since $f$ is $1-1$ and $onto$, $f(V)$ is the complement of $f(V^c)$. Hence $f(V)$ is open.

### Def. [Uniformly Continuous 均匀连续/一致连续/普遍连续] (4.18)
注：由于各个教材版本翻译大有不同，但英文都是 `Uniformly Continuous`，为了方便理解，本专栏后续都会采用`普遍连续`的翻译。这里简单说明一下几种翻译的异同：

`均匀连续`：连续是均匀的，大家都享有同一个控制宽度 $\delta$。

`一致连续`：连续是一致的，大家都用一致的 $\delta$ 控制函数变化程度。

`普遍连续`：连续在给定的区间内是具有普遍性的，即局部的连续性证明了之后可以放到全局使用。

个人更倾向使用`普遍连续`进行释义，后文不再对此翻译过多解释。

定义：

Let $f$ be a mapping of a metric space $X$ into a metric space $Y$. We say that $f$ is `uniformly continuous` on $X$ if for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
d_Y(f(p), f(q))<\varepsilon
$$
for all $p,q\in X$ for which $d_X(p,q)<\delta$.

**Note.** 普遍连续和连续性定义的对比：都是通过 $\delta-\varepsilon$ 进行控制，但连续性的 $\delta = \delta(\varepsilon)$，即 $\delta$ 是关于 $\varepsilon$ 的函数；可这里的普遍连续的 $\delta$ 是一个预先给定就可以不变的值，与 $\varepsilon$ 的取值无关。

定义可叙述为：
$X \overset{f}{\to} Y$, for fixed $\delta > 0$, $\forall \varepsilon>0$, s.t. $[d_X(p,q)<\delta]$ $\Longrightarrow$ $[d_Y(f(p),f(q))<\varepsilon]$.

**Remark** Every uniformly continuous function is continuous. That the two concepts are equivalent on compact sets follows from the next theorem.

### Theorem [紧集上的连续函数普遍连续] (4.19)
Let $f$ be a continuous mapping of a compact metric space $X$ into a metric space $Y$. Then $f$ is uniformly continuous on $X$.

**Thinking.** 由于紧致性，则可寻找一组有限开覆盖，使得在给定 $\varepsilon$ 的情况下 $\delta$ 的取值不为 $0$（$\delta = \min [\phi(p_i)]$, which $\phi(p_i)$ is the radius of $N(p_i)$, of the open cover.）。连立三角不等式则可证明函数的普遍连续性。

**Proof.** Let $\varepsilon>0$ be given. Since $f$ is continuous, we can associate to each point $p\in X$ a positive number $\phi(p)$ such that
$$
q\in X,\ d_X(p,q)< \phi(p) \quad implies \quad d_Y(f(p),f(q))<\frac{\varepsilon}{2}
$$
Let $J(p)$ be the set of all $q\in X$ for which（就是邻域 $N_{\frac{1}{2}\phi(p)}(p)$）
$$
d_X(p,q)<\frac{1}{2}\phi(p)
$$
Since $p\in J(p)$, the collection of all sets $J(p)$ is an open cover of $X$; and since $X$ is compact, there is a finite set of points $p_1,...,p_n$ in $X$, such that
$$
X\subset \bigcup_{i=1}^n J(p_i)
$$
We put
$$
\delta = \frac{1}{2}\min_{1\leq i \leq n} [\phi(p_i)]
$$
Then $\delta > 0$. （因为紧集有有限开覆盖，否则 $\delta$ 可以等于 $0$）

Now let $q$ and $p$ be points of $X$, such that $d_X(p,q)<\delta$. Then there is an integer $m$, $1\leq m\leq n$, such that $p\in J(p_m)$; hence
$$
d_X(p,p_m)<\frac{1}{2}\phi(p_m)
$$
and we also have
$$
d_X(q,p_m) \leq d_X(p,q)+d_X(p,p_m)< \delta + \frac{1}{2}\phi(p_m)\leq \phi(p_m)
$$
Finally, we have
$$
d_Y(f(p),f(q))\leq d_Y(f(p),f(p_m))+d_Y(f(q),f(p_m))<\varepsilon
$$
This completes the proof.

### Theorem [非紧致函数的性质 Properties of Noncompact Functions] (4.20)
Let $E$ be a `noncompact` set in $\mathbb R^1$. Then

(a) there exists a `continuous` function on $E$ which is `not bounded`;

(b) there exists a `continuous` and `bounded` function on $E$ which has `no maximum`.

If, in addition, $E$ is `bounded`, then

(c) there exists a `continuous` function on $E$ which is `not uniformly continuous`.

**Proof.**

(a) （反证法）Suppose first that $E$ is bounded, so that there exists a limit point $x_0$ of $E$ which is not a point of $E$. Consider
$$
f(x) = \frac{1}{x-x_0}\quad x\in E
$$
This is continuous on $E$ (【Theorem 4.9 代数运算保连续性】), but evidently unbounded.

(b) The function $g$ given by
$$
g(x) = \frac{1}{1+(x-x_0)^2} \quad x\in E
$$
is continuous on $E$, and is bounded, since $0< g(x)< 1$. It is clear that $\sup_{x\in E}g(x) = 1$ whereas $g(x)< 1$ for all $x\in E$. Thus $g$ has no maximum on $E$.

(c) This would be false if boundedness were omitted from the hypotheses. for, let $E$ be the set of all integers. Then every function defined on $E$ is uniformly continuous on $E$. To see this, we need merely take $\delta< 1$ in 【Def. 4.18】.

### Example [连续函数的反函数不连续的情况] (4.21)

Let $X$ be the half-open interval $[0,2\pi)$ on the real line, and let $\mathbf f$ be the mapping of $X$ onto the circle $Y$ consisting of all points whose distance from the origin is $1$, given by

$$
\mathbf f(t) = < \cos t, \sin t > \quad 0\leq t\leq 2\pi
$$
The continuity of the trigonometric functions consine and sine, as well as their periodicity properties, will be established in 【Chapter 8】. These results show that $\mathbf f$ is a continuous $1-1$ mapping of $X$ onto $Y$.

However, the inverse mapping (which exists, since $\mathbf f$ is $1-1$ and $onto$) fails to be continuous at the point $(1,0) = \mathbf f(0)$. Of course, $X$ is not compact in this example. (It may be of interest to observe that $\mathbf f^{-1}$ fails to be continuous in spite of the fact that $Y$ is compact!)

【小亦 2020-12-27 19:54】于深圳
