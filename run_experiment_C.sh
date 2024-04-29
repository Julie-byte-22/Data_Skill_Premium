source simp_model/bin/activate

#Experiment C # Change share of private data in the economy [x_f]


#Private data only | low private data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 10 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0.1 \
                      --x_o 0 \
                      --sigma 4

#Private data only | medium private data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 11 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0 \
                      --sigma 4

# Private data online | high private data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 12 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0.9 \
                      --x_o 0 \
                      --sigma 4


# Private and public data  | low private data high public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 13 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0.1 \
                      --x_o 0.5 \
                      --sigma 4

# Private and public data  | medium private data high public data
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 14 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0.5 \
                      --x_o 0.5 \
                      --sigma 4
                    

# Private and public data  | private and public data high
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 15 \
                      --eta 0.06 \
                      --kappa 0.5 \
                      --x_f 0.9 \
                      --x_o 0.5 \
                      --sigma 4