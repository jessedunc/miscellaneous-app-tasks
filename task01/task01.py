# task 01
# https://github.com/jharbeno/miscellaneous-app-tasks/task01/README.md
#
# convert input.json to output.json

import json

inputFilepath = 'input.json'
outputFilepath = 'output.json'

exampleOutputFilepath = 'desired-output.json'

## read the input file

with open(filepath, 'r') as f:
  data = json.load(f)

## get a sorted list that is the set of non-null labels
## - the label is in obj['core_props']['label']
## - if a node's label is null or None, ignore it
## - remember to filter out any null or None labels

setOfKeys = []

for d in data:
    if d['core_props']['label']:
      setOfKeys.append(d['core_props']['label'])

setOfKeys = set(setOfKeys)
setOfKeys = sorted(setOfKeys)

for s in setOfKeys:
    print(s)

## manipulate the data
## - remove edges
## - identify the label
## - rename, drop, or add properties as appropriate

print('manipulate the data here')

data = 'stuff'

## write the output file

with open(outputFilepath, 'w') as f:
  f.write(json.dumps(data, indent=4, sort_keys=True))

