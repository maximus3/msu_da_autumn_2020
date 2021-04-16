from collections import deque


class Node:

    def __init__(self, letter, prev=None):
        self.letter = letter
        self.isKey = False
        self.next = {}
        self.prev = prev

    def __hash__(self):
        return ord(self.letter)

    def __eq__(self, other):
        return self.letter == other.letter

    def __lt__(self, other):
        return self.letter < other.letter


class Trie:

    def __init__(self):
        self.len = 0
        self.baseNode = Node('')

    def add(self, word):
        node = self.baseNode
        for c in word:
            node = node.next.setdefault(c, Node(c, node))
        if not node.isKey:
            self.len += 1
            node.isKey = True
            return True
        return False

    def pop(self, word):
        node = self.baseNode
        for c in word:
            if c not in node.next:
                raise KeyError(word)
            node = node.next[c]
        if not node.isKey:
            raise KeyError(word)
        self.len -= 1
        node.isKey = False

        if node.next:
            return word
        needToDelete = True
        while node.prev is not None and needToDelete:
            letter = node.letter
            node = node.prev
            node.next.pop(letter)
            needToDelete = not (node.next or node.isKey)
        return word

    def __len__(self):
        return self.len

    def _searchNode(self, word):
        node = self.baseNode
        for c in word:
            if c not in node.next:
                return None
            node = node.next[c]
        return node

    def __contains__(self, word):
        node = self._searchNode(word)
        return (node is not None) and node.isKey

    def starts_with(self, prefix):
        return TrieIterator(self._searchNode(prefix), prefix)

    def __iter__(self):
        return TrieIterator(self.baseNode)


class TrieIterator:

    def __init__(self, node, prefix=None):
        self.deque = deque()
        self.prefix_deque = deque()
        if prefix is None:
            prefix = ''
        if node is not None:
            self.deque.append(node)
            self.prefix_deque.append('')

        self.prefix = prefix[:-1]

    def __next__(self):
        while True:
            if len(self.deque) == 0:
                raise StopIteration()

            node = self.deque.popleft()
            prefix = self.prefix_deque.popleft()

            vals = sorted(node.next.values())
            vals_len = len(vals)

            self.deque.extend(vals)
            self.prefix_deque.extend([prefix + node.letter] * vals_len)

            if node.isKey:
                return self.prefix + prefix + node.letter

    def __iter__(self):
        return self


if __name__ == '__main__':

    # Test 1
    trie = Trie()
    trie.add('apple')
    trie.add('mango')
    trie.add('juice')

    assert len(trie) == 3
    assert ('apple' in trie)

    # Test 2
    trie = Trie()
    trie.add('apple')
    trie.add('mango')
    trie.add('juice')

    assert ('apple' in trie)
    trie.pop('apple')
    assert not ('apple' in trie)
    assert len(trie) == 2

    # Test 3
    trie = Trie()
    trie.add('salad')
    trie.add('apple')
    trie.add('mango')
    trie.add('juice')
    trie.add('carrot')
    trie.add('broccoli')

    assert list(trie) == ['apple', 'juice', 'mango', 'salad', 'carrot',
                          'broccoli']

    # Test 4
    trie = Trie()
    trie.add('word')
    trie.add('world')
    trie.add('work')
    trie.add('wood')

    assert list(trie.starts_with('wor')) == ['word', 'work', 'world']

    # Test 5
    trie = Trie()
    try:
        trie.pop('summary')
        assert "KeyError" is None
    except KeyError as e:
        pass

    # Test 6
    trie = Trie()
    s = 'a' * 100000
    s1 = s + 'b'
    s2 = 'a' + 'b' * 100000
    trie.add(s)
    trie.add(s1)
    trie.add(s2)

    assert (s in trie)
    assert list(trie.starts_with('a')) == [s, s1, s2]
