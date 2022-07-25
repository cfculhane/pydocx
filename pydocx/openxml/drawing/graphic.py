from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.drawing.graphic_data import GraphicData


class Graphic(XmlModel):
    XML_TAG = "graphic"

    graphic_data = XmlChild(type=GraphicData)
