import argparse
import os
import xml.etree.ElementTree as ET


def config_args():
    parser = argparse.ArgumentParser(
        description="Parses pyqt ui files and outputs findchild statements")
    parser.add_argument("-f", "--file-path", type=str,
                        help="Path of the ui file")
    return parser

if __name__ == "__main__":
    parser = config_args()
    args = parser.parse_args()

    if not args.file_path:
        print("You must specify file path")
        exit()

    if not os.path.exists(args.file_path):
        print("File not Found.")
        exit()

    file_path = args.file_path
    xmlTree = ET.parse(file_path)

    print()
    for elem in xmlTree.iter():
        if elem.tag == "widget":
            name = elem.get("name")
            class_name = elem.get("class")
            print(
                f'self.{name}: {class_name} = self.findChild({class_name}, "{name}")')
