## Upper And Lower Limits [上下极限]

### Def. [发散 Divergent] (3.15)

Let $\{s_n\}$ be a sequence of real numbers with the following property: For every real $M$ there is an integer $N$ such that $n\geq N$ implies $s_n\geq M$. We then write
$$
s_n \to +\infty
$$
Similarly, if for every real $M$ there is an integer $N$ such that $n\geq N$ implies $s_n\leq M$, we write
$$
s_n\to -\infty
$$
We also say that $\{s_n\}$ diverges, or $\{s_n\}$ is divergent sequence.

### Def. [上下极限 Upper&Lower Limit] (3.16)

Let $\{s_n\}$ be a sequence of `real numbers`. Let $E$ be the set of numbers $x$ (in the `extended real number system`, contains $\infty$) such that $s_{nk}\to x$ for some subsequence $\{s_{nk}\}$. This set $E$ contains all subsequential limits as defined in 【Def. 3.5 子序列】, plus possibly the numbers $+\infty$, $-\infty$.

We now reall 【Def. 1.8】 and 【Def. 1.23】 and put
$$
\begin{aligned}
s^\star &= \sup E\\
s_\star &= \inf E
\end{aligned}
$$
The numbers $s^\star$, $s_\star$ are called the `upper limits` and `lower limits` of $\{s_n\}$; we use the notation
$$
\limsup_{n\to\infty}s_n=s^\star, \quad \liminf_{n\to\infty}s_n=s_\star
$$

### Theorem [上下极限的性质 Properties] (3.17)
Let $\{s_n\}$ be a sequence of real numbers. Let $E$ and $s^\star$ have the same meaning as in 【Def. 3.16 上下极限】（其实就是之前定义的收集部分极限全体的集 $E^\star$，此处无歧义则写作 $E$ 即可）. Then $s^\star$ has the following two properties:

(a) 【确界在极限集内】$s^\star \in E$.

(b) 【邻域 $N_{s^\star - s_N}(s^\star)$ 内序一致】If $x>s^\star$, there is an integer $N$ such that $n\geq N$ implies $s_n< x$.

【唯一性】Moreover, $s^\star$ is the only number with properties (a) and (b).

**Proof.** 

(a) 【分情况讨论，$+\infty$、$-\infty$、实数】

If $s^\star = +\infty$, then $E$ is not bounded above; hence $\{s_n\}$ is not bounded above, and there is a subsequence $\{s_{nk}\}$ such that $\{s_{nk}\to +\infty\}$.

If $s^\star$ is real, then $E$ is bounded above, and at least one subsequential limit exists, so that (a) follows from 【Theorem 3.7 收集部分极限全体的集为闭集】 and 【Theorem 2.28 $\mathbb R^1$ 中集合的上确界在闭包内】.

If $s^\star = -\infty$, then $E$ contains only one element, namely $-\infty$, and there is no subsequential limit. Hence, for any real $M$, $s_n>M$ for at most a finite number of values of $n$, so that $s_n\to-\infty$.

This establishes (a) in all cases.

(b) 【反证法】Suppose there is a number $x> s^\star$ such that $s_n\geq x$ for infinitely many values of $n$. In that case, there is a number $y\in E$ such that $y\geq x> s^\star$, contradicting the definition of $s^\star$.

Thus $s^\star$ satisfies (a) and (b).

(c) 【唯一性】 To show the uniqueness, suppose there are two numbers, $p$ and $q$, which satisfy (a) and (b), and suppose $p< q$. Choose $x$ such that $p< x< q$. Since $p$ satisfies (b), we have $s_n< x$ for $n\geq N$. But then $q$ cannot satisfy (a).

### Theorem [上下极限的序由序列本身决定] (3.19)

If $s_n\leq t_n$ for $n\geq N$, where $N$ is fixed, then
$$
\begin{aligned}
\liminf_{n\to\infty} s_n &\leq \liminf_{n\to\infty}t_n\\
\limsup_{n\to\infty} s_n &\leq \limsup_{n\to\infty}t_n
\end{aligned}
$$

## Some Special Sequences

这里会给出一些常见的特殊实数列，证明相对很容易就不展开了。

### Exapmles 3.20

(a) If $p>0$, then $\lim\limits_{n\to\infty}\frac{1}{n^p}=0$.

(b) If $p>0$, then $\lim\limits_{n\to\infty}\sqrt[n]{p}=1$.

(c) $\lim\limits_{n\to\infty}\sqrt[n]{n}=1$.

(d) If $p>0$ and $\alpha$ is real, then $\lim\limits_{n\to\infty}\frac{n^\alpha}{(1+p)^n}=0$.

(e) If $|x|< 1$, then $\lim\limits_{n\to\infty}x^n=0$

【小亦 2020-12-25 04:50】于深圳
