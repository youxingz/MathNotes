## Series [级数]

### Def. [级数 Series] (3.21)

Given a sequence $\{a_n\}$, we use the notation
$$
\sum_{n=p}^q a_n \quad (p\leq q)
$$
to denote the sum $a_p+a_{p+1}+\dotsb+a_q$. With $\{a_n\}$ we associate a sequence $\{s_n\}$, where
$$
s_n=\sum_{k=1}^n a_k
$$

For $\{s_n\}$ we also use the symbolic expression
$$
a_1+a_2+a_3+\dotsb
$$
or, more concisely,
$$
\sum_{n=1}^\infty a_n
$$
We call this `infinite series`, or just a `series`. The numbers $s_n$ are called the `partial sums` of the series. If $\{s_n\}$ converges to $s$, we say that the series `converges`, and write
$$
\sum_{n=1}^\infty a_n = s
$$
The number $s$ is called the sum of the series. But it should be clearly understood that $s$ is `the linit of a sequence of sums`, and is **not obtained simply by addition**.

If $\{s_n\}$ diverges, the series is said to `diverge`.

The `Cauchy criterion` (【Theorem 3.11】) can be restated in the following form:

### Theorem [柯西准则] (3.22)

$\sum a_n$ `converges` if and onky if for every $\varepsilon>0$ there is an integer $N$ such that
$$
\Bigl\lvert\sum_{k=n}^m a_k\Bigr\rvert\leq \varepsilon
$$
if $m\geq n\geq N$.

In particular, by taking $m=n$, it becomes
$$
\lvert a_n \rvert \leq \varepsilon\quad (n\geq N)
$$

### Theorem [收敛则通项必趋于0，反之不成立] (3.23)
If $\sum a_n$ `converges`, then $\lim_{n\to\infty}a_n=0$.

**Note.** 
The condition $a_n \to 0$ is not necessary to ensure convergence of $\sum a_n$. For instance, the series $\sum_{n=1}^\infty \frac{1}{n}$ diverges.

### Theorem [非负项级数收敛必有界，有界必收敛] (3.24)

A series of nonnegative terms converges if and only if its partial sums form a bounded sequence.

### Theorem [收敛的比较判别法] (3.25)

(a) If $|a_n|\leq |c_n|$ for $n\geq N_0$, where $N_0$ is some fixed integer, and if $\sum c_n$ converges, then $\sum a_n$ converges.

(b) If $a_n\geq d_n\geq 0$ for $n\geq N_0$, and if $\sum d_n$ diverges, then $\sum a_n$ diverges.
(Note that series consists of `nonnegative` terms $a_n$.)

**Proof.**
(a) Given $\varepsilon>0$, there exists $N\geq N_0$ such that $m\geq n\geq N$ implies
$$
\sum_{k=n}^m c_k \leq \varepsilon
$$
by the Cauchy criterion. Hence
$$
\Bigl\lvert\sum_{k=n}^m a_k\Bigr\rvert \leq
\sum_{k=n}^m |a_k| \leq
\sum_{k=n}^m c_k \leq
\varepsilon
$$
Then $\sum a_n$ converges.

(b) Follow from (a), for if $\sum a_n$ converges, so must $\sum d_n$.

## Series of Nonenegative Terms [非负项级数]

### Theorem [简单幂级数 Power Series] (3.26)
If $0\leq x\leq 1$, then
$$
\sum_{n=0}^\infty x^n= \frac{1}{1-x}
$$
If $x\geq 1$, the series diverges.

**Proof.**
If $x\neq 1$,
$$
s_n = \sum_{k=0}^n x^k = \frac{1-x^{n+1}}{1-x}
$$
The result follows if we let $n\to\infty$. For $x=1$, we get
$$
s_n = 1+1+1+\dotsb
$$
which evidently diverges.

### Theorem [柯西准则判别方式] (3.27)
Suppose $a_1\geq a_2\geq a_3\geq \dotsb \geq 0$. Then the series $\sum_{n=1}^\infty a_n$ converges if and only if the series
$$
\sum_{k=0}^\infty 2^ka_{2^k} = a_1 + 2a_2+4a_4+8a_8+\dotsb
$$
converges.

**Note.**
这玩意儿很好用，但不常能用到。构造形式：$\sum_{n}^\infty a_n \Rightarrow \sum_k^\infty 2^k \frac{1}{2^k\cdot c_n}$

**Proof.** By 【Theorem 3.24 非负项级数收敛必有界，有界必收敛】, it suffices to consider boundedness of the partial sums. Let
$$
\begin{aligned}
s_n = a_1 + a_2+\dotsb +a_n,\\
t_k=a_1+2a_2+\dotsb+2^ka_{2^k}.
\end{aligned}
$$
For $n< 2^k$,
$$
\begin{aligned}
s_n&\leq a_1+(a_2+a_3)+\dotsb+(a_{2^k}+\dotsb+a_{2^{k+1}-1}) \\
&\leq a_1 + 2a_2 + \dotsb + 2^k a_{2^k} \\
&=t_k
\end{aligned}
$$
so that $s_n \leq t_k$.

On the other hand, if $n> 2^k$,
$$
\begin{aligned}
s_n&\geq a_1+a_2+(a_3+a_4)+\dotsb+(a_{2^{k-1}+1}+\dotsb+a_{2^k}) \\
&\geq \frac{1}{2}a_1 + a_2 + 2a_4 + \dotsb + 2^{k-1} a_{2^k} \\
&=\frac{1}{2}t_k
\end{aligned}
$$
so that $2s_n\geq t_k$
Thus, the sequences $\{s_n\}$ and $\{t_n\}$ are either both bounded or both unbounded. This completes the proof.

### Theorem [p-series] (3.28)
$\sum \frac{1}{n^p}$ converges if $p>1$ and diverges if $p\leq 1$.

**Proof.** （用柯西判别证明即可）If $p\leq 0$, divergence follows from 【Theorem 3.23】. If $p>0$, 【Theorem 3.27】 is applicable, and we are led to the series
$$
\sum_{k=0}^\infty 2^k \cdot \frac{1}{2^{kp}} = \sum_{k=0}^\infty 2^{(1-p)k}
$$
Now, $2^{1-p}<1$ if and only if $1-p< 0$, that is $p>1$, then the series converges.

### Theorem [对数级数] (3.29)
If $p>1$,
$$
\sum_{n=2}^\infty \frac{1}{n(\log n)^p}
$$
converges; if $p\leq 1$, the series diverges.

**Note.** 证明略，同样使用柯西准则判别进行证明即可。（$\sum_{n}^\infty a_n \Rightarrow \sum_k^\infty 2^k \frac{1}{2^k\cdot c_n}$）

## The Number $e$ [自然底数]

由于自然底数过于常见且枯燥，则只列出几种形式和特点，不展开具体证明了。

### Def. [$e$] (3.30)
$$
e = \sum_{n=0}^\infty \frac{1}{n!}
$$

### Theorem (3.31)
$$e=\lim\limits_{n\to\infty}(1+\frac{1}{n})^n$$

### Theorem (3.32)

$e$ is irrational.

## The Root and Ratio Tests [根式判别法、比值判别法]

### Theorem [根式判别法] (3.33)
Given $\sum a_n$, put $\alpha = \limsup\limits_{n\to\infty} \sqrt[n]{|a_n|}$.
Then

(a) if $\alpha < 1$, $\sum a_n$ `converges`;

(b) if $\alpha > 1$, $\sum a_n$ `diverges`;

(c) if $\alpha = 1$, the test fail;

**Note.** 都是上极限比值哦。

### Theorem [比值判别法] (3.34)

The series $\sum a_n$

(a) `converges` if $\limsup\limits_{n\to\infty}\Bigl\lvert\frac{a_{n+1}}{a_n}\Bigr\rvert < 1$,

(b) `diverges` if $\Bigl\lvert\frac{a_{n+1}}{a_n}\Bigr\rvert \geq 1$ for all $n\geq n_0$, where $n_0$ is some fixed integer.

**Note.** 发散的判别中并不要求一定是下/上极限比值，但收敛的判别必须是上极限比值小于$1$。

### Remark (3.36)

根式判别法比较复杂，但判别要求更严格，如果计算更容易的比值判别法不管用了再用根式判别。

### Theorem [根式判别法和比值判别法比较] (3.37)

For any sequence $\{c_n\}$ of positive numbers,
$$
\begin{aligned}
\liminf_{n\to\infty}\frac{c_{n+1}}{c_n} &\leq \liminf_{n\to\infty} \sqrt[n]{c_n},\\
\limsup_{n\to\infty} \sqrt[n]{c_n} &\leq
\limsup_{n\to\infty}\frac{c_{n+1}}{c_n}.
\end{aligned}
$$

## Power Series [幂级数]

### Def. [幂级数] (3.38)

Given a sequence $\{c_n\}$ of complex numbers, the series
$$
\sum_{n=0}^\infty c_n z^n
$$
is called a `power series`. The numbers $c_n$ are called the `coeffocoents` of the series; $z$ is a `complex number`.

### Theorem [幂级数的收敛半径] (3.39)

Given the power series $\sum c_n z^n$, put
$$
\alpha = \limsup_{n\to\infty} \sqrt[n]{|c_n|}, \quad R=\frac{1}{\alpha}
$$
(If $\alpha=0$, $R=+\infty$; if $\alpha=+\infty$, $R=0$.)
Then $\sum c_n z^n$ `converges` if $|z|< R$, and `diverges` if $|z|>R$.

**Proof.** Put $a_n = c_n z^n$, and apply the `root test`:
$$
\limsup_{n\to\infty} \sqrt[n]{|a_n|} = |z|\limsup_{n\to\infty}\sqrt[n]{|c_n|} = \frac{|z|}{R}
$$
*Note:* R is called the `radius` of convergence of power series $\sum c_n z^n$.

### Examples (3.40)

| series | R | note. |
|--------|---|-------|
|$\sum n^nz^n$ | 0 | | 
|$\sum\frac{z^n}{n!}$ |$+\infty$| Apply ratio test easier |
|$\sum z^n$| $R=1$; if $\vert z\vert=1 \Rightarrow$ diverge | |
|$\sum \frac{z^n}{n}$  | $R=1$; diverges: $z=1$; converge: otherwise include $\vert z\vert=1$ | |
|$\sum \frac{z^n}{n^2}$ | $R=1$; converges for all $z$ with $\vert z\vert = 1$ | By comparison test, $\vert\frac{z^n}{n^2}\vert = \frac{1}{n^2}$ ||



【小亦 2020-12-26 04:28】于深圳
