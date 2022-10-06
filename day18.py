"""
in-order, pre-order and post-order traversal of binary tree

              A
             / \
            B   C
           / \   \
          D   E   F
         / \
        G   H

    in-order
    G->D->H->B->E->A->F->C
    pre-order
    A->B->D->G->H->E->C->F
    post-order
    G->H->D->E->B->F->C->A
"""


from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    data: str
    left: Optional[Node] = None
    right: Optional[Node] = None


@dataclass
class Tree:
    root: Node

    def in_order(self, node: Optional[Node]) -> None:
        if node:
            self.in_order(node.left)
            print(node.data, end="->")
            self.in_order(node.right)


if __name__ == "__main__":
    h = Node("H")
    g = Node("G")
    f = Node("F")
    e = Node("E")
    d = Node("D", g, h)
    c = Node("C", f)
    b = Node("B", d, e)
    a = Node("A", b, c)

    tree = Tree(a)
    print("\nin-order")
    tree.in_order(a)
