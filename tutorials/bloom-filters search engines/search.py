from pybloom import BloomFilter
import json
import re

def loadJSON(data_path: str):
    with open(data_path) as json_data:
        data = json.load(json_data)
        return data

# Turn our loaded list of dinosaur summaries into a dict 
search_data = loadJSON('./processed_dinodata.json')['dinosaurs']
key_name_data = {}
i = 0 
for summary in search_data:
    i += 1
    key_name_data[str(i)] = summary

# This dict has the format {title of post: set(words in the post)}
search_data_cleaned = {name: set(re.split("\W+", contents.lower())) for name, contents in key_name_data.items()}

filters = {}
for title, words in search_data_cleaned.items():
    filters[title] = BloomFilter(capacity=len(words), error_rate=0.1)
    for word in words:
        filters[title].add(word)

def search(search_string):
    search_terms = re.split("\W+", search_string)
    return [name for name, _filter in filters.items() if all(term in _filter for term in search_terms)]

print(search("android raspberry"))
print(search("2007 lizard"))