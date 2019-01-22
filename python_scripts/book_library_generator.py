#!/usr/bin/env python3
"""Generate a library file"""

import random

AUTHORS_FIRST = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Gerry",
    "Harry",
    "Irene",
    "Jenny",
]
AUTHORS_LAST = [
    "Kurose",
    "Lee",
    "Miller",
    "Null",
    "O'Reilly",
    "Patterson",
    "Quicksilver",
    "Ross",
    "Silberschatz",
    "Tanenbaum",
]
TITLES_ADV = [
    "Introduction to",
    "Mastering",
    "Developing",
    "Advanced",
    "Hacking",
    "Understanding",
    "Diving into",
]
TITLES_ADJ = [
    "Java",
    "C++",
    "Python",
    "Secure",
    "Computer",
    "Hardware",
    "Database",
    "Web",
    "Game",
    "Operating",
]
TITLES_NOUN = [
    "Basics",
    "Fundamentals",
    "Concepts",
    "Systems",
    "Security",
    "Problems",
    "Networks",
    "Principles",
]


class Book:
    """Book class"""

    def __init__(self):
        """
        Create a new book object
        isbn author(s) title year edition
        """
        self._isbn = "".join([str(random.randint(0, 9)) for _ in range(13)])
        self._authors = self.authors()
        self._title = self.title()
        self._edition = random.randint(1, 9)
        self._year = random.randint(1990, 2017)
        self._price = random.random() * 100

    def authors(self):
        """Generate the author(s)"""
        authors_str = f"{random.choice(AUTHORS_FIRST)} {random.choice(AUTHORS_LAST)}"
        if random.random() > 0.5:
            authors_str += (
                f" & {random.choice(AUTHORS_FIRST)} {random.choice(AUTHORS_LAST)}"
            )
        return authors_str

    def title(self):
        """Generate the title"""
        if random.random() > 0.5:
            return (
                random.choice(TITLES_ADV)
                + " "
                + random.choice(TITLES_ADJ)
                + " "
                + random.choice(TITLES_NOUN)
            )
        else:
            return random.choice(TITLES_ADJ) + " " + random.choice(TITLES_NOUN)

    def __str__(self):
        """Convert a book to a string"""
        return "{:15}{:40}{:^5}{:45}{:5}{:8.2f}".format(
            self._isbn,
            self._title,
            self._edition,
            self._authors,
            self._year,
            self._price,
        )


with open("library.txt", "w") as file_out:
    file_out.write(
        "{:15}{:40}{:^5}{:45}{:>5}{:^10}".format(
            "ISBN", "Title", "Ed", "Author(s)", "Year", "Price"
        )
        + "\n"
    )
    for _ in range(100):
        b = Book()
        file_out.write("{}\n".format(b))
