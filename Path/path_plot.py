import matplotlib.pyplot as plt
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type = str)
args = vars(parser.parse_args())
in_file = args["file"]

cfile = open(in_file)
read = csv.reader(cfile, delimiter="\t")
plots = []
color = []
for row in read:
  if int(row[1]) == 0:
    color.append("red")
  else:
    color.append("green")
  plots.append((float(row[2]), float(row[3])))
plt.scatter(*zip(*plots), color = color)
plt.show()