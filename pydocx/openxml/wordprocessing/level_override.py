from pydocx.models import XmlAttribute, XmlChild, XmlModel
from pydocx.openxml.wordprocessing.level import Level


class LevelOverride(XmlModel):
    XML_TAG = "lvlOverride"

    level_id = XmlAttribute(name="ilvl")
    start_override = XmlChild(name="startOverride", attrname="val")
    level = XmlChild(type=Level)
