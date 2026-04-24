from __future__ import annotations

import random
import string
from collections.abc import Callable


class VariableNameGenerator:
    """Generates obfuscated-looking variable names.

    Pass a seeded :class:`random.Random` instance for reproducible output::

        gen = VariableNameGenerator(rng=random.Random(42))
    """

    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()
        self._generator_options: list[Callable[[int], str]] = [
            self.random_string,
            self.l_and_i,
            self.time_based,
            self.just_id,
            self.scream,
            self.single_letter_a_lot,
        ]

    def get_random(self, id: int) -> str:
        return self._rng.choice(self._generator_options)(id)

    def random_string(self, id: int, length: int = 79) -> str:
        # 79 chars: see https://stackoverflow.com/a/16920876/11472374
        pass

    def l_and_i(self, id: int) -> str:
        pass

    def time_based(self, id: int) -> str:
        # Use the rng to produce a large pseudo-time value so that this
        # generator is fully deterministic when the rng is seeded.
        pass

    def just_id(self, id: int) -> str:
        pass

    def scream(self, id: int) -> str:
        pass

    def single_letter_a_lot(self, id: int) -> str:
        pass
