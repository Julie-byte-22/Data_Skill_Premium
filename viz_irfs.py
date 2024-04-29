import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import gEconpy.plotting as gp

def plot_irfs(mod, args, folder):

    figures_dir = os.path.join(os.getcwd(), f"{folder}/figures")
    if not os.path.exists(figures_dir):
        os.makedirs(figures_dir)

    perf_dir = os.path.join(os.getcwd(), f"{folder}/model_performance")
    if not os.path.exists(perf_dir):
        os.makedirs(perf_dir)

    irf = mod.impulse_response_function()
    irf.to_csv(f"{perf_dir}/IRF_DF_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.csv")

    #Create irf only for TFP shock
    epsilon_z_columns = [col for col in irf.columns if 'epsilon_z' in col]

    # Select only the rows for variables, not shocks, if that row exists
    if 'Variables' in irf.index or 'Shocks' in irf.index:
        TFP_irf = irf.loc[irf.index.drop(['Shocks']), epsilon_z_columns]
    else:
        TFP_irf = irf[epsilon_z_columns]

    #Create irf only for IST shock
    epsilon_q_columns = [col for col in irf.columns if 'epsilon_q' in col]

    # Select only the rows for variables, not shocks, if that row exists
    if 'Variables' in irf.index or 'Shocks' in irf.index:
        IST_irf = irf.loc[irf.index.drop(['Shocks']), epsilon_q_columns]
    else:
        IST_irf = irf[epsilon_q_columns]

    print(IST_irf.head())


    if args.mode == "original":
        '''Plots the correct adjusted IRFs for Lindquist original paper,
        suggests that he adjust the Taylor expanded IRF/Steady State deviation'''
        ss_series = pd.Series(mod.steady_state_dict)
        irf_adjusted = irf/ss_series.values[:, None]

        sigmas = np.diag(np.array([0.0038, 0.0076]))
        rho_zq = -0.31
        corr_mat = np.array([[1., rho_zq],
                            [rho_zq, 1.]])
        Q = sigmas @ corr_mat @ sigmas
        irf_corr = mod.impulse_response_function(shock_size=np.sqrt(Q[1, 1]))

        gp.plot_irf(
            irf_adjusted,
            vars_to_plot=["Y", "C", "I", "H", "r_s", "r_e", "K", "K_s", "K_e"],
            n_cols=3,
            figsize=(18, 7.5),
            legend=True,
        )
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/IRF_Set1__{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf", bbox_inches='tight')
        plt.close()


        gp.plot_irf(
            irf_adjusted,
            vars_to_plot=["h_s", "h_u", "w_s", "w_u", "C", "rel_hours", "equip_skill", "skill_p"],
            n_cols=2,
            figsize=(10, 12),
            legend=True,
        )
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/IRF_Set_2__{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf", bbox_inches='tight')
        plt.close()

    else:
        gp.plot_irf(
            irf,
            vars_to_plot=["Y_j", "C", "I", "H", "r_s", "r_e", "K", "K_s", "K_e"],
            n_cols=4,
            figsize=(12, 5),
            legend=True,
        )
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/IRF_Set_1_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf", bbox_inches='tight')
        plt.close()

        gp.plot_irf(
            irf,
            vars_to_plot=["h_s", "h_u", "w_s", "w_u", "C", "rel_hours", "equip_skill", "skill_p"],
            n_cols=4,
            figsize=(12, 5),
            legend=True,
        )
        plt.tight_layout()
        plt.draw()
        plt.savefig(f"{figures_dir}/IRF_Set_2_{args.mode}_EN{args.experiment_number}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}.pdf", bbox_inches='tight')
        plt.close()

        #Plot variables for IRF TFP shocks singular
        variables = list(TFP_irf.index)
        y_limits = {
            "Y_t" : (0, 1.6),
            "C": (0, 0.35),
            "K": (-0.1, 0.8), 
            "K_e": (-0.1, 0.8),  
            "K_s": (-0.1, 0.8),
            "I" : (-2, 15),
            "I_e": (-2,12),
            "I_s": (-5,40),
            "H": (-0.2,0.8),
            "h_u": (-0.2,0.8),
            "h_s": (-0.2,0.8),
            "equip_skill": (-0.7, 0.8),
            "rel_hours": (-0.15,0.15),
            "skill_p": (-0.15, 0.15),

            }
        for v in variables:
            shock = 'TFP'
            gp.plot_irf(
            TFP_irf,
            vars_to_plot=[v],
            n_cols=4,
            figsize=(12, 5),
            legend=False,
            )
            if v in y_limits:
                plt.ylim(y_limits[v])
            plt.tight_layout()
            plt.draw()
            plt.savefig(f"{figures_dir}/IRF_{args.mode}_EN{args.experiment_number}_{shock}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}_{v}.pdf", bbox_inches='tight')
            plt.close()
        
        #Plot variables for IRF IST shocks singular
        variables = list(IST_irf.index)
        y_limits_ist = {
            "Y_t" : (-0.05, 0.4),
            "C": (-0.3, 0.3),
            "K": (-0.1, 1.2), 
            "K_e": (-0.2, 1.2),  
            "K_s": (-2.5, 0.8),
            "I" : (-1, 5),
            "I_e": (-5,35),
            "I_s": (-60,20),
            "H": (-0.05,0.3),
            "h_u": (-0.05,0.3),
            "h_s": (-0.05,0.3),
            "equip_skill": (-0.2, 1.2),
            "rel_hours": (-0.2,0.1),
            "skill_p": (-0.15, 0.2)
            }
        for v in variables:
            shock = 'IST'
            gp.plot_irf(
            IST_irf,
            vars_to_plot=[v],
            n_cols=4,
            figsize=(12, 5),
            legend=False,
            )
            if v in y_limits_ist:
                plt.ylim(y_limits_ist[v])
            plt.tight_layout()
            plt.draw()
            plt.savefig(f"{figures_dir}/IRF_{args.mode}_EN{args.experiment_number}_{shock}_e{args.eta}_k{args.kappa}_x_f{args.x_f}_x_o{args.x_o}_s{args.sigma}_{v}.pdf", bbox_inches='tight')
            plt.close()

   