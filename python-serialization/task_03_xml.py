#!/usr/bin/python3
"""Serialize a Python dictionary into XML and deserialize it back."""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("root")
        for key, subdict in dictionary.items():
            child = ET.SubElement(root, key)
            if isinstance(subdict, dict):
                for subkey, subvalue in subdict.items():
                    subchild = ET.SubElement(child, subkey)
                    subchild.text = str(subvalue)
            else:
                child.text = str(subdict)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            if list(child):
                subdict = {}
                for subchild in child:
                    subdict[subchild.tag] = subchild.text
                result[child.tag] = subdict
            else:
                result[child.tag] = child.text
        return result
    except Exception:
        return None
