from pydocx.models import XmlAttribute, XmlChild, XmlModel
from pydocx.openxml.wordprocessing.paragraph_properties import (  # noqa
    ParagraphProperties,
)
from pydocx.openxml.wordprocessing.run_properties import RunProperties


class Level(XmlModel):
    XML_TAG = "lvl"

    level_id = XmlAttribute(name="ilvl")
    start = XmlChild(attrname="val")
    num_format = XmlChild(name="numFmt", attrname="val")
    restart = XmlChild(name="lvlRestart", attrname="val")
    paragraph_style = XmlChild(name="pStyle", attrname="val")
    run_properties = XmlChild(type=RunProperties)
    paragraph_properties = XmlChild(type=ParagraphProperties)

    def is_bullet_format(self):
        return self.num_format == "bullet"

    def format_is_none(self):
        if not self.num_format:
            return True
        return self.num_format.lower() == "none"
