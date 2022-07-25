from pydocx.models import XmlContent, XmlModel


class DeletedText(XmlModel):
    XML_TAG = "delText"

    text = XmlContent()
