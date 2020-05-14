class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size
    def root(self, x):
        if self.data[x] < 0:
            return x
        ans = self.root(self.data[x])
        self.data[x] = ans
        return ans
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.data[x] > self.data[y]:
            x, y = y, x
        self.data[x] += self.data[y]
        self.data[y] = x
        return True
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def size(self, x):
        return -self.data[self.root(x)]

"""
Union-Find 森
https://scrapbox.io/data-structures/Union_Find
UnionFind(size):
0 ~ size - 1 がそれぞれ別々の集合に属するものとして初期化
root(x) -> void:
x が属する集合を表す根付き木の頂点を返す
unite(x) -> Bool:
root(x) と root(y) の間に辺を張り, x が属する集合と y が属する集合を結合する
変更があったかが返る (もともと同じ集合に属していたら False)
same(x, y) -> Bool:
x と y が同じ集合に属するか判定する
size(x) -> Int:
x が属する集合の要素数を返す
実装について
data[x] は data[x] < 0 のとき根であり, data[x] == -size(x) となっています
また, data[x] >= 0 のとき子であり, data[x] は親の番号を表しています
unite(x) は 
if self.data[x] > self.data[y]:
    x, y = y, x
で計算量が落ちます(データ構造をマージする一般的なテク)
root(x) は
self.data[x] = ans
で計算量が落ちます(経路圧縮)
"""


# https://atcoder.jp/contests/arc097/tasks/arc097_b

n, m = map(int, input().split())
p = list(map(int, input().split()))
for i in range(n):
    p[i] -= 1
uf = UnionFind(n)
for i in range(m):
    x, y = map(int, input().split())
    uf.unite(x - 1, y - 1)
ans = 0
for i in range(n):
    ans += uf.same(i, p[i])
print(ans)