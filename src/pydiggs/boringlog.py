"""Define the BoringLog class."""

import xml.etree.ElementTree as ET
import pathlib

from jinja2 import Environment, PackageLoader, select_autoescape
import pdfkit
import xmlschema

class BoringLog:
    def __init__(self):
        self.log_data = {}

    def extract_xml(self, input_path):
        pydiggs_dir = pathlib.Path(__file__).parents[0]
        xsd = str(pydiggs_dir.joinpath('schema', 'Complete.xsd'))
        # schema = xmlschema.XMLSchema(xsd)
        # xml_data = schema.to_dict('tests/test_cases/examples/collection/collection.xml')
        # self.log_data['boring_id'] = 'temp'
        
        namespace = {
            'default': 'http://diggsml.org/schemas/2.5.a',
            'gml': 'http://www.opengis.net/gml/3.2'
        }
        tree = ET.parse(input_path)
        root = tree.getroot()
        first_feature = root.find('default:samplingFeature', namespace)
        borehole = first_feature.find('default:Borehole', namespace)
        name = borehole.find('gml:name', namespace)
        self.log_data['boring_id'] = name.text

    def to_pdf(self, output_path):
        # output_text = '<p>Pretend this is a boring log.</p>'
        # content = {'boring_id': 'B-1'}

        pydiggs_dir = pathlib.Path(__file__).parents[0]
        # template_file = str(pydiggs_dir.joinpath('templates', 'BoringLog.html'))
        env = Environment(
            loader=PackageLoader('pydiggs', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('BoringLog.html')
        output_text = template.render(**self.log_data)

        wkhtml = str(pydiggs_dir.joinpath('bin', 'wkhtmltopdf.exe'))
        config = pdfkit.configuration(wkhtmltopdf=wkhtml)
        pdfkit.from_string(output_text, output_path, configuration=config)
