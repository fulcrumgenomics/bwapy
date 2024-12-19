from pathlib import Path

from pysam import AlignmentHeader

ERROR_HANDLER: str
TEXT_ENCODING: str

class BwaIndex:
    header: AlignmentHeader
    def __init__(
        self, prefix: str | Path, bwt: bool = ..., bns: bool = ..., pac: bool = ...
    ) -> None: ...
