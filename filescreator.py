# List of filenames (without extensions)
filenames = [
'Friends S01E01 The One Where Monica Gets a New Roomate',
'Friends S01E02 The One With the Sonogram at the End',
'Friends S01E03 The One With the Thumb',
'Friends S01E04 The One With George Stephanopoulos',
'Friends S01E05 The One With the East German Laundry Detergent',

]

# Loop through each name and create an empty .txt file
for name in filenames:
    with open(f"{name}.txt", 'w') as file:
        pass  # Just create an empty file
