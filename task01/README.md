## Task 01

Possibly useful links: [Skip first line(field) in loop using CSV file?](https://stackoverflow.com/questions/14674275/skip-first-linefield-in-loop-using-csv-file) and [What is difference between shallow copy, deepcopy, and normal assignment operation?](https://stackoverflow.com/questions/17246693/what-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignment-oper)

### Task

There are a bunch of node objects in `nodes.json`. All nodes have the same five properties in their `core_props`. In `core_props`, the `id` is a unique 16-digit hex string. Don't worry about the dates or the `dest_sites` array. The label in `['core_props']['label']` determines the set of keys and values in `['label_props']`. The `label` is a string that starts with a capital letter and which determines the set of `label_props` included on the node.

The goal is to change the names of the label properties on all nodes of a given label in `nodes.json`.

Each row in the `changes.csv` file contains the label, the old prop string, and the new prop string.

For example, here is an existing Article object:

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

The CSV file would look like this:

```
label,old_prop,new_prop
Article,files,
Article,title,strTitle
Article,authors,relAuthors
Article,abstract,strAbstract
Article,publication,strPublication
Article,volume,strVolume
Article,issue,strIssue
Article,pages,strPages
Article,date,strYear
Article,doi,strDoi

```

That first case is empty. In that case, just delete the prop.

## Suggested Tasks

1. Read in the csv file and programmatically ignore the header
1. Read in the `nodes.json` file
1. For every row in the `changes.csv` file, 
    1. For every node with that label in `nodes.json`,
        1. If the keyword does not work, print the bad node & the row in `changes.csv`
        1. Otherwise, proceed to change it
            1. Make a DEEP copy of the node (not a shallow one)
            1. Save the value of that node's prop in a local tempvar
            1. Drop the old prop
            1. Create a new prop with the local tempvar in your deep copy of the node
            1. Drop the old node from `nodes.json`
            1. Add your new node to `nodes.json`.

## Notes for future tasks, maybe

Don't worry about this for the moment. It's just background info. 

The app mimics a graph database of objects called `nodes` connected to each other by relationships called `edges`. 

The word "schema" just means "what the data looks like" or "what form the data takes". In this case, we invented the schema in `input.json` based on a good guess about what we would need for the app. As we prototyped, though, we realized the original schema needs to be changed. Since we don't want to lose the data we've created with the app, we want to convert the existing nodes from the old schema to the new schema. 



