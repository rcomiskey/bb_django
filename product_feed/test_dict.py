# import csv

# reader = csv.DictReader(open('product_feed.csv', 'r'))
# dict_list = []


# for line in reader:
#     dict_list.append(line)

# print(dict_list)

# import csv

# with open('product_feed.csv', 'rt') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print 

import csv
dict_list = []
with open("product_feed.csv", 'r') as csvfile:

    reader = csv.DictReader(csvfile, delimiter=';')
  
    for row in reader:
        dict_list.append(dict(row))

new_dict_list = []      
for dict in dict_list:
    for dict_new in dict_list:
        if dict['product_name'] != dict_new['product_name']:
            new_dict_list.append(dict)
        else:
            dict['colour'] + "," + dict_new['colour']
print(new_dict_list)

data = new_dict_list
with open('product_feed', 'wt') as f:
    # Assuming that all dictionaries in the list have the same keys.
    headers = sorted([k for k, v in data[0].items()])
    csv_data = [headers]

    for d in data:
        csv_data.append([d[h] for h in headers])

    writer = csv.writer(f)
    writer.writerows(csv_data)

# with open('product_feed', 'w') as output_file:
#     dict_writer = csv.DictWriter(output_file)
#     dict_writer.writeheader()
#     dict_writer.writerows(new_dict_list)

# with open('product_feed', 'w') as f:  # Just use 'w' mode in 3.x
#     w = csv.DictWriter(f, dict_list.keys())
#     w.writeheader()
#     w.writerow(my_dict)
        
# print(dict_list[0]['product_name'])

# with open("product_feed.csv") as f:
#     reader = csv.DictReader(f)
#     data = [r for r in reader]
# print(data[0]['aw_deep_link'])
    