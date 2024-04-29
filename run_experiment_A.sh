source simp_model/bin/activate

#Experiment A Change importance of data in the economy

# Private data only | low importance
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 2 \
                      --eta 0.03 \
                      --kappa 0.5 \
                      --x_f 1 \
                      --x_o 0 \
                      --sigma 4

# Private data only | medium importance
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 3 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 1 \
                      --x_o 0 \
                      --sigma 4


# Private data only | high importance
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 4 \
                      --eta 0.12 \
                      --kappa 0.5 \
                      --x_f 1 \
                      --x_o 0 \
                      --sigma 4


# Private and public data | Medium importance
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 5 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 1 \
                      --x_o 0.5 \
                      --sigma 4



