from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.run import Run


class SmartTagRun(XmlModel):
    XML_TAG = "smartTag"

    children = XmlCollection(
        Run,
        "wordprocessing.SmartTagRun",
    )
