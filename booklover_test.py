# a test file for the BookLover class (booklover.py)

# Note that you do not need to create an __init__() method in this class, 
# nor do you have to define any class variables.
# Instead, treat every method as a small, stand-alone program 
# in which you create a new object for your test. 
# This is not the best practice in a production environment, 
# but it works and it will enable you to get the gist of unit testing.

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        
        # initiate the class:
        book_list_test = BookLover("Harry Potter", "potter@hogwarts.co.uk", "Fantasy")
        # add a book:
        book_list_test.add_book("Charlotte's Web", 2)
        # check if it was added to book_list:
        # self.assertIn(value, container, message)
        self.assertIn("Charlottes's Web", self.book_list, "Unknown Error: The book wasn't added to your list for some reason.") 
        
        
    def test_2_add_book(self):  
        # add the same book twice. 
        booklover_test.add_book("Mary Poppins", 4)
        booklover_test.add_book("Mary Poppins", 4)
        # test if it's in `book_list` only once.
        book_names = self.book_list.loc[:, "book_name"]
        assertTrue(book_names.is_unique)
        
        
    def test_3_has_read(self): 
        # pass a book in the list & test if answer is `True`.
        booklover_test.add_book("ABC", 1)
        self.assertTrue(booklover_test.has_read("ABC"))
        self.assertTrue(booklover_test.has read(booklover_test.book_list.iloc[0,0]))

        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        value = self.book_list.iloc[0,0]
        self.assertFalse(booklover_test.has_read(value[:5]))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklover_test.add_book("The Stand", 5)
        booklover_test.add_book("The Haunting of Hill House", 5)
        self.assertEqual(booklover_test.num_books == 5)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        booklover_test.add_book("Midnight in the Garden of Good and Evil", 4)
        booklover_test.add_book("Lord of the Rings", 5)
        booklover_test.add_book("Clear and Present Danger", 2)
        # Your test should check that the returned books have rating  > 3   
        self
        
                
if __name__ == '__main__':
    unittest.main(verbosity=3)