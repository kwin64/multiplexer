class Mux10:
    def __init__(self, inputs):
        if len(inputs) != 10:
            raise ValueError("Должно быть 10 информационных входов")

        for value in inputs:
            if value != 0 and value != 1:
                raise ValueError("Информационные входы должны быть 0 или 1")

        self.inputs = inputs

    def select(self, A3, A2, A1, A0):

        for value in (A3, A2, A1, A0):
            if value != 0 and value != 1:
                raise ValueError("Адрес должен содержать только 0 или 1")

        index = A0 + A1 * 2 + A2 * 4 + A3 * 8

        if index >= 10:
            raise ValueError("Такого информационного входа нет")

        return self.inputs[index]

        
mux = Mux10([
        1,  # D0
        0,  # D1
        1,  # D2
        0,  # D3
        1,  # D4
        1,  # D5
        0,  # D6
        1,  # D7
        0,  # D8
        1   # D9
    ])

result = mux.select(0, 0, 1, 0)

print("Выход:", result)