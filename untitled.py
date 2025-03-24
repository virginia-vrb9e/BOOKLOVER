from booklover.booklover import BookLover
BookLover
 # instantiates well:
booklover_oliver = BookLover("Oliver Twist", 'hardknocks@likethedickens.co.uk', "Children's")
booklover_oliver.name

#will not go beyond __init__() method; it's only partially installing 
# I could not figure out why...

booklover_oliver.add_book('ABC', 2)
