# coding: utf-8
# 1.4.2 クラス pp.10-11
# 『みんなのPython』p.253 参考

class Man:
    """サンプルクラス"""

    def __init__(self, name): # 初期化メソッドを定義=インスタンスを作る, 追加の引数 name を設定
        self.name = name # instance (self) に，attribute (name) にnameを代入して追加
        print("Initilized!")

    def hello(self): # hello() method を定義
        print("Hello " + self.name + "!")

    def goodbye(self): # goodbye() method を定義
        print("Good-bye " + self.name + "!")

m = Man("David") # Man Class から instance (m) を生成
m.hello() # instance (m)の hello() method を使う
m.goodbye() # instance (m)の goodbye() method を使う
