#!/usr/bin/python3
""" a module that multiplies 2 matrixes"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix containing integers or floats.
        m_b (list of lists): The second matrix containing integers or floats.

    Returns:
        list of lists: A new matrix resulting from the multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list of lists containing integers or
                   or if rows of m_a and m_b are not of the same size.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be multipl
        [[7, 10], [15, 22]]
        >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        [[13, 16]]
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    # Check if m_a is empty
    if not m_a:
        raise ValueError("m_a can't be empty")
    
    # Check if m_b is empty
    if not m_b:
        raise ValueError("m_b can't be empty")
    # Check if m_a is a list of lists containing only integers or floats
    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats")
    
    # Check if m_b is a list of lists containing only integers or floats
    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or floats")
    # Check if all rows of m_a are of the same size
    row_lengths_a = set(len(row) for row in m_a)
    if len(row_lengths_a) != 1:
        raise TypeError("each row of m_a must be of the same size")

    # Check if all rows of m_b are of the same size
    row_lengths_b = set(len(row) for row in m_b)
    if len(row_lengths_b) != 1:
        raise TypeError("each row of m_b must be of the same size")
     # Check if the number of columns in m_a is equal to the number of rows in m_b
    num_columns_a = len(m_a[0])
    num_rows_b = len(m_b)
    if num_columns_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    
    a_rows = len(m_a)
    a_cols = len(m_a[0])
    b_rows = len(m_b)
    b_cols = len(m_b[0])

    for row in m_a:
        if len(row) != a_cols:
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if len(row) != b_cols:
            raise TypeError("each row of m_b must be of the same size")

    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be empty")

    result = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(b_rows):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
