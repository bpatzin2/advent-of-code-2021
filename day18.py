from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    data: Optional[str]
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


def to_tree(pair_str: str) -> Node:
    if pair_str[0] == "[":
        comma_idx = comma_index(pair_str)
        left = to_tree(pair_str[1:comma_idx])
        right = to_tree(pair_str[comma_idx + 1 : -1])
        return Node(None, left, right)
    else:
        return Node(pair_str)


def comma_index(pair_str: str) -> int:
    open_parans = 0
    i = 1
    while not (open_parans == 0 and pair_str[i] == ","):
        if pair_str[i] == "[":
            open_parans += 1
        if pair_str[i] == "]":
            open_parans -= 1
        i += 1

    return i


if __name__ == "__main__":
    s = "[1, 2]"
    node = to_tree(s)
    tree = Tree(node)
    print("\nin-order")
    tree.in_order(node)
