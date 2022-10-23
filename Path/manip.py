import csv


cfile = open("cone_path_S.csv")
#read2 = csv.reader(cfile)
#for row in read2:
  #print(row)
#read2.close()
read = csv.reader(cfile, delimiter="\t")
new = open("cone_path_new.csv", "w")
write = csv.writer(new, delimiter="\t")
for row in read:
  new = [row[0], row[1], row[3], row[2]]
  write.writerow(new)
