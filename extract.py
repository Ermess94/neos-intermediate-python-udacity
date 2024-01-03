"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    result = []
    with open(neo_csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            keys = ['pdes', 'name', 'diameter', 'pha']

            data = {k: v if v != '' else None for (
                k, v) in row.items() if k in keys}

            designation: str = data['pdes']
            name: str = data['name']
            diameter: float = data['diameter']
            hazardous: bool = True if data['pha'] == 'Y' else False

            neo = NearEarthObject(designation, name, diameter, hazardous)
            result.append(neo)

    return result


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path) as file:
        data = json.load(file)
        keys = {'des', 'cd', 'dist', 'v_rel'}
        approaches = []
        for data_item in data['data']:
            approach = {data['fields'][i]: value for i, value in enumerate(
                data_item) if data['fields'][i] in keys}
            approaches.append(approach)
    return [CloseApproach(app['des'], app['cd'], app['dist'], app['v_rel']) for app in approaches]
