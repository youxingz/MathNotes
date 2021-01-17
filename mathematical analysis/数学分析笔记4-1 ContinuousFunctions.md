# CONTINUITY [连续性]

终于引入函数的概念了！
函数由三部分决定：映射关系、值域、定义域。通常表示为：
$$X\xrightarrow{f}Y$$ 
或者：
$$f: X \to Y$$
本章主要讨论赋距空间下的函数性质。

## Limits of Functions [函数的极限]

### Def. [函数的极限] (4.1)
Condition of the `limits of function` $f$:
$$
\begin{aligned}
X &\supset E\xrightarrow{f} Y \\
x\to p&\in E^\prime\quad [d_X(x,p)< \delta]\\
f(x)\to q&\in Y \quad [d_Y(f(x), q)< \varepsilon]
\end{aligned}
$$
More precisely:

Let $X$ and $Y$ be metric space; suppose $E\subset X$, $f$ maps $E$ into $Y$, and $p$ is a limit point of $E$. We write $f(x)\to q$ as $x\to p$, or
$$
\lim_{x\to p}f(x) = q
$$
if there is a point $q\in Y$ with the following property: For every $\varepsilon>0$ there exists a $\delta > 0$ such that
$$
d_Y(f(x), q) < \varepsilon
$$
for all points $x\in E$ for which
$$
0 < d_X(x, p) < \delta
$$
The symbols $d_X$ and $d_Y$ refer to the distances in $X$ and $Y$, respectively.

### Theorem [函数极限的序列表述] (4.2)
Let $X$, $Y$, $E$, $f$ and $p$ be as in 【Definition 4.1】. Then
$$
\begin{equation}
\lim_{x\to p} f(x) = q
\end{equation}
$$
if and only if
$$
\begin{equation}
\lim_{n\to\infty}f(p_n) = q
\end{equation}
$$
for every sequence $\{p_n\}$ in $E$ such that
$$
p_n \neq p, \quad\lim_{n\to\infty}p_n = p
$$

**Proof.** "$\Longrightarrow$":
Suppose (1) holds. Choose $\{p_n\}$ in $E$ satisfying (3). Let $\varepsilon > 0$ be given. Then there exists $\delta > 0$ such that $d_Y(f(x), q)< \varepsilon$ if $x\in E$ and $0< d_X(x,p)<\delta$. Also, there exists $N$ such that $n>N$ implies $0< d_X(p_n,p)<\delta$. Thus, for $n>N$, we have $d_Y(f(p_n), q)< \varepsilon$, which shows that (2) holds.

"$\Longleftarrow$": Conversely, suppose (2) is false. Then there exists some $\varepsilon > 0$ such that for every $\delta>0$ there exists a point $x\in E$ (depending on $\delta$), for which $d_Y(f(x), q)\geq \varepsilon$ but $0< d_X(x,p)<\delta$. Taking $\delta_n = \frac{1}{n}, n=1,2,3,...$, we thus find a sequence in $E$ satisfying (3) for which (2) is false.

("$\Longrightarrow$" 简述) Suppose (1) holds. $\{p_n\} \subset E$.

Then $\forall \varepsilon > 0$, $\exists \delta > 0$, s.t. $[0< d_X(x,p)<\delta,\ x\in E]$ $\Longrightarrow$ $[d_Y(f(x), q)<\varepsilon]$.

Also for such fixed $\delta$, $\exists\ N\in \mathbb N$, s.t. $[n>N]$ $\Longrightarrow$ $[0< d_X(p_n,p)<\delta]$. 

Combine such two, we have $\forall \varepsilon>0$, $\exists N\in \mathbb N$, s.t. $[n>N]$ $\Longrightarrow$ $[d_Y(f(p_n), q) < \varepsilon]$.

### Corollary (4.2)
If $f$ has a limit at $p$, this limit is unique.

### Theorem [$\mathbb R^k$ 中函数的代数运算] (4.3)
If $\mathbf f$ and $\mathbf g$ map $E$ into $\mathbb R^k$, we define $\mathbf f + \mathbf g$ and $\mathbf f \cdot \mathbf g$ by
$$
(\mathbf f + \mathbf g)(x) = \mathbf f(x) + \mathbf g(x), \quad (\mathbf f\cdot \mathbf g)(x) = \mathbf f(x) \cdot \mathbf g(x)
$$
and if $\lambda$ is a real number, $(\lambda\mathbf f)(x) = \lambda \mathbf f(x)$.

### Theorem [复数函数的代数运算] (4.4)
Suppose $E\subset X$, a metric space, $p$ is a limit point of $E$, $f$ and $g$ are `complex functions` on $E$, and
$$
\lim_{x\to p}f(x) = A, \quad \lim_{x\to p}g(x) = B
$$
Then

(a) $\lim\limits_{x\to p}(f+g)(x) = A+B$;

(b) $\lim\limits_{x\to p}(fg)(x) = AB$;

(c) $\lim\limits_{x\to p}(\frac{f}{g})(x)=\frac{A}{B}$, if $B\neq 0$.

### Remark (4.4)
If $\mathbf f$ and $\mathbf g$ map $E$ into $\mathbb R^k$, then (a) remains true, and (b) becomes (b') $\lim\limits_{x\to p}(\mathbf f \cdot \mathbf g)(x)=\mathbf A \cdot \mathbf B$.

## Continuous Functions [连续函数]

### Def. [连续函数] (4.5)
Suppose $X$ and $Y$ are metric spaces, $E\subset X$, $p\in E$, and $f$ maps $E$ into $Y$. Then $f$ is said to be `continuous` at $p$ if for every $\varepsilon > 0$ there exists a $\delta > 0$ such that
$$
d_Y(f(x),f(p))< \varepsilon
$$
for all points $x\in E$ for which $d_X(x,p)< \delta$.

**Note.** 简述定义：$f$ is `continous`: For $x,p\in E$, $X\supset E\xrightarrow{f}Y$. Then $\forall \varepsilon>0$, $\exists \delta > 0$, s.t. $[d_X(x,p)<\delta]$ $\Longrightarrow$ $[d_Y(f(x),f(p))<\varepsilon]$.

### Theorem [连续函数的等价叙述] (4.6)
In the situation given in 【Def. 4.5】, assume also that $p$ is a limit point of $E$. Then $f$ is `continous` at $p$ if and only if $\lim_{x\to p}f(x) = f(p)$

### Theorem [连续函数复合依然连续] (4.7)
Suppose $X$, $Y$, $Z$ are metric spaces, $E\subset X$, $f$ maps $E$ into $Y$, $g$ maps the range of $f$, $f(E)\subset Y$, into $Z$, and $h$ is the mapping of $E$ into $Z$ defined by
$$
h(x) = g(f(x))\quad x\in E
$$
If $f$ is contiunous at a point $p\in E$ and if $g$ is continuous at the point $f(p)$, then $h$ is continuous at $p$.

This function $h$ is called the `composition` or the `composite` of $f$ and $g$. The notation
$$
h = g\circ f
$$
is frequently used in this context.

**Proof.**
Let $\varepsilon>0$ be given. Since $g$ is continuous at $f(p)$, there exists $\eta > 0$ such that
$$
d_Z(g(y), g(f(p))) < \varepsilon\ \text{if}\ d_Y(y, f(p))< \eta\ \text{and}\ y\in f(E)
$$
Since $f$ is continuous at $p$, there exists $\delta > 0$ such that
$$
d_Y(f(x), f(p)) < \eta\ \text{if}\ d_X(x,p)< \delta \ \text{and}\ x\in E
$$
It follows that
$$
d_Z(h(x), h(p)) = d_Z(g(f(x)), g(f(p))) < \varepsilon
$$
if $d_X(x,p)<\delta$ and $x\in E$. Thus $h$ is continuous at $p$.

### Theorem [连续函数的逆映射函数] (4.8)
[逆映射将开集映入开集 $\Longleftrightarrow$ 函数连续]，这个定理十分十分十分重要且好用，特别是证明连续性的时候，只需要证明函数的逆映射把开集映射为开集就行。
$$
X\supset E_{(open)}\xrightleftharpoons[f^{-1}]{f} V_{(open)}\subset Y
$$
A mapping $f$ of a metric space $X$ into a metric space $Y$ is continuous on $X$ if and only if $f^{-1}(V)$ is open in $X$ for every open set $V\subset Y$.

**Proof.** "$\Rightarrow$": Suppose $f$ is continuous on $X$ and $V$ is an open set in $Y$. We have to show that every point of $f^{-1}(V)$ is an interior point of $f^{-1}(V)$.

So, suppose $p\in X$ and $f(p)\in V$. Since $V$ is open, there exists $\varepsilon > 0$ such that $y\in V$ if $d_Y(f(p), y)<\varepsilon$, and since $f$ is continuous at $p$, there exists $\delta > 0$ such that $d_Y(f(x),f(p))< \varepsilon$ if $d_X(x,p)<\delta$. Thus $x\in f^{-1}(V)$ as soon as $d_X(x,p)< \delta$.

"$\Leftarrow$": Conversely, suppose $f^{-1}(V)$ is open in $X$ for every open set $V$ in $Y$.

Fix $p\in X$ and $\varepsilon>0$, let $V$ be the set of all $y\in Y$ such that $d_Y(y,f(p))< \varepsilon$. Then $V$ is open; hence $f^{-1}(V)$ is open; hence there exists $\delta>0$ such that $x\in f^{-1}(V)$ as soon as $d_X(p,x)< \delta$. But if $x\in f^{-1}(V)$, then $f(x)\in V$, so that $d_Y(f(x),f(p))<\varepsilon$.

This complete the proof.


### Corollary (4.8)

A mapping $f$ of a metric space $X$ into a metric space $Y$ is continuous if and only if $f^{-1}(C)$ is closed in $X$ for every closed set $C$ in $Y$.

**Note.** Consider the complement is open, since $f^{-1}(E^c) = [f^{-1}(E)]^c$ for every $E\subset Y$.

### Theorem [代数运算保连续性] (4.9)
Let $f$ and $g$ be complex continuous functions on a metric space $X$. Then $f+g$, $fg$, and $\frac{f}{g}$ are continuous on $X$.

**Proof.** At limit points, the statement follows 【Theorem 4.4】 and 【Theorem 4.6】.

### Theorem [向量函数的连续性] (4.10)

(a) Let $f_1, ..., f_k$ be real functions on a metric space $X$, and let $\mathbf f$ be the mapping of $X$ into $\mathbb R^k$ defined by
$$
\mathbf f(x) = < f_1(x), ..., f_k(x) > \quad x\in X
$$
then $\mathbf f$ is continuous if and only if each of the functions $f_1, ..., f_k$ is continuous.

(b) If $\mathbf f$ and $\mathbf g$ are continuous mappings of $X$ into $\mathbb R^k$, then $\mathbf f + \mathbf g$ and $\mathbf f\cdot \mathbf g$ are continuous on $X$.

The functions $f_1, ..., f_k$ are called the `components` of $\mathbf f$. Note that $\mathbf f + \mathbf g$ is a mapping into $R^k$, whereas $\mathbf f \cdot \mathbf g$ is a real function on $X$.

**Proof.** Part (a) follows from the inequalities
$$
|f_j(x) - f_j(y)|\leq |\mathbf f(x) - \mathbf f(y)| = \sqrt{\sum_{i=1}^k|f_i(x)-f_i(y)|^2}
$$
（分距离不大于总距离）

for $j=1,...,k$. Part (b) follows from (a) and 【Theorem 4.9】.

### Remark

我们定义了赋距空间的子集的函数映射，但余集不起作用，所以之后会不谈子集的映射，而直接谈赋距空间的映射，这样可以简化很多定理的描述。


【小亦 2020-12-27 03:12】于深圳
