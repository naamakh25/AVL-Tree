# AVL-Tree
This project implements an AVL Tree, a self-balancing binary search tree, with added features such as rotations, node balancing, insertion, deletion, and rank selection. The AVL Tree ensures that the height difference between the left and right subtrees of any node is at most 1, providing logarithmic time complexity for insertion, deletion, and search operations.

Features
AVLNode Class:

Represents a node in the AVL tree.
Contains attributes such as key, value, height, size, and pointers to left, right, and parent nodes.
Provides various methods for accessing and modifying the node's properties, including get_key, get_height, set_left, and set_right.
Includes a method is_real_node to differentiate between real and virtual nodes.
AVLTree Class:

Represents the AVL Tree structure, containing the root node and minimum value node.
Implements core functionalities such as:
Insertion: Efficiently inserts a node while maintaining the AVL balance by performing rotations (left and right rotations).
Deletion: Deletes a node and performs necessary rebalancing.
Rank and Select: Computes the rank of a node and selects the i-th smallest element.
Tree Operations: Includes additional operations such as join, split, and rebalancing the tree when necessary.
Successor: Finds the successor of a node.
Array Conversion: Converts the AVL Tree into a sorted array.
Implements rotations to keep the tree balanced:
Left_rotation and Right_rotation adjust the tree's structure after insertion and deletion to maintain the AVL balance.
Rebalancing Operations:

The tree rebalances itself after every insertion or deletion through a series of rotations (single or double) to ensure that the height difference between left and right subtrees remains at most 1.
Additional Operations:

Split: Splits the tree into two based on a specific node.
Join: Joins two AVL trees with a given node, maintaining balance.
How to Use
Insertion:
You can insert a node into the tree with the following method:

python
Copy code
tree = AVLTree()
tree.insert(key, value)
Deletion:
To delete a node from the tree, use the delete method:

python
Copy code
tree.delete(node)
Rank and Select:
To find the rank of a node or to select the i-th smallest node, use:

python
Copy code
rank = tree.rank(node)
item = tree.select(i)
Tree Balancing:
After every insertion or deletion, the tree automatically rebalances itself, ensuring optimal time complexity for all operations.

Example
Here's an example of creating an AVL Tree, inserting nodes, and performing tree operations:

python
Copy code
tree = AVLTree()
tree.insert(10, "ten")
tree.insert(20, "twenty")
tree.insert(30, "thirty")

# Find the root of the tree
root = tree.get_root()

# Delete a node
tree.delete(root)

# Convert the tree to an array
array_representation = tree.avl_to_array()
print(array_representation)
Project Structure
AVLNode: The class representing the nodes in the AVL tree.
AVLTree: The class containing the AVL tree structure and all tree operations (insertion, deletion, rotations, and rebalancing).
