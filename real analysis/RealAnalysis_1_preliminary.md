# Introduction 【为什么要这些新理论】

实分析是对微积分的抽象，引入更一般的方法来进行微分积分，使得我们对微积分理论的刻画更加清晰。以下是作者 stein 简要介绍的几个方面我们所遇到的问题，以至于我们不得不迫切地希望能有新的理论来完善微积分原本的缺陷，使微积分理论进一步发展。而勒贝格在1900s年代完善了测度论，算是很好的解决了这一系列问题。

## Fourier series: completion 【傅立叶级数】

Whenever $f$ is (Riemann) integrable function on $[-\pi, \pi]$, we define the Fourier series $f\sim \sum a_n e^{inx}$ by
$$
a_n = {1\over2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}dx
$$
and we saw that one had Parseval’s identity:
$$
\sum_{n=-\infty}^{\infty}|a_n|^2 = {1\over2\pi}\int_{-\pi}^{\pi}|f(x)|^2dx
$$

However, the above relationship between functions and their Fourier coeﬃcients is not completely reciprocal when limited to Riemann integrable functions. 所以我们需要引入新的更广义的理论去重新描述可积的意义。

## Limit of continuous functions 【连续函数列的极限问题】

Suppose $\{f_n\}$ is a sequence of continuous functions on $[0,1]$. We assume that $\lim_{n\to\infty}f_n(x) = f(x)$ exists $\forall x$, and inquire as to the nature of the limiting function $f$.

If we suppose the convergence is uniform, and then $f$ is continuous everywhere. But, once we drop this assumption (uniformly convergence), things may change radically and the issues that arise can be quite subtle...

Example:

Let $\{f_n\}$ be a sequence of continuous functions and converging everywhere to $f$. and

(a) $0\leq f_n(x) \leq 1$ for all $x$.

(b) The sequence is montonically decrasing as $n\to\infty$.

(c) The limit function $f$ is not Riemann integrable.

Then, from (a) (b), the sequence $\int_0^1 f_n(x) dx$ converges to a limit. So it is natural to ask: What method of integration can be used to integrate $f$ s.t.
$$
\int_0^1 f(x) dx = \lim_{n\to\infty}\int_0^1 f_n(x) dx
$$

所以在黎曼可积性质不满足的时候，能否引入勒贝格测度来积这个函数是我们需要进一步研究的问题。

## Length of curves 【曲线长度问题】

Consider a continuous curve $\Gamma$ in the plane, given parametrically by $\Gamma=\{(x(t),y(t)) | a\leq t\leq b\}$, where $x,y$ are continuous functions of $t$. We define the `length` of $\Gamma$:

We say $\Gamma$ is `rectiﬁable` if its length is finite, and we have
$$
L=\int_a^b \sqrt{(x^\prime(t))^2+(y^\prime(t))^2} dt
$$

But, we can ask:

(a) What are the conditions on the functions $x(t)$ and $y(t)$ that guarantee the rectiﬁability of $\Gamma$?

(b) When (a) satisfied, does the formula above hold?

The first question is about `bounded-variation`, the second is about if (a) satisfied, then is the integral always meaningful? However, it fails usually. Then we need to find another way to consider these curve problem.

## Diﬀerentiation and integration 【微积分的问题】

The `Fundamental Theorem of Calculus` states:
$$
\begin{aligned}
F(b)-F(a) &= \int_a^b F^\prime(x)dx \\
{d\over dx} \int_0^x f(y) dy &= f(x)
\end{aligned}
$$
For the ﬁrst assertion, the existence of continuous functions F that are nowhere diﬀerentiable, or for which $F^\prime$ exists for every $x$, but $F^\prime$ is not integrable, then 我们需要怎么办才能使上面的式子成立？

## The problem of Measure 【测量(测度)的问题】

We need to find a non-negative function on the family of $E\subset \R$ $m$, s.t.

(a) $m(E)=b-a$, if $E$ is the interval $[a,b]$, $a\leq b$, of length $b-a$.

(b) 【countable additivity】$m(E)=\sum_{n=1}^\infty m(E_n)$ whenever $E=\bigcup_{n=1}^\infty E_n$ with the sets $E_n$ are disjoint.

And, easily, we have:

(b) implies: $m(E_1 \cup E_2) = m(E_1) + m(E_2)$ if $E_1$ and $E_2$ are disjoint.

(a) + (b) implies: $m(E+h)=m(E)$, for every $h\in\R$.

构造出这样的函数来刻画测量是我们接下来的主线任务。



2021-12-09/Thu
深圳
