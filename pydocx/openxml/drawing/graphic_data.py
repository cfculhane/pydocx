from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.drawing.pictures.picture import Picture


class GraphicData(XmlModel):
    XML_TAG = "graphicData"

    picture = XmlChild(type=Picture)
