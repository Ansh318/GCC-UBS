def data_encryption_solution():
    result = {'answer':[]}
    for i in range(len(input_data)):
        input_data[i] = input_data[i].replace(" ", "")
        input_str = input_data[i]
        encrypt_str = encrypted(input_str)
        result['answer'].append(encrypt_str)
    return result

def encrypted(input_string):
    matrix_rows = math.floor(math.sqrt(len(input_string)))
    matrix_cols = math.ceil(math.sqrt(len(input_string)))
     # Ensure rows * columns >= string_length
    while matrix_rows * matrix_cols < len(input_string):
        matrix_rows += 1
    # Initialize the matrix
    matrix = [[''] * matrix_cols for _ in range(matrix_rows)]
    k = 0
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            if k < len(input_string):
                matrix[i][j] = input_string[k]
                k += 1
    result = ''
    for j in range(matrix_cols):
        for i in range(matrix_rows):
            if matrix[i][j] != ' ':
                result += matrix[i][j]
        result += ' '

    return result.strip()
