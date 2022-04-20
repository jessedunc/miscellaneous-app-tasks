## Task 01

Take the `input.json` and convert it to match `output.json`. Don't worry about edge cases and error handling yet. 

The app mimics a graph database of objects called `nodes` connected to each other by relationships called `edges`. 

The word "schema" just means "what the data looks like" or "what form the data takes". In this case, we invented the schema in `input.json` based on a good guess about what we would need for the app. As we prototyped, though, we realized the original schema needs to be changed. Since we don't want to lose the data we've created with the app, we want to convert the existing nodes from the old schema to the new schema. 

All nodes have the same five properties in their `core_props`. The label in `['core_props']['label']` determines the set of keys and values in `['label_props']`. 

Example input Article object:

```
{
  "core_props": {
    "dest_sites": [],
    "id": "kubin2021personalexperiencesbridge",
    "date_created": 1635632174,
    "date_updated": 1635637123,
    "label": "Article"
  },
  "edges": [],
  "label_props": {
    "files": [
      "pdf"
    ],
    "title": "Personal experiences bridge moral and political divides better than facts",
    "authors": [
      "Emily Kubin",
      "Curtis Puryear",
      "Chelsea Schein",
      "Kurt Gray"
    ],
    "abstract": "",
    "publication": "Proceedings of the National Academy of Sciences",
    "volume": "118",
    "issue": "6",
    "pages": "",
    "date": "2021",
    "doi": "10.1073/pnas.2008389118"
  }
}
```

Example output Article object:

```
{
  "core_props": {
    "dest_sites": [],
    "id": "kubin2021personalexperiencesbridge",
    "date_created": 1635632174,
    "date_updated": 1635637123,
    "label": "Article"
  },
  "label_props": {
    "strTitle": "Personal experiences bridge moral and political divides better than facts",
    "relAuthors": [
      "Emily Kubin",
      "Curtis Puryear",
      "Chelsea Schein",
      "Kurt Gray"
    ],
    "strAbstract": "",
    "strPublication": "Proceedings of the National Academy of Sciences",
    "strVolume": "118",
    "strIssue": "6",
    "strPages": "",
    "strDate": "2021",
    "strDoi": "10.1073/pnas.2008389118"
  }
}
```

The desired output schema for each label is shown in `desired-output.json`. 

## Suggested Tasks

1. Read in the input file
1. Get a sorted list of all the labels
1. For each node,
    - Remove the `edges` section
    - Identify the label
    - Rename, drop, or add properties as appropriate
1. Write to an output file
1. Compare the output file to `desired-output.json`
