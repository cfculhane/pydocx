from pydocx.models import XmlCollection, XmlModel


class TxBxContent(XmlModel):
    XML_TAG = "txbxContent"
    children = XmlCollection(
        "wordprocessing.Paragraph",
        "wordprocessing.Table",
    )
