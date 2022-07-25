from pydocx.models import XmlAttribute, XmlModel


class Blip(XmlModel):
    XML_TAG = "blip"

    embedded_picture_id = XmlAttribute(name="embed")
    linked_picture_id = XmlAttribute(name="link")
