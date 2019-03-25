#/**********************************************************
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: cal_time.py
#     Author: Lina Hu
#     CreatedDate: Mon Mar 18 05:39:58 2019
#     
#**********************************************************/
import argparse

def cal_time(iters, t_per_iter):
    t = (iters * t_per_iter) / 3600/ 24
    return t

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', type=int, help='total iterations')
    parser.add_argument('--t', type=float, help='cost time per iteration')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_arguments()
    days = cal_time(args.i, args.t)
    print(days)
