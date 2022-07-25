from pydocx.models import XmlContent, XmlModel


class Text(XmlModel):
    XML_TAG = "t"

    text = XmlContent()
