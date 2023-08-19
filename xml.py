from xml import etree

def validate_xml(xml_filename, xsd_filename):
    xmlschema = etree.XMLSchema(file=xsd_filename)
    xml_parser = etree.XMLParser(schema=xmlschema)

    try:
        tree = etree.parse(xml_filename, xml_parser)
        print("XML document is valid.")
    except etree.XMLSyntaxError as e:
        print("XML document is not valid.")
        print("Validation errors:")
        for error in xmlschema.error_log:
            print(f"Line {error.line}, Column {error.column}: {error.message}")

if __name__ == "__main__":
    xml_file = "employees.xml"
    xsd_file = "employee_schema.xsd"
    validate_xml(xml_file, xsd_file)
