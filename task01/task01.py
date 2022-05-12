# task 01
# https://github.com/jharbeno/miscellaneous-app-tasks/task01/README.md
#
# convert input.json to output.json

import json

csvFilepath = 'changes.csv'     # in
nodesFilepath = 'nodes.json'    # in

outputFilepath = 'output.json'  # out

nodes = []                      # global nodes list

## read the input file

with open(nodesFilepath, 'r') as f:
  nodes = json.load(f)

## do stuff



## write the output file

with open(outputFilepath, 'w') as f:
  f.write(json.dumps(nodes, indent=4, sort_keys=True))

