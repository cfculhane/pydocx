from pydocx.models import XmlAttribute, XmlModel


class RFonts(XmlModel):
    XML_TAG = "rFonts"

    hint = XmlAttribute(name="hint")
    ascii = XmlAttribute(name="ascii")
    h_ansi = XmlAttribute(name="hAnsi")
    east_asia = XmlAttribute(name="eastAsia")
    cs = XmlAttribute(name="cs")
    ascii_theme = XmlAttribute(name="asciiTheme")
    h_ansi_theme = XmlAttribute(name="hAnsiTheme")
    east_asia_theme = XmlAttribute(name="eastAsiaTheme")
    cs_theme = XmlAttribute(name="cstheme")

    def is_symbol(self):
        return self.h_ansi == "Symbol"
