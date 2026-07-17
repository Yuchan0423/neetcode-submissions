# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        part = list()
        def add_to_encode(node, pos_str):
            encode = ""
            if node is None:
                encode = encode + pos_str
                encode = encode + "N"
            else:
                encode = encode + pos_str
                if node.val < 0:
                    encode = encode + "-"
                else:
                    encode = encode + "+"
                val = abs(node.val)
                encode = encode + str(val // 1000)
                encode = encode + str((val // 100) % 10)
                encode = encode + str((val // 10) % 10)
                encode = encode + str(val % 10)

                part.append(encode)

                add_to_encode(node.left, pos_str + "L")
                add_to_encode(node.right, pos_str + "R")

        add_to_encode(root, "X")
        return "".join(part)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def decoder(root, pos, encode):
            if encode[len(pos)] != "N" :
                sign = -1 if encode[len(pos)] == "-" else 1
                tho = encode[len(pos) + 1]
                hun = encode[len(pos) + 2]
                tens = encode[len(pos) + 3]
                ones = encode[len(pos) + 4]
                root.val = sign * ( 1000 * int(tho) + 100 * int(hun) + 10 * int(tens) + int(ones) )
                cut = len(encode) - 1
                check = 0
                for i in range(len(pos) + 5, len(encode) - len(pos)):
                    if check == 0 and encode[i] == "X" and encode[i + len(pos)] == "R":
                        cut = i
                        check = 1
                
                if len(encode) != len(pos) + 5:
                    if cut == len(pos) + 5:
                        root.right = TreeNode()
                        decoder(root.right, pos + "R", encode[cut : ])
                    elif cut == len(encode) - 1:
                        root.left = TreeNode()
                        decoder(root.left, pos + "L", encode[len(pos) + 5 : ])
                    else:
                        root.left = TreeNode()
                        root.right = TreeNode()
                        decoder(root.left, pos + "L", encode[len(pos) + 5 : cut])
                        decoder(root.right, pos + "R", encode[cut: ])
                
        node = None
        if data:
            node = TreeNode()
            decoder(node, "X", data)
        return node

