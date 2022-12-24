Problem 1
Write a function assoc_list(l) that, given a list l, returns a list of tuples where the first integer represents the element of the int list l and the second integer represents the number of occurrences of that element in the list. This associative list should not contain duplicates. Order does not matter. For example, assoc_list [1, 2, 2, 1, 3] = [(2, 2), (1, 2), (3, 1)]. You may use the reduce function for this if you wish. (We had this problem before in Assignment 2.)

from functools import reduce

def assoc_list (l):
    # YOUR CODE HERE
result = assoc_list [1; 2; 2; 1; 3]
result.sort(key=lambda x:x[0]) # sort the result list by the first element of a tuple.
assert (result == [(1,2), (2, 2), (3, 1)])


Problem 2
Write a function buckets(equiv, lst) that partitions a list into equivalence classes. That is, buckets (equiv, lst) should return a list of lists where each sublist in the result contains equivalent elements, where two elements a and b are considered equivalent if equiv (a, b) returns True. For example:

buckets (lambda a, b : a == b, [1,2,3,4]) == [[1], [2], [3], [4]]
buckets (lambda a, b : a == b, [1,2,3,4,2,3,4,3,4]) == [[1], [2, 2], [3, 3, 3], [4, 4, 4]]
buckets (lambda a, b : a % 3 == b % 3, [1,2,3,4,5,6]) == [[1, 4], [2, 5], [3, 6]]
In the examples above, we have used the key word lambda to lead to an anounymous function passed to equiv. The order of the buckets must reflect the order in which the elements appear in the original list. For example, the output of buckets (lambda a, b : a == b, [1,2,3,4]) should be [[1],[2],[3],[4]] and not [[2],[1],[3],[4]] or any other permutation.

The order of the elements in each bucket must reflect the order in which the elements appear in the original list. For example, the output of buckets (lambda a, b : a % 3 == b % 3, [1,2,3,4,5,6]) should be [[1;4],[2;5],[3;6]] and not [[4;1],[5;2],[3;6]] or any other permutations.

Assume that the comparison function equiv: ('a -> 'a -> bool) is commutative, associative and idempotent. (We had this problem before in Assignment 2.)

def buckets (equiv, lst):
     # YOUR CODE HERE
assert (buckets (lambda a, b : a == b, [1,2,3,4]) == [[1], [2], [3], [4]])
assert (buckets (lambda a, b : a == b, [1,2,3,4,2,3,4,3,4]) == [[1], [2, 2], [3, 3, 3], [4, 4, 4]])
assert (buckets (lambda a, b : a % 3 == b % 3, [1,2,3,4,5,6]) == [[1, 4], [2, 5], [3, 6]])
Trees
In Python, you can define a tree data structure using Class:

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # construct tree from a list of values `ls`
    def list_to_tree(self, ls):
        self.val = self.left = self.right = None # clear the current tree

        if not ls: # ls is None or l == []
            return # tree is None

        i = 0
        self.val = ls[i]
        queue = [self]
        while queue: # while queue is not empty
            i += 1
            node = queue.pop(0)
            if node.val is None:
                continue

            if 2*i -1 >= len(ls) or ls[2*i-1] is None:
                pass
            else:
                node.left = TreeNode(ls[2*i-1])
                queue.append(node.left)

            if 2*i >= len(ls) or ls[2*i] is None:
                pass
            else:
                node.right = TreeNode(ls[2*i])
                queue.append(node.right)
The TreeNode class contains 3 fields representing the value of a node val, its left child left and its right child right. Both left and right are instances of TreeNode. The class also contains a member function list_to_tree(self, ls) that reads a list and reinitilize an instance of the class itself to a tree as specified by the list ls. The self parameter refers to the class instance (like this in Java). The list ls represents the serialized format of a binary tree using level order traversal, where None signifies a path terminator where no node exists below. See the above code for how to create a TreeNode instance and how to access the values of its fields.

root_1 = TreeNode()
root_1.list_to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
For example, the above code creates a tree root_1 as the following:

root_2 = TreeNode()
root_2.list_to_tree([1,2,3])
As another example, the code above creates a tree root_2:

Problem 3
Given the root of a binary tree, return the level order traversal of its nodes' values, i.e., from left to right, level by level.

def levelOrder(root: TreeNode) -> List[List[int]]:
Example: the returned result of levelOrder(root_1) should be a nested list [[5], [4, 8], [11, 13, 4], [7, 2, 5, 1]]. The ith elment of the nested list is a list of tree elements at the ith level of root_1 from left to right. (We had this problem before in Assignment 3.)

def level_order(root: TreeNode):
    # YOUR CODE HERE
assert (level_order(root_1) == [[5], [4, 8], [11, 13, 4], [7, 2, 5, 1]])
assert (level_order(root_2) == [[1], [2, 3]])


Problem 4
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths, from let to right, where each path's sum equals targetSum. A leaf is a node with no children.

def pathSum(sroot: TreeNode, targetSum: int) -> List[List[int]]:
Example: the returned result of pathSum(root_1, 22) should be a nested list [[5, 4, 11, 2], [5, 8, 4, 5]], The ith element of the nested list is a list of tree elements that is the ith tree path of root_1, from let to right, whose sum equals 22.

def pathSum(root: TreeNode, targetSum: int) -> List[List[int]]:
    # YOUR CODE HERE
assert (pathSum(root_1, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]])
assert (pathSum(root_2, 4) == [[1, 3]])
