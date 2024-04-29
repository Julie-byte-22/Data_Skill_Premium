source simp_model/bin/activate

#Experiment B # Change weight of private data as compared to public data [kappa]

#Private data only | kappa low
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 6 \
                      --eta 0.06 \
                      --kappa 0.25 \
                      --x_f 1 \
                      --x_o 0 \
                      --sigma 4

#Private data only | kappa high
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 7 \
                      --eta 0.06 \
                      --kappa 0.9 \
                      --x_f 1 \
                      --x_o 0 \
                      --sigma 4

# Private and public data  | kappa low
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 8 \
                      --eta 0.06 \
                      --kappa 0.25 \
                      --x_f 1 \
                      --x_o 0.5 \
                      --sigma 4

# Private and public data  | kappa high
python solve_model.py --mode data_monopol-generic \
                      --experiment_number 9 \
                      --eta 0.06 \
                      --kappa 0.9 \
                      --x_f 1 \
                      --x_o 0.5 \
                      --sigma 4

