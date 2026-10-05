from multiplexer import Mux10

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

mux = Mux10(inputs)

def test_all_inputs():

    assert mux.select(0, 0, 0, 0) == 0  # D0
    assert mux.select(0, 0, 0, 1) == 1  # D1
    assert mux.select(0, 0, 1, 0) == 0  # D2
    assert mux.select(0, 0, 1, 1) == 1  # D3
    assert mux.select(0, 1, 0, 0) == 0  # D4
    assert mux.select(0, 1, 0, 1) == 1  # D5
    assert mux.select(0, 1, 1, 0) == 0  # D6
    assert mux.select(0, 1, 1, 1) == 1  # D7
    assert mux.select(1, 0, 0, 0) == 0  # D8
    assert mux.select(1, 0, 0, 1) == 1  # D9

    print("Все 10 входов: OK")


def test_invalid_addresses():

    invalid_addresses = [
        (1, 0, 1, 0),  # 1010
        (1, 0, 1, 1),  # 1011
        (1, 1, 0, 0),  # 1100
        (1, 1, 0, 1),  # 1101
        (1, 1, 1, 0),  # 1110
        (1, 1, 1, 1)   # 1111
    ]

    for address in invalid_addresses:

        try:
            mux.select(*address)

        except ValueError:
            pass

        else:
            raise AssertionError(
                f"Адрес {address} должен быть недопустимым"
            )

    print("Недопустимые адреса: OK")

def test_invalid_number_of_inputs():

    try:
        Mux10([0, 1, 0])

    except ValueError:
        pass

    else:
        raise AssertionError(
            "Мультиплексор должен отклонять не 10 входов"
        )

    print("Проверка количества входов: OK")


def test_invalid_input_values():

    try:
        Mux10([
            0, 1, 0, 1, 0,
            1, 0, 1, 0, 2
        ])

    except ValueError:
        pass

    else:
        raise AssertionError(
            "Мультиплексор должен отклонять значения кроме 0 и 1"
        )

    print("Проверка значений входов: OK")

def test_invalid_address_values():

    invalid_addresses = [
        (2, 0, 0, 0),
        (0, 2, 0, 0),
        (0, 0, 2, 0),
        (0, 0, 0, 2)
    ]

    for address in invalid_addresses:

        try:
            mux.select(*address)

        except ValueError:
            pass

        else:
            raise AssertionError(
                f"Адрес {address} должен быть недопустимым"
            )

    print("Проверка значений адреса: OK")
