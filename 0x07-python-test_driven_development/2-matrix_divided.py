def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix: initial 2D list
        div: integer which is the divisor

    Returns:
        New matrix containing the divided elements
        rounded to 2 decimal places
    """
    error_mess = ("matrix must be a matrix (list of lists)"
                  " of integers/floats")
    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError(error_mess)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(elem, (int, float)) for row in matrix
               for elem in row):
        raise TypeError(error_mess)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
