import csv
import json
import uuid
from datetime import datetime
from datetime import date
import time

csvFile = open('plants.csv', 'r', encoding='utf8')

plants = []

fieldNames = (
    "id",
    "common_name",
    "latin_name",
    "family",
    "in_hells_canyon_book",
    "is_invasive",
    "native_nonnative",
    "color",
    "note",
    "desc",
    "photographer")

reader = csv.DictReader(csvFile, fieldnames=fieldNames)


def convertTimestampToYYYYMMDD(ts):
    """ Given a unix epoch timestamp of form "1651192385",
    returns a string in the form "20220428" """

    return datetime.strftime(datetime.fromtimestamp(ts), '%Y%m%d')


def convertYYYYMMDDtoTimestamp(timestring):
    """ Given a string in the form "20220428",
    returns a unix epoch timestamp integer of form "1651129200" """

    return int(time.mktime(datetime.strptime(timestring, "%Y%m%d").timetuple()))


def getHexstring(desiredChars, arr):
    """Return a unique hex string containing chars 0-9 and lowercase a-f"""

    while True:
        hexstring = uuid.uuid4()
        hexstring = str(hexstring)

        if hexstring not in arr:
            break
    hexstring = hexstring.replace('-', '')
    return str(hexstring)[:desiredChars]


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


def nativity(isInvasive):
    if isInvasive:
        return 'Non-Native & Invasive'
    elif not isInvasive:
        return 'Native'
    else:
        return 'Unsure'


def colors(colorStr):
    """colorStr can take form of 'WHITE' or 'WHITE / YELLOW' and should
    return a string of form 'White' or 'White / Yellow' """

    colorArr = colorStr.split(' / ')
    colorArr = [c.capitalize() for c in colorArr]
    colorStr = ' / '.join(colorArr)
    
    return colorStr


def generateJson():
    for row in reader:

        if (row["in_hells_canyon_book"]) == "TRUE":
            plants.append(
                {"core_props":
                    {
                        "dest_sites": [],
                        "id": getHexstring(16, [])[:23],
                        "date_created": convertYYYYMMDDtoTimestamp(
                            str(date.today()).replace('-', '')),
                        "date_updated": convertYYYYMMDDtoTimestamp(
                            str(date.today()).replace('-', '')),
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
                            "relTimestamp": ['date' + str(date.today()).replace('-', '')],
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
                        "id": getHexstring(16, [])[:23],
                        "date_created": convertYYYYMMDDtoTimestamp(
                            str(date.today()).replace('-', '')),
                        "date_updated": convertYYYYMMDDtoTimestamp(
                            str(date.today()).replace('-', '')),
                        "label": "Plant"
                    },
                        "label_props": {
                            "strCommonName": row['common_name'],
                            "strFamily": row['family'],
                            "strLatinName": row['latin_name'],
                            "relDestBooks": ["hohmann2022hellscanyon"],
                            "relArtwork": [],
                            "strNativity": row['native_nonnative'],
                            "strColor": colors(row['color']),
                            "strDescription": row['desc'],
                            "relNotes": ""
                        }
                    }
                )
    findImages()

    with open ('plants.json', 'w') as jsonFile:
        json.dump(plants, jsonFile, indent=4)

if __name__ == '__main__':

    generateJson()

