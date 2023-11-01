Girl_Money = 50
Price_Of_USB = 6

num_usb_sticks = Girl_Money // Price_Of_USB
money_left = Girl_Money % Price_Of_USB

print("The lovely girl who likes USB can buy", num_usb_sticks, "USB sticks.")
print("In return, she will have £", money_left, "left.")