amount_due = 50
stop = False

while stop == False:
        print(f"Amount Due: {amount_due}")
        amount_inserted = int(input("Insert Coin: "))
        if amount_inserted == 5 or amount_inserted == 10 or amount_inserted == 25:
            amount_due = amount_due - amount_inserted
        if amount_due <= 0:
            print(f"Change Owned: {amount_due * -1}")
            stop = True