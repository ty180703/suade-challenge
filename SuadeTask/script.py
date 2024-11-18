import os
import argparse
from lxml import etree


def resolve_relative_path(schema_folder, schema_content):
    """
    Dynamically resolves the relative path for included schemas.

    Args:
        schema_folder (str): Path to the folder containing the schema files.
        schema_content (str): Original schema content as a string.

    Returns:
        str: Updated schema content with corrected paths.
    """
    original_path = "../../CommonTypes/v14/CommonTypes-Schema.xsd"
    resolved_path = os.path.join(schema_folder, "CommonTypes-Schema.xsd")
    
    # Replace the relative path with the actual location in the schema content
    return schema_content.replace(original_path, resolved_path)


def load_schema(schema_folder):

    schema_path = os.path.join(schema_folder, "FSA029-Schema.xsd")
    common_types_path = os.path.join(schema_folder, "CommonTypes-Schema.xsd")

    try:
        # Read the schema file
        with open(schema_path, 'r', encoding='utf-8') as schema_file:
            schema_content = schema_file.read()

        # Resolve the include path to an absolute URI
        schema_content = schema_content.replace(
            '../../CommonTypes/v14/CommonTypes-Schema.xsd',
            common_types_path.replace("\\", "/")  # Convert to URI-compatible format
        )

        # Parse the updated schema
        schema_root = etree.XML(schema_content.encode('utf-8'))
        return etree.XMLSchema(schema_root)

    except Exception as e:
        print(f"Error loading schema: {e}")
        exit(1)


def validate_xml(schema, xml_file):
    """
    Validates an XML file against the schema.

    """
    try:
        with open(xml_file, 'rb') as file:
            xml_doc = etree.parse(file)

        if schema.validate(xml_doc):
            print(f"{xml_file} is valid.")
        else:
            print(f"{xml_file} is invalid.")
            print("Errors:")
            for error in schema.error_log:
                print(f"  Line {error.line}: {error.message}")

    except Exception as e:
        print(f"Error validating XML: {e}")
        exit(1)


def main():
    """
    Main function to parse arguments and validate the XML file.
    """
    parser = argparse.ArgumentParser(description="Validate FSA029 XML against its schema.")
    parser.add_argument("schema_folder", help="Path to the folder containing the schema files.")
    parser.add_argument("xml_file", help="Path to the XML file to validate.")
    args = parser.parse_args()

    schema_folder = args.schema_folder
    xml_file = args.xml_file

    # does the schema folder and XML file exist
    if not os.path.exists(schema_folder):
        print(f"Schema folder '{schema_folder}' does not exist.")
        exit(1)
    if not os.path.exists(xml_file):
        print(f"XML file '{xml_file}' does not exist.")
        exit(1)

    # Load the schema
    schema = load_schema(schema_folder)

    # Validate the XML file
    validate_xml(schema, xml_file)


if __name__ == "__main__":
    main()
