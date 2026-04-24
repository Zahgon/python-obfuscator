from __future__ import annotations
import ast
from typing import ClassVar

from ..base import ASTTransform, TechniqueMetadata
from ..registry import register

@register
class ExecWrapper(ASTTransform):
    """Replaces the module body with a single exec('...') call."""
    metadata: ClassVar[TechniqueMetadata] = TechniqueMetadata(
        name="exec_wrapper",
        description="Replaces the module body with a single exec('...') call.",
        priority=100,
    )

    def apply(self, tree: ast.Module) -> ast.Module:
        raise NotImplementedError
