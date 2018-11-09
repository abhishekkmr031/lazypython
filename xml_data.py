## retrieves XML data xml.etree.ElementTree
import xml.etree.ElementTree as ET

var = '''
        <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
        </country>
'''

tree = ET.fromstring(var)

print(type(tree))
# print(tree.find('year').text)
# print(tree.find('neighbor').get('name'))
# print(tree.find('neighbor').get('direction'))
