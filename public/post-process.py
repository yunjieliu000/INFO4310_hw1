# Simple post-processing script to create a clean subset of tree data
#     - JRz, for personal use and not indended for real-world applications

#  NOTE: This is eliminating valid, useful data in lieu of something easier to visualize
#        It's possible that this will mask trends, as it is often VERY likely that missing data are non-randomly distributed (e.g. more missing data pre-1955 in this dataset)


import csv

def passes_filter(row):
    # Filter criteria:
    #   Only listed trees that have full species name supplied
    if len(row['qSpecies']) < 3 or 'Tree(s) ::' in row['qSpecies']:
        return False
    #   Only trees that have a lat and lng provided
    elif len(row['Latitude']) < 2 or len(row['Longitude']) < 2:
        return False
    #   Only trees with valid SiteInfo
    elif len(row['qSiteInfo']) < 1 or row['qSiteInfo'] == ':':
        return False
    #   Only trees that have a DBH provided
    elif len(row['DBH']) < 1:
        return False
    else:
        return True
    
    # think about what other filters you could run here...

# import and run passes_filter
data = []
header = []
with open('Street_Tree_List-2022-01-30_RAW.csv','r') as f:
    reader = csv.DictReader(f)
    
    header = reader.fieldnames
    for row in reader:
        if passes_filter(row):
            # you might consider doing some additional processing here
            # e.g. splitting up qSpecies
            data.append(row)

print(len(data))

# export to new CSV       
with open('Street_Tree_List-2022-01-30_FILTERED.csv','w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
