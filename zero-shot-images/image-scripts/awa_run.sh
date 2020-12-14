#!/bin/sh
#sbatch --job-name=awa --gres=gpu:1 --mem=32768 --cpus-per-task=4 --output=output_awa.out awa_run.sh

python run_awa_tfvaegan.py