
from phplex import analyze_code
from phpparser import parse

# Define interactive mode to interpret and process PHP code
def interpret_code(code):
    """Function to analyze and interpret input PHP code."""
    # First, analyze the code using lexer (to get the tokens)
    tokens = analyze_code(code)
    
    # Now, parse the code using the parser
    result = parse(code)
    
    # Return the result of the interpretation
    return result

# Function to start interactive mode
def start_interactive_mode():
    """Interactive mode to run PHP-like code."""
    print("PHP Interactive Mode")
    print("Enter PHP code to interpret. Type 'exit' to quit.")
    
    while True:
        try:
            # Prompt the user to enter PHP code
            code = input('PHP> ')
            
            if code.lower() == 'exit':
                print("Exiting PHP Interactive Mode.")
                break
            
            # If the code is empty, continue to the next prompt
            if not code.strip():
                continue
            
            # Pass the entered code to interpret
            result = interpret_code(code)
            
            # Display the result (if any)
            if result:
                print(result)
            else:
                print("No output or result from code.")
        
        except Exception as e:
            print(f"Error: {str(e)}")

# Main entry point
if __name__ == '__main__':
    start_interactive_mode()
