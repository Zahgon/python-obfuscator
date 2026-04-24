from __future__ import annotations
import ast
import random
from dataclasses import dataclass
from typing import ClassVar

from ...helpers import RandomDataTypeGenerator, VariableNameGenerator
from ..base import ASTTransform, TechniqueMetadata
from ..registry import register

@dataclass(frozen=True)
class InjectionParams:
    stmts_per_scope_min: int = 3
    stmts_per_scope_max: int = 10
    cross_ref_probability: float = 0.35

@register
class DeadCodeInjector(ASTTransform):
    """Recursively injects dead variable assignments at every scope level."""
    metadata: ClassVar[TechniqueMetadata] = TechniqueMetadata(
        name="dead_code_injector",
        description="Recursively injects dead code at every scope level.",
        priority=30,
    )

    def __init__(
        self,
        rng: random.Random | None = None,
        params: InjectionParams | None = None,
    ) -> None:
        raise NotImplementedError

    def apply(self, tree: ast.Module) -> ast.Module:
        raise NotImplementedError
