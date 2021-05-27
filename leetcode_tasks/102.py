from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        result_list = []
        if root:
            queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                item = queue.popleft()
                level.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            result_list.append(level)
        return result_list


def main():
    pass


if __name__ == '__main__':
    main()
