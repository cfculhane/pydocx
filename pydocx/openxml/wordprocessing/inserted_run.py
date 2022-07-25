from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.run import Run
from pydocx.openxml.wordprocessing.smart_tag_run import SmartTagRun


class InsertedRun(XmlModel):
    XML_TAG = "ins"

    children = XmlCollection(
        Run,
        SmartTagRun,
        "wordprocessing.InsertedRun",
        # TODO Needs DeletedRun
    )
