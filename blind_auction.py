# Import required modules
from replit import clear
from art import logo

def main():
    print(logo)
    auction = blind_auction()
    person, bid_value = higher_bid(auction)
    print(f"The winner is {person} with a bid of ${bid_value}")

def blind_auction():
    # Collects bids in a blind auction
    auction_bids = {}
    while True:
        name = input("What is your name?: ").capitalize()
        bid = int(input("What is your bid? $"))
        ask_continue = input("Are there any other bidders? Type 'yes' or 'no'.")

        auction_bids[name] = bid  # Add bid to the dictionary

        if ask_continue.lower() == "yes":
            clear()  # Clear screen for next bidder
            continue
        else:
            break  # End loop if no more bidders
    
    return auction_bids

def higher_bid(auction):
    # Find highest bid and corresponding bidder
    highest_bid = 0
    winner = ""
    for bidder, bid in auction.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    return winner, highest_bid

# Run main if script is executed directly
if __name__ == "__main__":
    main()
