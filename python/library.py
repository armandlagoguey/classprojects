books = [
    ("B01", "1984", "available"),
    ("B02", "Dune", "borrowed"),
    ("B03", "Foundation", "available"),
    ("B04", "It", "borrowed"),
    ("B05", "Hamlet", "available")
]

library={}

for bookid, title, status in books:
    library[bookid] = {
        "title":title,
        "status":status
    }

for index, (bookid,info) in enumerate(library.items(), start=1):
    title = info["title"]
    status = info["status"]
    print(f"{index}. {bookid} - {title} ({status})")

available = 0
borrowed = 0

for book_id, info in library.items():
    if info["status"] == "available":
        available += 1
    elif info["status"] == "borrowed":
        borrowed += 1

print("Available:", available)
print("Borrowed:", borrowed)

available_titles = []

for book_id, info in library.items():
    if info["status"] == "available":
        available_titles.append(info["title"])

print("Available book titles:", available_titles)

