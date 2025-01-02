#
# Student Name
# Date
# X Pattern Generator
#

# Do not change the next line. Just ignore it.
FillThisIn = None

# Replace the FillThisIn below with correct code.
# Do not change or remove any other parts of the
# code or comments.

# Ask the user for the size of the pattern
# Use the prompt from the Sample Output.
size = FillThisIn

# Iterate over the rows.
for row in range(FillThisIn):
    # Iterate over the columns.
    for col in range(FillThisIn):
        # Test if the position is on the diagonal
        # Hint: Test if col and row are equal
        if FillThisIn:
            print('*', end='')
        # Test if col and row are on the other diagonal
        # Hint: The other diagonal is where the sum of
        # the row and column indices equals the size - 1
        elif FillThisIn:
            print('*', end='')
        else:
            print(' ', end='')

    # Go to the next row.
    print()
