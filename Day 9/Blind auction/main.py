bidders = {}

while True:
    name = input("What is your name? ")
    print(f"Welcome, {name}!")

    current_bid = int(input("What's your bid? $"))
    
    bidders[name] = current_bid

    check = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if check != 'yes':
        break

if bidders:
    highest_bidder = max(bidders, key=bidders.get)
    highest_bid = bidders[highest_bidder]

    print("\nBidding Results:")
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

    print("\nAll Bids:")
    for bidder, bid in bidders.items():
        print(f"{bidder}: ${bid}")
else:
    print("No bids were placed.")
