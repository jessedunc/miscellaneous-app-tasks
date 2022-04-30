import csv
import json
import task05.task05
import task03.task03
import datetime

csvFile = open('plants.csv', 'r', encoding='utf8')

plants = []
fieldNames = (
    "id", "common_name", "latin_name", "family", "in_hells_canyon_book", "is_invasive", "native_nonnative", "color",
    "note", "desc")

reader = csv.DictReader(csvFile, fieldnames=fieldNames)


def containsLatinName(latinName):
    for plant in plants:
        if plant['core_props']['label'] == "Plant":
            if plant['label_props']['strLatinName'] == latinName:
                return True


def findImages():
    for plant in plants:
        images = []
        if plant['core_props']['label'] == 'Plant':
            for obj in plants:
                if obj['core_props']['label'] == 'Artwork':
                    if obj['label_props']['strPlant'] == plant['label_props']['strLatinName']:
                        images.append(obj['core_props']['id'])
            plant['label_props']['relArtwork'] = images


def nativity(invasive):
    if invasive:
        return 'Non-Native & Invasive'
    elif not invasive:
        return 'Native'
    else:
        return 'Unsure'


for row in reader:

    if (row["in_hells_canyon_book"]) == "TRUE":
        plants.append(
            {"core_props":
                {
                    "dest_sites": [],
                    "id": task05.task05.getHexstring(16, [])[:23],
                    "date_created": task03.task03.convertYYYYMMDDtoTimestamp(
                        str(datetime.date.today()).replace('-', '')),
                    "date_updated": task03.task03.convertYYYYMMDDtoTimestamp(
                        str(datetime.date.today()).replace('-', '')),
                    "label": 'Artwork'
                },
                "label_props":
                    {
                        "strMedium": "photo",
                        "relCreatedBy": [
                            "placeholder"
                        ],
                        "strLocation": "",
                        "strCaption": "",
                        "relTimestamp": ['date' + str(datetime.date.today()).replace('-', '')],
                        "strHeightPx": "",
                        "strWidthPx": "",
                        "strOrientation": "",
                        'strPlant': row['latin_name']
                    },

            })

        if containsLatinName(row['latin_name']) is None:
            plants.append(
                {"core_props": {

                    "dest_sites": [],
                    "id": task05.task05.getHexstring(16, [])[:23],
                    "date_created": task03.task03.convertYYYYMMDDtoTimestamp(
                        str(datetime.date.today()).replace('-', '')),
                    "date_updated": task03.task03.convertYYYYMMDDtoTimestamp(
                        str(datetime.date.today()).replace('-', '')),
                    "label": "Plant"
                },
                    "label_props": {
                        "strCommonName": row['common_name'],
                        "strFamily": row['family'],
                        "strLatinName": row['latin_name'],
                        "relDestBooks": [],
                        "relArtwork": [],
                        "strNativity": nativity(row['is_invasive']),
                        "strColor": row['color'],
                        "strDescription": row['desc'],
                        "relNotes": ""
                    }
                }
            )
findImages()

with open ('output/plants.json', 'w') as jsonFile:
    json.dump(plants, jsonFile, indent=4)
