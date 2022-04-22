## Task 04

Every row in the included `plants.csv` file is associated with a jpg image. Each row has the following columns:

- id
- common_name
- latin_name
- family
- in_hells_canyon_book
- is_invasive
- native_nonnative
- color
- note
- desc
- photographer

The task is to convert the .csv file into a JSON file that is a list of objects, roughly: 

```
[
  {plant node},
  {plant node},
  {artwork node},
  {artwork node}
]
```

The nodes don't have to be in any particular order.

**Creating identifiers**

Complete [Task 5](../task05/REASDME.md) first.

`id` should be a random 16-digit hex token. 

**Artwork Nodes**

Every item's csv row represents an Artwork, but for now we're only interested in the rows where `in_hells_canyon_book` is `true`. For each row, create an Artwork node:

```
{
  "core_props": {
    "dest_sites": [],
    "id": "",
    "date_created": 1635632174,
    "date_updated": 1635637123,
    "label": "Artwork"
  },
  "label_props": {
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
  }
}
```

- The `id` should be of the form `placeholder2022latinnameNUM` where NUM starts from 1. 
- The `core_props` timestamps should be true to the moment of creation. 
- Can you detect whether a prop is prefixed by `str` or `rel`? 
- the `strMedium` for all these is "photo".
- The `relTimestamp` is pointing at the identifier for a Date node with today's date.
- Can you programmatically get the height/width and therefore orientation? You can assume the images are rotated correctly. 

**Plant Nodes**

Plants are unique by Latin name (`strLatinName`). Create a node for each unique plant and include the identifiers of Artwork nodes in the `relArtwork` list property.

```
{
  "core_props": {
    "dest_sites": [],
    "id": "b2f6443ac6041d79",
    "date_created": 1635632174,
    "date_updated": 1635637123,
    "label": "Plant"
  },
  "label_props": {
    "strCommonName": "",
    "strFamily": "",
    "strLatinName": "",
    "relDestBooks": [],
    "relArtwork": [],
    "strNativity": "",
    "strColor": "",
    "strDescription": "",
    "relNotes": ""
  }
}
```

If `in_hells_canyon_book` is true, add a string "placeholder2022plantshellscanyon" to the `relDestBooks` list.

`strNativity` takes three possible strings:

1. Native
1. Non-Native
1. Non-Native & Invasive

For now, if `is_invasive` is true, set `strNativity` to "Non-Native & Invasive". If it's false, set `strNativity` to Native. Otherwise, set `strNativity` to "Unsure".

**Further Questions**

- How do you know you didn't miss a row? 

## Test header
