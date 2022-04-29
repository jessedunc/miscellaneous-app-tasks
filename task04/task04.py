import subprocess
import csv
import json
import task05.task05
import task03.task03
import datetime


def containsLatinName(latinName):
    for plant in plants:
        if plant['core_props']['label'] == "Plant":
            if plant['label_props']['strLatinName'] == latinName:
                return True


csvFile = open('plants.csv', 'r', encoding='utf8')

plants = []
fieldNames = (
    "id", "common_name", "latin_name", "family", "in_hells_canyon_book", "is_invasive", "native_nonnative", "color",
    "note", "desc")

reader = csv.DictReader(csvFile, fieldnames=fieldNames)

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
                        "strCaption": "Looking across Bear Creek.",
                        "relTimestamp": ["date20220422"],
                        "strHeightPx": "3024",
                        "strWidthPx": "4032",
                        "strOrientation": "landscape"
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
                        "strNativity": "",
                        "strColor": "",
                        "strDescription": "",
                        "relNotes": ""
                    }
                }
            )
