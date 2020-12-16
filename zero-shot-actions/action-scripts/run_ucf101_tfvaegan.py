#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:52:45 2019
@author: akshita
"""
import os

# CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=8
os.system('''python /content/gzsl/zero-shot-actions/train_tfvaegan.py \
--encoded_noise --gzsl_od --workers 8 --nclass_all 101 \
--dataset ucf101 --dataroot /content/drive/MyDrive/colab_data/action_datasets \
--syn_num 600 --preprocessing --cuda --gammaD 10 --gammaG 10 \
--action_embedding i3d --class_embedding att \
--nepoch 100 --ngh 4096 --ndh 4096 --lambda1 10 --critic_iter 5 \
--batch_size 64 --nz 115 --attSize 115 --resSize 8192 --lr 0.0001 \
--recons_weight 0.1 --feedback_loop 2 --a2 1 --a1 1 --bce_att --feed_lr 0.00001 --dec_lr 0.0001''')


# --dataset ucf101_i3d/split_{split}
# --image_embedding_path ucf101_i3d

