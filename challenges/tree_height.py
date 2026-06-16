from data_structures.node import Node


def tree_height(root: Node | None) -> int:
    atual = root
    if root is None:
        return -1

    esquerda = tree_height(root.left)
    direita = tree_height(root.right)

    return 1 + max(esquerda, direita)
