# Auction Program


def auction_run():
    # ask the user for the item being auctioned
    item = input("What is the auction for?: ")
    # ask the user for the reserve price
    reserve_price = float(input("What is the reserve price? "))
    # set the current bid to be the reserve price
    bid = 0
    # keep looping until the user enters -1
    while bid != -1:
        # display the current highest bid
        print(f"Highest Bid so far is ${bid:.2f}")
        # ask the user for their bid
        user_bid = float(input("What is your bid?: "))
        # if the user's bid is higher than the current bid, update the current bid
        if user_bid > bid:
            bid = user_bid
        # if the user enters -1, end the auction and exit the loop
        elif user_bid == -1:
            print(f"The auction for {item} has finished with no winning bid")
            break
        # if the user's bid is less than or equal to the current bid, ask them to bid higher
        else:
            print("Please bid higher than the current bid.")
    # after the loop, check if the winning bid meets the reserve price or not
    if bid >= reserve_price:
        print(f"The auction for {item} has finished with a winning bid of ${bid:.2f}")
    else:
        print(f"The auction for {item} has finished without meeting the reserve price of ${reserve_price:.2f}")


# call the auction_run function to start the program
auction_run()
