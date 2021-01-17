## Subsequences

### Def. [子序列 Subsequence] (3.5)

Given a sequence $\{p_n\}$, consider a sequene $\{n_k\}$ of positive integers, such that $n_1< n_2< n_3< \dotsb$. Then the sequence $\{p_{ni}\}$ is called a `subsequence` of $\{p_n\}$. If $\{p_{ni}\}$ converges, its `limit` is called a `subsequential limit` of $\{p_n\}$.

It is clear that $\{p_n\}$ converges to $p$ if and only if every subsequence of $\{p_n\}$ converges to $p$.

**Note.** 子序列顺序不可重排，否则收敛性不一定能保证一致，“子序列极限”和“母序列极限”会收敛到同一个值。

### Theorem [关于紧集的特点] (3.6)

(a) If $\{p_n\}$ is a sequence in a compact metric space $X$, then some subsequence of $\{p_n\}$ converges to a point of $X$.（紧集中的序列必有收敛子序列）

(b) Every bounded sequence in $\mathbb R^k$ contains a convergent subsequence.（$\mathbb R^k$里闭集中的序列必有收敛子序列）

**Proof.**

(a) Let $E$ be the `range` of $\{p_n\}$.

If $E$ is `finite` then there is a $p\in E$ and a sequence $\{n_i\}$ with $n_1< n_2< n_3< \dotsb$, such that
$$
p_{n1} = p_{n2} = \dotsb = p
$$
The subsequence $\{p_{ni}\}$ so obtained converges evidently to $p$.（构造完全相等的一串点作为序列）

If $E$ is `infinite`, 【Theorem 2.37 紧集中的无限子集有极限点】 shows that $E$ has a limit point $p\in X$. Choose $n_1$ so that $d(p,p_{n1})< 1$. Having chosen $n_1, ..., n_{i-1}$, we see from 【Theorem 2.20 极限点的集的内点含有无限个点】 that there is an integer $n_i > n_{i-1}$ such that $d(p, p_{ni})<\frac{1}{i}$. Then $\{p_{ni}\}$ converges to $p$.（因为紧集中的无限子集必有极限点 $p$，所以用关于 $n$ 的邻域 $V_{\frac{1}{n}}(p)$ 来构造一个点序列）

(b) This follows from (a), since 【Theorem 2.41 海涅博雷尔定理 Heine Borel】 implies that every bounded subset of $\mathbb R^k$ lies in a compact subset of $\mathbb R^k$.

### Theorem [收集部分极限全体的集为闭集] (3.7)

The `subsequential limits` of a sequence $\{p_n\}$ (denote by $E^\star$) in a metric space $X$ form a `closed` subset of $X$.

**Proof.** （思路）Let $E^\star$ be the set of all subsequential limits of $\{p_n\}$, and let $q$ be a limit point of $E^\star$. We have to show that $q\in E^\star$. (By Definition of closed set.)

（证明过程）Choose $n_1$ so that $p_{n1}\neq q$. (If no such $n_1$ exists, then $E^\star$ has only one point which is $q$ itself, and there is nothing to prove.)

Put $\delta = d(q,p_{n1})$. Suppose $n_1, n_2, ..., n_{i-1}$ are chosen. Since $q$ is a limit point of $E^\star$, there is an $x\in E^\star$ with $d(x,q)< \frac{1}{2}^i\delta$. Since $x\in E^\star$, there is an $n_i > n_{i-1}$ such that $d(x, p_{ni})< \frac{1}{2}^i\delta$. Thus
$$
\begin{aligned}
d(q, p_{ni}) &\leq d(q, x) + d(x, p_{ni}) \\
&\leq \frac{1}{2}^{i}\delta + \frac{1}{2}^{i}\delta \\
&= \frac{1}{2}^{i-1}\delta
\end{aligned}
$$
for $i=1,2,3,...$. This says that $\{p_{ni}\}$ converges to $q$. Hence $q\in E^\star$.

#### Figure

![Figure for Theorem 3.7](https://imgkr2.cn-bj.ufileos.com/06e98e68-51a2-4b07-81a1-cf4c60e5fac9.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=Wl%252BmlzwCQGTf9vfj2ha09EcJmBU%253D&Expires=1608835114)


## Cauchy Sequences

### Def. [柯西序列] (3.8)

A sequence $\{p_n\}$ in a metric space $X$ is said to be a `Cauchy sequence` if every $\varepsilon>0$ there is an integer $N$ such that $d(p_n,p_m)<\varepsilon$ if $n\geq N$ and $m\geq N$.

简述：A sequence $\{p_n\}$ in $(X,d)$ is `Cauchy sequence`: $\forall \varepsilon >0$, $\exists m,n\geq N$, s.t. $d(p_n,p_m)<\varepsilon$.

### Def. [序列直径 Diameter] (3.9)

Let $E$ be a nonempty subset of a metric space $X$, and let $S$ be the set of all real numbers of the form $d(p,q)$, with $p, q\in E$ . The sup of $S$ is called the `diameter` of $E$.

If $\{p_n\}$ is a sequence in $X$ and if $E_N$ consists of the points $p_N,p_{N+1}, p_{N+2},...$, it is clear from the two preceding definitions that $\{p_n\}$ is a `Cauchy sequence` if and only if 
$$
\lim_{N\rightarrow\infty} diam\ E_N = 0
$$

由于序列直径的概念不是很重要，理解起来也很直观容易，所以此处只贴几个定理，证明过程就不展开了（更准确说是我们老师也没讲。。）。

### Theorem [Properties] (3.10)

(a) If $\bar E$ is the closure of a set $E$ in a metric space $X$, then
$$
diam\ \bar E = diam\ E
$$
(b) If $K_n$ is a sequence of compact sets in $X$ such that $K_n\supset K_{n+1}$, $n=1,2,3,...$, and if
$$
\lim_{n\to\infty} diam\ K_n = 0
$$
then $\cap_1^\infty K_n$ consists of exactly one point.

### Theorem [柯西序列与收敛序列] (3.11)
(a) In any metric space $X$, every convergent sequence is a Cauchy sequence.

(b) If $X$ is a compact metric space and if $\{p_n\}$ is a Cauchy sequence in $X$, then $\{p_n\}$ converges to some point of $X$.

(c) In $\mathbb R^k$, every Cauchy sequence converges.

**Note.** The difference between the definition of `convergence` and the definition of a `Cauchy sequence` is that: the `limit` is explicitly involved in the former, bu not in the latter（前者直接关联了极限的定义，而后者木有）. Thus 【Theorem 3.11.b】 may enable us to decide whether or not a given  sequence converges **without knowledge of the limit** to which it may converge（柯西列不需要知道极限就能判断收敛性）.

The fact (contained in 【Theorem 3.11】) that a sequence converges in $\mathbb R^k$ if and only if it is a Cauchy sequence is usually called the `Cauchy criterion` for convergence.

**Proof.**

(a) If $\{p_n\}\to p$ and if $\varepsilon>0$, there is an integer $N$ such that $d(p,p_n)< \varepsilon$ for all $n\geq N$. Hence
$$
d(p_n,p_m)\leq d(p_n,p)+d(p,p_m)< 2\varepsilon
$$
as soon as $n\geq N$ and $m\geq N$. Thus $\{p_n\}$ is a Cauchy sequence. 

(a[简述]) 利用 $p$，$p_n$，$p_m$ 的三角不等式可证。

(b) Let $\{p_n\}$ be a Cauchy sequence in the compact space $X$. For $N=1,2,3,...$, Let $E_N$ be the set consisting of $p_N,p_{N+1},p_{N+2},...$. Then
$$
\lim_{N\to\infty} diam\ \bar E = 0
$$
by 【Def. 3.9】 and 【Theorem 3.10.a】. Being a closed subset of the compact space $X$, each $\bar E_N$ is compact (【Theorem 2.35 闭集与紧集的交为紧】). Also $E_N\supset E_{N+1}$, so that $\bar E_N \supset \bar E_{N+1}$.

【Theorem 3.10.b】 shows now that there is a unique $p\in X$ which lies in every $\bar E_N$.

Let $\varepsilon>0$ be given. There is an integer $N_0$ such that $diam\ \bar E_N < \varepsilon$ if $N\geq N_0$. Since $p\in \bar E_N$, it follows that $d(p,q)< \varepsilon$ for every $q\in \bar E_N$, hence for every $q\in E_N$. In other words, $d(p, p_n)< \varepsilon$ if $n\geq N_0$. This says precisely that $p_n\to p$.

(b[简述]) 造一组邻域 $\bar E_N\supset \bar E_{N+1}$，利用收敛序列在紧集中直径终将趋于0的特点来证明存在这个极限点 $p$，使得这组序列 $p_n\to p$。

(c) Let $\{\mathbf x_n\}$ be a Cauchy sequence in $\mathbb R^k$. Define $E_N$ as in (b), with $\mathbf x_i$ in place of $p_i$. For some $N$, $diam\ E_N < 1$. The range of $\{\mathbf x_n\}$ is the union of $E_N$ and the finite set $\{\mathbf x_1,...,\mathbf x_{N-1}\}$. Hence $\{\mathbf x_n\}$ is bounded. Since every bounded subset of $\mathbb R^k$ has compact closure in $\mathbb R^k$ (【Theorem 2.41 海涅博雷尔定理 Heine Borel】), (c) follows from (b).

(c[简述]) 综合上述定理，收敛序列必有界，$\mathbb R^k$ 中有界集合的闭包必然是闭集，则序列集为紧集，由 (b) 自然得证。

### Def. [完备性 Complete] (3.12)

A metric space in which every Cauchy sequence converges is said to be `complete`.

Thus 【Theorem 3.11 柯西序列与收敛序列】 says that all `compact metric spaces` and all `Euclidean spaces` are complete. Also every `closed subset` $E$ of a `complete metric space` $X$ is complete.

#### Example

The set of rational numbers with $d(x,y)=|x-y|$ is not complete.

### Def. [序列的单调性] (3.13)
A sequence $\{s_n\}$ of real numbers is said to be

(a) `monotonically increasing` if $s_n\leq s_{n+1}$, $n=1,2,3,...$;

(b) `monotonically decreasing` if $s_n \geq s_{n+1}$, $n=1,2,3,...$.

The class of monotonic sequences consists of the increasing and the decreasing sequences.

### Theorem [收敛序列的单调有界定理] (3.14)

Suppose $\{s_n\}$ is `monotonic`. Then $\{s_n\}$ `converges` if and only if it is `bounded`.

**Note.** 这玩意儿很重要，是一个很基础的定理。在赋距赋序空间（比如$\mathbb R^1$）中的收敛序列必有界。

**Proof.** Suppose $s_n\leq s_{n+1}$. Let $E$ be the range of $\{s_n\}$.

"$\Leftarrow$": If $\{s_n\}$ is bounded, let $s$ be the least upper bound of $E$ ($supE$). Then
$$
s_n \leq s \quad n=1,2,3,...
$$
For every $\varepsilon > 0$, there is an integer $N$ such that
$$
s-\varepsilon < s_N \leq s
$$
for otherwise $s-\varepsilon$ would be an upper bound of $E$. Since $\{s_n\}$ increases, $n\geq N$ therefore implies
$$
s-\varepsilon < s_n \leq s
$$
which shows that $\{s_n\}$ converges to s.

"$\Rightarrow$": The converse follows from 【Theorem 3.2.c】.

(简述)："$\Leftarrow$":  既然有界，设界为 $E$，上确界为 $s=\sup E$，所以存在一个邻域 $V_{\varepsilon}s \ni s_n, \forall n\geq N$，其中 $\varepsilon$ 由 $N$ 确定。因为 $\{s_n\}$ 单调，所以邻域内的点必然收敛至 $s$。

"$\Rightarrow$": 同【Theorem 3.2.c】，以 $r$ 为半径构造邻域，半径设为 $r = max\{1, d(s_1, s), ... , d(s_N,s)\}$ 即可。则 $N_r(s)$ 是其界。


【小亦 2020-12-25 03:45】于深圳
