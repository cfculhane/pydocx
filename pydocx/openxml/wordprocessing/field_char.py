from pydocx.models import XmlAttribute, XmlModel


class FieldChar(XmlModel):
    XML_TAG = "fldChar"

    _char_type = XmlAttribute(name="fldCharType")

    @property
    def char_type(self):
        if not self._char_type:
            return
        return self._char_type.lower()

    def is_type_begin(self):
        return self.char_type == "begin"

    def is_type_separate(self):
        return self.char_type == "separate"

    def is_type_end(self):
        return self.char_type == "end"
