from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.markup_compatibility.fallback import Fallback


class AlternateContent(XmlModel):
    XML_TAG = "AlternateContent"
    children = XmlCollection(Fallback)
