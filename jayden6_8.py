


"""
name of dictonary
age  
gpa
school
major 


make a dictonary about a book  use user input
title= name of dictonary
author
num_pages
date

book
title
author
pages
chapters - a list***


title =input("whats the name of the book? ")
author  = input("who wrote it? ")
pages = input("how many pages does it have? ")
"""
title = "bob"
author = "bob"
pages = "bob"



book = {"title": title, "author": author, "pages": pages}

print (book)


chapters = []
flag = True
while flag:
    chapter = input("Enter chapter name. Type 'n' to quit ")
    if chapter == "n":
        flag = False
    else: 
        chapters.append(chapter)
        
book["Chapters"] = chapters

print(book)
    