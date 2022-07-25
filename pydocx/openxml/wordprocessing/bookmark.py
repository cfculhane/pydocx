from pydocx.models import XmlAttribute, XmlModel


class Bookmark(XmlModel):
    XML_TAG = "bookmarkStart"

    name = XmlAttribute(name="name")
