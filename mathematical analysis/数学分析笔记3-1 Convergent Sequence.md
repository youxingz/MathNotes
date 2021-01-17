## Convergent Sequences [收敛序列]

### Def. [收敛性 Convergent] (3.1)

A sequence $\{p_n\}$ in a metric space $X$ is said to `converge` if there is a point $p\in X$ with the following property: For every $\varepsilon>0$ there is an integer $N$ such that $n\geq N$ implies that $d(p_n,p)< \varepsilon$. (Here $d$ denotes the distance in $X$.)

In this case we also say that $\{p_n\}$ `converges to` $p$, or that $p$ is the `limit` of $\{p_n\}$ [see 【Theorem 3.2(b)】], and we write $p_n\rightarrow p$, or
$$
\lim_{n\rightarrow\infty}p_n=p
$$
If $\{p_n\}$ does not converge, it is said to `diverge`.

**Note.** 很明显，收敛性必须依赖对“距离”函数的定义，所以必须在一个赋距空间中讨论。

上述定义表述可以简单叙述为：

**Another Def. (3.1)**
For sequence $\{p_n\}$, If $\forall \varepsilon>0, \exists n\geq N$, s.t. $d(p_n, p)< \varepsilon$, we say that $\{p_n\}$ `converges to` $p$. Denote with: $\lim_{n\rightarrow\infty}p_n = p$ or $p_n\rightarrow p$.

And we say that $p$ is the `limit` of $\{p_n\}$.

If $p = \infty$, we say that $\{p_n\}$ `diverges`.

### Theorem [Properties] (3.2)
Let $\{p_n\}$ be a sequence in a metric space $X$.

(a) 【$\varepsilon-N-r$（柯西性+邻域性）】$\{p_n\}$ `converges` to $p\in X$ if and only if every neighborhood of $p$ contains $p_n$ for all but finitely many $n$. ($N(p)\ni p_n$ for all $p_n$ which $n$ is finite.)

(b) 【唯一性】if $p\in X$, $p^\prime \in X$, and if $\{p_n\}$ converges to $p$ and to $p^\prime$, then $p=p^\prime$

(c) 【有界性】If $\{p_n\}$ `converges`, then $\{p_n\}$ is `bounded`.

(d) 【有极限点则必有收敛子序列】If $E\subset X$ and if $p$ is a limit point of $E$, then there is a sequence $\{p_n\}$ in $E$ such that $p=\lim_{n\rightarrow\infty}p_n$.

**Proof.**

(a) "$\Rightarrow$": Suppose $\{p_n\}\rightarrow p$ and let $V$ be a neighborhood of $p$. For some $\varepsilon>0$, the conditions $d(q,p)< \varepsilon$ imply $q\in V$. Corresponding to this $\varepsilon$, there exists $N$ such that $n\geq N$ implies $d(p_n, p)<\varepsilon$. Thus $n\geq N$ implies $p_n \in V$.

"$\Leftarrow$": Conversely, suppose every neighborhood of $p$ contains all but finitely many of the $p_n$. Fix $\varepsilon>0$, and let $V$ be the set of all $q\in X$ such that $d(p,q)<\varepsilon$. By assumption, there exists $N$ (corresponding to this $V$) such that $p_n\in V$ if $n\geq N$. Thus $d(p_n,p)< \varepsilon$ if $n\geq N$; hence $p_n\rightarrow p$.

(a[简述]) "$\Rightarrow$": By the convergent ($p_n\rightarrow p$), $\forall\varepsilon>0$, $\exists n\geq N$, s.t. $d(p_n, p)< \varepsilon$. Then let $r=max\{d(p_n, p)\}$, $n$ is finite, s.t. $p_n\in N_r(p)$.

"$\Leftarrow$": By the neighborhood ..., $\forall\varepsilon >0$, $\exists q$, s.t. $q\in N_\varepsilon(p)$. Thus $d(q, p)< \varepsilon$, and by the asumption $\exists n \geq N$, s.t. $p_n \in N_\varepsilon(p)$, that means $\exists n \geq N$, s.t. $d(p_n, p)< \varepsilon$, so its convergent.

(b) Let $\varepsilon>0$ be given. There exist integers $N$, $N^\prime$ such that
$$
\begin{aligned}
n\geq N\quad implies\quad d(p_n, p)< \frac{\varepsilon}{2},\\
n\geq N^\prime\quad implies\quad d(p_n, p^\prime)< \frac{\varepsilon}{2}.
\end{aligned}
$$

Hence if $n\geq max(N, N^\prime)$, we have
$$
d(p, p^\prime)\leq d(p, p_n) + d(p_n, p^\prime) < \varepsilon
$$
Since $\varepsilon$ was arbitrary, we conclude that $d(p,p^\prime)=0$.

(b[简述]) 假设两个点不唯一，利用三角不等式证明两个点距离被 $\varepsilon$ 控制即可。

(c) Suppose $p_n\rightarrow p$. There is an integer $N$ such that $n>N$ implies $d(p_n,p)< 1$. Put
$$
r=max\{1, d(p_1,p),..., d(p_N,p)\}
$$
Then $d(p_n,p)\leq r$ for $n=1,2,3,...$.

(c[简述]) 因为收敛性，所以有最大 $r$，则可用此半径做邻域，即为界。

(d) For each positive integer $n$, there is a point $p_n\in E$ such that $d(p_n,p)<\frac{1}{n}$. Given $\varepsilon>0$, choose $N$ so that $N_\varepsilon > 1$. If $n>N$, it follows that $d(p_n, p)< \varepsilon$. Hence $p_n\rightarrow p$.

(d[简述]) 因为收敛性，所以取半径为 $\frac{1}{n}$（与 $n$ 相关）的邻域，每一个邻域中取一个点组成序列 $\{p_n\}$ 即可，该序列自然收敛于 $p$。

This completes the prood.

### Theorem [复数下序列的代数性质] (3.3)

Suppose $\{s_n\}$, $\{t_n\}$ are complex sequences, and $\lim_{n\rightarrow\infty}s_n=s$, $\lim_{n\rightarrow\infty}t_n=t$. Then

(a)【加法封闭】$\lim_{n\rightarrow\infty}(s_n+t_n)=s+t$;

(b)【与常数乘法加法】$\lim_{n\rightarrow\infty}cs_n=cs$, $\lim_{n\rightarrow\infty}(c+s_n)=c+s$, for any number $c$;

(c)【乘法封闭】$\lim_{n\rightarrow\infty}s_nt_n=st$;

(d)【除法封闭】$\lim_{n\rightarrow\infty}\frac{1}{s_n}=\frac{1}{s}$, provided $s_n\neq 0$ ($n=1,2,3,...$), and $s\neq 0$.

**Proof.**

(a) Given $\varepsilon>0$, there exist integers $N_1$, $N_2$ such that
$$
\begin{aligned}
n\geq N\quad implies\quad d(s_n, s)< \frac{\varepsilon}{2},\\
n\geq N^\prime\quad implies\quad d(t_n, t)< \frac{\varepsilon}{2}.
\end{aligned}
$$
which $d(...)$ is distance function $|...| = \sqrt{a^2+(ib)^2}$ in $\mathbb C$.

If $N=max(N_1,N_2)$, then $n\geq N$ implies
$$
|(s_n+t_n)-(s+t)|\leq |s_n-s|+|t_n-t|\leq \varepsilon
$$
This proves (a).

(a[简述]) 利用收敛性的 $\varepsilon$ 来控制“两个极限的和”与“两个数字的和”的距离，从而确保相等。

(b) Let $c=\lim_{n\rightarrow\infty}c$, from (a), then (b) prove done.

(c) We use the identity
$$
s_nt_n - st = (s_n-s)(t_n-t) + s(t_n-t)+t(s_n-s)
$$
Given $\varepsilon > 0$, there are integers $N_1$, $N_2$ such that

$$
\begin{aligned}
n\geq N\quad implies\quad d(s_n, s)< \sqrt{\varepsilon},\\
n\geq N^\prime\quad implies\quad d(t_n, t)< \sqrt{\varepsilon}.
\end{aligned}
$$
If we take $N=max(N_1, N_2)$, $n\geq N$ implies
$$
d(s_n,s)\cdot d(t_n,t)< \varepsilon
$$
so that
$$
\lim_{n\rightarrow\infty}|s_n-s||t_n-t| = 0
$$
We now apply (a) and (b) to the identity equation, and conclude that
$$
\begin{aligned}
\lim_{n\rightarrow\infty}(s_nt_n-st) &= (s_n-s)(t_n-t) + s(t_n-t)+t(s_n-s) \\
&=0+s\cdot 0+t\cdot 0 \\
&=0
\end{aligned}
$$

(c[简述]) 原理同 (a) 完全一致，通过因式分解后，寻找多项式相应部分的 $\varepsilon$ 控制即可。

(d) Choose $m$ such that $|s_n-s|< \frac{1}{2}|s|$ if $n\geq m$, we see that
$$
|s_n|> \frac{1}{2}|s| \quad (n\geq m)
$$
Given $\varepsilon> 0$, there is an integer $N>m$ such that $n\geq N$ implies
$$
|s_n-s|< \frac{1}{2}|s|^2\varepsilon
$$
Hence, for $n\geq N$,
$$
\begin{aligned}
|\frac{1}{s_n}-\frac{1}{s}| &= |\frac{sn-s}{s_ns}| \\
&< \frac{2}{|s|^2}|s_n-s| \\
&< \varepsilon
\end{aligned}
$$
Thus complete all proof.

### Theorem [向量的收敛] (3.4)

(a)【向量收敛 $\Longleftrightarrow$ 各个分量独立收敛】Suppose $\mathbf x_n\in \mathbb R^k$ ($n=1,2,3,...$) and
$$
\mathbf x_n = < \alpha_{1,n},...,\alpha_{k,n} >
$$
Then $\{\mathbf x_n\}$ converges to $\mathbf x=< \alpha_{1}, ..., \alpha_{k} >$ if and only if
$$
\lim_{n\rightarrow\infty}\alpha_{j,n}=\alpha_j \quad (1\leq j\leq k)
$$

(b)【加法、数乘、实系数乘法封闭】Suppose $\{\mathbf x_n\}$, $\{\mathbf y_n\}$ are sequences in $\mathbb R^k$, $\{\beta_n\}$ is a sequence of real numbers, and $\mathbf x_n\rightarrow \mathbf x$, $\mathbf y_n\rightarrow \mathbf y$, $\beta_n\rightarrow \beta$. Then
$$
\begin{aligned}
&\lim_{n\rightarrow\infty}(\mathbf x_n + \mathbf y_n) = \mathbf x+\mathbf y \\
&\lim_{n\rightarrow\infty}\mathbf x_n \cdot \mathbf y_n = \mathbf x \cdot \mathbf y \\
&\lim_{n\rightarrow\infty}\beta_n \mathbf x_n = \beta \mathbf x
\end{aligned}
$$

**Proof.**
(a) If $\mathbf x_n \rightarrow \mathbf x$, the inequalities
$$
|\alpha_{j,n}-\alpha_{j}| \leq |\mathbf x_n - \mathbf x|
$$
which follow immediately from the definition of the norm in $\mathbb R^k$, show that result holds.

Conversely, if result holds, then to each $\varepsilon > 0$ there corresponds an integer $N$ such that $n\geq N$ implies
$$
|\alpha_{j,n}-\alpha_j|< \frac{\varepsilon}{\sqrt{k}}
$$
Hence $n\geq N$ implies
$$
|\mathbf x_n - \mathbf x| = \sqrt{\sum_{j=1}^k |\alpha_{j,n}-\alpha_j|^2}
$$
so that $\mathbf x_n \rightarrow \mathbf x$. This proves (a).

Part (b) follows from (a) and 【Theorem 3.3】. 用各分量的代数运算即可得出 $\varepsilon$ 控制。

【小亦 2020-12-24 01:14】于深圳
