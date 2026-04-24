from __future__ import annotations
import ast
from abc import ABC
from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class TechniqueMetadata:
    name: str
    description: str
    priority: int  # lower numbers run first

class ASTTransform(ast.NodeTransformer, ABC):
    """Base for all obfuscation transforms."""
    metadata: ClassVar[TechniqueMetadata]

    def apply(self, tree: ast.Module) -> ast.Module:
        raise NotImplementedError
