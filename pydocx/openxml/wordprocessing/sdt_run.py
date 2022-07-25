from pydocx.models import XmlChild, XmlModel
from pydocx.openxml.wordprocessing.sdt_content_run import SdtContentRun


class SdtRun(XmlModel):
    XML_TAG = "sdt"

    content = XmlChild(type=SdtContentRun)
