from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.deleted_run import DeletedRun
from pydocx.openxml.wordprocessing.inserted_run import InsertedRun
from pydocx.openxml.wordprocessing.paragraph import Paragraph
from pydocx.openxml.wordprocessing.table import Table


class SdtContentBlock(XmlModel):
    XML_TAG = "sdtContent"

    children = XmlCollection(
        Paragraph,
        Table,
        InsertedRun,
        DeletedRun,
        # SdtBlock,
    )
