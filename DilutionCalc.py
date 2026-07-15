stock_concentration = float(input("Enter stock concentration (mM): "))
target_concentration = float(input("Enter target concentration (mM): "))
final_volume = float(input("Enter final volume (mL): "))

stock_volume = (target_concentration * final_volume) / stock_concentration

print(f"\nAdd {stock_volume:.2f} mL of stock solution.")
print(f"\nBring to {final_volume:2f} mL of total volume with diluent.")
