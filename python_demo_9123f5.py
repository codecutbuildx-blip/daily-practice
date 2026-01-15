# Learning Objective: Develop an interactive command-line interface (CLI) tool
# that effectively uses `argparse` for robust argument parsing and `rich` for
# producing beautiful, structured, and informative output. This tutorial focuses
# on creating a simple 'greeter' tool that can be customized via arguments.

import argparse
import sys # Used here only to demonstrate a timestamp from execution context
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

def main():
    """
    The main function where our CLI tool's logic resides.
    It handles argument parsing and generates rich output.
    """

    # --- Step 1: Initialize ArgumentParser ---
    # Create an ArgumentParser object. This object will hold all the information
    # needed to parse the command line arguments into Python data types.
    # The 'description' argument is displayed when the user asks for help
    # (e.g., by running `python your_script_name.py --help`).
    parser = argparse.ArgumentParser(
        description="A customizable greeter CLI tool using argparse and rich."
    )

    # --- Step 2: Define Arguments ---
    # Add various types of arguments to demonstrate argparse capabilities.

    # 1. Positional Argument: 'name'
    # This argument is required and its position on the command line matters.
    # The user must provide a name directly after the script name.
    parser.add_argument(
        "name", # No leading '-' or '--' means it's a positional argument.
        help="The name of the person to greet." # Help message for this argument.
    )

    # 2. Optional Argument with a default value: '--message'
    # This argument allows the user to customize the greeting message.
    # If the user doesn't provide this argument, the 'default' value will be used.
    parser.add_argument(
        "--message", # Leading '--' denotes an optional argument (a long option).
        type=str,    # Specifies that the argument's value should be treated as a string.
        default="Hello", # The value to use if this argument is not specified.
        help="The greeting message to use (e.g., 'Hi', 'Welcome')."
    )

    # 3. Boolean Flag: '--show-details'
    # This is a common pattern for "on/off" or "true/false" arguments.
    # If the flag is present on the command line, `args.show_details` will be `True`.
    # If the flag is absent, it will be `False` (this is the default for `store_true`).
    parser.add_argument(
        "--show-details",
        action="store_true", # This action automatically sets the argument to True if present.
        help="Display additional details about the greeting process."
    )

    # 4. Optional Argument with choices: '--level'
    # This argument restricts the user's input to a predefined set of values,
    # making your CLI more robust and preventing invalid inputs.
    parser.add_argument(
        "--level",
        choices=["info", "warning", "error"], # A list of valid options the user can provide.
        default="info",                      # The default choice if the argument is not specified.
        help="Set the display level for the greeting (info, warning, error)."
    )

    # --- Step 3: Parse the Arguments ---
    # Call `parse_args()` to process the command-line arguments provided by the user.
    # This method parses `sys.argv` (the list of command-line arguments) and returns
    # an object where each argument is stored as an attribute (e.g., `args.name`, `args.message`).
    args = parser.parse_args()

    # --- Step 4: Prepare Rich Console for Output ---
    # Create a `Console` object from the `rich` library.
    # This is the primary way to print styled content to the terminal, offering
    # powerful features like colors, styles, and structured rendering.
    console = Console()

    # --- Step 5: Generate Structured and Beautiful Output using Rich ---

    # Display a main greeting using a `rich.Panel` for clear separation and styling.
    # Panels automatically add borders and padding, making output look professional and organized.
    greeting_panel = Panel(
        # f-string for easy text formatting. Rich supports styling directly within strings.
        f"[bold blue]{args.message}, {args.name}![/bold blue]\n\n"
        f"We're delighted to have you here.",
        title=f"[bold green]Greeter Tool - Level: {args.level.upper()}[/bold green]", # Panel title with style.
        subtitle="Powered by argparse & rich", # Optional subtitle for the panel.
        border_style="dim yellow", # Customize the border color and style.
        expand=False # Setting to False makes the panel fit its content, not fill the entire terminal width.
    )
    console.print(greeting_panel) # Print the styled panel to the console.

    # Conditionally display additional details based on the `--show-details` flag.
    if args.show_details:
        console.print("\n[bold magenta]--- Additional Details ---[/bold magenta]")

        # Use `rich.Markdown` for formatted text within the details section.
        # This allows for easy inclusion of headings, bullet points, code blocks, etc.,
        # leveraging Markdown syntax for rich text formatting.
        details_markdown = Markdown(f"""
        # Greeting Summary
        *   **Name greeted:** `{args.name}`
        *   **Custom message used:** `{args.message}`
        *   **Display level:** `{args.level}`
        *   **Timestamp:** `{sys.argv[0].split('/')[-1]} was run at {console.get_datetime().strftime('%Y-%m-%d %H:%M:%S')}`
        """)
        console.print(details_markdown) # Print the Markdown content.

        # Example of conditional styling based on the 'level' argument.
        # This demonstrates how argument values can directly influence output presentation.
        if args.level == "warning":
            console.print("[yellow]Warning: This is a special warning-level greeting.[/yellow]")
        elif args.level == "error":
            console.print("[red bold]Error: Critical attention required for this greeting![/red bold]")
        else: # For 'info' level or any other unhandled case.
            console.print("[green]Info: Standard information level details.[/green]")

    # --- Step 6: Example Usage Instructions ---
    # Provide clear examples for the user to try after running the script.
    # This helps users quickly understand how to interact with your CLI tool.
    console.print("\n[bold underline]Try these commands:[/bold underline]")
    # Make sure to replace 'my_greeter.py' with the actual filename if you save it differently.
    console.print("  [green]python my_greeter.py Alice[/green]")
    console.print("  [green]python my_greeter.py Bob --message 'Welcome back'[/green]")
    console.print("  [green]python my_greeter.py Charlie --show-details --level warning[/green]")
    console.print("  [green]python my_greeter.py --help[/green]")


# This `if __name__ == "__main__":` block is a standard Python idiom.
# It ensures that the `main()` function is called only when the script is executed directly
# (e.g., `python my_greeter.py`), not when it's imported as a module into another script.
if __name__ == "__main__":
    main()