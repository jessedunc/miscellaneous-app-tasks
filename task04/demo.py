import os
import subprocess
import csv
import json

csvfile = open('plants.csv', 'r')
jsonfile = open('output/plants.json', 'w')
mdfile = open('output/plants.md', 'w')

## build list of json objects from csv file

plants = []

fieldnames = ("id","common_name","latin_name","family","in_hells_canyon_book","is_invasive","native_nonnative","color","note","desc")
reader = csv.DictReader(csvfile, fieldnames)


# only capture rows that should be in this hells canyon book

for row in reader:
    if row['in_hells_canyon_book'] == 'TRUE':
        plants.append(row)

list_of_plants_sorted_family_first = sorted(plants, key=lambda x: (x['family'], x['latin_name']))

## create the list of book pages

page_objects = []
page_num = 6

# for each plant in list of plants sorted by family
    # if page_objects doesn't exist, create the first entry
    # otherwise, check to see if plant['latin_name'] is already in page_objects
      # if yes, only add the id
      # otherwise, add a new pageObj to page_objects list

for plant in list_of_plants_sorted_family_first:

    if not page_objects: # create the first entry

      pageObj = {'page': page_num,
                 'latin_name': plant['latin_name'],
                 'common_name': plant['common_name'],
                 'family': plant['family'],
                 'notes': [],
                 'ids': [],
                 'desc': [],
                 'colors': [],
                 'is_invasive': plant['is_invasive']}

      if plant['note'] != '':
        pageObj['notes'].append(plant['note'])

      if plant['id'] != '':
        pageObj['ids'].append(plant['id'])

      if plant['desc'] != '':
        pageObj['desc'].append(plant['desc'])

      if plant['color'] != '':
        pageObj['colors'].append(plant['color'])

      page_num = page_num + 1
      page_objects.append(pageObj)

    else: # check to see if plant['latin_name'] is already in page_objects

      foundFlag = False

      for page in page_objects:

        if plant['latin_name'] == page['latin_name']:
          if plant['note'] != '':
            pageObj['notes'].append(plant['note'])

          if plant['id'] != '':
            pageObj['ids'].append(plant['id'])

          if plant['desc'] != '':
            pageObj['desc'].append(plant['desc'])

          if plant['color'] != '':
            pageObj['colors'].append(plant['color'])

          foundFlag = True
          break

      else:
        pageObj = {'page': page_num,
                   'latin_name': plant['latin_name'],
                   'common_name': plant['common_name'],
                   'family': plant['family'],
                   'notes': [],
                   'ids': [],
                   'desc': [],
                   'colors': [],
                   'is_invasive': plant['is_invasive']}

        if plant['note'] != '':
          pageObj['notes'].append(plant['note'])

        if plant['id'] != '':
          pageObj['ids'].append(plant['id'])

        if plant['desc'] != '':
          pageObj['desc'].append(plant['desc'])

        if plant['color'] != '':
          pageObj['colors'].append(plant['color'])

        page_num = page_num + 1
        page_objects.append(pageObj)


## sort page_objects by page number

sorted_page_objects = sorted(page_objects, key=lambda x: x['page'])

## print meta info to stdout

print(f'We have {len(page_objects)} pages')

## print the yaml header to override font limits

mdfile.write('---\n')
mdfile.write('documentclass: extarticle\n')
mdfile.write('fontsize: 12pt\n')
mdfile.write('---\n\n')

## print the table of contents by family, then plant

mdfile.write("### Table of Contents\n\n")

mdfile.write('\small' + '4' + '\t...\t' + 'Dedication  \n')
mdfile.write('\small' + '5' + '\t...\t' + 'Preface / Forward  \n')

for p in page_objects:

    if p['common_name'] == 'Oregon Sunshine / Woolly Yellow Daisy':
        mdfile.write('\small' + str(p['page']) + '\t...\t' + p['family'] + ' &bull; ' + p['latin_name'] + ' &bull; ' + 'Oregon Sunshine' + '  \n')
    elif p['common_name'] == 'Green Gentian / Monument Plant':
        mdfile.write('\small' + str(p['page']) + '\t...\t' + p['family'] + ' &bull; ' + p['latin_name'] + ' &bull; ' + 'Green Gentian' + '  \n')
    elif p['common_name'] == 'Hot Rock Penstemon / Scabland Penstemon':
        mdfile.write('\small' + str(p['page']) + '\t...\t' + p['family'] + ' &bull; ' + p['latin_name'] + ' &bull; ' + 'Hot Rock Penstemon' + '  \n')
    elif p['common_name'] == 'Houndstongue / Beggar Ticks':
        mdfile.write('\small' + str(p['page']) + '\t...\t' + p['family'] + ' &bull; ' + p['latin_name'] + ' &bull; ' + 'Houndstongue' + '  \n')
    else:
        mdfile.write('\small' + str(p['page']) + '\t...\t' + p['family'] + ' &bull; ' + p['latin_name'] + ' &bull; ' + p['common_name'] + '  \n')

mdfile.write('\n\n')

## write foreword pages

mdfile.write("\clearpage")
mdfile.write("### Dedication\n\nJenner Hanni\n\nHolly Goebel (Wallowa Public Library)\n\nJanet Hohmann\n\nRob Taylor (USFWS)\n\nJerry Hustafa (USFS)\n\n")

mdfile.write("\clearpage")
mdfile.write("### Preface / Forward\n\n")

mdfile.write("This is a small sampling of species found in Hells Canyon. \n\n")
mdfile.write("The book is arranged alphabetically by plant family and then Latin name, according to “Flora of the Pacific Northwest - an Illustrated Manual 2nd edition” by C. Leo Hitchcock and Arthur Cronquist, 2018. The table of contents lists plants by family name. The index will list plants also by common name and color.\n\n")

mdfile.write("It's often hard to specify the color of a bloom in one word.\n\n")

mdfile.write("**Many other good plant ID books**\n\n\clearpage\n\n")

## write individual pages

for p in page_objects:

    mdfile.write("# " + p['common_name'] + "\n\n")

    if len(p['ids']) > 0:
      for plantId in p['ids']:
        if p['common_name'] in {'Yellowbell', 'Prickly Pear', 'Ponderosa Pine', 'Sugar Scoop / Vase Flower'}:
            mdfile.write("![](/home/jenner/fangorn/sites/jan/img/" + plantId + ".jpg){width=100} ")
        else:
            mdfile.write("![](/home/jenner/fangorn/sites/jan/img/" + plantId + ".jpg){width=200} ")

    mdfile.write("\n\n")

    if p['family'] == '':
      mdfile.write("Family name: ")
    else:
      mdfile.write(p['family'])

    if p['latin_name'] == '':
      mdfile.write(" &bull; Latin name: \n\n")
    else:
      mdfile.write(" &bull; *" + p['latin_name'] + "*\n\n")

#    if len(p['ids']) > 0:
#      mdfile.write("<div style='display: flex;'>\n\n")
#      for plantId in p['ids']:
#        mdfile.write("  <img src='/home/jenner/fangorn/sites/jan/img/"+plantId+".jpg' width='100px' />\n\n")
#      mdfile.write("</div>\n\n")

    if p['is_invasive'] == '':
      mdfile.write("Native or invasive?")
    else:
      if p['is_invasive'] == 'TRUE':
        mdfile.write("Invasive")
      else:
        mdfile.write("Native")

    if len(p['colors']) == 0:
      mdfile.write(" &bull; color?\n\n")
    else:
      colorSet = set(p['colors'])
      mdfile.write(" &bull; ")
      newArr = []
      for plantColor in colorSet:
        newArr.append(plantColor.title())
      mdfile.write(", ".join(newArr))
      mdfile.write("\n\n")

    mdfile.write("## Notes\n\n")
    if len(p['notes']) == 0:
      mdfile.write("\n&nbsp;\n&nbsp;\n\n")
    else:
      for plantNote in p['notes']:
        mdfile.write(plantNote + "\n&nbsp;\n&nbsp;\n\n")

    mdfile.write("## Description\n\n")
    if len(p['desc']) == 0:
      mdfile.write("\n&nbsp;\n&nbsp;\n\n")
    else:
      for plantDesc in p['desc']:
        mdfile.write(plantDesc + "\n&nbsp;\n&nbsp;\n\n")

    mdfile.write("\clearpage" + "\n\n")

# set the output file paths

mdfile = 'output/plants.md'
htmlfile = 'output/plants.html'
pdffile = 'output/plants.pdf'

#subprocess.call(['/usr/bin/pandoc', '/home/user/program/content.md',
#    '-V',  'title="Wartość"', '-V', 'authors="Jerry"',
#    '--output=/home/user/program/outputs/book_33.pdf'])

#text=f"pandoc -t html {mdfile} | pandoc -f html -o {pdffile}"

#os.system(text)

#subprocess.run(["pandoc", "-t", "html", "geometry:margin=0.8in",  "--pdf-engine=xelatex", "-o", pdffile])
subprocess.run(["pandoc", mdfile, "-V", "geometry:margin=0.5in", "-V", "papersize:a5", "--pdf-engine=xelatex", "-o", pdffile])

