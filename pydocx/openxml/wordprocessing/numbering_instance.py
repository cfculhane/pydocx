from pydocx.models import XmlAttribute, XmlChild, XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.level_override import LevelOverride


class NumberingInstance(XmlModel):
    XML_TAG = "num"

    num_id = XmlAttribute(name="numId")
    abstract_num_id = XmlChild(name="abstractNumId", attrname="val")

    level_overrides = XmlCollection(LevelOverride)
