# calculate pay by hours worked
sh = input('Enter hours: ')
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)
print(fh, fr)
if fh > 40:
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg,otp)
    xp = reg + otp 
else: 
    
    
print(f"Score")