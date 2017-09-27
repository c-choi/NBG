import json

def json_link(f):

    with open(f, 'r') as infile:
        contents = json.load(infile)

    #contents is now a dictionary of your json but it's a json array/list
    #continuing on you would then iterate through each dictionary
    #and fetch the pieces you need.
        links_list = []
        for item in contents:
             for key, val in item.items():
                   if 'http' in key:
                        links_list.append(key)
                   if 'http' in value:
                      if isinstance(value, list):
                           for link in value:
                                  links_list.append(link)
                      else:
                           links_list.append(value)
        #get rid of dupes
        links_list = list(set(links_list))
    #do rest of your crawling with list of links
        print(links_list)