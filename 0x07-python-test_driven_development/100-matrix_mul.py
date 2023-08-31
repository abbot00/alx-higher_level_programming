#!/usr/bin/python3
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

    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row)
               for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row)
               for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty" if len(m_a) == 0 else "m_b can't be empty")

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
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(b_rows):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
