# Use Flowchart or Programming (you can choose any language) to determine
# integration of 𝑓(𝑥) = 𝑥^2 + 2𝑥 on interval [1, 3]. If you use program/coding, the
# program must show the graph as an illustration of this problem.

import sympy as solver  # BUAT INTEGRALNYA
import matplotlib.pyplot as plotter  # BUAT GRAPHNYA
import numpy as solverpt2  # BUAT LINSPACE DOANG ANJAYYY

x = solver.Symbol("x")  # bikin x
f = x**2 + 2 * x  # fungsi integralnya

result = solver.integrate(f, (x, 1, 3))  # integralnya

x_val = solverpt2.linspace(0, 4, 500)  # bikin x buat graph dari 0 sampai 4

f_function = solver.lambdify(x, f)  # bikin fungsi integralnya jadi function

y_val = f_function(x_val)  # bikin nilai y pake fungsi x

integralText = r"$\int_1^3 (x^2 + 2x) \, dx = $" + str(
    result
)  # teks integral (gapaham formattingya jir)
plotter.text(
    min(x_val) * 1.75, max(y_val) * 0.75, integralText
)  # naro teks integral di graph

plotter.plot(x_val, y_val, color="blue")  # garis kurva untuk graphnya
plotter.fill_between(x_val, y_val, color="gray", alpha=0.2)  # warnain seluruh area
plotter.fill_between(
    x_val, y_val, where=(x_val >= 1) & (x_val <= 3), color="gray"
)  # warnain area integral 1-3

# plotter.grid(True) #tadinya mau kasih grid tpi jadi rame jadi gak jadi
plotter.xlabel("x")  # teks utk bagian bawah nandain X
plotter.ylabel("f(x)")  # teks bagian samping buat y yaitu f(X)
plotter.show()  # nampilin graphnya

# SEKIAN TERIMAKASIH
