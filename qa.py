word1 = "Good"
word2 = "Day"
word3 = "Tom"

sent = word1 + " " + word2 + " " + word3 + " "

print(sent)

books = {"Margaret Atwood":"The Handmaiden's Tale", "J.R.R. Tolkien":["The Hobbit", "The Lord of the Rings"], "Roald Dahl":"Charlie and the Chocolate Factory"}
author_input = input("Enter author: ")
author_list = books[author_input]
books_join = (", ".join(sorted(author_list)))
print(books_join)
