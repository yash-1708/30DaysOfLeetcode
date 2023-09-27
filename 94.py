# recursive solution:
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        resPart1 = []
        resPart2 = []
        resPart3 = []

        if root is None:
            return

        if root.left:
            resPart1 = self.inorderTraversal(root.left)

        resPart2 = [root.val]

        if root.right:
            resPart3 = self.inorderTraversal(root.right)

        res = [*resPart1, *resPart2, *resPart3]

        return res

#iterative solution:
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        myStack=[]
        res=[]

        while root or myStack:
            while root:
                myStack.append(root)
                root=root.left

            root = myStack.pop()
            res.append(root.val)

            root=root.right
        
        return res   