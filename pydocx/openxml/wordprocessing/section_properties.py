from pydocx.models import XmlChild, XmlModel


class SectionProperties(XmlModel):
    XML_TAG = "sectPr"

    page_size = XmlChild(name="pgSz", type=lambda el: dict(el.attrib))
