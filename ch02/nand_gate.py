# coding: utf-8
# p.27
import numpy as np


def NAND(x1, x2):
    x = np.array([x1, x2])
    # AND gate のパラメータの符号を全て反転
    w = np.array([-0.5, -0.5]) # 重み
    b = 0.7 # バイアス
    tmp = np.sum(w*x) + b # w1*x1+w2*x2+b=(-0.5*x1)+(-0.5*x2)+0.7
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
