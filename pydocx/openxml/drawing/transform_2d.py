from pydocx.models import XmlAttribute, XmlChild, XmlModel
from pydocx.openxml.drawing.extents import Extents


class Transform2D(XmlModel):
    XML_TAG = "xfrm"

    extents = XmlChild(type=Extents)
    rotate = XmlAttribute(name="rot", default=None)
