#!/bin/bash

#$ -q short.qc
#$ -o /well/seymour/users/uhu195/python/shoes/
#$ -e /well/seymour/users/uhu195/python/shoes/

# note that you must load whichever main Python module you used to create your virtual environments before activating the virtual environment
module load Tkinter/2.7.15-foss-2018b-Python-2.7.15

# Activate the ivybridge or skylake version of your python virtual environment
# NB The environment variable MODULE_CPU_TYPE will evaluate to ivybridge or skylake as appropriate
source /well/seymour/users/uhu195/python/bigflica-py2.7.15-${MODULE_CPU_TYPE}/bin/activate

# continue to use your python venv as normal
python /well/seymour/users/uhu195/python/pain/test.py