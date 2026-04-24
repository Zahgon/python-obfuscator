import sys
from pathlib import Path
from typing import Annotated

import typer

from python_obfuscator.config import ObfuscationConfig
from python_obfuscator.obfuscator import Obfuscator
from python_obfuscator.techniques import all_technique_names
from python_obfuscator.version import __version__

DEFAULT_OUTPUT_DIR = "obfuscated"


def _resolved_output_path(input_path: Path) -> Path:
    """Write under ./obfuscated/, preserving path relative to cwd when possible."""
    pass


def main(
    input_path: Annotated[
        Path,
        typer.Option(
            ...,
            "--input",
            "-i",
            help="File to obfuscate",
            exists=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    stdout: Annotated[
        bool,
        typer.Option(
            "--stdout",
            help="Print obfuscated code to stdout instead of writing a file.",
        ),
    ] = False,
    disable: Annotated[
        list[str],
        typer.Option(
            "--disable",
            "-d",
            help=(
                "Disable a technique by name.  May be repeated.  "
                f"Available: {', '.join(sorted(all_technique_names()))}"
            ),
        ),
    ] = [],
) -> None:
    pass


def cli() -> None:
    pass
