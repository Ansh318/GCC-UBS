import json 

sample_data_files= {
    "inputs": ['abccccdd', 'a']
}

# Writing the data to a JSON file
with open('sample_data.json', 'w') as json_file:
    json.dump(sample_data_files, json_file, indent=4)
    
    
sample_data = {
    'inputs':[[
               "5 4 10", 
               " 4 2 4 6 1", 
               "2 1 8 5"
              ],
              [
                  "3 7 3696",
                  "12 21 102",
                  "167 244 377 56 235 269 23"
              ]]
}

# Writing the data to a JSON file
with open('sample_data_2.json', 'w') as json_file:
    json.dump(sample_data, json_file, indent=4)
    