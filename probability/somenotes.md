$$
\begin{aligned}
&\quad\quad \sum_{r=1}^n \frac{1}{r} = \log n + \gamma + \varepsilon_n \\
&\Rightarrow
n \sum_{r=1}^n \frac{1}{r} =n \log n + n\gamma + n\varepsilon_n \sim p
\end{aligned}
$$

### 随机游走

可以用于醉汉行走、股价模拟等。

【随机游走】在初始位置 $x_0$ 处，随机走第 $i$ 步，每步长度 $X_i$，且每步都独立。
Let $E(x_i) = \mu$, $Var(X_i) = \sigma^2$, $S(n)= x_0 + \sum_{i=1}^n X_i$, then we have
$$
\begin{aligned}
E(S(n)) &= E(x_0+\sum_{i=1}^n X_i)\\
&=E(x_0) + E(\sum_{i=1}^n X_i)\\
&=x_0 + \sum_{i=1}^n E(X_i) \\
&=x_0 + \sum_{i=1}^n \mu \\
&=x_0 + n\mu \\
\end{aligned}
$$
$$
\begin{aligned}
Var(S(n)) &= Var(x_0+\sum_{i=1}^n X_i)\\
&=Var(\sum_{i=1}^n X_i)\\
&=\sum_{i=1}^n Var(X_i) \\
&=\sum_{i=1}^n \sigma^2 \\
&=n\sigma^2 \\
\end{aligned}
$$

### 蒙特卡洛积分方法 (Monte Carlo Method)
计算
$$
I(f) = \int_0^1 f(x) dx
$$
一般初等方法是无法求解这个积分的，只能通过数值办法求解。这里提供蒙特卡洛方法。

考虑大数定律，有
$$
\hat I(f) = {1\over n}\sum_{i=1}^n f(X_i) = E(f(X))
$$
且知道
$$
E(f(X)) = \int_0^1 f(x) dx = I(f(x))
$$
所以
$$
I(f(x)) =  \hat I(f(x))
$$
总结一下：当大数定律成立的条件满足时，可以通过蒙特卡洛方法求得近似的数值解。
（见《数理统计与数据分析》P124/例5.2.1）
