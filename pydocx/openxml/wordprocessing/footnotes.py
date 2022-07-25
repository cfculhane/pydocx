from pydocx.models import XmlCollection, XmlModel
from pydocx.openxml.wordprocessing.footnote import Footnote


class Footnotes(XmlModel):
    XML_TAG = "footnotes"

    children = XmlCollection(Footnote)

    def __init__(self, *args, **kwargs):
        super(Footnotes, self).__init__(*args, **kwargs)

        footnote_by_id = {}
        for footnote in self.children:
            if footnote.footnote_id:
                footnote_by_id[footnote.footnote_id] = footnote
        self._footnote_by_id = footnote_by_id

    def get_footnote_by_id(self, footnote_id):
        return self._footnote_by_id.get(footnote_id)
