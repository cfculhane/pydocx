from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.wordprocessing.sdt_content_block import SdtContentBlock


class SdtBlock(XmlModel):
    XML_TAG = "sdt"

    content = XmlChild(type=SdtContentBlock)
