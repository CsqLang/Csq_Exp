class TreeNode:
    pass

class Num(TreeNode):
    val : int | float
    stage = 0
    def __init__(self, val:int|float):
        self.val = val
    def visit(self):
        return self.val

class Str(TreeNode):
    val : str
    stage = 0
    def __init__(self, val:str):
        self.val = val
    def visit(self):
        return self.val

class BinOp(TreeNode):
    left  : TreeNode
    right  : TreeNode
    ltype = ""
    rtype = ""
    op : str

    def __init__(self,l,r,op):
        self.left = l
        self.right = r
        self.op = op
    
    def visit(self):
        if self.ltype == self.rtype:
            match self.op:
                case '+':
                    if self.ltype == 'str':
                        return self.left.visit() + self.right.visit()
                    else:
                        return self.left.visit() + self.right.visit()
                case '-':
                    if self.ltype != "str":
                        return self.left.visit() - self.right.visit()
                    else:
                        return ""
                case '*':
                    if self.ltype != "str":
                        return self.left.visit() * self.right.visit()
                    else:
                        return ""
                case '/':
                    if self.ltype != "str":
                        return Num(self.left.visit() / self.right.visit())
                    else:
                        return ""
                case '%':
                    if self.ltype != "str":
                        return self.left.visit() % self.right.visit()
                    else:
                        return ""
        else:
            return ""

def visit(ast: TreeNode):test_BinOp()
    return ast.visit()

def test_BinOp():
    left = Num(2)
    right = Num(5)
    t = BinOp(left,right,"+")
    t2 = BinOp(t,t,"+")
    print(visit(t2))
