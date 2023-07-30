#ヒープキュー
from heapq import heappop as hpop
from heapq import heappush as hpush
from heapq import heapify as hfy
# hfy(hoge)
# hpop(hoge)
# hpush(hoge,n)


#神ヒープキュー
#get…最小値が何か
#pop…最小値排除
#push…単純に数入れる
#remove…要素削除
import heapq
from collections import defaultdict

class LazyHeap():
    def __init__(self, init_arr=[]):
        self.heap = []
        self.members = defaultdict(int)
        self.removed = defaultdict(int)
        self.len = 0
        for init_element in init_arr:
            heapq.heappush(self.heap, init_element)
            self.members[init_element] += 1
            self.len += 1
 
    def __len__(self):
        return self.len
 
    def push(self, k):
        heapq.heappush(self.heap, k)
        self.members[k] += 1
        self.len += 1
 
    def pop(self):
        self._clear()
        self.len -= 1
        self.members[self.get()] -= 1
        return heapq.heappop(self.heap)
 
    def get(self):
        self._clear()
        return self.heap[0]
 
    def _clear(self):
        while True:
            cand = self.heap[0]
            if self.removed[cand] > 0:
                heapq.heappop(self.heap)
                self.removed[cand] -= 1
            else:
                return
 
    def remove(self, k):
        if self.members[k] > 0:
            self.removed[k] += 1
            self.members[k] -= 1
            self.len -= 1
 
    def __str__(self):
        return str(self.heap)
 
    def __contains__(self, item):
        return True if self.members[item] > 0 else False