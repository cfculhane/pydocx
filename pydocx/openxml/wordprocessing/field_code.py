from pydocx.models import XmlContent, XmlModel


class FieldCode(XmlModel):
    XML_TAG = "instrText"

    content = XmlContent()
