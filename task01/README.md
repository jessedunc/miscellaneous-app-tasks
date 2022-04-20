## Task 01

Take the `input.json` and convert it to match `output.json`. Don't worry about edge cases and error handling yet. 

The app mimics a graph database of objects called `nodes` connected to each other by relationships called `edges`. 

The word "schema" just means "what the data looks like" or "what form the data takes". In this case, we invented the schema in `input.json` based on a good guess about what we would need for the app. As we prototyped, though, we realized the original schema needs to be changed. Since we don't want to lose the data we've created with the app, we want to convert the existing nodes from the old schema to the new schema. 

All nodes have the same four properties in their `core_props`. The label in `['core_props']['label']` determines the set of keys and values in `['label_props']`. 

Example input Article object

```

```

Example output Article object

```

```

The desired output schema is shown in `desired-output.json`. 

## Suggested Tasks

1. Read in the input file
1. Get a sorted list of all the labels
1. For each node,
    - Remove the `edges` section
    - Identify the label
    - Rename, drop, or add properties as appropriate
1. Write to an output file
1. Compare the output file to `desired-output.json`
