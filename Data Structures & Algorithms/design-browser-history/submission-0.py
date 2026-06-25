class HomePage:

    def __init__(self, homepage: str):
        self.next = None
        self.prev = None
        self.homepage = homepage

class BrowserHistory:

    def __init__(self, homepage: str):
        curr = HomePage(homepage)
        self.curr = curr
        
    def visit(self, url: str) -> None:
        curr = HomePage(url)
        curr.prev = self.curr
        self.curr.next = curr
        self.curr = curr

    def back(self, steps: int) -> str:
        pos = self.curr
        i = 0
        while i < steps and pos.prev:
            pos = pos.prev
            i += 1
        self.curr = pos
        return pos.homepage        

    def forward(self, steps: int) -> str:
        pos = self.curr
        i = 0
        while i < steps and pos.next:
            pos = pos.next
            i += 1
        self.curr = pos
        return pos.homepage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)