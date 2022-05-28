class trieNode:
    def __init__(self):
        self.children = {}

class trie:
    def __init__(self):
        self.root = trieNode()

    def search(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return
        return currentNode

    def insert(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = trieNode()
                currentNode.children[char] = newNode
                
                currentNode = newNode
        currentNode.children["*"] = None
            
    def collectAllWords(self, node = None, word = "", words = None):
        words = [] if words is None else words
        # start at beginning if no node passed in
        currentNode = node or self.root
        for key, child in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(child, word + key, words)
        return words
    def autocomplete(self, prefix):
        startNode = self.search(prefix)
        if not startNode:
            return None
        return self.collectAllWords(startNode, prefix)

    def traverseAndPrint(self, node = None):
        currentNode = node or self.root
        
        for key, child in currentNode.children.items():
            print(key)
            if key != "*":
                return self.traverseAndPrint(child)

    def autcorrect(self, word):
        currentNode = self.root
        prefix = ''
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
                prefix = prefix + char
            else:
                return self.collectAllWords(currentNode, prefix)[0]
        return word

test = trie()

test.insert("ball")
test.insert("bald")
test.insert("balance")
test.insert("balter")
test.insert("banter")
test.insert("attack")
test.insert("cat")
test.insert("catnip")
test.insert("catnap")
print(test.collectAllWords())
print(test.autocomplete("b"))
print(test.autocomplete("ban"))
print(test.autcorrect("carnap"))

