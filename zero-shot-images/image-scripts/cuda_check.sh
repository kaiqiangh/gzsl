#!/bin/sh
#sbatch --job-name=cuda --gres=gpu:1 --mem=1024 cuda_check.sh
python cuda_check.py
