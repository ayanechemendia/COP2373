"""
Cinema Ticket Pre-Sales Application

This program allows users to pre-purchase cinema tickets.
Each buyer may purchase up to 4 tickets.
A maximum of 20 tickets may be sold in total.

The program continues until all tickets are sold,
then displays the total number of buyers.
"""

MAX_TICKETS = 10
MAX_PER_BUYER = 4


def get_ticket_request(remaining_tickets):
    """
    Prompts the user for the number of tickets they want to buy.

    Args:
        remaining_tickets (int): The number of tickets still available.

    Returns:
        int: A valid number of tickets requested.
    """
    tickets = int(input(
        f"\nThere are {remaining_tickets} tickets remaining.\n"
        f"How many tickets would you like to buy (1–{MAX_PER_BUYER})? "
    ))
    return tickets


def sell_tickets():
    """
    Controls the ticket-selling process, tracks remaining tickets
    and counts the number of buyers.
    """
    remaining_tickets = MAX_TICKETS
    total_buyers = 0  # accumulator

    while remaining_tickets > 0:
        requested = get_ticket_request(remaining_tickets)

        if requested < 1 or requested > MAX_PER_BUYER:
            print("Error: You may only purchase between 1 and 4 tickets.")
        elif requested > remaining_tickets:
            print("Error: Not enough tickets remaining.")
        else:
            remaining_tickets -= requested
            total_buyers += 1
            print(f"Purchase successful! Tickets remaining: {remaining_tickets}")

    print("\nAll tickets have been sold!")
    print(f"Total number of buyers: {total_buyers}")


# Program entry point
sell_tickets()


