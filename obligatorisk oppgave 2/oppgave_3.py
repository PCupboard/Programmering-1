"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 3
Leveringsfrist: 29. september, 23.59
"""

tolkien_books = ["The Hobbit",
                 "Farmer Giles of Ham",
                 "The Fellowship of the Ring",
                 "The Two Towers",
                 "The Return of the King",
                 "The Adventures of Tom Bombadil",
                 "Tree and Leaf"]

print("Printer de to første og de to siste bøkene i listen:")
for book in [0, 1, 5, 6]:
    print(tolkien_books[book])

# Legger til bøkene
tolkien_books.extend(("The Silmarillion",
                     "Unfinished Tales"))


for book_index in range(len(tolkien_books)):
    if tolkien_books[book_index].lower() == "the fellowship of the ring":
        tolkien_books[book_index] = "Lord of the Rings: The Fellowship of the Ring"

    elif tolkien_books[book_index].lower() == "the two towers":
        tolkien_books[book_index] = "Lord of the Rings: The Two Towers"

    elif tolkien_books[book_index].lower() == "the return of the king":
        tolkien_books[book_index] = "Lord of the Rings: The Return of the King"

tolkien_books.sort()

print("\nPrinter ut den sorterte listen:")
for book in tolkien_books:
    print(book)