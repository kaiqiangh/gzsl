#!/bin/sh
#sbatch --job-name=awa --gres=gpu:1 --mem=8196 --cpus-per-task=2 --output=output_awa.out awa_run.sh

python run_awa_tfvaegan.py