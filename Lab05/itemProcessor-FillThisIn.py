#
# Student Name
# Date
# Module to help process item data
#

# Global Constants - Use these in your program where it makes sense
TAX_RATE = 0.065  # 6.5% sales tax
VOLUME_DISCOUNT = 0.95  # 95% of total is 5% off


def get_item_count(item_name, max_allowed, discount_threshold):
    """
    This function will ask the user to enter the number of items and
    validate the number entered is between 0 and the max_allowed
    inclusive. The number of items the user enters is returned.

    :param item_name: Name of item being prompted about
    :param max_allowed: Maximum number of items the user can enter
    :param discount_threshold: Minimum number of items eligible for 5% discount
    :return: Number of items entered by user (validated)
    """

    print(f'Enter the number of {item_name}.')
    items = int(input(f'\t{discount_threshold} or more receive a discount: '))
    # TODO: Add the input validation code here
    return items


def get_item_total(num_items, unit_price, discount_threshold):
    """
    This function calculates the total cost for the items and
    returns that value.

    :param num_items: Number of items
    :param unit_price: The cost of each item
    :param discount_threshold: Minimum number of items eligible for 5% discount
    :return: Total cost of item
    """
    # TODO: Remove the following pass statement, then implement
    #  this function.
    pass


def calc_and_display_receipt(book_total, dvd_total, game_total):
    """
    This function will calculate total before tax, the tax on the total,
    and the total after tax is added.

    The receipt should display the total cost of books, DVDs, and
    games IF the item cost is greater than 0. The receipt should also
    include the subtotal, tax, and total.

    :param book_total: Total cost of books
    :param dvd_total: Total cost of DVDs
    :param game_total: Total cost of games
    :return:
    """

    # TODO: Remove the following pass statement, then implement
    #  this function.
    pass
