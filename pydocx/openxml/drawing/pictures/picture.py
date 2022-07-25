from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.drawing.pictures.blip_fill import BlipFill
from pydocx.openxml.drawing.pictures.shape_properties import ShapeProperties


class Picture(XmlModel):
    XML_TAG = "pic"

    shape_properties = XmlChild(type=ShapeProperties)
    blip_fill = XmlChild(type=BlipFill)
