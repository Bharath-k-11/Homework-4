import sys

def convert_to_float(value):
    """Helper function to safely convert input to float."""
    try:
        return float(value)
    except ValueError:
        return None

def calculate(num1, num2, operation):
    """Perform the specified arithmetic operation on two numbers."""
    
    # Convert inputs to floats
    float_num1 = convert_to_float(num1)
    float_num2 = convert_to_float(num2)
    
    if float_num1 is None or float_num2 is None:
        return f"Invalid number input: {num1} or {num2} is not a valid number."

    # Perform the operation
    if operation == "add":
        result = float_num1 + float_num2
    elif operation == "subtract":
        result = float_num1 - float_num2
    elif operation == "multiply":
        result = float_num1 * float_num2
    elif operation == "divide":
        if float_num2 == 0:
            return "An error occurred: Cannot divide by zero"
        result = float_num1 / float_num2
    else:
        return f"Unknown operation: {operation}"

    # Format result: If it's an integer, return without ".0"
    formatted_result = int(result) if result.is_integer() else result
    return f"The result of {num1} {operation} {num2} is equal to {formatted_result}"

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
    else:
        num1, num2, operation = sys.argv[1], sys.argv[2], sys.argv[3]
        print(calculate(num1, num2, operation))
