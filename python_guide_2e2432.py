# Visualize the Abstract Syntax Tree (AST) of Python code to understand program structure.
#
# Learning Objective:
# This tutorial will guide you through the process of visualizing the Abstract Syntax Tree (AST)
# of Python code. Understanding the AST is crucial for comprehending how Python code is parsed
# and structured internally. It's a fundamental concept for anyone looking to delve deeper
# into Python's internals, write code analysis tools, or even understand how certain
# metaprogramming techniques work. We'll use Python's built-in `ast` module and a simple
# visualization library to achieve this.

import ast
import astor  # We'll use astor for a more readable AST representation, but you can also print raw node types.
            # Install it if you don't have it: pip install astor

def get_python_code_ast(code_string: str) -> ast.AST:
    """
    Parses a given Python code string and returns its Abstract Syntax Tree (AST).

    Args:
        code_string: A string containing valid Python code.

    Returns:
        An ast.AST object representing the parsed code.
    """
    try:
        # The ast.parse() function takes a string of Python code and returns an AST object.
        # This object is the root of the tree structure that represents your code.
        tree = ast.parse(code_string)
        return tree
    except SyntaxError as e:
        # It's important to handle potential syntax errors. If the code isn't valid Python,
        # ast.parse() will raise a SyntaxError.
        print(f"Error parsing code: {e}")
        return None

def print_ast_structure(node: ast.AST, indent: str = "") -> None:
    """
    Recursively prints the structure of the AST nodes. This provides a text-based
    representation of the tree.

    Args:
        node: The current AST node to print.
        indent: The string used for indentation to visually represent the tree depth.
    """
    # Get the type of the current node. For example, it could be a Module, FunctionDef, Assign, etc.
    node_type = type(node).__name__
    print(f"{indent}- {node_type}")

    # For nodes that contain other nodes (like a Module containing statements,
    # or a FunctionDef containing a body), we need to traverse them.
    # The ast module provides 'iter_child_nodes' to easily get all direct children.
    for child_node in ast.iter_child_nodes(node):
        # Recursively call print_ast_structure for each child node, increasing the indentation.
        # This creates the hierarchical visual effect.
        print_ast_structure(child_node, indent + "  ")

def get_ast_as_string(node: ast.AST) -> str:
    """
    Uses the astor library to generate a more readable string representation of the AST.
    This is often more helpful than just node types for understanding the code structure.

    Args:
        node: The root AST node.

    Returns:
        A string representation of the AST.
    """
    # astor.to_source() is a convenient way to get a Python source code-like
    # representation of the AST. It's great for debugging and understanding.
    # Note: This won't be exact source code, but a representation of the structure.
    return astor.to_source(node)

# --- Example Usage ---

if __name__ == "__main__":
    # Let's define some sample Python code to analyze.
    sample_code = """
def greet(name):
    message = f"Hello, {name}!"
    print(message)
    return len(message)

result = greet("World")
"""

    print("--- Analyzing Sample Python Code ---")
    print(sample_code)
    print("\n--- Abstract Syntax Tree (AST) Structure ---")

    # First, parse the code to get the AST.
    program_ast = get_python_code_ast(sample_code)

    if program_ast:
        # If parsing was successful, we can now explore the AST.

        # Option 1: Print a structured, hierarchical view of the node types.
        # This is good for seeing the tree shape and node categories.
        print("\n--- Text-based AST Structure ---")
        print_ast_structure(program_ast)

        # Option 2: Use astor to get a more readable string representation.
        # This often shows more detail about the content of the nodes.
        print("\n--- AST as Readable String (using astor) ---")
        print(get_ast_as_string(program_ast))

        # You can also inspect individual nodes. For example, let's find
        # all the function definitions in the AST.
        print("\n--- Finding Function Definitions ---")
        for node in ast.walk(program_ast):
            # ast.walk() is a utility that recursively yields all nodes in the tree.
            if isinstance(node, ast.FunctionDef):
                # If a node is an instance of ast.FunctionDef, it's a function definition.
                print(f"Found function: {node.name}")
                # The 'node.name' attribute holds the name of the function.

        print("\n--- Inspecting a Specific Node (e.g., the first assignment) ---")
        # Let's try to find the first assignment statement.
        for node in ast.walk(program_ast):
            if isinstance(node, ast.Assign):
                print(f"Found an assignment: {astor.to_source(node).strip()}")
                # 'node.targets' is a list of the variables being assigned to.
                # 'node.value' is the expression on the right-hand side.
                print(f"  Target(s): {[astor.to_source(t).strip() for t in node.targets]}")
                print(f"  Value: {astor.to_source(node.value).strip()}")
                break # Stop after finding the first one for demonstration.