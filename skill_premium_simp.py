import sympy as sp
import numpy as np
import pandas as pd

#Variables
w_u, w_s, h_u, h_s, k_e, k_s, mcq, mcs, mcy, S, z, Q = sp.symbols('w_u w_s h_u h_s k_e k_s mcq mcs mcy S z Q')

#Parameters
s, u, lda, phi, mu, nu, N, x_o, k, x_f, eta, theta, sigma = sp.symbols('s u lda phi mu nu N x_o x_f k eta theta sigma', positive=True)

equation_Q = (S**nu * (1 - mu) + mu * (u * h_u)**nu)**(1/nu)
equation_S = (k_e**phi * lda + (s*h_s)**phi * (1-lda))**(1/phi)
equation_mcy = (sigma -1)/sigma *  N**(1/sigma-1)


equation_mcq = ((N * x_o * (1 - k) + k * x_f)**(eta / (1 - eta))** k_s**(theta / (1 - eta)) * (1 - theta) * z**(1 / (1 - eta)) * mcy * Q**((1 - theta) / (1 - eta) - 1)) / (1 - eta)

equation_mcq = equation_mcq.subs({mcy: equation_mcy, Q: equation_Q})


equation_mcs = (S**nu * (1-mu) + mu * (u*h_u)**nu)**((1/nu) -1) * (1-mu) * mcq * S**nu

equation_mcs = equation_mcs.subs({S: equation_S, mcq: equation_mcq})

# Equations for w_s and w_u
equation_ws = (u * h_u)**nu * mu * mcq * (S**nu * (1-mu) + mu * (u * h_u)**nu)**(1/nu -1) / (u * h_u)
equation_wu = (1 - lda) * (s * h_s)**phi * mcs * (k_e**phi * lda + (s*h_s)**phi * (1-lda))**(1/phi -1) / (s * h_s)


#Substitutions
equation_ws = equation_ws.subs({mcq: equation_mcq, S: equation_S})
equation_wu = equation_wu.subs({mcs: equation_mcs})


#Calculation of skill premium
skill_p = w_s/w_u

skill_p_s = skill_p.subs({w_u: equation_wu, w_s: equation_ws})

#Simplification
simplified_sp = sp.simplify(skill_p_s)
print(simplified_sp)

