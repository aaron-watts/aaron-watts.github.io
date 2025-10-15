import xml.etree.ElementTree as ET


def add_xsl(xml_file, xsl_path):
    """
    Adds an XSL style instruction based on xsl_path to an xml_file
    """
    with open(xml_file, "r") as inf:
        contents = inf.readlines()

    transform = f'<?xml-stylesheet href="{xsl_path}" type="text/xsl"?>\n'
    contents.insert(1, transform)

    with open(xml_file, "w") as outf:
        contents = "".join(contents)
        outf.write(contents)


def root_element(ns, root_elem):
    """
    Return root element of an XML tree as object
    """
    for namespace in ns:
        ET.register_namespace("", ns[namespace])
    root = ET.Element(root_elem)
    for namespace in ns:
        nsid = "xmlns"
        if len(namespace) > 0:
            nsid += f":{namespace}"
        root.set(nsid, ns[namespace])
    return root


def child_element(parent, child, innerText=None):
    """
    Return child element of an XML tree as object
    """
    child = ET.SubElement(parent, child)
    if innerText:
        child.text = innerText
    return child


def set_attribute(elem, attr, val):
    """
    Set version for XML element
    """
    elem.set(attr, val)
    return elem
