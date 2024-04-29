import argparse
import gEconpy as ge
import numpy as np
import pandas as pd
import os
from scipy import optimize
from scipy import stats
from functools import wraps
import gEconpy.plotting as gp
import matplotlib.pyplot as plt
import seaborn as sns
import json


def main():
    parser = argparse.ArgumentParser(description="Solve DSGE model")
    parser.add_argument("--mode", type=str, help="Model type")
    parser.add_argument("--experiment_number", type=float, help="Experiment")
    parser.add_argument("--eta", type=float, help="Importance of data")
    parser.add_argument("--kappa", type=float, help="Weight on private data")
    parser.add_argument("--x_f", type=float, help="Share of private data")
    parser.add_argument("--x_o", type=float, help="Share of public data")
    parser.add_argument("--sigma", type=float, help="Elasticity of substitution retail firm")
    args = parser.parse_args()

    #Create folder for each experiment
    exp_dir = os.path.join(os.getcwd(), f"{args.mode}_{args.experiment_number}")
    if not os.path.exists(exp_dir):
        os.makedirs(exp_dir)

    #Save txt file with parameters
    parameters = {
        'mode': args.mode,
        'experiment': args.experiment_number,
        'eta': args.eta,
        'kappa': args.kappa,
        'x_f': args.x_f,
        'x_o': args.x_o,
        'sigma': args.sigma
        }

    # Save the dictionary to a txt file using JSON
    with open(f'{exp_dir}/parameters.txt', 'w') as file:
        json.dump(parameters, file, indent=4)
    
    #Load model 
    file_path = f"GCN_Files/RBC_Lindquist_{args.mode}.gcn"
    mod = ge.gEconModel(file_path)

    #Set parameters
    if args.mode == "data_monopol-generic":
        mod.free_param_dict['eta'] = args.eta
        mod.free_param_dict['kappa'] = args.kappa
        mod.free_param_dict['x_f'] = args.x_f
        mod.free_param_dict['x_o'] = args.x_o
        mod.free_param_dict['sigma'] = args.sigma

    #Solve model
    from solver import solve_mod
    solve_mod(mod, args.mode, args.experiment_number, exp_dir)

    # Print policy matrix
    for name, policy_matrix in zip(["T", "R"], [mod.T, mod.R]):
        print(name.center(10).center(50, "="))
        print(policy_matrix.to_string())

    #Write policy matrix
    policy_dir = os.path.join(os.getcwd(), f"{exp_dir}/policy_m")
    if not os.path.exists(policy_dir):
        os.makedirs(policy_dir)

    T_df = pd.DataFrame(mod.T)
    R_df = pd.DataFrame(mod.R)
    T_df.to_csv(f'{policy_dir}/T_matrix_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.csv', index=True)
    R_df.to_csv(f'{policy_dir}/R_matrix_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.csv', index=True)

    # Check Blanchard Kahn Conditions
    mod.check_bk_condition()

    #Visualise model performance
    from viz_irfs import plot_irfs
    plot_irfs(mod, args, exp_dir)

    from viz_performance import plot_cov
    plot_cov(mod, args, exp_dir)

    #Write dynare file 
    dynare_dir = os.path.join(os.getcwd(), f"{exp_dir}/dynare")
    if not os.path.exists(dynare_dir):
        os.makedirs(dynare_dir)

    dynare = ge.make_mod_file(mod)
    file_path_mod = f"{dynare_dir}/lindquist_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.mod"

    with open(file_path_mod, 'w') as file:
        file.write(dynare)


if __name__ == "__main__":
    main()
