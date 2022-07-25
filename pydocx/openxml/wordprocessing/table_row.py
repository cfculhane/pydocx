from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.table_cell import TableCell


class TableRow(XmlModel):
    XML_TAG = "tr"

    cells = XmlCollection(
        TableCell,
    )
