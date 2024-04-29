source simp_model/bin/activate

#Experiment E Change elasticity of substitution of retail firm [sigma]
# Importance of data overall high in the economy


# Private data only | low sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 22 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0 \
                      --sigma 2

# Private data only | medium sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 23 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0 \
                      --sigma 4

# Private data only | high sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 24 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0 \
                      --sigma 10

# Public data  | low sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 25 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0 \
                      --x_o 0.5 \
                      --sigma 2

# Public data  | medium sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 26 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0 \
                      --x_o 0.5 \
                      --sigma 4


# Public data  | high sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 27 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0 \
                      --x_o 0.5 \
                      --sigma 10
    


# Public and private data  | low sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 28 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0.5 \
                      --sigma 2

# Publicand private data  | medium sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 29 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0.5 \
                      --sigma 4


# Public and private data  | high sigma
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 30 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0.5 \
                      --sigma 10
    