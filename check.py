import os

for root, dirs, files in os.walk(r'/Users/vivekreddy'):
    for name in files:
        if name == 'sorted_data.csv':
            print (os.path.abspath(os.path.join(root, name)))