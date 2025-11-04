while True:
    fraction = input("Fraction: ")
    try: 
        a, b = fraction.split("/")
        a, b = int(a), int(b)
        gauge = a / b
    except (ZeroDivisionError, ValueError):
        continue       
    else:
        break

if gauge == 1.0:
    print("F")
    
elif gauge < 1.0 and gauge > 0.1:
    gauge = gauge * 100
    gauge = str(gauge)
    gauge = gauge.replace(".0", "")
    print(f"{gauge}" + "%")
elif gauge <= 0.1:
    print("E")
        
