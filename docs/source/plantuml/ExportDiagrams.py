import os
import pathlib

import plantuml

PLANT_PATH = r'C:\Source\plantuml.jar'

def export():
    is_local = os.path.exists(PLANT_PATH)
    if is_local:
        print('Using local PlantUML jar.')
    else:
        print('Using PlantUML server.')
    puml = plantuml.PlantUML('http://www.plantuml.com/plantuml/img/')

    plant_dir = pathlib.Path(__file__).parents[0]
    docs_dir = plant_dir.parents[0]
    for input_file in plant_dir.glob('*.puml'):
    # for file_name in ['KeynetixConverter.puml']:
        # input_file = plant_dir / file_name
        print(input_file.name)
        output_name = input_file.name.replace('.puml', '.png')
        output_dir = docs_dir.joinpath('images')
        output_file = output_dir.joinpath(output_name)
        if is_local:
            os.system('java -jar {} {} -o {}'.format(PLANT_PATH, input_file, output_dir))
        else:
            puml.processes_file(input_file, output_file)

if __name__ == '__main__':
    export()
