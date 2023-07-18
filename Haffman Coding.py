string = 'ABCCDADCCABDCCDA'

class NodeTrees(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def node(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def Huffman_code_tress(node, left=True, binstring=' '):
    if type(node) is str:
        return {node: binstring}
    (l, r) = node.children()
    d=dict()
    d.update(Huffman_code_tress(l, True, binstring + '0'))
    d.update(Huffman_code_tress(r, False, binstring + '1'))
    return d

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

nodes = freq
while len(nodes)>1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTrees(key1, key2)
    nodes.append((node, c1+c2))

    nodes = sorted(nodes, key=lambda x:x[1], reverse=True)

huffmanCode = Huffman_code_tress(nodes [0][0])

print('Char | Huffman code')
print('------------------------')
for(char, frequency) in freq:
    print('%-4r |%8s' % (char, huffmanCode[char]))





str = "ABCDABCDABCDABCDABCDAABCCD"

class NodTrees(object):
    def __init__(self, l = None, r = None):
        self.l = l
        self.r = r

    def child(self):
        return (self.l, self.r)

    def node(self):
        return (self.l, self.r)

    def __str__(self):
        return '%s %s' % (self.r, self.l)

def HaffCodeTrees(node, left=True, binstring=' '):
    if type(node) is str:
        node ={node : binstring}

