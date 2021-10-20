from edftools import *
from testedfs import *

print(str(p_2_1) + ":")
#print_ed(p_2_1, 19)
print("Is edf? " + str(is_edf(p_2_1, 19)))
print("Is strong edf? " + str(is_sedf(p_2_1, 19)))
print("----")

print(str(non_edf_1) + ":")
#print_ed(non_edf_1, 31)
print("Is edf? " + str(is_edf(p_2_1, 31)))
print("Is strong edf? " + str(is_sedf(p_2_1, 31)))
print("----")

for h in h_7_all_with_mods:
    h_sedf = h[0]
    h_mod = h[1]
    print(str(h_sedf) + ":")
    print("Is edf? " + str(is_edf(h_sedf, h_mod)))
    print("Is strong edf? " + str(is_sedf(h_sedf, h_mod)))
    print("----")

print(str(d_3_1) + ":")
print("Is edf? " + str(is_edf(d_3_1, 4)))
print("Is strong edf? " + str(is_sedf(d_3_1, 4)))
print("----")