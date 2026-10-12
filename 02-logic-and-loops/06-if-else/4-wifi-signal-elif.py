
# Challenge: Wi-Fi Signal
# Give customers a discount based on the number of Wi-Fi signal bars.

signal = 2  # out of 5 bars

if signal == 5:
    print("Full bars, no discount today!")
elif signal >= 3:
    print("10% off")
elif signal >= 1:
    print("25% off")
else:
    print("50% off, sorry about the Wi-Fi!")

#output - 25% off