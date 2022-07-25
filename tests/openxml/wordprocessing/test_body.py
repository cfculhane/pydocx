from unittest import TestCase

from pydocx.openxml.wordprocessing import Body
from pydocx.util.xml import parse_xml_from_string


class BodyTestCase(TestCase):
    def _load_from_xml(self, xml):
        root = parse_xml_from_string(xml)
        return Body.load(root)
