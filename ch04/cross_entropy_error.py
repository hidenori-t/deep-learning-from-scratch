# 4.2.4 p.94
def cross_entropy_error(y, t): # y=NNの出力, t=教師データ
    if y.ndim == 1: # データひとつあたりの交差エントロピー誤差を求める場合
        t = t.reshape(1, t.size) # 1×tの配列の要素数のサイズに変形
        y = y.reshape(1, y.size) # 1×yの配列の要素数のサイズに変形

    batch_size = y.shape[0] # # yの第1次元の要素の長さ，すなわちベクトルの長さ
    return -np.sum(t * np.log(y[np.arange(batch_size), t])) / batch_size
