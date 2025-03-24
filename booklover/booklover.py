import numpy as np
import pandas as pd

class BookLover:
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
    Methods:
    --------
    """

    # constructor
    def __init__(self, name, email, fav_genre= None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        num_books = 0  # initialize at zero, then add
        book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
   
    # Method 1: add_book             
    def add_book(self, book_name, book_rating):
        """
        Takes a book title and a numeric rating from 1 to 5 and adds it to a unique list of books.
        Parameters
        ----------
        book_name :  str
        book_rating : int
            a rating from 1 - 5 with 1 being the lowest rating and 5 the highest
        Raises
        ------
        none
        """
        
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        #self.book_name = book_name
        #self.book_rating = book_rating
        #new_book_input = {book_name : book_rating}
        if book_name in self.book_list:
            print("You already put that book in your list. Choose another one.")
        else:
            # self.book_list.update(new_book_input)
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            # return book_list

    # Method 2: has_read
    def has_read(self, book_list, book_name):
        """
        Checks to see if a book title has already been added to the list
        Parameters
        ----------
        book_name : str
            a book title
        Raises
        ------
        none
        """
        if book_name in book_list:
            return True
        else:
            return False
     
    # Method 3: num_books_read   
    def num_books_read(book_list):
        """
        This method is a static method 
        It returns a value that is the number of books read 
        (according to the book list)
        Return:
        -------
        num_books_read : int
        """
        return len(book_list)

    # Method 4: fav_books
    def fav_books(book_rating, book_list):
        """
        This is another static method. 
        It returns a filtered DataFrame
        of a person's favorite books (rating > 3).
        Return:
        ------
        fav_books : pd.DataFrame
        """
        fav_books = [x for x in book_list if x > 3]
        return pd.DataFrame(fav_books)



if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    # And so forth  