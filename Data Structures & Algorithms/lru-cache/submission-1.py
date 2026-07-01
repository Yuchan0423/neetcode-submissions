class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.order = []
        self.dic = {}

    def get(self, key: int) -> int:
        if key in self.dic:
            self.order.remove(key)
            self.order.append(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if(len(self.order) == self.cap):
                x = self.order.pop(0)
                self.dic.pop(x)
            self.order.append(key)
            self.dic[key] = value

            
