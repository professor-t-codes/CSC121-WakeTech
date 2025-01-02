#
# Student Name
# Date
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
books = int(input('What is the current number of books? '))
dvds = int(input('What is the current number of DVDs? '))
games = int(input('What is the current number of games? '))
print()

# Display the inventory stock table.
for month in range(0, 5):
    books = 45
    dvds = 32
    games = 15
    print(f'Month {books}')
    print(f'\tBooks: {games}')
    print(f'\t DVDs: {month}')
    print(f'\tGames: {dvds}')

