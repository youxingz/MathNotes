## Cauchy-Riemann Equation

If $f$ is holomorphic, we write $z=x+iy$, and $f(z) = u(x,y) + iv(x,y)$, then
$$
{\partial u \over \partial x} = {\partial v \over \partial y}\quad\quad {\partial u \over \partial y} = -{\partial v \over \partial x}
$$

**Proof**

$$
\begin{align}
{\partial f \over \partial x} &= {\partial u \over \partial x} + {\partial iv \over \partial x} = {\partial u \over \partial x} + i{\partial v \over \partial x}\\
{\partial f \over \partial iy} &= {\partial u \over \partial iy} + {\partial iv \over \partial iy} = -i{\partial u \over \partial y} + {\partial v \over \partial y}
\end{align}
$$
since ${\partial f \over \partial x} = {\partial f \over \partial iy}$, we have
$$
{\partial u \over \partial x} = {\partial v \over \partial y}\quad \text{and} \quad {\partial u \over \partial y} = -{\partial v \over \partial x}
$$

