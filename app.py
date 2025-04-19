import streamlit as st

def factorial(n):
    """
    Calculate the factorial of a number using iteration.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Set page config
st.set_page_config(
    page_title="Factorial Calculator",
    page_icon="🔢",
    layout="centered"
)

# Title and description
st.title("🔢 Factorial Calculator")
st.markdown("""
This app calculates the factorial of a number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
""")

# Input number
number = st.number_input(
    "Enter a number:",
    min_value=0,
    max_value=100,  # Limiting to 100 to prevent very large numbers
    value=5,
    step=1,
    help="Enter a non-negative integer to calculate its factorial"
)

# Calculate and display result
if st.button("Calculate Factorial"):
    try:
        result = factorial(number)
        st.success(f"The factorial of {number} is: {result:,}")
    except ValueError as e:
        st.error(str(e))

# Add some additional information
st.markdown("""
### How it works
- The factorial of a number n (denoted as n!) is calculated as:
  - n! = n × (n-1) × (n-2) × ... × 2 × 1
- For example:
  - 5! = 5 × 4 × 3 × 2 × 1 = 120
  - 0! = 1 (by definition)
""") 