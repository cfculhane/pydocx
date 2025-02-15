from pydocx.models import XmlCollection, XmlModel


class Fallback(XmlModel):
    XML_TAG = "Fallback"

    # It would be better to refer to the grandparent's children XmlCollection
    # lazily. The problem is that we don't have a good way to represent lazy
    # fields, nor do we have a way for those fields to reference their parents
    # before they are initialized with content.
    children = XmlCollection(allow_all_children=True)
