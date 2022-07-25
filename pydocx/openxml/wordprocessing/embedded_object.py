from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.vml.shape import Shape


class EmbeddedObject(XmlModel):
    """
    reference:  https://msdn.microsoft.com/en-us/library/documentformat.openxml
    .wordprocessing.embeddedobject%28v=office.15%29.aspx
    """

    XML_TAG = "object"

    children = XmlCollection(Shape)
