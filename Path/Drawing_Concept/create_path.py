from PIL import Image
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type = str)
args = vars(parser.parse_args())
in_file = args["file"]

def main(line_width, in_file, out_file_name):
  image = Image.open(in_file)
  x, y = image.size
  new_image = Image.new("RGB", (x, y))
  pixels = image.load()

  direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  g_cone_idx = 0
  r_cone_idx = 0

  new = open(out_file_name, "w")
  out_file = csv.writer(new, delimiter="\t")

  midx, midy = x // 2, y // 2
  SCALE = x / 10

  for itr_x in range(0, x):
    for itr_y in range(0, y):
      if (pixels[itr_x, itr_y][0] == 0 and pixels[itr_x, itr_y][1] == 0 and pixels[itr_x, itr_y][2] == 0):
        ardc = 0
        for nx, ny in direc:
          if (pixels[itr_x + nx, itr_y + ny][0] != 0 and pixels[itr_x + nx, itr_y + ny][1] != 0 and pixels[itr_x + nx, itr_y + ny][2] != 0):
            ardc += 1
        if ardc == 1 or ardc == 2:
          new_image.putpixel((itr_x, itr_y), (0,255,0))
          coord_x, coord_y = itr_x - midx, itr_y - midy
          new_line = [g_cone_idx, 1, coord_x / SCALE, coord_y / SCALE]
          out_file.writerow(new_line)
          g_cone_idx += 1
      else:
        new_image.putpixel((itr_x, itr_y), (255, 255, 255))
  return new_image

main(None, in_file, "cone_path_new.csv").show()