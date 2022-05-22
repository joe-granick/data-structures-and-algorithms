class trieNode:
    def __init__(self):
        children = {}

class trie:
    def __init__(self):
        root = trieNode()

    def search(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
            return currentNode

    def insert(self, prefix):
        currentNode = self.root
        for char in prefix:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = trieNode()
                currentNode.children[char] = newNode
        currentNode.children["*"] = None
            
    def collectAllWords(self, node = None, word = "", words = []):
        currentNode = node or self.root

        for key, child in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(child, word + key, words)


    def autocomplete(self, prefix):
        startNode = self.search(prefix)
        if not startNode:
            return None
        else:
            return self.collectAllWords(startNode, prefix)

