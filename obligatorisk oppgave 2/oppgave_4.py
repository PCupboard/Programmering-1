"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 4
Leveringsfrist: 29. september, 23.59
"""

tolkien_books = ["Farmer Giles of Ham",
                 "Lord of the Rings: The Fellowship of the Ring",
                 "Lord of the Rings: The Return of the King",
                 "Lord of the Rings: The Two Towers",
                 "The Adventures of Tom Bombadil",
                 "The Hobbit",
                 "The Silmarillion",
                 "Tree and Leaf",
                 "Unfinished Tales"]

lotr_books = []

for book in tolkien_books:
    if not book.lower().find("lord of the rings: "):
        lotr_books.append(book)

for book_index in range(len(lotr_books)):
    print(lotr_books[book_index])




