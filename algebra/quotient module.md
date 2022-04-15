## Quotient Modules & Module Homomorphisms

### Def. [Homomorphism, Isomorphism]

Let $R$ be a ring and $M,N$ be $R$-modules.

1) A map $\varphi:M\to N$ is an $R$-module homomorphism if it respects the $R$-module structures of $M$ and $N$, i.e.,
   
   a) $\varphi(x+y) = \varphi(x) + \varphi(y)$, for all $x,y \in M$

   b) $\varphi(rx)=r\varphi(x)$, for all $r\in R, x\in M$.

2) An $R$-module homomorphism is an isomorphism (of $R$-module) if it is both injective and surjective. The modules $M$ and $N$ are said to be isomorphic (denoted $M\cong N$) if there is some $R$-module isomorphism $\varphi: M\to N$.
   
3) If $\varphi: M\to N$ is an $R$-module homomorphism, denote: $Ker(\varphi) := \{m\in M | \varphi(m)=0\}$, $Im(\varphi)=\varphi(M)=\{n\in N | n = \varphi(m) \text{ for some }m\in M\}$.

4) Let $M,N$ be $R$-modules and define $Hom_R(M,N)$ to be the set of all $R$-module homomorphisms from $M$ to $N$.

Remark: Any homomorphism in $Hom_R(M,N)$ is a homomorhpism of the additive groups, but converse is not always true (since (b) may not satisfied).

Kernel and Image of a $R$-module are submodules.

### Examples

1. $R$ is a ring and $M=R$, is a module over itself. Then $R$-module homomorphisms need not be ring homomorphisms and ring homomorphisms need not be $R$-module homomorphisms. (彼此互不依赖). For example, 
   
   1. when $R=\Z$ the $\Z$-module homomorphism $x\mapsto 2x$ is not a ring homomorphism ($1$ does not map to $1$).

   2. when $R=F[x]$ the ring homomorphism $\varphi: f(x) \mapsto f(x^2)$ is not an $F[x]$-module homomorphism (if it were, we would have $x^2=\varphi(x)=\varphi(x\cdot 1) = x\varphi(1)=x$). 
   
  mark: For 1.2, 这个证明有问题，再研究研究 ring homomorphism: (Recall: $f(x)=\sum a_i x^i$, $f(x^2)=\sum a_i x^{2i}$, then $\varphi(f(x))=f(x^2)\implies r\varphi(f(x))=rf(x^2) = r\sum a_i x^{2i} = \sum a_i rx^{2i} \neq \sum a_i (rx)^{2i} = f(rx^2)$, is not $F[x]$-module homomorphism; but $\varphi(f(x) + f(y)) = \varphi(\sum a_ix^i + \sum a_i y^i) = \varphi(\sum a_i(x^i+y^i)) =\varphi(f(x+y))= f(x^2) + f(y^2)=\varphi(f(x)) + \varphi(f(y))$, hence it is an ring homomorphism.)

2. Let $R$ be a ring, $n\in \Z^+$ and $M=R^n$. For each $i$, the `projection map` $\pi_i:R^n\to R$ by $\pi_i(x_1,\cdots,x_n)=x_i$ is a surjective map ($R$-module homomorphism) with kernel equal to the submodule of $n$-tuples which have a zero in position $i$, i.e. $Ker(\pi_i)=\{(x_1,\cdots,x_{i-1},0,x_{i+1},\cdots, x_n) | (...) \in R^n\}$.

3. If $R$ is a field, $R$-module homomorphism are called `linear transformations`.

4. For ring $R=\Z$, the action of ring elements (integers) on any $\Z$-module amounts to just adding and subtracting within the (additive) abelian group structure of the module so that in this case condition (b) of a homomorphism is implied by (a). For example, $\varphi(2x)=\varphi(x+x)=\varphi(x)+\varphi(x)=2\varphi(x)$. It follows that: $\Z$-module homomorphisms are the same as abelian group homomorphisms. // (Consider abelian additive group $V=(n_i)$ with basis $(\log p_i)$, then <$\Z,V$> is an $\Z$-module ($(\Z,V)\to V$) and we only need check (a).)

5. Let $R$ be a ring, $I$ be a 2-sided ideal of $R$ and suppose $M$ and $N$ are $R$-modules annihilated by $I$ (i.e., $am=0$ and $an=0$ for all $a\in I$, $m\in M$, $n\in N$). Any $R$-module homomorphism from $N$ to $M$ is then automatically a homomorphism of $R/I$-modules. In particular, if $A$ is an additive abelian group s.t. for some prime $p$, $px=0$ for all $x\in A$, then any group homomorphism from $A$ to $A$ itself is a $\Z/p\Z$-module homomorphism, i.e., is a linear transformation over the field $\mathbb F_p$. In particular, the group of all (group) automorphisms of $A$ is the group of invertible linear transformations from $A$ to $A$ itself: $GL(A)$. (of $R$-module 的，自动变成 of $R/I$-module 的 homomorphism，想象 Ann 是一个等价关系，做商后把所有的 $R$ 中的元素归类，且使得 0 映射到 0，故单射，即 homomorphism.)

### Prop 2.