import csv
import json
import copy

outputFilePath = 'output.json'
inputFilePath = 'nodes.json'

labels = []

with open('changes.csv', mode='r') as csvFile:
    reader = csv.reader(csvFile)
    next(csvFile)
    for row in reader:
        labels.append(row)

with open(inputFilePath, 'r') as f:
    data = json.load(f)


for node in data:

    newNode = copy.deepcopy(node)
    for label in labels:
        if node['core_props']['label'] == label[0]:
            try:
                label_value = node['label_props'][label[1]]
                del newNode['label_props'][label[1]]
                if label[2] != '':
                    newNode['label_props'].update({label[2]: label_value})

            except KeyError:
                print(f'{label[1]} {labels.index(label) + 2}')

    data.insert(data.index(node), newNode)
    data.remove(node)

with open(outputFilePath, mode='w') as file:
    json.dump(data, file, indent=4)