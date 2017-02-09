# coding: utf-8
# p.137
class MulLayer: # 乗算layer
    def __init__(self):
        self.x = None # 順伝播時の入力値を保持するため cf.p.135
        self.y = None

    def forward(self, x, y): # 順伝播
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout): # 逆伝播 dout=微分
        dx = dout * self.y # 乗算ノードなので微分と，保持した伝播時の入力値をかけて x と y をひっくり返す cf.p.134
        dy = dout * self.x

        return dx, dy

# p.139
class AddLayer: # 加算layer
    def __init__(self):
        pass

    def forward(self, x, y): # 順伝播
        out = x + y

        return out

    def backward(self, dout): # 逆伝播
        dx = dout * 1
        dy = dout * 1

        return dx, dy
