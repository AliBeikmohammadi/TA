# TA-Explore
Implementation of **TA-Explore**, as presented in TA-Explore: Teacher-Assisted Exploration for Facilitating Fast Reinforcement Learning.
KDD2022

## How to Plot the Results
```
python plot_results.py -h


usage: plot_results.py [-h] [--Env ENV] [--input_dir INPUT_DIR] [--TA_dir TA_DIR] [--baseline_dir BASELINE_DIR] [--save_dir SAVE_DIR] [--O_RT [O_RT ...]] [--O_RA [O_RA ...]] [--x_min X_MIN] [--x_max X_MAX]

optional arguments:
  -h, --help            show this help message and exit
  --Env ENV             Env name; default RW - RW:RandomWalk, TC: Temperature Control, FT: Four Tank
  --input_dir INPUT_DIR
                        Input file directory; default./Results/RandomWalk/RW_s5_r100_e100.csv
  --TA_dir TA_DIR       TA-explore file directory; default ./Results/Temperature_Control/Temperature_Control_e8000_omega1_beta1_E4000.csv
  --baseline_dir BASELINE_DIR
                        Baseline file directory; default ./Results/Temperature_Control/Temperature_Control_e8000_omega1_beta0_E4000.csv
  --save_dir SAVE_DIR   Save plots directory; default ./Results/RandomWalk/
  --O_RT [O_RT ...]     Plot O_RT; default False
  --O_RA [O_RA ...]     Plot O_RA; default False
  --x_min X_MIN         lower bound xlim; default 0
  --x_max X_MAX         upper bound xlim; default 8000
```
## How to Run Experiments

```
python RandomWalk.py -h


usage: RandomWalk.py [-h] [--N N] [--E E] [--R R] [--b [B ...]] [--l [L ...]] [--d D] [--save_dir SAVE_DIR]

optional arguments:
  -h, --help           show this help message and exit
  --N N                Number of states (including the ending states); default 5
  --E E                Number of episodes per each test; default 100
  --R R                Number of independent test; default 100
  --b [B ...]          initial_beta; default [0, 1, 100] if 0: only R^T, if 100: only only R^A, if (0, 1) if adaptive beta*R^A + (1-adaptive beta)*R^T where adaptive beta =
                       initial_beta*((lambda)**episode)
  --l [L ...]          lambda; default [0.1, 0.5, 0.9]
  --d D                debug_level; default 0 0:nothing print 1:print average result over runs, 2:print result after end of each episode, 3:print all information, like actions and reward in each state
  --save_dir SAVE_DIR  Save Directory; default ./Results/RandomWalk/
```

```
python Optimal_Temperature_Control_with_Constraint.py -h


usage: Optimal_Temperature_Control_with_Constraint.py [-h] [--e E] [--b B] [--E E] [--w W] [--save_dir SAVE_DIR] [--d [D ...]]

optional arguments:
  -h, --help           show this help message and exit
  --e E                Total episodes to train through all environments; default 8000
  --b B                initial_beta; default 1 if 0: only R^T, if (0, 1] adaptive_beta*R^A + (1-adaptive_beta)*R^T where beta = max((E-e)*initial_beta/E),0)
  --E E                Episode in which the beta is zero; default 4000
  --w W                omega, weighting values to the control objective; default 1
  --save_dir SAVE_DIR  Save Directory; default ./Results/Temperature_Control/
  --d [D ...]          debug_level; default False False:nothing print True:print result per each episode
```

```
python A_Coupled_Four_Tank_MIMO_System.py -h


usage: A_Coupled_Four_Tank_MIMO_System.py [-h] [--e E] [--b B] [--E E] [--w W] [--save_dir SAVE_DIR] [--d [D ...]]

optional arguments:
  -h, --help           show this help message and exit
  --e E                Total episodes to train through all environments; default 30000
  --b B                initial_beta; default 0.5 if 0: only R^T, if (0, 1] adaptive_beta*R^A + (1-adaptive_beta)*R^T where beta = max((E-e)*initial_beta/E),0)
  --E E                Episode in which the beta is zero; default 3000
  --w W                omega, weighting values to the control objective; default 1
  --save_dir SAVE_DIR  Save Directory; default ./Results/Four_Tank/
  --d [D ...]          debug_level; default False False:nothing print True:print result per each episode
```
