"""
testing bigflica

working with bmrc - in shared drive

"""

import sys, os
# sys.path.append('..')
from BigFLICA import BigFLICA_cpu



base_dir = '/well/tracey/shared/fps-ukb/'
sj_dir = 'subjs_paincontrol'
npy_dir = os.path.join(base_dir, sj_dir)

# get all npys
npy_ls = os.listdir(npy_dir)
npy_path = [os.path.join(npy_dir, f) for f in npy_ls]
# print(npy_path)

# define output
curr_dir = os.path.join(base_dir, 'bigflica_output')
output_dir = os.path.join(curr_dir, 'output_paincontrol_500')

try:
    os.mkdir(output_dir)
except (OSError):
    pass
except Exception as e:
    raise e
    
# run bigflica
# nlat = 30
# migp_dim = 100
# dicl_dim = 1000
# nlat = 50
nlat = 200
migp_dim = 500
dicl_dim = 1000
ncore = 1

BigFLICA_cpu.BigFLICA(npy_path, nlat, output_dir, migp_dim, dicl_dim, ncore)
