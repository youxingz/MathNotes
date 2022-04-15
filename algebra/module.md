## Module

### Definition. Module $M$

把 $R$-module 理解为：对一个对象 $M$，是否可用环 $R$ 来操作（action），如果有这个办法（homomorphism），就可以将 $M$ 当作一个 $R$-module.

比如：任意交换群都是 $\Z$-module. 因为整数作用到交换群 $G$ 内的元素可以用 $ng=g+g+\cdots+g$ (n times) 表示（这种乘法可以理解为一种环作用），其明显满足 module 的 4 条公理。

Let $R$ be a ring. A *left $R$-module* or a *left module over $R$* is a set $M$ together with

1) a binary operation $+$ on $M$ under which $M$ is an abelian group.
2) an action of $R$ on $M$ (i.e. a map $R\times M \to M$) denoted by $rm$, for all $r\in R$ and $m\in M$ satisfies
   1) $(r+s)m = rm + sm$
   2) $(rs)m = r(sm)$
   3) $r(m+n)=rm+rn$
   4) $1m=m$, if ring $R$ has a $1$.

Note: *modules over a field $F$ and vector spaces over $F$ are the same*.

### Example 1

1) Let $R$ be a ring, $M=R$ is a left $R$-module. In particular, every field can be considered as a (1-dimensional) vector space over itself. When $M=R$, the submodules of $R$ are the left ideals of $R$ (respect right-xx).

2) Let $R=F$ be a field. Then every vector space over $F$ is an $F$-module and vice versa. Let $n\in \Z^+$ and $F^n = \{(a_1,a_2,\cdots,a_n)|a_i\in F\}$ (called `affine n-space` over $F$). Define the componentwise addition and scalar multiplcation, then affine $n$-space is a vector space of dimension $n$ over $F$.

3) Following Example 2, let $R$ be a ring with $1$, define $R^n=\{(a_1,a_2,\cdots,a_n)| a_i\in R\}$, define the componentwise addition and scalar multiplcation, then we call the module $R^n$ *the free module of rank $n$ over $R$*.

4) If $M$ is an $R$-module, and $S$ is a subring of $R$ with $1_S = 1_R$, then $M$ is automatically an $S$-module as well. Example: the field $\R$ is a $\R$-module, a $\mathbb Q$-module, and a $\Z$-module.

5) If $M$ is an $R$-module and for some ideal $I$ of $R$, $am=0$ for **all** $a\in I$, $m\in M$, we say $M$ is `annihilated` by $I$. In this situation, we can make $M$ into an $(R/I)$-module by defining an action of the quotient ring $R/I$ on $M$ as follows: for each $m\in M$ and coset $r+I\in R/I$, let $(r+I)m = rm$. In particular, when $I$ is a maximal ideal in the commutative ring $R$ and $IM=0$, then $M$ is a vector space over the field $R/I$. (If $I$ is maximal ideal, then $R/I$ is a field).

### Example 2 ($\Z$-module)

Every abelian group is a $\Z$-module. $\Z$-modules are the same as abelian groups.

Proof. Let $R=\Z$, $A$ be any abelian group (finite or infinite) and write the operation of $A$ as $+$. Make $A$ into a $\Z$-module as follows: for any $n\in \Z$ and $a\in A$ define:
$$
na=\left\{
  \begin{aligned}
  &a+a+\cdots+a,\ (n \text{ times}), & \text{ if } n>0\\
  &0  & \text{ if } n = 0 \\
  &-a-a-\cdots-a, (-n \text{ times}), & \text{ if } n< 0
  \end{aligned}\right.
$$
which $0$ is the additive identity of group $A$.

This definition makes $A$ into a $\Z$-module, and the module axioms show that this is the only possible action of $\Z$ on $A$ makeing it a (unital) $\Z$-module.

Note: For a cyclic group $\langle a\rangle$, such addition is multiplication, and $na$ is $a^n$.

Note: If $A$ is an abelian group containing an element $x$ of finite order $n$ then $nx=0$. Then a $\Z$-module may have nonzero elements $x$ s.t. $nx=0$ for some nonzero ring element $n$. Then $A$ is a module over $\Z/m\Z$.

Note: If $p$ is a prime, and $A$ is a abelian group s.t. $px=0$, for all $x\in A$. Then $A$ is a $\Z/p\Z$-module. Since $\Z_p \cong \Z/p\Z$ is a field, then $A$ can be considered as a vector space over field $\Z_p$.


### Example 3 ($F[x]$-module)

Let $F$ be a field, let $x$ be an indeterminate and let $R$ be the polynomial ring $F[x]$. Let $V$ be a vector space over $F$ and $T$ a linear transformation from $V$ to $V$ itself. (Obviously, $V$ is $F$-module) The linear map $T$ will enable us to make $V$ into an $F[x]$-module.

First, define $T^0=I$, $T^n=TT\cdots TT$ (n times), where $I$ is identity map in $Hom(V,V)$.

And, define $(\alpha A + \beta B)(v) = \alpha(A(v))+\beta(B(v))$, where $A,B\in Hom(V,V)$ and $\alpha,\beta\in F$.

Then $\alpha A + \beta B$ is easily seen to be a linear transformation in $Hom(V,V)$, so that linear combinations of linear transformations are again linear transformations.

We now define the action of any polynomial in $x$ on $V$.

Let $p(x)$ be the polynomial $p(x)=\sum_{i=0}^n a_ix^i$, where $a_i\in F$. For each $v\in V$, we define an action of the ring element $p(x)$ on the module element $v$ by
$$
p(x)v = (\sum_{i=0}^n a_i T^i)(v) =  \sum_{i=0}^n (a_i T^i v)
$$

($x$ acts on $V$ as the linear transformation $T$, we extend this to an action of $F[x]$ on $V$ in a natural way.) Is is easy to check this definition of an action of $F[x]$ on $V$ makes $V$ into an $F[x]$-module.

The field $F$ is naturally a subring of $F[x]$ ($F$ is the constant polynomials), and the action of these field elements is same as their action when viewed $F$ as constant polynomials. Hence, the definition of $F[x]$ extends the action of $F$ to an action of the larger ring $F[x]$.

The way $F[x]$ acts on $V$ depends on the choice of $T$ so that there are many different $F[x]$-module structures on the same vector space $V$. Example: 

1) if $T=0$, then $p(x)v = a_0 v$, that is, the polynomial $p(x)$ acts on $v$ simply by multiplying by the constant term of $p(x)$, so that $F[x]$-module structure is just the $F$-module structure.
   
2) if $T=I$, then $p(x)v=\sum_{i=0}^n (a_i v) = (\sum_{i=0}^n a_i) v$, so that $p(x)$ mutipiles $v$ by the sum of the coefficients of $p(x)$.

3) if $T$ is the `shift operator`, i.e. $T(x_1,x_2,\cdots,x_n) = (x_2,x_3,\cdots,x_n, 0)$. Let $e_i$ be the usual $i^{th}$ basis vector $(0,0,\cdots,0,1,0,\cdots,0,0)$. Then $T^k(e_i) = e_{i-k}$ if $i>k$, otherwise $T^k(e_i) = 0$. Hence $(\sum_{i=0}^m a_i x^i)e_n = (0,\cdots,0, a_m, a_{m-1},\cdots,a_0)$ for $m<n$.

The construction of an $F[x]$-module from a vector space $V$ over $F$ and a linear transformation $T$ in $Hom(V,V)$ in fact describes all $F[x]$-modules. Another words, an $F[x]$-module is a vector space together with a linear transformation which specifies the action of $x$.


## ---

An abelian group $M$ may have many different $R$-module structures, even if the ring $R$ does not vary. We shall see that the structure of an $R$-module is reflected by the ideal structure of $R$. When $R$ is a field, all $R$-modules will be seen to be products of copies of $R$ (i.e. $R^n$).

### Prop 1. The Submodule Criterion

Let $R$ be a ring and $M$ be an $R$-module. A subset $N\subseteq M$ is a submodule of $M$ if and only if 1) $N\neq \varnothing$, and 2) $x+ry\in N$ for all $x,y\in N, r\in R$.

### Def. $R$-Algebra

Let $R$ be a commutative ring with identity. An $R$-algebra is a ring $A$ with identity together with a ring homomorphism $f: R\to A$ mapping $1_R$ to $1_A$ s.t. the subring $f(R)$ of $A$ is contained in the center of $A$.

### Def. $R$-Algebra morphism

Let $A$ and $B$ are two $R$-algebras, and $R$-algebra homomorphism (or isomorphism) is a ring homomorphism (or isomorphism) $\varphi : A\to B$ mapping $1_A$ to $1_B$ s.t. $\varphi(ra)=r\varphi(a)$ for all $r\in R$ and $a\in A$.

### Examples

Let $R$ be a commutative ring with identity 1.

1. Any ring with identity is a $\Z$-algebra.
2. Any ring $A$ with identity, if $R$ is a subring of the center of $A$ containing the identity of $A$, then $A$ is an $R$-algebra. (If $A$ is commutative, then $A$ is $R$-algebra for any subring $R$ of $A$ containing $1$). Examples: The polynomial ring $R[x]$ is an $R$-algebra; the polynomial ring over $R$ in many variables is an $R$-algebra; the group ring $RG$ for a finite group $G$ is an $R$-algebra.
3. If $A$ is an $R$-algebra then the $R$-module structure of $A$ depends only on the subring $f(R)$ contained in the center of $A$ (like above 2.). If we replace $R$ by its image $f(R)$ we see that "up to a ring homomorphism" every algebra $A$ arises from subring of the center of $A$ that contaings $1_A$.
4. Continue from 3., if $R=F$ is a field, then $F$ is isomorphic to its image $f(F)$, so we can identify $F$ itself as a subring of $A$. Hence, saying $A$ is an algebra over a field $F$ is the same as saying the ring $A$ contains the field $F$ in its center and share same identity of $A$ and $F$.

Suppose $A$ is an $R$-algebra, then $A$ is a ring with $1$. Which satisfying $r(ab)=(ra)b=a(rb)$ for all $r\in R, a,b\in A$.

Conversely, these conditions on a ring $A$ define an $R$-algebra. (Sometimes used as the definition of an $R$-algebra)

