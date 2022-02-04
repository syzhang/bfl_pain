"""
testing bigflica

working with bmrc

"""

import sys, os
# sys.path.append('..')
from BigFLICA import BigFLICA_cpu


################## modify these paths to match npy locations
base_dir = '/well/seymour/users/uhu195/python/'
# sj_dir = 'extract_npy/npy/subjs_patients_pain'
sj_dir = 'extract_npy/npy/subjs_patients_pain_exmult'

# sj_dir = 'extract_npy/npy/subjs_digestive'
npy_dir = os.path.join(base_dir, sj_dir)

# get all npys
npy_ls = os.listdir(npy_dir)
npy_path = [os.path.join(npy_dir, f) for f in npy_ls]
# print(npy_path)


################ modify these names of output directories
# define output
curr_dir = os.path.join(base_dir, 'pain')
# output_dir = os.path.join(curr_dir, 'output_digestive')
output_dir = os.path.join(curr_dir, 'output_patients_exmult_500')
# output_dir = os.path.join(curr_dir, 'output_matched')
try:
    os.mkdir(output_dir)
except (OSError):
    pass
except Exception as e:
    raise e
    
# run bigflica
# nlat = 30
# nlat = 50
nlat = 100
migp_dim = 500
dicl_dim = 1000
ncore = 1

BigFLICA_cpu.BigFLICA(npy_path, nlat, output_dir, migp_dim, dicl_dim, ncore)
