from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.drawing.graphic import Graphic


class Inline(XmlModel):
    XML_TAG = "inline"

    graphic = XmlChild(type=Graphic)
