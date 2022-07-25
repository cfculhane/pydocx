from pydocx.models import XmlChild, XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.deleted_run import DeletedRun
from pydocx.openxml.wordprocessing.inserted_run import InsertedRun
from pydocx.openxml.wordprocessing.paragraph import Paragraph
from pydocx.openxml.wordprocessing.sdt_block import SdtBlock
from pydocx.openxml.wordprocessing.section_properties import SectionProperties
from pydocx.openxml.wordprocessing.table import Table


class Body(XmlModel):
    XML_TAG = "body"

    children = XmlCollection(
        Paragraph,
        Table,
        InsertedRun,
        DeletedRun,
        SdtBlock,
    )

    final_section_properties = XmlChild(type=SectionProperties)
