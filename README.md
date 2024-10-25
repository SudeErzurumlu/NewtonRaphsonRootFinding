# Newton-Raphson Root Finding

This project implements the Newton-Raphson method to find the roots of any differentiable function using Python.

## Project Structure

- `src/newton_raphson.py`: Contains the Newton-Raphson root-finding algorithm.
- `tests/test_newton_raphson.py`: Test cases for verifying algorithm functionality.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SudeErzurumlu/NewtonRaphsonRootFinding.git
    cd NewtonRaphsonRootFinding
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the Newton-Raphson root-finding algorithm, import `newton_raphson` and define the target function and its derivative:

```python
from src.newton_raphson import newton_raphson

f = lambda x: x**2 - 9
f_prime = lambda x: 2 * x
root = newton_raphson(f, f_prime, x0=3)
print(f"Root found: {root}")
```

## Running Tests
To run the tests, execute:

    python -m unittest discover -s tests
   

