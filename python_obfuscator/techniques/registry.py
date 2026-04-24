from __future__ import annotations
from .base import ASTTransform

_REGISTRY: dict[str, type[ASTTransform]] = {}

def register(cls: type[ASTTransform]) -> type[ASTTransform]:
    raise NotImplementedError

def all_technique_names() -> frozenset[str]:
    raise NotImplementedError

def get_transforms(enabled: frozenset[str]) -> list[type[ASTTransform]]:
    raise NotImplementedError
