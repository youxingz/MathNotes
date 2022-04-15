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

Let $M,N,L$ be $R$-modules.

1. A map $\varphi: M\to N$ is an $R$-homomorphism if and only if $\varphi(rx+y)=r\varphi(x)+\varphi(y)$ for all $x,y\in M, r\in R$.
   
2. [加法和数乘] Let $\varphi,\psi \in Hom_R(M,N)$, define $\varphi+\psi$ by $(\varphi+\psi)(m)=\varphi(m)+\psi(m)$ for all $m\in M$. Then $\varphi+\psi\in Hom_R(M,N)$ and $Hom_R(M,N)$ is an additive abelian group. If $R$ is commutative, then $\forall r\in R$, define $r\varphi$ by $(r\varphi)(m)=r(\varphi(m))$ for all $m\in M$. Then $r\varphi\in Hom_R(M,N)$ and $Hom_R(M,N)$ is an $R$-module.

3. [乘法] If $\varphi \in Hom_R(L,M)$ and $\psi\in Hom_R(M,N)$, then $\psi\varphi \in Hom_R(L,N)$.

4. With addition and multiplication defined as above (2,3), $Hom_R(M,M)$ is a ring with $1$. When $R$ is commutative, $Hom_R(M,M)$ is an $R$-algebra.

### Def. Endomorphism

Define the endomorphism ring of $M$ as $End(M)=End_R(M)=Hom_R(M,M)$. (Remark: $End(M)$ is a ring, proved by above (4).)

When $R$ is commutative, there is a natural map from $R$ into $End(M)$ given by $r\mapsto rI$, which endomorphism of $M$ is just multiplication by $r$ on $M$.

The image of $R$ is contained in the center of $End(M)$ so if $R$ has identity, $End(M)$ becomes an $R$-algebra.

The ring homomorphism from $R$ to $End(M)$ may not be injective since for some $r$ we may have $rm=0$ for all $m\in M$. (e.g., $R=\Z$, $M=\Z/2\Z$, $r=2$, then $rm=0, \forall m\in M$, hence not injective.)

When $R$ is a field, the ring map is injective. And the copy of $R$ in $End(M)$ is called the (subring of) scalar transformations.

### 'Normal' Sense

Every submodule $N$ of an $R$-module $M$ is "normal" in the sense that we can always form the quotient module $M/N$, and the natural projection $\pi: M\to M/N$ is an $R$-module homomorphism with $Ker(\pi)=N$.

Idea: Since a module is an abelian group, then every submodule is automatically a normal subgroup; Same for module homomorphism, any homomorphism is a homomorphism of abelian groups.

We then rest need to check that the action of $R$ is compatible with these group quotients and homomorphisms. That is:
  1. $M$ is an $R$-module (no need check)
  2. $M/N$ is an $R$-module
  3. $\pi$ is a module homomorphism ($\pi(x+y)=\pi(x)+\pi(y)$ is no need to check, since it is already a group homomorphism, we then only need to check (b) i.e., $r\pi(x)=\pi(rx)$.)

### Prop 3.

Let $R$ be a ring, $M$ be an $R$-module and $N$ be a submodule of $M$. The (additive, abelian) quotient group $M/N$ can be made into an $R$-module by defining an action of elements of $R$ by
$$
r(x+N)=(rx)+N, \text{ for all } r\in R, x+N \in M/N
$$

The natural projection map $\pi: M\to M/N$ defined by $\pi(x)=x+N$ is an $R$-module homomorphism with kernel $N$.

Proof. Since $M$ is an abelian group under $+$, the quotient group $M/N$ is defined and is an abelian group.

To see the action of the ring element $r$ on the coset $x+N$ is well defined: suppose $x+N=y+N$, then $x-y\in N$, since $N$ is a (left) $R$-submodule, then $r(x-y)\in N$, thus $rx-ry\in N \implies rx+N = ry +N$, hence well defined.

Since the operations in $M/N$ are "compatible" with those of $M$, the axioms for an $R$-module are easily checked in the same way as was done for quotient groups. For example, axiom 2(b) holds since: for all $r_1,r_2\in R$, $x+N\in M/N$, by the definition of the action of ring elements on elements of $M/N$ (:: $R$ act on $M/N$), we have $(r_1r_2)(x+N)=(r_1r_2x)+N=r_1(r_2x+N)=r_1(r_2(x+N))$.

Finally, the natural projection map $\pi$ is the natural projection of the abelian group $M$ onto the abelian group $M/N$. Hence is a group homomorphism with kernel $N$. The kernel of any module homomorphism is the same as its kernel when viewed as a homomorphism of the abelian group structures. Then we only need to show $\pi$ is a module homomorphism, i.e., $\pi(rm) = r\pi(m)$. Since $\pi(rm)=rm+N(\text{by def.})=r(m+N)=r\pi(m)$, this completes the proof.

Remark: All the isomorphism theorems stated for groups also hold for $R$-modules. The proofs can be like: begin by invoking the corresponding theorem for groups and then prove that the group homomorphisms are also $R$-module homomorphisms.

To state the Second Isomorphism Theorem, we need the following:

### Def. [Sum]
Let $A,B$ be submodules of the $R$-module $M$. The `sum` of $A$ and $B$ is the set
$$
A+B = \{a+b\ |\ a\in A, b\in B\}
$$

Remark: The sum of two submodules $A$ and $B$ is a submodule, and is the smallest submodule contains both $A$ and $B$.

### Theorem [Isomorphism Theorems]

1. (The First Isomorphism Theorem for Modules) Let $M,N$ be $R$-modules and $\varphi: M\to N$ be an $R$-module homomorphism. Then $Ker(\varphi)$ is a submodule of $M$, and $M/Ker(\varphi) \cong \varphi(M)$.
2. (The Second Isomorphism Theorem) Let $A,B$ be submodules of the $R$-module $M$, then $(A+B)/B\cong A/(A\cap B)$.
3. (The Third Isomorphism Theorem) Let $M$ be an $R$-module, and $A,B$ submodules of $M$ with $A\subseteq B$. Then $(M/A)/(B/A)\cong M/B$.
4. (The Fourth or Lattice Isomorphism Theorem) Let $N$ be a submodule of the $R$-module $M$. There is a bijection between submodules of $M$ which contains $N$ and the submodules $M/N$. The correspondence is given by $A \leftrightarrow A/N$ for all $A\supseteq N$. The correspondence commutes with the processes of taking sums and intersections (i.e., is a lattice isomorphism between the lattice of submodules of $M/N$ and the lattice of submodules of $M$ which contains $N$).

