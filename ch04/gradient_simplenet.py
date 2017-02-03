# coding: utf-8
# 4.4.2 p.110
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self): # 初期化用 method=constructor
        self.W = np.random.randn(2,3) # 標準正規分布による 2x3 の行列の乱数

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])

net = simpleNet()

# 勾配を求める
f = lambda w: net.loss(x, t) # 損失関数を計算する新しい関数 f を定義
dW = numerical_gradient(f, net.W)

print(dW)
