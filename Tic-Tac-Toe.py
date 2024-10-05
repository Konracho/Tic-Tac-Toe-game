class MyMatrix:
    def __init__(self, input_str: str):
        self.matrix = self.bild_matrix(input_str)
        self.input = input_str

    def bild_matrix(self, input_str: str):
        length_matr = round(len(input_str) ** 0.5)
        list_input = []
        for i in range(0, len(input_str), length_matr):
            list_input1 = []
            for j in input_str[i: i + length_matr]:
                list_input1.append(j)
            list_input.append(list_input1)
        return list_input

    def print_matrix(self):
        print('---------')
        for i in self.matrix:
            print(f"| {' '.join(i)} |")
        print('---------')

    def exam_str(self):
        for i in self.matrix:

            if all(j == i[0] and j != ' ' for j in i):
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

            if all(j == output_stolb[0] and j != ' ' for j in output_stolb):
                return (f"{output_stolb[0]} wins")

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

        if all(j == diag_L_R[0] and j != ' ' for j in diag_L_R):
            return (f"{diag_L_R[0]} wins")

        if all(j == diag_R_L[0] and j != ' ' for j in diag_R_L):
            return (f"{diag_R_L[0]} wins")


    def draw(self):
        no_elem = 0

        for row in self.matrix:
            for i in row:
                if i == ' ':
                    no_elem += 1

        if no_elem == 0:
            return (f'Draw')

    def exams(self):
        if self.exam_str():
            return self.exam_str()

        elif self.exam_diag():
            return self.exam_diag()

        elif self.exam_stolb():
            return self.exam_stolb()

        elif self.draw():
            return self.draw()

def main():
    obj = MyMatrix('         ')
    obj.print_matrix()
    n = 1
    while True:
        player = input().split(' ')

        if player[0].isdigit() == False or player[1].isdigit() == False:
            print(f'You should enter numbers!')
            continue
        else:
            if int(player[0]) > 3 or int(player[1]) > 3:
                print(f'Coordinates should be from 1 to 3!')
                continue
            else:
                stroka = int(player[0]) - 1
                stolb = int(player[1]) - 1

        if n % 2 != 0:

            if obj.matrix[stroka][stolb] == 'X' or obj.matrix[stroka][stolb] == 'O':
                print(f'This cell is occupied! Choose another one!')
                continue

            obj.matrix[stroka][stolb] = 'X'
            obj.print_matrix()

            if obj.exams():
                print(obj.exams())
                return

        else:
            if obj.matrix[stroka][stolb] == 'X' or obj.matrix[stroka][stolb] == 'O':
                print(f'This cell is occupied! Choose another one!')
                continue

            obj.matrix[stroka][stolb] = 'O'
            obj.print_matrix()

            if obj.exams():
                print(obj.exams())
                return

        n += 1

if __name__ == '__main__':
    main()
