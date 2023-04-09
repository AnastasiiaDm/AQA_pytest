"""
Implement provided methods. You need to convert the class instance to JSON or XML. When the user provides the command
json to cli, the program should call convert_to_json, when providing xml to cli program should convert the class
instance to xml string. And print it, or even better write it to a separate file.

You can use third parties libraries for this. If you use such a library please add it to requirenment.txt
"""
import json
import xml.etree.ElementTree as ET
import xmltodict


class Human:
    def __init__(self, name=str, age=int, gender=str, birth_year=str, marital=bool):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year
        self.marital = marital

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def get_xml_text(self, data):
        for key, value in self.__dict__.items():
            ET.SubElement(data, key).text = str(value)

    def convert_to_xml(self):
        self.get_xml_text(data=ET.Element('Human'))
        return xmltodict.unparse({'Human': self.__dict__})

    def convert_to_xml_with_none(self):
        data = ET.Element('Human')
        self.get_xml_text(data)
        return ET.tostring(data, encoding='unicode', xml_declaration=True)
        # return ET.tostring(data, encoding='unicode', method='xml')

    @classmethod
    def convert_to_json_or_xml(cls, command, *args):
        human = cls(*args)
        if command == 'json':
            json_data = human.convert_to_json()
            print(json_data)
            with open('human.json', 'w') as file:
                file.write(json_data)
        elif command == 'xml':
            xml_data = human.convert_to_xml()
            print(xml_data)
            with open('human.xml', 'w') as file:
                file.write(xml_data)
        elif command == 'xml_with_none':
            xml_data = human.convert_to_xml_with_none()
            print(xml_data)
            with open('human_.xml', 'w') as file:
                file.write(xml_data)
        else:
            print(f'Invalid command: {command}. Please enter "json" or "xml".')


if __name__ == '__main__':
    Human.convert_to_json_or_xml('xml', 'Yen', 95, 'female', None, False)
    Human.convert_to_json_or_xml('json', 'Yen', 95, 'female', None, False)
    Human.convert_to_json_or_xml('xml_with_none', 'Yen', 95, 'female', None, False)
