from pydocx.models import XmlAttribute, XmlChild, XmlModel
from pydocx.openxml.wordprocessing.run_properties import RunProperties


class Style(XmlModel):
    XML_TAG = "style"

    style_type = XmlAttribute(name="type", default="paragraph")
    style_id = XmlAttribute(name="styleId", default="")
    name = XmlChild(attrname="val", default="")
    run_properties = XmlChild(type=RunProperties)
    parent_style = XmlChild(name="basedOn", attrname="val")

    def is_a_heading(self):
        if not self.name:
            return False
        return self.name.lower().startswith("heading")
