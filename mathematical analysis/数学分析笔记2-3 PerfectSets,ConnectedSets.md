## Perfect Sets

### Def. [完全性 Perfect] (2.18.h)

**$E$ is `perfect` if $E$ is closed and if every point of $E$ is a limit point of $E$.**

**Note.** 对比闭集的定义：$E$ is `closed` if every limit point of $E$ is a point of $E$. 和完全集的定义：$E$ is `perfect` if $E$ is closed and if every point of $E$ is a limit point of $E$.

则，完全集的定义可以描述为：
$E$ is `perfect` if every limit point of $E$ is a point of $E$, and every point of $E$ is a limit point of $E$.（即极限点是集合上的点，集合上的点也是极限点）

#### Theorem [完全集不可数] (2.43)

**Let $P$ be a `nonempty` `perfect` set in $\mathbb{R}^k$. Then $P$ is `uncountable`.**

**Proof.** Since $P$ has limit points, $P$ must be infinite. Suppose $P$ is countable, and denote the points of $P$ by $\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3,...$. We shall construct a sequence $\{V_n\}$ of neighborhoods, as follows.

Let $V_1$ be any neighborhood of $\mathbf x_1$. If $V_1$ consists of all $\mathbf y \in \mathbb R^k$ such that $|\mathbf y - \mathbf x_1|< r$, the closure $\overline V_1$ of $V_1$ is the set of all $\mathbf y \in \mathbb R^k$ such that $|\mathbf y - \mathbf x_1|< r$.

Suppose $V_n$ has been constructed, so that $V_n\cap P$ is not empty. Since every point of $P$ is a limit point of $P$, there is a neighborhood $V_{n+1}$ such that (i) $\overline V_{n+1} \subset V_n$, (ii) $\mathbf x_n \notin \overline V_{n+1}$, (iii) $V_{n+1}\cap P$ is not empty. By (iii), $V_{n+1}$ satisfies our induction hypothesis, and the construction can proceed.

Put $K_n=\overline V_n \cap P$. Since $\overline V_n$ is closed and bounded, $\overline V_n$ is compact. Since $\mathbf x_n \notin K_{n+1}$, no point of $P$ lies in $\cap_1^\infty K_n$. Since $K_n \subset P$, this implies that $\cap_1^\infty K_n$ is empty. But each $K_n$ is nonempty, by (iii), and $K_n \supset K_{n+1}$, by (i),; this contradicts the 【Corollary 2.36】.

### Corollary [闭区间不可数] (2.43)

**Every `interval` $[a,b]$ $(a< b)$ is `uncountable`. In particular, the set of all real numbers is uncountable.**

### Remark [康托集 Cantor Set] (2.44)
The set which we are now going to construct shows that there exist perfect sets in $\mathbb R^1$ which contain no segment (open interval).（测度为0，但不可数）

**Note.** 非重点，故此处不给详细的证明了，只给出构造方法。

**Construct.** Let $E_0$ be the interval $[0,1]$. Remove the segment $(\frac{1}{3}, \frac{2}{3})$, and let $E_1$ be the union of the intervals: $[0,\frac{1}{3}] \cup [\frac{2}{3}, 1]$.

Remove the middle thirds of these intervals, and let $E_2$ be the union of the intervals: $[0, \frac{1}{9}] \cup [\frac{2}{9}, \frac{3}{9}]\cup [\frac{6}{9}, \frac{7}{9}]\cup [\frac{8}{9}, 1]$.

Continuing in this way, we obtain a sequence of compact sets $E_n$, such that

(a) $E_1\supset E_2\supset E_3\supset \dotsb$;

(b) $E_n$ is the union of $2^n$ intervals, each of length $\frac{1}{3}^n$.

The set
$$
P=\bigcap_{n=1}^\infty E_n
$$

is called the Contor set. $P$ is clearly compact, and 【Theorem 2.36】 shows that $P$ is not empty. Also $P$ is perfect and contains no segment.


## Connected Sets

### Def. [分离集] (2.45)

Two subsets $A$ and $B$ of a metric space $X$ are said to be `separated` if both $A\cap \bar B$ and $\bar A cap B$ are empty, i.e., if no point of $A$ lies in the closure of $B$ and no point of $B$ lies in the closure of $A$.

#### Figure

![](https://imgkr2.cn-bj.ufileos.com/986ef7f2-c366-4427-a52c-b337fb14dee5.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=1f8Am%252Bz%252FqGUNmMnGinNOTvUGObo%253D&Expires=1608743576)


### Def. [连通集] (2.45)

A set $E\subset X$ is said to be `connected` if $E$ is *not* a union of two nonempty separated sets.

#### Figure


![](https://imgkr2.cn-bj.ufileos.com/a22409d9-2b7f-4aa6-b16a-c41487f878e5.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=yfRog6Dak2Aow067bjSqdryyDtM%253D&Expires=1608744112)


### Remark [分离和不交的关系] (2.46)

Separated sets are of course disjoint, but disjoint sets need not be separated. For example, the interval $[0,1]$ and the segment $(1,2)$ are not separated, since $1$ is a limit point of $(1,2)$. However, the segments $(0,1)$ and $(1,2)$ are separated.

The connected subsets of the line have a particularly simple structure:

### Theorem [实轴下的连通集的序的特点] (2.47)

A subset $E$ of the real line $\mathbb R^1$ is connected if and only if it has the following property: If $x\in E$, $y\in E$, and $x< z< y$, then $z\in E$.

**Thinking.** （反证法）假设区间内的点 $z$ 不在 $E$ 中，根据连通性找出矛盾。反之亦然，证明 $z\notin E$ 来得出矛盾。

**Proof.** "$\Rightarrow$": If there exists $x\in E$, $y\in E$, and some $z\in (x,y)$ such that $z\notin E$, then $E=A_z\cup B_z$ where
$$
A_z = E\cap (-\infty, z),\quad B=E\cap (z,+\infty)
$$
Since $x\in A_z$ and $y\in B_z$, $A$ and $B$ are nonempty. Since $A_z \subset (-\infty, z)$ and $B_z \subset (z,+\infty)$, they are separated. Hence $E$ is not connected. (矛盾)

"$\Leftarrow$": To prove the converse, suppose $E$ is not connected. Then there are nonempty separated sets $A$ and $B$ such that $A\cup B = E$. Pick $x\in A$, $y\in B$, and asssume (without loss of generality) that $x< y$. Define
$$
z=sup(A\cap [x,y])
$$

By 【Theorem 2.28】, $z\in \bar A$; hence $z\notin B$. In particular, $x\leq z < y$.

If $z\notin A$, it follows that $x< z< y$ and $z\notin E$.

If $z\in A$, then $z\notin \bar B$, hence exists $z_1$ such that $z< z_1< y$ and $z_1 \notin B$. Then $x< z_1 < y$ and $z_1 \notin E$.



本章由于并非常考点，故简单记录，不做特别补充。

【小亦 2020-12-23 00:55】于深圳
