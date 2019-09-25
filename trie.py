
class Trie:

    def __init__(self):
        wordsFile = "./words.txt"
        with open(wordsFile, "r") as f:
            words = f.readlines()
            self.build(words)
        f.close()


    def build(self, words):
        self.x = words[10]


    def test(self):
        return self.x


class TrieNode:

    def __init__(self, value):
        self.value = value
        self.children = {}
        self.endsWord = False
