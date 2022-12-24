from typing import List
from functools import reduce
import sys
import traceback
import collections
#################
### Problem  1 ##
#################

def assoc_list (l):
    tuple_list = [(0,0)]   
    counter = 1
    for i in l:
        for k in tuple_list:
            curr_indx = tuple_list.index(k)
            target = i
            if k[0]==target:
                b = k[1]
                tuple_list.remove(k)
                tuple_list.append((target, b+1))
                break
            elif(curr_indx==len(tuple_list)-1):
                tuple_list.append((target, 1))  
                counter += 1
                break
            else:
                continue
    tuple_list.remove((0,0))     
    return tuple_list
#################
### Problem  2 ##
#################

def buckets (f, l):
    new_list = [] 
    bool_flag = False
    for i in l: 
        for j in new_list:
            if f(i, j[0]): 
                j.append(i)
                bool_flag = True
                break
        if bool_flag == False:
            new_list.append([i])
            bool_flag - False
    return new_list


###################################
# Definition for a binary tree node
###################################

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


#################
### Problem  3 ##
#################

def level_order(root: TreeNode):  
    depth_res = depth(root)
    list = []
    if(depth_res == 0):
        return list
    else:
        queue = collections.deque()
        queue.append(root)
        for i in range(depth_res):
            queue_size = len(queue)
            temp = []

            while queue_size > 0:
                temp_node = queue.popleft()
                temp.append(temp_node.val)
                queue_size -= 1

                if temp_node.left != None:
                    queue.append(temp_node.left)
                if temp_node.right != None:
                    queue.append(temp_node.right)
            list.append(temp)
        return list
    
def depth(r):
    if r == None:
        return 0
    else:
        left_tree = depth(r.left)
        right_tree = depth(r.right)

        if left_tree > right_tree:
            return left_tree + 1
        else:
            return right_tree + 1

#################
### Problem  4 ##
#################

def pathSum(root: TreeNode, targetSum: int) -> List[List[int]]:
    result = []
    if root == None:
        return result
    elif root.val == targetSum:
        result.append([root.val])
        return result
    else:
        tmp_lst = []
        rec_target(root, targetSum, result, tmp_lst)
    return result
def rec_target(rt, target, list, tmp):
    if rt.val == target and rt.left == None and rt.right == None:
        tmp.append(rt.val)
        tmp1 = []
        for i in tmp:
            tmp1.append(i)
        list.append(tmp1)
        tmp.pop()
    else:
        tmp.append(rt.val)
        if rt.left != None:
            rec_target(rt.left, (target - rt.val), list, tmp)
        if rt.right != None:
            rec_target(rt.right, (target - rt.val), list, tmp)
        tmp.pop()
    return list



#################
### Test cases ##
#################

def main():
    print ("Testing your code ...")
    error_count = 0

    # Testcases for Problem 1
    try:
        result = assoc_list([1, 2, 2, 1, 3])
        result.sort(key=lambda x:x[0])
        assert (result == [(1,2), (2, 2), (3, 1)])

        result = assoc_list(["a","a","b","a"])
        result.sort(key=lambda x:x[0])
        assert (result == [("a",3), ("b",1)])

        result = assoc_list([1, 7, 7, 1, 5, 2, 7, 7])
        result.sort(key=lambda x:x[0])
        assert (result == [(1,2), (2,1), (5,1), (7,4)])
    except AssertionError as err:
        error_count += 1
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
    except:
        error_count += 1
        print("Unexpected error:", sys.exc_info()[0])
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)

    # Testcases for Problem 2
    try:
        assert (buckets (lambda a, b : a == b, [1,2,3,4]) == [[1], [2], [3], [4]])
        assert (buckets (lambda a, b : a == b, [1,2,3,4,2,3,4,3,4]) == [[1], [2, 2], [3, 3, 3], [4, 4, 4]])
        assert (buckets (lambda a, b : a % 3 == b % 3, [1,2,3,4,5,6]) == [[1, 4], [2, 5], [3, 6]])
    except AssertionError as err:
        error_count += 1
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
    except:
        error_count += 1
        print("Unexpected error:", sys.exc_info()[0])
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)

    ### Specify 3 trees for testing problems 3 & 4
    root_1 = TreeNode()
    root_1.list_to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])

    root_2 = TreeNode()
    root_2.list_to_tree([1,2,3])

    root_3 = TreeNode()
    root_3.list_to_tree([1,2])

    # Testcases for Problem 3
    try:
        assert (level_order(root_1) == [[5], [4, 8], [11, 13, 4], [7, 2, 5, 1]])
        assert (level_order(root_2) == [[1], [2, 3]])
        assert (level_order(root_3) == [[1], [2]])
    except AssertionError as err:
        error_count += 1
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
    except:
        error_count += 1
        print("Unexpected error:", sys.exc_info()[0])
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)

    # Testcases for Problem 4
    try:
        assert (pathSum(root_1, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]])
        assert (pathSum(root_2, 4) == [[1, 3]])
        assert (pathSum(root_3, 0) == [])
    except AssertionError as err:
        error_count += 1
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
    except:
        error_count += 1
        print("Unexpected error:", sys.exc_info()[0])
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)

    print (f"{error_count} out of 4 programming questions are incorrect.")

main()
