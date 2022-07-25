from pydocx.models import XmlCollection, XmlModel


class Textbox(XmlModel):
    XML_TAG = "textbox"

    children = XmlCollection(
        "wordprocessing.TxBxContent",
    )
