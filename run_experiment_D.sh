source simp_model/bin/activate

#Experiment D # Change share of public data in the economy [x_o]

# if CASE = 19: x_f = 1, eta = 0.06, kappa = 0.5, x_o=0.1 (both priv and pub)
# if CASE = 20: x_f = 1, eta = 0.06, kappa = 0.5, x_o=0.5
# if CASE = 21: x_f = 1, eta = 0.06, kappa = 0.5, x_o=0.9

#Public data only | low public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 16 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0 \
                      --x_o 0.1 \
                      --sigma 4

# Public data only | medium public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 17 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0 \
                      --x_o 0.5 \
                      --sigma 4

# Public data only | high public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 18 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0 \
                      --x_o 0.9 \
                      --sigma 4

# Public and private data | low public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 19 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 1.0 \
                      --x_o 0.1 \
                      --sigma 4

# Public and private data | medium public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 20 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 1.0 \
                      --x_o 0.5 \
                      --sigma 4

# Public and private data only | high public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 21 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 1.0 \
                      --x_o 0.9 \
                      --sigma 4