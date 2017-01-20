# coding: utf-8
# 1.4.2 クラス pp.10-116
class Man:
    """サンプルクラス"""

    def __init__(self, name):
        self.name = name
        print("Initilized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David") # Man クラスから m というインスタンス(オブジェクト)を生成
m.hello()
m.goodbye()
