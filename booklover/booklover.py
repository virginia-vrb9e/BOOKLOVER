import numpy as np
import pandas as pd
    
"""
This class creates a database of contact information and beloved books
for book lovers (users). 
Attributes:
----------
name :      (type:string) user's name
email :     (type:string) user's email
fav_genre : (type:string) user's favorite genre; (default=None)
num_books : (type:int) number of books user has read/logged
book_list : (type:pd.DataFrame) a DataFrame of:
                book titles (type:string) and 
                ratings (type: integer) provided by the user 
                on a scale of 1 - 5: 
                    1(lowest rating) 
                    5(highest rating)
"""
class BookLover:
    def __init__(self, name, email, fav_genre):  # constructor
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        self.num_books = 0 # initialize at zero
        
    def add_book(self, book_name, book_rating):  #Method #1: add_book
        
        """
        Takes a book title and adds it to a unique list of books.
        Parameters
        ----------
        book_name :  str
        book_rating : int
            a rating from 1 - 5 with 1 being the lowest rating and 5 the highest
        """
        
        if book_name in self.book_list["book_name"].values: #indexing into dictionary key vector
            print(f"You've already added '{book_name}' to your list.")
            return
        
        # add book
        new_book = pd.DataFrame({'book_name': [book_name],'book_rating': [book_rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        print(f"'{book_name}' with a rating of {book_rating} has been added to your list.")
        self.num_books += 1
        return self.book_list # this makes the DF print out. 

        
    def has_read(self, new_book_name):  # Method 2: has_read
  
        """
        Checks to see if a book title has already been added to the list
        Parameters
        ----------
        book_name : str
            a book title
        """
    
        if new_book_name in self.book_list["book_name"].values:
            return True
            # print('True')
        else:
            return False

    def num_books_read(self):  # Method 3: num_books_read   
        """
        This method is a static method 
        It returns a value that is the number of books read 
        (according to the book list)
        Return:
        -------
        num_books_read : int
        """
        print(self.num_books)       

    def fav_books(self):  # Method 4: fav_books
        """
        This is another static method. 
        It returns a filtered DataFrame
        of a person's favorite books (rating > 3).
        Return:
        ------
        fav_books : pd.DataFrame
        """
        fav_books_list = []
        for index, row in self.book_list.iterrows():  # df.iterrows()
            if (row['book_rating'] > 3):
                fav_books_list.append(row['book_name'])
        return fav_books_list
    
if __name__ == '__main__':  
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.has_read("The Martian")
    test_object.num_books_read()
    test_object.fav_books()
    
# Testing Class for Correct Functioning    
#testing method #1    
    # instantiate
# booklover_mary = BookLover('Mary Lamb', 'maryhada@littlelamb.com', "Children's")
# booklover_mary.name
# booklover_mary.book_list
# booklover_mary.book_list.book_name # ok
# bk = np.array(booklover_mary.book_list.book_name) #ok
# bk[-1] # ok

#testing method #2
# booklover_mary = BookLover('Mary Lamb', 'maryhada@littlelamb.com', "Children's")
# booklover_mary.has_read('Lord of the Flies')
# booklover_mary.has_read('A')

# testing method #3
# booklover_mary = BookLover('Mary Lamb', 'maryhada@littlelamb.com', "Children's")
# booklover_mary.add_book('Middlemarch', 5)
# booklover_mary.add_book('Fahrenheit 451', 5)
# booklover_mary.add_book('To Kill a Mockingbird', 5)
# booklover_peter = BookLover('Peter Parker', 'spidey@boynextdoor.com', "Travel")
# booklover_peter.add_book('Harry Potter', 2)
# booklover_peter.num_books_read()
    

# testing method #4
# booklover_peter = BookLover('Mary Lamb', 'maryhada@littlelamb.com', "Children's")
# booklover_peter.add_book('Harry Potter IV', 2)
# booklover_peter.add_book('Lord of the Flies IV', 4)
# booklover_peter.add_book('Leaves of Grass IV', 5)
# booklover_peter.fav_books()

# https://stackoverflow.com/questions/40659212/futurewarning-elementwise-comparison-failed-returning-scalar-but-in-the-futur
                 
                 
                 
                 
                 
                 
                 
                 
                 
            