from multiplexer import Mux10
from faults import (
    output_stuck,
    invert_output,
    address_stuck,
    data_input_stuck,
    wrong_input
)

inputs = [
    0,  # D0
    1,  # D1
    0,  # D2
    1,  # D3
    0,  # D4
    1,  # D5
    0,  # D6
    1,  # D7
    0,  # D8
    1   # D9
]


# Создаём обычный мультиплексор
mux = Mux10(inputs)

def test_output_stuck_at_0():

    # Выбираем D1
    # D1 = 1
    result = mux.select(0, 0, 0, 1)

    # Вносим неисправность:
    # выход постоянно равен 0
    faulty_result = output_stuck(result, 0)

    assert faulty_result == 0

def test_output_stuck_at_1():

    # Выбираем D0
    # D0 = 0
    result = mux.select(0, 0, 0, 0)

    # Вносим неисправность:
    # выход постоянно равен 1
    faulty_result = output_stuck(result, 1)

    assert faulty_result == 1

def test_inverted_output():
    # Выбираем D1
    # D1 = 1
    result = mux.select(0, 0, 0, 1)

    # Инвертируем выход
    faulty_result = invert_output(result)

    # 1 должен превратиться в 0
    assert faulty_result == 0

def test_A0_stuck_at_0():

    # Изначальный адрес:
    #
    # A3 A2 A1 A0
    #  0  0  0  1
    #
    # Это D1

    A3 = 0
    A2 = 0
    A1 = 0
    A0 = 1

    # A0 становится постоянно 0
    A3, A2, A1, A0 = address_stuck(
        A3,
        A2,
        A1,
        A0,
        bit=0,
        value=0
    )

    # Теперь адрес:
    #
    # 0000
    #
    # Выбирается D0
    result = mux.select(A3, A2, A1, A0)

    assert result == 0

def test_D5_stuck_at_0():

    # Адрес:
    #
    # 0101
    #
    # Это D5

    result = mux.select(0, 1, 0, 1)

    # D5 в нормальном состоянии = 1
    assert result == 1

    # Вносим неисправность D5:
    # D5 постоянно равен 0

    faulty_result = data_input_stuck(
        index=5,
        result=result,
        faulty_input=5,
        value=0
    )

    assert faulty_result == 0

def test_wrong_input():

    # Нормально выбран D5
    index = 5

    # Из-за неисправности выбирается следующий вход
    faulty_index = wrong_input(index)

    # Вместо D5 должен быть выбран D6
    assert faulty_index == 6
