class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = self.Node()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end == True
            else:
                if word[i] == ".":
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    else:
                        return dfs(i+1, node.children[word[i]])
            return False
        return dfs(0,self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)