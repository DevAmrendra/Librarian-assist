pages = int(input("Enter number of pages"))

if pages <= 100:
    print("Short Book")
elif pages > 100 and pages <= 300:
    print("Medium Book")
else:
    print("Long Book")

=