from pydocx.models import XmlAttribute, XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.deleted_run import DeletedRun
from pydocx.openxml.wordprocessing.inserted_run import InsertedRun
from pydocx.openxml.wordprocessing.paragraph import Paragraph
from pydocx.openxml.wordprocessing.table import Table


class Footnote(XmlModel):
    XML_TAG = "footnote"

    footnote_id = XmlAttribute(name="id")

    children = XmlCollection(
        Paragraph,
        Table,
        InsertedRun,
        DeletedRun,
    )
