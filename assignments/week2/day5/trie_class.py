class TrieNode:
    def __init__(self):
        self.children={}
        self.end_word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
                
        curr.end_word=True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr=curr.children[c]
            else:
                return False
         
        return curr.end_word 
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr=curr.children[c]
            else:
                return False
         
        return True 