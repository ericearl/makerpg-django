# imports
import json
import yaml
from pathlib import Path

# globals
HERE = Path(__file__).parent


# read all YAML files in the src/systems directory whether they have a .yaml or .yml extension
def read_system_yamls():
    systems = []
    for file in HERE.joinpath('systems').glob('*'):
        if file.suffix == '.yaml' or file.suffix == '.yml':
            with open(file, 'r') as stream:
                try:
                    systems.append(yaml.safe_load(stream))
                except yaml.YAMLError as exc:
                    print(f'{exc} in {file}')
    return systems

# main function
def main():
    systems = read_system_yamls()
    pk = 1
    fixture = []
    for system in systems:
        if 'system' not in system:
            continue

        s = {'model': 'CharacterCreator.System', 'pk': pk, 'fields': {}}
        s['fields']['name'] = system['system']['name']
        if 'edition' in system['system']:
            s['fields']['edition'] = system['system']['edition']
        if 'copyright' in system['system']:
            s['fields']['copyright'] = system['system']['copyright']
        if 'publisher' in system['system']:
            s['fields']['publisher'] = system['system']['publisher']
        
        fixture.append(s)
        pk += 1

        s_pk = pk - 1
        for i, op in enumerate(system['order']):
            o = {'model': 'CharacterCreator.Operation', 'pk': pk, 'fields': {}}

            for key, val in op.items():
                o['fields']['name'] = key
                o['fields']['alias'] = val

            if i == 0:
                o['fields']['previous'] = None
            else:
                o['fields']['previous'] = pk - 1

            o['fields']['system'] = s_pk

            fixture.append(o)
            pk += 1

    with open(HERE.parent.joinpath('CharacterCreator/fixtures/systems.json'), 'w') as f:
        json.dump(fixture, f, indent=4)


# if this is called as a script, run the main function
if __name__ == '__main__':
    main()
