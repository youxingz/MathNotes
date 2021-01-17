# 数学分析【定义定理整理】

## Compact 紧集

### Def. [开覆盖 Open Cover] (2.31)

**By an `open cover` of a set $E$ in a metric space $X$ we mean a collection $\{G\}$ of open subsets of $X$ such that $E\subset \cup_\alpha G_\alpha$.**

### Def. [紧致 Compact] (2.32)

**A subset $K$ of a metric space $X$ is said to be `compact` if every open cover of $K$ contains a *finite* subcover.**

**More explicitly, if $\{G_\alpha\}$ is an open cover of $K$, then there are `finitely many indices` $\alpha_1,\alpha_2,\alpha_3,...,\alpha_n$ such that**
$$
K\subset G_{\alpha_1}\cup\dotsb\cap G_{\alpha_n}
$$

### Theorem [紧致集合的保局部性质] (2.33)

**Suppose $K\subset Y\subset X$. Then $K$ is `compact relative to` $X$ if and only if $K$ is `compact relative to` $Y$.**

**Thinking.** 利用紧致性的定义，寻找一组在 $X$ 中的有限开集 $V_\alpha$，证明这组开集就是在 $Y$ 中的 $K$ 的开覆盖；反之在 $Y$ 中的有限开集可做 $K$ 在 $X$ 中的开覆盖。

核心点在于 $X$ 中的开集 $G_\alpha$ 如何与 $Y$ 中的开集 $V_\alpha$ 建立联系（令 $V_\alpha = Y \cap G_\alpha$ 即可），让这两者交替担任 $K$ 的 “开覆盖”，达到传递作用。

**Proof.** "$\Rightarrow$": Suppose $K$ is compact relative to $X$, we will show that $K$ is also compact relative to $Y$.

Let $\{V_\alpha\}$ be a collection of sets, open relative to $Y$, such that $K\subset \cup_\alpha V_\alpha$.

By【Theorem 2.30 降临定理】, there are sets $G_\alpha$, open relative to $X$, such that $V_\alpha = Y \cap G_\alpha$, for all index $\alpha$.

Since $K$ is compact relative to $X$ (By suppose), we have
$$
K\subset G_{\alpha_1}\cup\dotsb\cup G_{\alpha_n}
$$

for some choice of finitely many indices $\alpha_1,\alpha_2,\alpha_3,...,\alpha_n$.

Since $[K\subset Y, K\subset G_\alpha]$ $\Rightarrow$ $[K \subset Y\cap G_\alpha = V_\alpha]$, impiles
$$
K\subset V_{\alpha_1}\cup\dotsb\cup V_{\alpha_n}
$$
This proves that $K$ is compact relative to $Y$.

"$\Leftarrow$": 【逆流而上倒着写一遍即可】Suppose $K$ is compact relative to $Y$, let $\{G_\alpha\}$ be a collection of open subsets of $X$ which covers $K$, and put $V_\alpha=Y\cap G_\alpha$. Then $K\subset V_{\alpha_1}\cup\dotsb\cup V_{\alpha_n}$ for some choice of $\alpha_1,\alpha_2,\alpha_3,...,\alpha_n$; and since $V_\alpha\subset G_\alpha$, then $K\subset G_{\alpha_1}\cup\dotsb\cup G_{\alpha_n}$. That means $K$ is compact relative to $X$.

This completes the proof.

#### Figure:

![](https://imgkr2.cn-bj.ufileos.com/cf9147be-3e43-409a-b742-9638c3b46ddf.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=Qy6A2buG9ayGRCBcLsOTDdKLZmo%253D&Expires=1608716447)

### Theorem [紧集必然是闭集] (2.34)

**`Compact subsets` of metric space are `closed`.**

**Thinking.** 闭性不好搞，用补集的开性来证。

**Proof.** Let $K$ be a compact subset of a metric space $X$. We shall prove that the complement of $K$ is an open subset of $X$.

Suppose $p\in X$, $p\notin K$. if $q\in K$, let $V(p)$ and $W(q)$ be neighborhoods of $p$ and $q$, the radius less than $\frac{1}{2}d(p,q)$.

Since $K$ is compact, there are finitely many points $q_1, q_2, ... , q_n$ in $K$ such that
$$
K\subset W(q_1) \cup \dotsb \cup W(q_n) = W(q)
$$

Let $V(p)=\cap_i^n V_{q_i}(p_i)$, then $V(p)$ is a neighborhood of $p$ which does not intersect $W(q)$. Hence $V(p)\subset K^c$, so that $p$ is an interior point of $K^c$, then $K^c$ is open.

### Theorem [紧集的闭子集为紧集] (2.35)

**`Closed subsets` of `compact` sets are `compact`.**

**Thinking.** 为 $K$ 的闭子集 $F$ 找一组开覆盖 $\{V_\alpha\}$，如果指标 $\alpha$ 为有限个，则闭子集 $F$ 为紧集。考虑 $\{V_\alpha\} + F^c$ 为 $K$ 的开覆盖，则必为有限覆盖，则 $\{V_\alpha\}$ 有有限个指标，得证。

**Proof.** Suppose $F\subset K\subset X$, $F$ is closed (relative to $X$), and $K$ is compact. Let $\{V_\alpha\}$ be an open cover of $F$. If $F^c$ is adjoined to $\{V_\alpha\}$ (concat $F^c$ into $\{V_\alpha\}$, named $\Omega$), we obtain an open cover $\Omega$ of $K$. Since $K$ is compact, there is a finite subcollection $\Phi$ of $\Omega$ which covers $K$, and hence $F$. If $F^c$ is a member of $\Omega$, we may remove it from $\Omega$ and still retain an open cover of $F$. We have thus shown that a finite subcollection of $\{V_\alpha\}$ covers $F$.

### Corollary [闭集与紧集的交为紧] (2.35)

**If $F$ is `closed` and $K$ is `compact`, then $F\cap K$ is `compact`.**

**Proof.** 【Theorem 2.24(b) 极限点的定义】 and 【Theorem 2.34 紧集必然是闭集】 show that $F\cap K$ is closed; since $F\cap K \subset K$, 【Theorem 2.35 紧集的闭子集为紧集】shows that $F\cap K$ is compact.

### Theorem [紧集的有限任意交非空则无限交也非空] (2.36)

**If $\{K_\alpha\}$ is a collection of `compact subsets` of a metric space $X$ such that the intersection of every finite subcollection of $\{K_\alpha\}$ is nonempty, then $\cap K_\alpha$ is nonempty.**

**Thinking.** 逆否命题，假设无限交为空（没有点在交集中），则固定其中一个紧集 $K_1$，其余紧集的补集形成它的开覆盖，因为开覆盖有限个，所以其余紧集的补集为有限个，且交为空（已知），则有限交为空，得证。

**Proof.** （逆否命题）Fix a member $K_1$ of $\{K_\alpha\}$ and put $G_\alpha = K_\alpha^c$. Assume that no point of $K_1$ belongs to every $K_\alpha$. 

(***Why this suppose hold?*** The sets $G_\alpha$ form **an** open cover of $K_1$($K_1\subset G_\alpha = K_\alpha^c$); and since $K_1$ is compact, there are finitely many indices $\alpha_1, ...,\alpha_n$ such that $K\subset G_{\alpha_1}\cup\dotsb\cup G_{\alpha_n}$. It holds for such condition.)

This means that
$$
K_1 \cap K_{\alpha_1} \cap \dotsb \cap K_{\alpha_n}
$$
is empty. So in contradiction to our hypothesis.

### Corollary [紧集套 K-Cells] (2.36)

If $\{K_n\}$ is a sequence of nonempty compact sets such that $K_n\supset K_{n+1}$, $n=1,2,3,...$, then $\cap_1^\infty K_n$ is not empty.

### Theorem [紧集中的无限子集有极限点] (2.37)

**If $E$ is an `infinite subset` of a compact set $K$, then $E$ has a `limit point` in $K$.**

**Note.** 这个很重要，后面很多分析的地方都会用到

**Thinking.** （反证法）假设 $E$ 中没有极限点（各个都是孤立点，$q\in K$, $q\in E \Rightarrow$ $q\in V(q)\cap E$，$V(q)$ 只包含 $q$ 这一个点），则 $\{V_0^\infty(q_i)\}\supset E$，$\{V(q_i)\}$ 形成一组开覆盖，则$\{V(q_i)\}+ E^c$ 可成为 $K$ 的一组开覆盖，但 $K$ 是紧的，所以开覆盖是有限覆盖，则与假设矛盾（假设中 $V(q_i)$ 是无限个，因为 $q_i\in E$ 是无限个）。

**Proof.** If no point of $K$ were a limit point of $E$, then each $q\in K$ would have a neighborhood $V(q)$ which contains at most one point of $E$ (namely, $q$, if $q\in E$). It is clear that no finite subcollection of $\{V(q)\}$ can cover $E$; and the same is true of $K$, since $E\subset K$. This contradicts the compactness of $K$.

### Theorem [区间套交集非空] (2.38)

If $\{I_n\}$ is a sequence of `intervals` in $\mathbb{R}^1$, such that $I_n \supset I_{n+1}$, $n=1,2,3,...$, then $\cap_1^\infty I_n$ is not empty.

**Thinking.** 交完的区间愈来愈小，最终会成为一个点（如果无限交的话），区间 $E$ 的上确界有限交则是 $x=maxE$，无限交则是 $x = supE$，但无论如何都是不空的。

**Proof.** If $I_n = [a_n, b_n]$, let $E$ be the set of all $a_n$. Then $E$ is nonempty and bounded above (by $b_1$). Let $x$ be the sup of $E$. If $m$ and $n$ are positive integers, then
$$
a_n \leq a_{m+n} \leq b_{m+n} \leq b_m
$$
so that $x\leq b_m$ for each $m$. Since it is obvious that $a_m\leq x$, we see that $x\in I_m$ for $m=1,2,3,...$.

#### Figure
![](https://imgkr2.cn-bj.ufileos.com/2d658504-faa8-4fe9-9d4e-2135ccc66f11.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=PGsCff0uE1lWWGVLmoa7bfa00Ug%253D&Expires=1608732482)

### Theorem [K-Cell 的交集非空] (2.39)

**Let $k$ be a positive integer. If $\{I_n\}$ is a sequence of `k-cells` such that $I_n\supset I_{n+1}$, $n=1,2,3,...$, then $\cap_1^\infty I_n$ is not empty.**

**Thinking.** 这是区间套定理在赋距空间下的推广，对每一维度单独利用定理【Theorem 2.38】进行证明，然后得到一个 $k$ 维的点即可证明非空。

**Proof.** Let $I_n$ consist of all points $x=< x_1, x_2, ..., x_k>$ such that
$$
a_{n,j} \leq x_j \leq b_{n,j}
$$
for all $1\leq j \leq k; n = 1,2,3,...$.

And put $I_{n,j} = [a_{n,j},b_{n,j}]$. For each j, the sequence $\{I_{n,j}\}$ satisfies the hypotheses of 【Theorem 2.38】. Hence there are real numbers $x_j^\star$ ($1\leq j\leq k$) such that
$$
a_{n,j}\leq x_j^\star \leq b_{n,j}
$$
for all $1\leq j \leq k; n = 1,2,3,...$.

Setting $\boldsymbol{x^\star}=< x_1^\star,...,x_n^\star>$, we see that $\boldsymbol{x^\star}\in I_n$ for $n=1,2,3,...$. The theorem follows.

### Theorem [K-Cell 必紧] (2.40)

**Every k-cell is compact**

**Proof.** Let $I$ be a k-cell, sonsisting of all points $\boldsymbol{x}=< x_1,...,x_k>$, such that $a_j\leq x_j\leq b_j$. Put
$$
\delta=distance(\boldsymbol{a}, \boldsymbol{b}) = \{\sum_1^k (a_j-b_j)^2\}^\frac{1}{2}
$$
Then $|\boldsymbol{x}-\boldsymbol{y}|\leq \delta$, if $\boldsymbol{x},\boldsymbol{y}\in I$.

Suppose, to get a contradiction, that there exists an open cover $\{G_\alpha\}$ of $I$ which contains no finite subcover of $I$. Put $c_j = (a_j+b_j)/2$. The intervals $[a_j, c_j]$ and $[c_j, b_j]$ then determine $2^k$ k-cells $Q_i$ whose union is $I$. At least one of these sets $Q_i$, call it $I_1$, cannot be covered by any finite subcollection of $\{G_\alpha\}$ (otherwise $I$ could be so covered). We next subdivide $I_1$ and continue the process. We obtain a sequence $\{I_n\}$ with the following properties:

(a) $I\supset I_1\supset I_2\supset I_3\supset\dotsb$;

(b) $I_n$ is not covered by any finite subcollection of $\{G_\alpha\}$;

(c) if $\boldsymbol{x}\in I_n$ and $\boldsymbol{y}\in I_n$, then $|\boldsymbol{x}-\boldsymbol{y}|\leq \frac{1}{2}^{n}\delta$.

By (a) and 【Theorem 2.39】, there is a point $\boldsymbol{x^\star}$ which lies in every $I_n$. For some $\alpha, \boldsymbol{x^\star}\in G_\alpha$. Since $G_\alpha$ is open, there exists $r>0$ such that $|\boldsymbol{y}-\boldsymbol{x^\star}|< r$ implies that $\boldsymbol{y}\in G_\alpha$. If $n$ is so large that $\frac{1}{2}^{n}\delta < r$ (there is such an $n$, for otherwise $2^{n}\leq \delta/r$ for all positive integers $n$, which is absurd since $\mathbb{R}$ is archimedean), then (c) implies that $I_n \subset G_\alpha$, which contradicts (b).

This completes the proof.

### Theorem [海涅博雷尔定理 Heine Borel] (2.41)

**If a set $E$ in $\mathbb{R}^k$ has one of the following three properties, then it has the other two:**

**(a) $E$ is `closed` and `bounded`;**

**(b) $E$ is `compact`;**

**(c) Every `infinite subset` of $E$ has a `limit point` in $E$.**

**Note.** 这个可重要了，这就是著名的海涅博雷尔定理啊啊啊啊啊啊！

值得注意的是，在任意赋距空间里，(b) 和 (c)  都是等价的，但 (a) 在一般情况并不能推出 (b) 和 (c) 来（在欧式空间 $\mathbb{R}^k$ 中可以）。

**Thinking.** (a)是闭有界性 (b)是紧性 (c)是无限子集必有极限点的性质【Theorem 2.37】
我们只需要循环证明即可，证明链为：(a)$\Rightarrow$(b)$\Rightarrow$(c)$\Rightarrow$(a)

**Proof.**

If (a) holds, then $E\subset I$ for some k-cell $I$, and (b) follows from 【Theorem 2.40, 2.35】. 【Theorem 2.37】shows that (b) implies (c). It remains to be shown that (c) implies (a).

"(c)$\Rightarrow$(a)": （反证法）

First, for bounded: If $E$ is not bounded, then $E$ contains points $\boldsymbol{x}_n$ with
$$
|\boldsymbol{x}_n|>n,\quad n=1,2,3,...
$$
The set $S$ consisting of these points $\boldsymbol{x}_n$ is infinite and clearly has no limit point in $\mathbb{R}^k$, hence has none in $E$. Thus (c) implies that $E$ is bounded.

Next, for closed: If $E$ is not closed, the there is a point $\boldsymbol{x}_0 \in \mathbb{R}^k$ which is a limit point of $E$ but not a point of $E$. For $n=1,2,3,...$, there are points $\boldsymbol{x}_n\in E$ such that $|\boldsymbol{x}_n - \boldsymbol{x}_0|< \frac{1}{n}$. Let $S$ be the set of these points $\boldsymbol{x}_n$. Then $S$ is infinite (otherwise $|\boldsymbol{x}_n - \boldsymbol{x}_0|$ would have a constant positive value, for infinitely many $n$), $S$ has $\boldsymbol{x}_0$ as a limit point, and $S$ has no other limit point in $\mathbb{R}^k$. For if $\boldsymbol{y}\in \mathbb{R}^k, \boldsymbol{y}\neq \boldsymbol{x}$, then
$$
\begin{aligned}
|\boldsymbol{x}_n - \boldsymbol{y}| &\geq |\boldsymbol{x}_0 - \boldsymbol{y}| - |\boldsymbol{x}_n - \boldsymbol{x}_0| \\
&\geq|\boldsymbol{x}_0 - \boldsymbol{y}| - \frac{1}{n} \\
&\geq \frac{1}{2}|\boldsymbol{x}_0 - \boldsymbol{y}|
\end{aligned}
$$
for all but finitely many $n$; this shows that $y$ is not a limit point of $S$ (【Theorem 2.20】).

Thus $S$ has no limit point in $E$; hence $E$ must be closed if (c) holds.

### Theorem [Weierstrass 定理] (2.42)

**Every `bounded` `infinite subset` of $\mathbb{R}^k$ has a `limit point` in $\mathbb{R}^k$.**

**Proof.** Being bounded, the set $E$ in question is a subset of a k-cell $I\subset \mathbb{R}^k$. By【Theorem 2.40】, $I$ is compact, and so $E$ has a limit point in $I$, by【theorem 2.37】.

【小亦 2020-12-22 23:22】于深圳