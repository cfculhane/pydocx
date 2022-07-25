from pydocx.models import XmlAttribute, XmlChild, XmlModel
from pydocx.openxml.wordprocessing.body import Body


class Document(XmlModel):
    XML_TAG = "document"

    conformance = XmlAttribute(name="conformance")
    body = XmlChild(type=Body)
