def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with elements
        divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists containing integers
        or floats,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
        TypeError: If rows of the matrix are not of the same size.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0, 1.5],
         [2.0, 2.5, 3.0],
         [3.5, 4.0, 4.5]]
    """

    # Check if matrix is a list of lists containing numbers
    if not all(
        isinstance(row, list) and all(isinstance(num, (int, float)) for
                                      num in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix of integers/floats")

    # Check if all rows have the same size
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide elements and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix


# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
divisor = 2
result = matrix_divided(matrix, divisor)
for row in result:
    print(row)
