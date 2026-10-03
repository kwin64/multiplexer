import random
from multiplexer import multiplexer


mux = multiplexer()

D = [random.randint(0, 1) for _ in range(10)]
A3 = random.randint(0, 1)
A2 = random.randint(0, 1)
A1 = random.randint(0, 1)
A0 = random.randint(0, 1)
mux.add_error("D2_D3_SWAP")
# D = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

result = mux.process(
    D,
    A3,
    A2,
    A1,
    A0

    # A3 = 0,
    # A2 = 0,
    # A1 = 2,
    # A0 = 0
)

print(result)