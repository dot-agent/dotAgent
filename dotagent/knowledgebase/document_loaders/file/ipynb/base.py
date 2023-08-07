import re
from pathlib import Path
from typing import Dict, Optional, List

from dotagent.knowledgebase.document_loaders.basereader import BaseReader
from dotagent.schema import DocumentNode


class IPYNBReader(BaseReader):
    """Ipynb file loader.

    Reads jupyter notebook files.

    """

    def __init__(
        self,
        parser_config: Optional[Dict] = None,
        concatenate: bool = False,
    ):
        """Init params."""
        self._parser_config = parser_config
        self._concatenate = concatenate

    def load_data(
        self, file: Path, extra_info: Optional[Dict] = None
    ) -> List[DocumentNode]:
        """Parse file."""

        if file.name.endswith(".ipynb"):
            try:
                import nbconvert  # noqa: F401
            except ImportError:
                raise ImportError("Please install nbconvert 'pip install nbconvert' ")
        string = nbconvert.exporters.ScriptExporter().from_file(file)[0]
        # split each In[] cell into a separate string
        splits = re.split(r"In\[\d+\]:", string)
        # remove the first element, which is empty
        splits.pop(0)

        if self._concatenate:
            docs = [DocumentNode(text="\n\n".join(splits))]
        else:
            docs = [DocumentNode(text=s) for s in splits]
        return docs
