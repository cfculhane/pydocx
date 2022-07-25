from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.drawing.graphic import Graphic


class Anchor(XmlModel):
    XML_TAG = "anchor"

    graphic = XmlChild(type=Graphic)
