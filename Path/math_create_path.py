import csv
import math

def write(out_file, func, density, color):
  count = 0
  gen_func = []
  temp = ""
  for ch in func:
    if ch == "x":
      gen_func.append(temp)
      temp = ""
    else:
      temp += ch
  if temp != "":
    gen_func.append(temp)

  for i in range(-200, 200, density):
    new_str = "(" + str(i / 100) + ")"
    new_func = new_str.join(gen_func)
    y = eval(new_func)
    if (y >= -2 and y <= 2):
      new_line = [count, color, i / 100, y]
      out_file.writerow(new_line)
      count += 1

### Density = 0: High Density, 500: Low Density
def main(fname, gfunc, rfunc, density):
  new = open(fname, "w")
  out_file = csv.writer(new, delimiter = "\t")

  write(out_file, gfunc, density, 0)
  write(out_file, rfunc, density, 1)

main("quadratic.csv", "(x ** 2) - 2", "(1.5 * (x ** 2) - 0.35)", 25)
main("linear.csv", "x + 1", "x * 1", 25)
main("sin.csv", "math.sin((100/70) * x) - 0.9", "math.sin((100/70) * x) + 0.9", 35)
main("easy_one.csv", "math.sin(x) - 0.9", "math.sin(x) + 0.9", 35)
main("easy_two.csv", "-0.3 * (x ** 2) + 1.7", "-0.45 * (x ** 2)", 35)
