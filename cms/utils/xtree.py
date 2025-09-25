import xml.etree.ElementTree as ET

def root_element(ns, root_elem):
    for namespace in ns:
        ET.register_namespace("", namespace)
    root = ET.Element(root_elem)
    for namespace in ns:
        root.set("xmlns", namespace)
    return root

def child_element(parent, child, innerText=None):
    child = ET.SubElement(parent, child)
    if innerText:
        child.text = innerText
    return child
