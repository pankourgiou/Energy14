from guppylang import guppy
from guppylang.std.quantum import qubit, h, measure

@guppy
def demo() -> None:
    q = qubit()
    h(q)
    result = measure(q)
