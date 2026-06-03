from main import app

import app as book

#------------Book-----------#
app.add_url_rule("/add_book", view_func=book.add_book, methods=["GET", "POST"])

# app.add_url_rule("/edit_book/<bid>",view_func=book.edit_book,methods=["GET","POST"])

# app.add_url_rule("/delete_book/<bid>",view_func=book.delete_book,methods=["GET","POST"])

# app.add_url_rule("/search_book",view_func=book.search_book)



