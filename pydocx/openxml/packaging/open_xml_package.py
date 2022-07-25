from pydocx.openxml.packaging.open_xml_part_container import (  # noqa
    OpenXmlPartContainer,
)
from pydocx.packaging import ZipPackage


class OpenXmlPackage(OpenXmlPartContainer):
    """
    Creates a ZipPackage and manages package-level OpenXmlParts.

    See also: http://msdn.microsoft.com/en-us/library/documentformat.openxml.packaging.openxmlpackage%28v=office.14%29.aspx  # noqa
    """

    def __init__(self, path):
        super(OpenXmlPackage, self).__init__()
        self.package = ZipPackage(path=path)
