import sys
sys.path.insert(0,'..')

from edftools import *
from testedfs import *


colormap = {
    0: "red",
    1: "blue",
    2: "olive",
    3: "orange",
    4: "purple"
}
# Print all external differences aligned for latex
def print_ed_colors(sets, modulus, sort=True, perline=6):
    ed = get_ed(sets, modulus)
    if sort:
        ed = dict(sorted(ed.items(), key=lambda item: item[1]))
    count = 0
    for diff in ed.keys():
        print("& " + color(diff[0]) + " - " + color(diff[1]) + " = " + color(ed[diff]))
        count += 1
        if count % perline == 0:
            print("\\\\")
            if count % 10 == 0:
                print("\\\\")
            # if count == 30 or count == 70 or count == 110 :
            #     print("\\\\")

def color(el):
    return "\\textcolor{" + colormap[el % 5] + "}{" + str(el) + "}"

#print_ed_colors(d_3_1, 4, perline=5)
print_ed_colors(h_7_3, 10, perline=5, sort=True)