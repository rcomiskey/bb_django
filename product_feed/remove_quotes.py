with open('product_feed', 'r') as f, open('product_feed.csv', 'w') as fo:
    for line in f:
        fo.write(line.replace('"', '').replace("'", ""))

