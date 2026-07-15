import math

pka = float(input("Enter pKa value: "))
base_concentration = float(input("Enter [A-] value (M): "))
acid_concentration = float(input("Enter [HA] value (M): "))

ph = pka + math.log10(
    base_concentration / acid_concentration
)

print(f"The calculated pH is {ph:.1f}.")
