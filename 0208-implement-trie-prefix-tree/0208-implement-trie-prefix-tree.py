class Trie:

    def __init__(self):
        self.c={}
        self.e=False
    def insert(self,word):
        t=self
        for x in word:
            if x not in t.c:
                t.c[x]=Trie()
            t=t.c[x]
        t.e=True
    def search(self,word):
        t=self
        for x in word:
            if x not in t.c:
                return False
            t=t.c[x]
        return t.e
    def startsWith(self,prefix):
        t=self
        for x in prefix:
            if x not in t.c:
                return False
            t=t.c[x]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)