import math

def evaluate_expression(expression):
    try:
        # Replace visual symbols with Python equivalents
        expression = expression.replace('π', 'math.pi').replace('e', 'math.e')
        result = eval(expression, {'__builtins__': None}, {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'math': math
        })
        return str(round(result, 10))  # Limit decimal places
    except Exception as e:
        return f"Error: {str(e)}"