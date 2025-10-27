greeting = input("Greeting: ").lower()

if greeting == "hello":
    print("0$")
elif "h" in greeting[0] and greeting != "hello":
    print("20$")
else:
    print("100$")