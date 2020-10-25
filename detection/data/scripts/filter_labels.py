import sys
from os import listdir
from os.path import join, isfile


"""
Generate new dataset from COCO that only has labels for desired classes.
A rather simplistic and slow solution, but it works.

Also must change a line in dataset.py for the labels/ directory.
"""


def convert(data_dir, new_dir, filename, labels):
    out = ''
    with open(join(data_dir, filename), 'r') as f:
        line = f.readline()
        while line:
            if line[0] in labels:
                out += line
            line = f.readline()

    with open(join(new_dir, filename), 'a+') as f:
        f.write(out)


if __name__ == '__main__':
    data_dir = sys.argv[1]
    new_dir = sys.argv[2]
    labels = sys.argv[3:]

    label_files = [filename for filename in listdir(data_dir) if isfile(join(data_dir, filename))]
    for f in label_files:
        convert(data_dir, new_dir, f, labels)
