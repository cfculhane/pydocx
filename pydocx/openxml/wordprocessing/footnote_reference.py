from pydocx.models import XmlAttribute, XmlModel


class FootnoteReference(XmlModel):
    XML_TAG = "footnoteReference"

    footnote_id = XmlAttribute(name="id")

    @property
    def footnote(self):
        if not self.footnote_id:
            return
        part = self.container.footnotes_part
        if not part:
            return
        footnotes = part.footnotes
        footnote = footnotes.get_footnote_by_id(footnote_id=self.footnote_id)
        return footnote
