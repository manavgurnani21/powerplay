
# Online Python - IDE, Editor, Compiler, Interpreter
import numpy as np
def build(items):
    # need to calculate number of elements in the array
    
    segTree = np.zeros(4*len(items))
    print(segTree)
    
    def buildTree(node, s, e):
        if s == e:
            segTree[node] = items[s]
        else:
            midpoint = (s + e)//2
            # build left child
            buildTree(2*node, s, midpoint)
            # build right child
            buildTree(2*node + 1, midpoint+1, e)
            # set values
            segTree[node] = min(segTree[2*node], segTree[2*node + 1])
        
    buildTree(1, 0, len(items)-1)
    print(segTree)
    return segTree

def query(tree, n, l, r):
    def queryTree(node, s, e):
        # case 1: if start of range is after r or end of range is before l
        if e < l or s > r:
            return float('inf')
        # case 2: complete inside
        if l <= s and e <= r:
            return tree[node]
        # case 3: partial overlap
        midpoint = (s + e) // 2
        # recurse left tree
        left = queryTree(2*node, s, midpoint)
        # recurse right tree
        right = queryTree(2*node + 1, midpoint + 1, e)
        return min(left, right)
        
    return queryTree(1, 0, n-1)

def update(tree, n, i, newVal):
    def updateTree(node, s, e):
        if s == e:
            tree[node] = newVal
        else:
            midpoint = (s + e)//2
            # build left child
            if i <= midpoint:
                updateTree(2*node, s, midpoint)
            # build right child
            else:
                updateTree(2*node + 1, midpoint+1, e)
            # set values
            tree[node] = min(tree[2*node], tree[2*node + 1])
        
    updateTree(1, 0, n-1)
    return tree
    
def find_critical_periods(tree, beds, n, threshold):
    ranges = []
    def traverseTree(node, s, e):
        if s == e:
            if tree[node] < threshold:
                ranges.append([s, s])
        else:
            midpoint = (s + e) // 2
            if tree[node] >= threshold:
                return
            else:
                traverseTree(2*node, s, midpoint)
                traverseTree(2*node + 1, midpoint + 1, e)
    traverseTree(1, 0, n-1)
    return ranges

beds = [10, 8, 15, 6, 12, 9, 14]
tree = build(beds)
print(find_critical_periods(tree, beds, len(beds), 9))
