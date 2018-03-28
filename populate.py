import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'webapp.settings')

import django
django.setup()
from webapp.models import Book, Location

def populate():

    books = [
        {"title": "The dear green place",
        "author": "Archie Hind",
        "summary": "The dear green place is a perceptive portrayal of Glasgow"
                   " and the struggle of its hero Mat Craig to realise his ambition to be a writer. "
                   "Mat moves from office, to slaughterhouse to poverty obsessed by his need to create.",
        "quotes": "Beyond the railway embankment lay stretches of derelict land of the kind seen on the edges "
                  "of big cities. Broken down furnaces and kilns were still crumbling around where the claypits"
                  " had once been worked. <..> Further on than this slag heaps and dumps for industrial refuse"
                  " - here in Glasgow they are called coups - stretched down the Clyde. ",
        "location_mentioned":"Glasgow",
        "isbn":"9780904919813"
         } ]

    locations = [
        {
            "name": "Glasgow",
            "country": "United Kingdom",
            "region": "Scotland",
            "description":"Glasgow is a port city on the River Clyde in Scotland's western Lowlands. "
                          "It's famed for its Victorian and art nouveau architecture, a rich legacy of "
                          "the city's 18th–20th-century prosperity due to trade and shipbuilding."
                          " Today it's a national cultural hub, home to institutions including the "
                          "Scottish Opera, Scottish Ballet and National Theatre of Scotland, as well"
                          " as acclaimed museums and a thriving music scene. "
        }
    ]

    for book, book_data in books.items():
        c = add_book(book)
        for p in book_data[""]

    def add_book(book, title, author, summary, quotes, location_mentioned, isbn):
        p = Page.objects.get_or_create()