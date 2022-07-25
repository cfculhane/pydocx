from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.drawing.transform_2d import Transform2D


class ShapeProperties(XmlModel):
    XML_TAG = "spPr"

    xfrm = XmlChild(type=Transform2D)
