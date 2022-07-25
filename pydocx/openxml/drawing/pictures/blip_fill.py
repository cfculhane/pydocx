from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.drawing.blip import Blip


class BlipFill(XmlModel):
    XML_TAG = "blipFill"

    blip = XmlChild(type=Blip)
