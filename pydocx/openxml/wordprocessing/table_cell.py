from pydocx.models import XmlChild, XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.paragraph import Paragraph
from pydocx.openxml.wordprocessing.table_cell_properties import (  # noqa
    TableCellProperties,
)


class TableCell(XmlModel):
    XML_TAG = "tc"

    properties = XmlChild(type=TableCellProperties)

    children = XmlCollection(
        Paragraph,
        "wordprocessing.Table",
    )
