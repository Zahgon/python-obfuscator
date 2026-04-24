from __future__ import annotations

import random
import string
from collections.abc import Callable


class RandomDataTypeGenerator:
    """Generates random Python literal values (str or int).

    Pass a seeded :class:`random.Random` instance for reproducible output::

        gen = RandomDataTypeGenerator(rng=random.Random(42))
    """

    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()
        self._generator_options: list[Callable[[], str | int]] = [
            self.random_string,
            self.random_int,
        ]

    def get_random(self) -> str | int:
        return self._rng.choice(self._generator_options)()

    def random_string(self, length: int = 79) -> str:
        # 79 chars: see https://stackoverflow.com/a/16920876/11472374
        pass

    def random_int(self) -> int:
        pass
