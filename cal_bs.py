#/**********************************************************
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: cal_time.py
#     Author: Lina Hu
#     CreatedDate: Mon Mar 18 05:39:58 2019
#     
#**********************************************************/
import argparse

def cal_bs(fei, ssi, fee, see):
    bs1 = (30462 * fee) / fei / 1000
    bs2 = (30462 * fee) / ssi / 1000
    final_iters = (30462 * see) / bs2 / 1000
    return bs1, bs2, final_iters

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fei', '-first-end-iters', type=int)
    parser.add_argument('--ssi', '-second-start-iters', type=int)
    parser.add_argument('--fee', '-first-end-epoches', type=int)
    parser.add_argument('--see', '-second-end-epoches', type=int)

    
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_arguments()

    bs1, bs2, final_iters = cal_bs(args.fei, args.ssi, args.fee, args.see)
    print("first bs {}, second bs {}, final_iters {}".format(bs1, bs2, final_iters))
