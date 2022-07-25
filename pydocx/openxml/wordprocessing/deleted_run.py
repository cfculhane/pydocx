from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.run import Run
from pydocx.openxml.wordprocessing.smart_tag_run import SmartTagRun


class DeletedRun(XmlModel):
    XML_TAG = "del"

    children = XmlCollection(
        Run,
        SmartTagRun,
        "wordprocessing.DeletedRun",
        # TODO Needs InsertedRun
    )
