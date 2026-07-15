desired_ph = float(
    input(
        "Enter the desired pH you are trying to achieve: "))
pka = float(
    input(
        "Enter the pka of the acid you are using: "
    )
)
total_concentration = float(
    input(
        "Enter the total concentration of the buffer you are making (M): "
    )
)

ratio = 10 ** (desired_ph - pka)

acid_concentration = total_concentration / (1 + ratio)
base_concentration = total_concentration - acid_concentration

print(f"Acid Concentration required for buffer: {acid_concentration:.4f} M")

print(f"Base Concentration required for buffer: {base_concentration:.4f} M")

acid_mw = float(
    input(
        "Enter the molecular weight of your acid (g/mol): "
    )
)

base_mw = float(
    input(
        "Enter the molecular weight of your base (g/mol): "
    )
)

volume_milliliters = float(
    input(
        "Enter the final volume of the buffer you would like to make (mL): "
    )
)

volume_liters = volume_milliliters / 1000

acid_moles = acid_concentration * volume_liters

base_moles = base_concentration * volume_liters

acid_mass = acid_moles * acid_mw

base_mass = base_moles * base_mw

print(f"You will need {acid_mass:.3f}g of [HA] and {base_mass:.3f}g of [A-].")