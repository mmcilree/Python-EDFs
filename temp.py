from setfamily import *


# [ [ <identity ...>, x, y, x^2, y^2, x^3, x^2*y, x*y^2, x^2*y^3, x*y^4, x^3*y^3, x^3*y^4 ], 
#   [ x*y, y^3, x^3*y, x^2*y^2, x*y^3, y^4, x^4*y, x^3*y^2, x^4*y^2, x^2*y^4, x^4*y^3, x^4*y^4 ] ]

sedf = [[(0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (3, 0), (2, 1), (1, 2), (2, 3), (1, 4), (3, 3), (3, 4)],
        [(1, 1), (0, 3), (3, 1), (2, 2), (1, 3), (0, 4), (4, 1), (3, 2), (4, 2), (2, 4), (4, 3), (4, 4)]]

print(sedf)

test = CyclicProductSetFamily(sedf, 5)
print(test.is_edf())
print(test.is_sedf())
test.print_external_differences(sort_by="value")
test.print_external_differences_tables()

d10table = [[x-1 for x in y] for y in [[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], [ 2, 1, 4, 3, 6, 5, 8, 7, 10, 9 ], 
  [ 3, 10, 5, 2, 7, 4, 9, 6, 1, 8 ], [ 4, 9, 6, 1, 8, 3, 10, 5, 2, 7 ], 
  [ 5, 8, 7, 10, 9, 2, 1, 4, 3, 6 ], [ 6, 7, 8, 9, 10, 1, 2, 3, 4, 5 ], 
  [ 7, 6, 9, 8, 1, 10, 3, 2, 5, 4 ], [ 8, 5, 10, 7, 2, 9, 4, 1, 6, 3 ], 
  [ 9, 4, 1, 6, 3, 8, 5, 10, 7, 2 ], [ 10, 3, 2, 5, 4, 7, 6, 9, 8, 1 ] ]]

d = SetFamily([ [ 0, 5, 1, 6, 2, 7, 3 ], [ 5, 1, 2, 7, 8, 4, 9 ] ], d10table) 
d.print_external_differences(sort_by="value")