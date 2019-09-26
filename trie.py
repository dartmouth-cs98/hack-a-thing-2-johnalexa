
class Trie:

    def __init__(self, results_limit=5):
        self.results_limit = results_limit
        wordsFile = "./words.txt"
        with open(wordsFile, "r") as f:
            words = f.read().splitlines()
            self.build(words)
        f.close()


    def build(self, words):
        self.root = TrieNode('')
        for word in words:
            word = word.lower()
            self.root.insert(word)


    def lookup(self, word):
        word = word.lower()
        if not word or not word.isalpha():
            raise Exception("Input a valid alphabetic word")

        base = self.root
        for value in word:
            idx = ord(value) - ord('a')
            base = base.children[idx]
            if not base:
                raise NotAWordException("No words start with those letters")
            if base.ends_word and base.depth > 3:
                raise FinishedWordException("Those letters already finish a word.")

        suffixes = []
        base.find_suffixes(self.results_limit, suffixes)
        return [word + suffix for suffix in suffixes]


class TrieNode:

    def __init__(self, value, depth=0):
        self.value = value
        self.children = [None] * 26
        self.ends_word = False
        self.depth = depth


    def insert(self, word, depth=1):
        if word is None:
            return

        if word == '':
            self.ends_word = True
            return

        value = word[0]
        idx = ord(value) - ord('a')
        child = self.children[idx]
        if not child:
            child = TrieNode(value, depth=depth)
            self.children[idx] = child

        if not (child.ends_word and child.depth > 3):
            child.insert(word[1:], depth=depth+1)


    def find_suffixes(self, limit, results, prefix=""):
        if len(results) >= limit:
            return

        if self.ends_word and self.depth > 3:
            results.append(prefix[1:] + self.value)
        else:
            for child in self.children:
                if child:
                    child.find_suffixes(limit, results, prefix=prefix+self.value)


    def __eq__(self, other):
        return self.value == other.value


class FinishedWordException(Exception):
    pass


class NotAWordException(Exception):
    pass
