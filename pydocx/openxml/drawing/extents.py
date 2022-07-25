from pydocx.models import XmlAttribute, XmlModel


class Extents(XmlModel):
    XML_TAG = "ext"

    length = XmlAttribute(name="cx")
    width = XmlAttribute(name="cy")
