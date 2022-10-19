#! /usr/bin/env python3

class Node:
    def __init__(self, children_amount, metadata_amount):
        self.children_amount = children_amount
        self.metadata_amount = metadata_amount
        self.children = []
        self.metadata = []


def build_tree(array: list, shift: int = 0):
    """
    Recursively builds a tree from an array
    :param array: the list which represents nodes
    :param shift: the index which is points at the beginning of new node
    :return: a node with linked children and shift
    """
    node = Node(
        children_amount=int(array[shift]),
        metadata_amount=int(array[shift + 1])
    )
    shift += 2

    children = []
    for _ in range(node.children_amount):
        new_child, shift = build_tree(array, shift)
        children.append(new_child)
    node.children = children

    for element in array[shift:shift + node.metadata_amount]:
        node.metadata.append(int(element))
    shift += node.metadata_amount

    return node, shift


def _get_node_metadata(node: Node):
    """
    Recursively extracts metadata from node
    :param node: a node
    :return: the list with node's and its children metadata
    """
    metadata = []
    for child in node.children:
        for element in _get_node_metadata(child):
            metadata.append(element)

    for element in node.metadata:
        metadata.append(element)

    return metadata


def get_sum_of_metadata(node: Node):
    """
    Returns the sum
    :param node: a node
    :return: the sum of metadata
    """
    metadata_sum = 0
    for element in _get_node_metadata(node):
        metadata_sum += element

    return metadata_sum


def get_root_value(node: Node):
    """
    Recursively calculates a root value of a tree
    :param node: a node
    :return: the root value
    """
    value = 0
    if node.children_amount == 0:
        for element in node.metadata:
            value += element
    else:
        for element in node.metadata:
            if node.children_amount > element - 1:
                value += get_root_value(node.children[element - 1])

    return value


if __name__ == '__main__':
    with open('data.txt') as f:
        file_data = f.read()

    tree, _ = build_tree(file_data.split())

    metadata_sum = get_sum_of_metadata(tree)
    root_value = get_root_value(tree)

    print(f'Metadata sum: {metadata_sum}')
    print(f'Root node value: {root_value}')
