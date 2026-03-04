class Solution:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False
    def __init__(self): 
        self.root = self.Node()
    def add(self, word):
        current = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in current.children:
                current.children[c] = self.Node()
            current = current.children[c]
        current.is_end = True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dct = Solution()
        ans = []
        for word in dictionary:
            dct.add(word)
        lst = sentence.split(" ")
        for word in lst:
            current = dct.root
            root = ''
            flag = False # flag = whether we broke from the loop
            for i in range(len(word)):
                c = word[i]
                root += c
                if c in current.children:
                    if current.children[c].is_end == True:
                        ans.append(root)
                        flag = True
                        break
                    else:
                        current = current.children[c]
                else:
                    ans.append(word)
                    flag = True
                    break
            if flag == False and current.is_end == False:
                ans.append(word)
        ans_string = " ".join(ans)
        print(ans)
        print(ans_string)
        return ans_string

                


        
