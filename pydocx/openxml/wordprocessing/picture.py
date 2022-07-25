from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.vml import Rect, Shape


class Picture(XmlModel):
    XML_TAG = "pict"

    children = XmlCollection(Shape, Rect)
