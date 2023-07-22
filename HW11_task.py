# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        rows = []
        rows.append('----------------')
        for row in self.data:
            rows.append(' | '.join(str(element) for element in row))
            rows.append('----------------')
        return '\n'.join(rows)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
                result = []
                for i in range(len(self.data)):
                    row = []
                    for j in range(len(self.data[i])):
                        row.append(self.data[i][j] + other.data[i][j])
                    result.append(row)
                return Matrix(result)
            else:
                print("Matrix dimensions must match for addition")
        else:
            print("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if len(self.data[0]) == len(other.data):
                result = []
                for i in range(len(self.data)):
                    row = []
                    for j in range(len(other.data[0])):
                        element = 0
                        for k in range(len(self.data[i])):
                            element += self.data[i][k] * other.data[k][j]
                        row.append(element)
                    result.append(row)
                return Matrix(result)
            else:
                print("Matrix dimensions are not compatible for multiplication")
        else:
            print("Unsupported operand type")



################################################################
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

print('Matrix1:', '\n', matrix1, '\n')
print('Matrix2:', '\n', matrix2, '\n')

print('Matrix1==Matrix2:', matrix1 == matrix2, '\n')

matrix3 = matrix1 + matrix2
print('Matrix1+Matrix2:', '\n', matrix3, '\n')

matrix4 = matrix1 * matrix2
print('Matrix1*Matrix2:', '\n', matrix4)