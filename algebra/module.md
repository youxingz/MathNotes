## Module

### Definition. Module $M$

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

