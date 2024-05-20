import argparse
import os


parse = argparse.ArgumentParser(description='PyTorch Polyp Segmentation')

"-------------------data option--------------------------"
parse.add_argument('--root', type=str, default='./')
parse.add_argument('--dataset', type=str, default='kvasir_SEG')
parse.add_argument('--train_data_dir', type=str, default='data/test2')
parse.add_argument('--valid_data_dir', type=str, default='data/valid')
parse.add_argument('--test_data_dir', type=str, default='data/valid')



"-------------------training option-----------------------"
parse.add_argument('--mode', type=str, default='train')
parse.add_argument('--nEpoch', type=int, default=250)
parse.add_argument('--batch_size', type=float, default=2)
parse.add_argument('--num_workers', type=int, default=1)
parse.add_argument('--use_gpu', type=bool, default=False)
parse.add_argument('--load_ckpt', type=str, default=True)
parse.add_argument('--model', type=str, default='ACSNet')
parse.add_argument('--expID', type=int, default=0)
parse.add_argument('--ckpt_period', type=int, default=5)

"-------------------optimizer option-----------------------"
parse.add_argument('--lr', type=float, default=1e-3)
parse.add_argument('--weight_decay', type=float, default=1e-5)
parse.add_argument('--mt', type=float, default=0.9)
parse.add_argument('--power', type=float, default=0.9)

parse.add_argument('--nclasses', type=int, default=1)

opt = parse.parse_args()
