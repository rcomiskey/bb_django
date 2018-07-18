# import pandas as pd
# df = pd.read_csv('/product_feed.csv')
# df_reorder = df[['description', 'aw_deep_link']] # rearrange column here
# df_reorder.to_csv('/new_product_feed.csv', index=False)

import csv

with open('product_feed.csv', 'r') as infile, open('new_product_feed.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['description', 'aw_deep_link']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)