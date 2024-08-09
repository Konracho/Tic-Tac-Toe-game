class MyMatrix:
    def __init__(self, input_str: str):
        self.matrix = self.bild_matrix(input_str)
        self.input = input_str

    def bild_matrix(self, input_str: str):
        length_matr = round(len(input_str) ** 0.5)
        list_input = []
        for i in range(0, len(input_str), length_matr):
            list_input.append(input_str[i: i + length_matr])
        return list_input

    def print_matrix(self):
        print('---------')
        output_string = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                output_string += self.matrix[i][j]
            print(f"| {' '.join(output_string)} |")
            output_string = ''
        print('---------')

    def exam_str(self):
        for i in self.matrix:
            if all(j == i[0] for j in i):
                # print(f"{' '.join(i)}\n{i[0]} wins")
                return (f"{i[0]} wins")
            else:
                continue

    def exam_stolb(self):
        n = 0
        while n <= len(self.matrix) - 1:
            output_stolb = ''
            for i in self.matrix:
                output_stolb += i[n]
            if all(j == output_stolb[0] for j in output_stolb):
                return (f"{' '.join(output_stolb)}\n{output_stolb[0]} wins")
            n += 1

    def exam_diag(self):
        diag_L_R = ''
        diag_R_L = ''
        n = 0
        len_inv_matr = len(self.matrix) - 1
        while n <= len(self.matrix) - 1:
            diag_L_R += self.matrix[n][n]
            diag_R_L += self.matrix[n][len_inv_matr-n]
            n += 1
        # print(diag_L_R)
        # print(diag_R_L)
        if all(j == diag_L_R[0][0] for j in diag_L_R):
            # print(f"{' '.join(diag_L_R)}\n{diag_L_R[0]} wins")
            return (f"{diag_L_R[0]} wins")
        if all(j == diag_R_L[0][0] for j in diag_R_L):
            # print(f"{' '.join(diag_R_L)}\n{diag_R_L[0]} wins")
            return (f"{diag_R_L[0]} wins")

    def not_finish(self):
        # self.exam_str()
        # self.exam_stolb()
        # self.exam_diag()
        if self.impossible():
            return (self.impossible())
        else:
            for i in self.matrix:
                for j in i:
                    if j == '_':
                        return (f"Game not finished")
                break

    def draw(self):
        return ('Draw')

    def impossible(self):
        count_X = ''.join(self.matrix).count('X')
        count_O = ''.join(self.matrix).count('O')
        if count_O >= count_X + 2 or count_X >= count_O + 2:
            return ('Impossible')
        if self.input[0] == self.input[3] and self.input[0] == self.input[6]:
            if self.input[1] == self.input[4] and self.input[1] == self.input[7]:
                return ("Impossible")

def main():
    # obj = MyMatrix('XOOOXOXXO')
    obj = MyMatrix(input())
    obj.print_matrix()
    # print(obj.exam_stolb())
    # print(obj.exam_str())
    # print(obj.impossible())
    # print(obj.not_finish())
    if obj.exam_str():  # если она выполнилась
        print(obj.exam_str())
    else:
        if obj.exam_diag():
            print(obj.exam_diag())
        else:
            if obj.exam_stolb():
                if obj.impossible():
                    print(obj.impossible())
                else:
                    print(obj.exam_stolb())
            else:
                if obj.not_finish():
                    print(obj.not_finish())
                else:
                    if obj.draw():
                        print(obj.draw())

if __name__ == '__main__':
    main()
