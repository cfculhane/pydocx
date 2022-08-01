from pydocx.models import XmlChild, XmlModel


class TableCellProperties(XmlModel):
    XML_TAG = "tcPr"

    grid_span = XmlChild(name="gridSpan", attrname="val")

    vertical_merge = XmlChild(name="vMerge", type=lambda el: dict(el.attrib))  # noqa

    def should_close_previous_vertical_merge(self) -> bool:
        # If vMerge is omitted, then this cell shall not be part of any
        # vertically merged grouping of cells, and any vertically merged group
        # of preceding cells shall be closed.
        if self.vertical_merge is None:
            return True
        merge = self.vertical_merge.get("val", "continue")
        if merge != "continue":
            return True
        return False
