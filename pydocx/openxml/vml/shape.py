from pydocx.models import XmlAttribute, XmlCollection, XmlModel
from pydocx.openxml.vml.image_data import ImageData


class Shape(XmlModel):
    XML_TAG = "shape"

    style = XmlAttribute()
    children = XmlCollection(ImageData, "vml.Textbox")

    # TODO perhaps we could have a prepare_style, or clean_style convention?
    def get_style(self):
        if self.style:
            return dict(item.split(":", 1) for item in self.style.split(";") if item)
        return {}
