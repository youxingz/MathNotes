## Summation By Parts [分部求和法/阿贝尔变换]

### Theorem (3.41)

Given two sequence $\{a_n\}$, $\{b_n\}$, put
$$
A_n = \sum_{k=0}^N a_k
$$
if $n\geq 0$; put $A_{-1}=0$. Then, if $0\leq p\leq q$, we have
$$
\sum_{n=p}^q a_n b_n =\sum_{n=p}^{q-1}A_n(b_n-b_{n+1}) + A_qb_q -A_{p-1}b_p 
$$

**Note.** 分部求和公式被用来证明积分第二中值定理。可写作：
$$
\sum_{{k=m}}^{n}f_{k}(g_{{k+1}}-g_{k})=\left[f_{{n+1}}g_{{n+1}}-f_{m}g_{m}\right]-\sum _{{k=m}}^{n}g_{{k+1}}(f_{{k+1}}-f_{k})
$$
或更对称的形式：
$$
\begin{aligned}
&\quad\sum_{{i=m+1}}^{n}\left(b_{i}-b_{{i-1}}\right)a_{i}+\sum_{{i=m+1}}^{n}\left(a_{i}-a_{{i-1}}\right)b_{{i-1}} \\
&=a_{n}b_{n}-a_{m}b_{m} \\
&=\sum _{{i=m+1}}^{n}\left(b_{i}-b_{{i-1}}\right)a_{{i-1}}+\sum _{{i=m+1}}^{n}\left(a_{i}-a_{{i-1}}\right)b_{i}
\end{aligned}
$$

**Proof.**

$$
\begin{aligned}
&\quad\sum_{n=p}^q a_bb_n \\
&= \sum_{n=p}^q(A_n-A_{n-1})b_n \\
&= \sum_{n=p}^q A_nb_n - \sum_{n=p}^q A_{n-1}b_n \\
&= \sum_{n=p}^q A_nb_n - \sum_{n=p-1}^{q-1} A_{n}b_{n+1} \\
&= A_qb_q + A_{p-1}b_{p-1} + (\sum_{n=p-1}^{q-1} A_nb_n - \sum_{n=p-1}^{q-1} A_{n}b_{n+1}) \\
&=A_qb_q + A_{p-1}b_{p-1} + \sum_{n=p-1}^{q-1}A_n(b_n-b_{n+1}) \\
&=A_qb_q + A_{p-1}b_{p-1} + \sum_{n=p}^{q-1}A_n(b_n-b_{n+1}) + A_{p-1}(b_{p-1} - b_{p})\\
&=\sum_{n=p}^{q-1}A_n(b_n-b_{n+1}) + A_qb_q -A_{p-1}b_p
\end{aligned}
$$
This formula is called `partial summation formula`, is useful in the investigation of series of the form $\sum a_nb_n$, particularly when $\{b_n\}$ is monotonic.

### Theorem [比较判别法] (3.42)
Suppose

(a) the partial sums $A_n$ of $\sum a_n$ form a bounded sequence;

(b) $b_0\geq b_1\geq b_2\geq \dotsb$;

(c) $\lim\limits_{n\to\infty}b_n = 0$.

Then $\sum a_nb_n$ converges.

**Proof.** Since $A_n$ were bounded, Choose $M$ such that $|A_n|\leq M$ for all $n$. Given $\varepsilon > 0$, there is an integer $N$ such that $b_N\leq \varepsilon / 2M$. For $N\leq p\leq q$, we have
$$
\begin{aligned}
\Bigl\lvert \sum_{n=p}^q a_n b_n \Bigr\rvert &= \Bigl\lvert \sum_{n=p}^{q-1}A_n(b_n - b_{n+1}) + A_qb_q -A_{p-1}b_p \Bigr\rvert \\
&\leq M \Bigl\lvert \sum_{n=p}^{q-1}(b_n - b_{n+1}) + b_q + b_p \Bigr\rvert \\
&= 2Mb_p \leq 2Mb_N \leq \varepsilon
\end{aligned}
$$
Converges now follows from the Cauchy criterion. We note that the first inequality in the above chain depends of course on the fact that $b_n-b_{n+1}\geq 0$.

### Theorem [莱布尼茨判别法] (3.43)

Suppose

(a) $|c_1|\geq |c_2|\geq |c_3|\geq\dotsb$;

(b) $c_{2m-1}\geq 0$, $c_{2m}\leq 0$, $m=1,2,3,...$;

(c) $\lim_{n\to\infty}c_n = 0$.

Then $\sum c_n$ converges.

**Proof.** Apply 【Theorem 3.42】, with $a_n = (-1)^{n+1}$, %b_n = |c_n|%.

### Theorem [幂级数的收敛（半径为1时）] (3.44)

Suppose the radius of convergence of $\sum c_n z^n$ is $1$, and suppose $c_0\geq c_1\geq c_2\geq \dotsb$, $\lim_{n\to\infty}c_n = 0$. Then $\sum c_n z^n$ converges at every point on the circle $|z|=1$, except possibly at $z=1$.

**Proof.** Put $a_n = z^n$, $b_n = c_n$. The hypotheses of 【Theorem 3.42】 are then satisfied, since
$$
|A_n| = \Bigl\vert\sum_{m=0}^n z^m \Bigr\vert = \Bigl\vert \frac{1-z^{n+1}}{1-z} \Bigr\vert \leq \frac{2}{|1-z|}
$$
if $|z|=1$, $z\neq 1$.


## Absolute Convergence [绝对收敛]

The series $\sum a_n$ is said to `converge absolutely` if the series $\sum |a_n|$ converges.

### Theorem [绝对收敛必条件收敛] (3.45)
If $\sum a_n$ converges absolutely, then $\sum a_n$ converges.

**Proof.**
The assertion follows from the inequality
$$
|\sum_{k=n}^m a_k| \leq \sum_{k=m}^n|a_k|
$$
plus the Cauchy criterion. （柯西判别可知：$\sum_{k=m}^n|a_k| \leq \varepsilon\Longrightarrow \sum_{k=m}^na_k\leq \varepsilon$）

### Remarks [收敛但不绝对收敛 Converge Nonabsolutely] (3.46)
For series of positive terms, absolute convergence is the same as convergence.

If $\sum a_n$ converges, but $\sum |a_n|$ diverges, we say that $\sum a_n$ `converges nonabsolutely`. For instance, the series
$$
\sum \frac{(-1)^n}{n}
$$
converges nonabsolutely (【Theorem 3.43 莱布尼茨判别法】).

**Note.** 无限级数绝对收敛可重排序求和，但非绝对收敛则不可换序求和。

## Addition and Multiplication of Series [级数的加法和乘法运算]

### Theorem [] (3.47)

If $\sum a_n = A$, and $\sum b_n=B$, then $\sum (a_n+b_n) = A+B$, and $\sum ca_n = cA$, for any fixed $c$.

**Proof.**
Let
$$
A_n = \sum_{k=0}^n a_k, \quad B_n = \sum_{k=0}^n b_k
$$
Then
$$
A_n + B_n = \sum _{k=0}^n (a_k+b+k)
$$

Since $\lim+{n\to\infty}A_n = A$ and $\lim_{n\to\infty}B_n = B$, we see that
$$
\lim_{n\to\infty}(A_n+B_n) = A+B
$$

The proof of the second assertion is even simpler.

### Theorem [柯西乘积 Cauchy Product] (3.48)
Given $\sum a_n$ and $\sum b_n$, we put
$$
c_n = \sum_{k=0}^n a_kb_{n-k} \quad n=0,1,2,...
$$
and call $\sum c_n$ the `product` of the two given seires.

**Note.** This definition may be motivated as follows. If we take two power series $\sum a_n z^n$ and $\sum b_n z^n$, multiply them term by term, and collect terms containing the same power of $z$, we get
$$
\begin{aligned}
\sum_{n=0}^\infty a_n z^n \cdot \sum_{n=0}^\infty b_n z^n &= (a_0 + a_1 z + a_2 z^2+\dotsb)(b_0 + b_1 z + b_2 z^2+\dotsb) \\
&=a_0 b_0 + (a_0 b_1 + a_1 b_0) z + (a_0 b_2 + a_1 b_1 + a_2 b_0) z^2 + \dotsb \\
&= c_0 + c_1 z+ c_2 z^2 + \dotsb
\end{aligned}
$$
Setting $z=1$, we arrive at the above definition.

### Example [收敛级数乘积不收敛的情况] (3.49)

If
$$
A_n = \sum _{k=0}^n a_k, \quad B_n = \sum_{k=0}^n b_k, \quad C_n = \sum_{k=0}^n c_k
$$
and $A_n \to A$, $B_n \to B$, then it is not at all clear that $\{C_n\}$ will converges to $AB$ since we do not have $C_n = A_nB_n$. The dependence of $\{C_n\}$ on $\{A_n\}$ and $\{B_n\}$ is quite a complicated one (see the proof of 【Theorem 3.50】). We shall now that the product of two convergent series may actually diverge.

The series
$$
\sum_{n=0}^\infty\frac{(-1)^n}{\sqrt{n+1}} = 1 - \frac{1}{\sqrt 2} + \frac{1}{\sqrt 3} -\frac{1}{\sqrt 4} + \dotsb
$$
And the product of this series with itself:
$$
\begin{aligned}
\sum_{n=0}^\infty c_n &= 1 - (\frac{1}{\sqrt 2}+\frac{1}{\sqrt 2}) + (\frac{1}{\sqrt 3}+\frac{1}{\sqrt 2 \sqrt 2}+\frac{1}{\sqrt 3})\\
&\quad - (\frac{1}{\sqrt 4}+ \frac{1}{\sqrt 3\sqrt 2} + \frac{1}{\sqrt 2\sqrt 3} + \frac{1}{\sqrt 4}) + \dotsb
\end{aligned}
$$
so that
$$
c_n = (-1)^n\sum_{k=0}^n\frac{1}{\sqrt{(n-k+1)(k+1)}}
$$
Since
$$
(n-k+1)(k+1) = (\frac{n}{2} + 1)^2 - (\frac{n}{2}-k)^2 \leq (\frac{n}{2}+1)^2
$$
we have
$$
|c_n|\geq \sum_{k=0}^n \frac{2}{n+2} = \frac{2(n+1)}{n+2} \to 2
$$
so that the condition $c_n\to 0$, which is necessary for the convergence of $\sum c_n$, is not satisfied.

### Theorem [含有绝对收敛的乘积收敛] (3.50)

Suppose

(a) $\sum_{n=0}^\infty a_n$ `converges absolutely`,

(b) $\sum_{n=0}^\infty a_n = A$,

(c) $\sum_{n=0}^\infty b_n = B$,

(d) $c_n = \sum_{k=0}^n a_k b_{n-k}\quad n=0,1,2,...$.
Then
$$
\sum_{n=0}^\infty c_n = AB
$$
That is, the product of two convengent series converges, and to the right value, if **at least one of the two series converges absolutely**.

**Proof.** 用分部求和公式和柯西控制即可

### Theorem [级数都收敛则乘积可一致] (3.51)

If the series $\sum a_n$, $\sum b_n$, $\sum c_n$ converge to $A$, $B$, $C$, and $c_n = a_0b_n+\dotsb +a_nb_0$, then $C=AB$.

**Note.** No need absolutely convenge for any seq.

## Rearrangements [重排列]

### Def. [重排列] (3.52)
Let $\{k_n\}$, $n=1,2,3,...$, be a sequnece in which every positive integer appears once and only once (that is, $\{k_n\}$ is a $1-1$ function from $J$ onto $J$, in the notation of 【Def. 2.2】). Putting
$$
a_n^\prime = a_{kn}\quad n=1,2,3,...
$$
we say that $\sum a_n^\prime$ is a `rearrangement` of $\sum a_n$

**Note.** If $\{s_n\}$, $\{s_n^\prime\}$ are the sequence of partial sums of $\sum a_n$, $\sum a_n^\prime$, it is easily seen that, in general, these two sequences consist of entirely different numbers. We are thus led to the problem of determining under what conditions all rearrangements of a convergent series will converge and whether the sums are necessarily the same.

### Example (3.53)
Consider the convergent series
$$
1-\frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \dotsb
$$
and one of its rearrangements
$$
1+\frac{1}{3} - \frac{1}{2} + \frac{1}{5} + \frac{1}{7} - \frac{1}{4} + \frac{1}{9}+\frac{1}{11}-\frac{1}{6}+\dotsb
$$
in which two positive terms are always followed by one negative. If $s$ is the sum of the first rearrangement, then
$$
s< 1-\frac{1}{2}+\frac{1}{3}=\frac{5}{6}
$$
Since
$$
\frac{1}{4k-3}+\frac{1}{4k-1}-\frac{1}{2k}>0
$$
for $k\geq 1$, we see that $s_3^\prime < s_6^\prime < s_9^\prime < \dotsb$, where $s_n^\prime$ is $n$th partial sum of the second rearrangement. Hence
$$
\limsup_{n\to\infty}s_n^\prime > s_3^\prime = \frac{5}{6}
$$
so that certainly does not converge to $s$ (but the first does, converge).

### Theorem [黎曼重排列定理] (3.54)

Let $\sum a_n$ be a series of real numbers which converges, but not absolutely. Suppose
$$
-\infty \leq \alpha \leq \beta \leq \infty
$$
Then there exists a rearrangement $\sum a_n^\prime$ with partial sums $s_n^\prime$ such that
$$
\liminf_{n\to\infty} s_n^\prime = \alpha, \quad \limsup_{n\to\infty} s_n^\prime = \beta
$$

**Note.** 这就是老师上课说的那个一生得一定理即可终生无憾的定理。黎曼重排列说明任何`非绝对收敛`级数都可以通过重排列使之收敛到`任意实数`。

**Proof.** 证明考察变换：
$$
p_n = \frac{|a_n|+a_n}{2}, \quad q_n = \frac{|a_n|-a_n}{2}\quad n=1,2,3,...
$$
其中 $p_n - q_n = a_n$，$p_n + q_n = |a_n|$，$p_n\geq 0$，$q_n \geq 0$。考察级数 $\sum p_n$ 和 $\sum q_n$ （都是发散）的重排列（使重排列收敛）即可。

### Theorem [绝对收敛级数的重排列不影响收敛值] (3.55)

If $\sum a_n$ is a series of complex numbers which `converges absolutely`, then every rearrangement of $\sum a_n$ converges, and they all converge to the same sum.

**Proof.** （柯西性，因为都是非负项，所以可以消除重复项，而剩余项的和依然具有柯西性）
Let $\sum a_n^\prime$ be a rearrangement, with partial sums $s_n^\prime$. Given $\varepsilon > 0$, there exists an integer $N$ such that $m \geq n\geq N$ implies
$$
\sum_{i=n}^m |a_i| \leq \varepsilon
$$
Now choose $p$ such that the integers $1,2,...,N$ are all contained in the set $k_1, k_2, ..., k_p$ (we use the notation of 【Def. 3.52 重排列】). Then if $n>p$, the numbers $a_1, ...,a_N$ will cancel in the difference $s_n - s_n^\prime$, so that $|s_n - s_n^\prime|\leq \varepsilon$, by this inequality above. Hence $\{s_n^\prime\}$ converges to same sum as $\{s_n\}$.

【小亦 2020-12-27 00:42】于深圳
