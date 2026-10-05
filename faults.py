# неисправности выхода
def output_stuck(result, value):
    # выход постоянно находится в заданном состоянии.
    # value = 0 -> stuck-at-0
    # value = 1 -> stuck-at-1
    return value

def invert_output(result):
    # Инверсия выходного сигнала.
    return 1 - result

# неисправности адресных входов
def address_stuck(A3, A2, A1, A0, bit, value):
    # один из адресных входов постоянно находится в заданном состоянии.
    address = [A3, A2, A1, A0]
    address[3 - bit] = value

    return tuple(address)


# неисправности информационного входа 
def data_input_stuck(index, result, faulty_input, value):
    # определённый информационный вход постоянно находится в заданном состоянии.
    if index == faulty_input:
        return value

    return result


# неисправности выбора входа 
def wrong_input(index, number_of_inputs=10):
    # вместо выбранного входа выбирается следующий.
    index = index + 1
    if index >= number_of_inputs:
        index = 0

    return index