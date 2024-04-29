import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import gEconpy.plotting as gp
import seaborn as sns

def plot_cov(mod, args, folder):

    figures_dir = os.path.join(os.getcwd(), f"{folder}/figures")
    if not os.path.exists(figures_dir):
        os.makedirs(figures_dir)
        
    #Plot Eigenvalues
    gp.plot_eigenvalues(mod)
    plt.savefig(f"{figures_dir}/eigenvalues_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf")


    sigma = mod.compute_stationary_covariance_matrix()
    acorr_matrix = mod.compute_autocorrelation_matrix(n_lags=30)

    #Calculate correlation matrix
    std_devs = np.sqrt(np.diag(sigma))
    std_dev_matrix = np.outer(std_devs, std_devs)
    correlation_matrix = sigma / std_dev_matrix
    print(correlation_matrix)


    if args.mode == "original":
        #Plot covariance matrix
        gp.plot_covariance_matrix(
            sigma,
            ["Y", "K", "C", "I", "H", "r_e", "r_s", "w_s", "w_u", "skill_p"],
            figsize=(5, 5),
            cbar_kw=dict(shrink=0.5),
        )
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{args.figure}/covariance_matrix_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf")

        #Plot correlation matrix
        variables = ["Y", "K", "C", "I", "H", "r_e", "r_s", "w_s", "w_u", "skill_p", "c_u", "c_s", "h_s", "h_u", "I_e", "I_s", "rel_hours",
        "equip_skill"]
        correlation_matrix = correlation_matrix.loc[variables, variables]
        plt.figure(figsize=(10, 8))  # Adjust the size as needed
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm',
                    xticklabels=variables, yticklabels=variables, cbar_kws={'shrink': 0.5})
        plt.title('Correlation Matrix Heatmap')
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/correlation_matrix_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf")

    else:
        #Plot covariance matrix
        gp.plot_covariance_matrix(
            sigma,
            ["Y_j", "K", "C", "I", "H", "r_e", "r_s", "w_s", "w_u", "skill_p"],
            figsize=(5, 5),
            cbar_kw=dict(shrink=0.5),
        )
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/covariance_matrix_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf")

        #Plot correlation matrix
        variables = ["Y_j", "K", "C", "I", "H", "r_e", "r_s", "w_s", "w_u", "skill_p", "c_u", "c_s", "h_s", "h_u", "I_e", "I_s", "rel_hours",
        "equip_skill"]
        correlation_matrix = correlation_matrix.loc[variables, variables]
        plt.figure(figsize=(10, 8))  
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm',
                    xticklabels=variables, yticklabels=variables, cbar_kws={'shrink': 0.5})
        plt.title('Correlation Matrix Heatmap')
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/correlation_matrix_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf")
    

    if args.mode == "original":
        #Plot autocorrelation matrix
        gp.plot_acf(acorr_matrix, vars_to_plot=["Y", "K", "C", "I", "H", "r_e", "r_s", "w_s", "w_u", "skill_p"], n_cols=3)
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/autocovariance_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf")

    else:
        gp.plot_acf(acorr_matrix, vars_to_plot=["Y_j", "K", "C", "I", "H", "r_e", "r_s", "w_s", "w_u", "skill_p"], n_cols=3)
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/autocovariance_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf")