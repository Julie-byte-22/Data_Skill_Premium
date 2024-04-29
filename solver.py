import sympy as sp
from scipy import optimize
from scipy import stats
from functools import wraps
import numpy as np
import pickle

def solve_mod(mod, mode, experiment, folder):
    # Stage 1: Minimiser to populate steady state equations
    # --------------------------------------------------------------------

    mod.steady_state(method='minimize', 
                    optimizer_kwargs={'method':'powell'}, 
                    use_jac=False,
                    use_hess=False,
                    verbose = False)

    # Scipy splits the function inputs into two groups: x is the steady-state variables, and args are the parameters.
    ss_vars = [x.to_ss() for x in mod.variables]
    params = list(mod.free_param_dict.to_sympy().keys())

    # Lambdify compiles a sympy expression to numpy 
    _f_ss_resid = sp.lambdify(ss_vars + params, mod.steady_state_system)


    # Wrapper translates format from the scipy signature (ss_values, parameters) to a lambdify function (needed to pass to the minimiser)

    def scipy_optimize_wrapper(f):
        @wraps(f)
        def inner(ss_values, params):
            return f(*ss_values, *params)
        return inner

    f_ss_resid = scipy_optimize_wrapper(_f_ss_resid)

    # Compute jacobian of the steady-state system
    jac = sp.Matrix([[eq.diff(x) for x in ss_vars] for eq in mod.steady_state_system])
    _f_ss_jac = sp.lambdify(ss_vars + params, jac)
    f_ss_jac = scipy_optimize_wrapper(_f_ss_jac)


    # mse = sum([x ** 2 for x in mod.steady_state_system]) / mod.n_variables
    # _f_mse = sp.lambdify(ss_vars + params, mse)

    # # Compute the gradient
    # mse_grad = [mse.diff(x) for x in ss_vars]
    # _f_mse_grad = sp.lambdify(ss_vars + params, mse)

    # # Compute the hessian
    # mse_hess = [[eq.diff(x) for x in ss_vars] for eq in mse_grad]
    # _f_mse_ess = sp.lambdify(ss_vars + params, mse)

    #%% Stage 2: Recover the values from stage 1 

    # Transform the parameter dictionary into an array
    param_vals = np.array(list(mod.free_param_dict.values()))
    x0 = np.array(list(mod.steady_state_dict.values()))

    def stage_2_ss(mod, param_vals, x0, verbose = True):

        ''' Function injects the new solution back into the model to start stage 2 of finding the steady state
        '''
        res = optimize.root(f_ss_resid, jac=f_ss_jac, x0=x0, args=(param_vals, ),
                            method='lm')
        #res

        
        for i, k in enumerate(mod.steady_state_dict.keys()):
            mod.steady_state_dict[k] = res.x[i]

        mod.steady_state_solved = res.success
        assert mod.steady_state_solved
        if verbose:
            print("Steady state found! :D")
            mod.print_steady_state()

    stage_2_ss(mod, param_vals, x0)


    #%% Solve the model
    #-------------------------------------------------------------------------------

    if mode == 'original':
        # Solver using Taylor series expansion (Original Lindquist paper)
        model_solved = mod.solve_model(solver='gensys', not_loglin_variable = [x.base_name for x in mod.variables])
    else:
        # Solver with Log Linearisation
        model_solved = mod.solve_model(solver='gensys')
    
    
    with open(f'{folder}/model_solved_{mode}_{experiment}.pkl', 'wb') as f:
        pickle.dump(model_solved, f)
    


