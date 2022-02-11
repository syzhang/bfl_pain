## bigflica
* This repo contains environment info and script to run bigflica on imaging data (extracted as npys, see [bfl_extract](https://github.com/syzhang/bfl_extract) for more information)

### python environment
* On bmrc, use `module load Tkinter/2.7.15-foss-2018b-Python-2.7.15` version of python
* Install `requirements.txt` in a virtualenv (see `bfl_extract` repo for directions)
* Use `sub_lines_2.7.15.sh` to submit bigflica jobs
* Output of bigflica should be npy matrices that can be used for classifier construction, where the pipeline development notebooks are stored in `bfl_extract` repo 