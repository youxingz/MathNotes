# Review

## Holomorphic functions
3 ways to describe:
* complex diff. $f^\prime (z) = \lim_{x\to 0} {f(z+x) - f(z) \over x}$
  - CR Equation. (${\partial u \over \partial x} = ...$)
* local analystic: to be a power series.
  - 洛朗展开
* satisfy Cauchy Integral Formula. [考试：至少两题]
  - singularity? point / pole
  - residue formula.
  - primitive func / path integral, Coursat's thm.

properties:
* holomorphic diff.
  - locally uniform convergence. (if on any complex subset the f converges to some subset.)
* max/min modules princeple
* open mapping thm. on an open set.
* Riemann extension thm.
* holo func is a mapping.
  - the Schwatz lemma.
  - the Riemann mapping thm.

special properties:
* holomorphic factorx thm.
* Gamma function
* Zeta function [考试不会出现]

## Examples

$$
\int_0^{2\pi} \log |1-ae^{i\theta}| d\theta = 0,\ |a| \lt 1
$$
$$
\int_0^{2\pi} \log |1-e^{i\theta}| d\theta = 0
$$
for the image circle: holo func 圆周上平均值为圆心的值
$$
{1\over 2\pi} \int_0^{2\pi} g(e^{i\theta}) d\theta \\
= 
{1\over 2\pi i} \int_{|z|=1} {g(z) \over z} dz = g(0)
$$
处理实值函数的积分：基本都是将其代数化
for 1, let $z=ae^{i\theta}$; for 2, let $z=e^{i\theta}$, and consider for:
$$???
\int_0^{2\pi} \log |1-e^{i\theta}| d\theta\\
= \int_{|z|=1} {1\over 2i}\log(1-z) {dz\over z} - \int_{|\bar z|=1} {1\over 2i}\log(1-\bar z) {d\bar z\over z} \\
= \int_{|z|=1} ...
$$
(Note: ${d\bar z \over dz} = -{dz\over z}$)

从真正问题的结构来解决问题，而非暴力计算。


## Example Ex14
f: entire func, f injective then $f(z) = az+b, a\neq 0$ (线性)

[Proof] consider $f({1\over z})$, and some cases of xx?
