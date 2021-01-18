
## Important Integral Example
Calculate this complex integral:
$$
\int_C {dz\over (z-a)^n}
$$

**Solution**

Let $z = re^{i\theta}$, then
$$
\begin{aligned}
\int_C {dz\over (z-a)^n} &= \int_C {dre^{i\theta} \over (re^{i\theta}-a)^n}\\
&=\int_0^{2\pi} {ire^{i\theta}d\theta \over r^ne^{in\theta}}\\
&={i\over r^{n-1}} \int_0^{2\pi} e^{i(1-n)\theta}d\theta\\
\end{aligned}
$$
If $n = 1$, we have
$$
{i\over r^{n-1}} \int_0^{2\pi} e^{i(1-n)\theta}d\theta = {i\over 1} \int_0^{2\pi} 1 d\theta = 2\pi i
$$
If $n\neq 1$, we have
$$
\begin{aligned}
{i\over r^{n-1}} \int_0^{2\pi} e^{i(1-n)\theta}d\theta &= {i\over r^{n-1}} \left. {1\over i(1-n)}e^{i(1-n)\theta} \right| _0^{2\pi} \\
&= {i\over r^{n-1}} {1\over i(1-n)} [e^{i(1-n)2\pi} - e^{i(1-n)0}] \\
&= {i\over r^{n-1}} {1\over i(1-n)} [1 - 1] \\
&= 0
\end{aligned}
$$

So we have:

$$
\int_C {dz\over (z-a)^n} =
\begin{cases}{}
2\pi i, &n=1\\
0, &n\neq 1, &n\ is\ integer
\end{cases}
$$
