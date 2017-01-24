# 3.5.1 p.69 分類問題で使うソフトマックス関数
def softmax(a):
    c = np.max(a) # 入力信号の中で最大の値

    exp_a = np.exp(a - c) # 分子の exp(a_k)にオーバーフロー対策をした
    sum_exp_a = np.sum(exp_a) # 指数関数の和 分母
    y = exp_a / sum_exp_a

    return y
