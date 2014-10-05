#!/usr/bin/python
# -*- coding: utf-8 -*-



'''

This is the verbose version of my response to the Python code prompt. I may have gotten carried away making it interactive...

"Use object-oriented Python to model a public library (w/ three classes: Library, Shelf, & Book). *  

- The library should be aware of a number of shelves.
- Each shelf should know what books it contains.
- Make the book object have "enshelf" and "unshelf" methods that control what shelf the book is sitting on.
- The library should have a method to report all books it contains.

Note: this should *not* be a Django (or any other) app - just a single file with three classes (plus commands at the bottom showing it works) is all that is needed."

'''

import string
import random




class Library:
    
    def __init__(self):
    
        ''' Create a Library containing Shelf objects that contain Book objects, and can be queried with report_library_state() and list_all_shelf_contents(). A Library can fill itself with Book and Shelf objects via the regenerate_library() method and return its exact book count using count_books_in_this_library(). '''
        
        ## Create the_card_catalogue, which will contain all shelves and the books therein. They live in the little card drawers. It's a very small library.
        ## The keys of the_card_catalogue are lowercase letters of the alphabet corresponding to shelf names.
        self.the_card_catalogue = {}
    
        ## Books can be taken out of those musty old drawers. Who knows why anyone would want to.
        ## The keys of the_dictionary_of_unshelved_books are book title strings corresponding to the title of the book stored as each key's value.
        self.the_dictionary_of_unshelved_books = {}
    
        self.regenerate_library()
        
        
        
    def report_library_state(self):
    
        print( "\nThe library currently contains %r books in its %r shelves." % ( self.count_books_in_this_library(), len(self.the_card_catalogue) ) )
        print( "\n%r books are currently checked out of the library." % (len(self.the_dictionary_of_unshelved_books)) )
    
    
    
    def list_all_shelf_names(self):
    
        shelf_list_handler = []
    
        for each_shelf in sorted(self.the_card_catalogue):
        
            shelf_list_handler.append("%r (%r)" % (each_shelf, len(self.the_card_catalogue[each_shelf].shelf_contents)))
  
        shelf_list_string = ", ".join(shelf_list_handler)
        
        print("\nThis library contains the following shelves (with this many books):")
        
        print(shelf_list_string)
        
    
    
    def list_all_shelf_contents(self):
    
        for each_shelf in sorted(self.the_card_catalogue):
            self.the_card_catalogue[each_shelf].report_shelf_contents()

            
            
    def list_the_contents_of_this_particular_shelf(self, which_shelf_letter):
    
        ## Input sanitization.
        if determine_if_this_is_a_valid_shelf_name(which_shelf_letter):
        
            self.the_card_catalogue[which_shelf_letter].report_shelf_contents()
    
    
    
    def create_new_book(self, title=None):
    
        if title == None:
            
            new_book_title_list = []
    
           
            for each_new_book_title_character in range(0, random.randint(3, 6)):
            
                ## 97 through 122 are the ASCII ordinals for the lowercase letters a through z, inclusive.
                new_book_title_list.append(chr(random.randint(97, 122)))
     
                
            new_book_title = "".join(new_book_title_list)
            
        else:
        
            if title.isalpha():
                
                new_book_title = title
                
                
            else:
                
                raise ValueError("%r is not a valid character string." % (title))
            
            
        ## Note: Books are enshelved automatically upon initialization. This process requires the Book to know which library it's in so it can find its Shelf.
        ## Due to the automatic enshelvenation protocol, no return statement is necessary for this robotic library's create_new_book() method.
        the_new_book = Book(self, new_book_title)   
        
        
        
    def regenerate_library(self, new_books_to_create=None):
   
        ## In order to make a new library, you must:

        ## Burn down the building
        del self.the_card_catalogue
        del self.the_dictionary_of_unshelved_books
        
        ## Repair the ruins
        self.the_card_catalogue = {}
        self.the_dictionary_of_unshelved_books = {}
        
        ## Recarve the shelves
        for each_ordinal_for_the_letters_of_the_alphabet in range(97, 123):
        
            the_shelf_letter = chr(each_ordinal_for_the_letters_of_the_alphabet)
            
            self.the_card_catalogue[the_shelf_letter] = Shelf(the_shelf_letter)
        
        ## Gather monkeys and typewriters
        new_books_to_create = random.randint(30, 60)
      
        ## Rewrite the books
        for each_new_book in range(0, new_books_to_create):
            
            self.create_new_book()
    
    

    def count_books_in_this_library(self):

        number_of_books_in_the_library = 0
        
        for each_shelf_key_name in self.the_card_catalogue:
            
            for each_book_key_name in self.the_card_catalogue[each_shelf_key_name].shelf_contents:
                
                number_of_books_in_the_library += 1
    

        return number_of_books_in_the_library
    


class Shelf:
    
    def __init__(self, supplied_shelf_letter):

        ''' Create a Shelf named with a shelf_letter with shelf_contents inside it that can be known by calling report_shelf_contents(). '''
        
        self.shelf_letter = supplied_shelf_letter
        
        self.shelf_contents = {}
        
        
        
    def report_shelf_contents(self):
            
        if len(self.shelf_contents) > 0:
        
            print("\n  Shelf letter %r contains the following %r books:" % (self.shelf_letter, len(self.shelf_contents)))
            
            for each_book in sorted(self.shelf_contents):
            
                print("    " + self.shelf_contents[each_book].title)

        else:
            
            print("\n  Shelf letter %r is currently empty." % (self.shelf_letter))
                
                

    
class Book:
    
    def __init__(self, supplied_library_object, supplied_book_title):
    
        ''' Create a Book with a title that is_on_this_shelf and can be enshelf()ed amd unshelf()ed. '''
        
        self.reference_variable_for_the_library_this_book_is_inside = supplied_library_object
    
        #self.title = supplied_book_title
        self.title = supplied_book_title[0].upper() + supplied_book_title[1:]
        
        
        self.is_on_this_shelf = None
        
        self.enshelf()


     
    def unshelf(self, no_shuffle_trace=False):
        
        ''' Ensure this Book is not in a Shelf by removing it from any Shelf it might be in and inserting it into the_dictionary_of_unshelved_books. '''
        
        ## If this book is NOT in the pile of unshelved books...
        if self.is_on_this_shelf != self.reference_variable_for_the_library_this_book_is_inside.the_dictionary_of_unshelved_books:
        
            ## If the book was recently created, it might have None as its Shelf reference. foo.pop() wouldn't like that, so handle it with a simple conditional:
            if self.is_on_this_shelf != None:
            
                ## Cancelling the confusing half of the spamminess at the start:
                if no_shuffle_trace == False:
            
                    old_shelf_letter = self.is_on_this_shelf.shelf_letter
                    
                    old_shelf_contents = ", ".join(sorted(list(self.reference_variable_for_the_library_this_book_is_inside.the_card_catalogue[old_shelf_letter].shelf_contents)))
            
                    print(" || Shelf %r contents: %r" % (old_shelf_letter, old_shelf_contents))
                    
                    print(" <--- Book %r has been removed from shelf %r." % (self.title, self.is_on_this_shelf.shelf_letter))
                    
                    self.is_on_this_shelf.shelf_contents.pop(self.title)
            
                    old_shelf_contents = ", ".join(sorted(list(self.reference_variable_for_the_library_this_book_is_inside.the_card_catalogue[old_shelf_letter].shelf_contents)))
            
                    print(" || Shelf %r contents: %r" % (old_shelf_letter, old_shelf_contents))
            
                ## This else is necessary because before pop() the book is still on the old shelf and after pop() it's gone, and without taking that into account the print messages aren't as nifty.
                else:
                
                    self.is_on_this_shelf.shelf_contents.pop(self.title)
                
            ## Now put the book in the unshelved pile:
            self.reference_variable_for_the_library_this_book_is_inside.the_dictionary_of_unshelved_books[self.title] = self
            
            ## ... and make sure it knows it's there.
            self.is_on_this_shelf = self.reference_variable_for_the_library_this_book_is_inside.the_dictionary_of_unshelved_books           
                
    
    
    def enshelf(self, which_shelf_letter=None, no_shuffle_trace=True):
    
        if which_shelf_letter == None:
            which_shelf_letter = self.title[0].lower()
            
        
        ## First, ensure the book is 100% unshelved and placed in the unshelved Book pile:
        self.unshelf(no_shuffle_trace=True) # enshelf() shouldn't use no_shuffle_trace=False.
        
                
        ## The Book must now be removed from the pile of unshelved Books:
        self.reference_variable_for_the_library_this_book_is_inside.the_dictionary_of_unshelved_books.pop(self.title)
        
        ## Now we need to obtain a reference to the specific Shelf this Book must go in:
        shelf_to_put_this_book_on = self.reference_variable_for_the_library_this_book_is_inside.the_card_catalogue[which_shelf_letter]
                
        ## The act of putting a Book in a Shelf is creating a key inside the Shelf's shelf_contents dictionary and setting its value to this Book object.
        shelf_to_put_this_book_on.shelf_contents[self.title] = self
            
        self.is_on_this_shelf = shelf_to_put_this_book_on
   

        ## This removes the spam during Book initialization and saves it for Book shuffling:
        if no_shuffle_trace == False:
        
            print(" ---> Book %r has been moved to shelf letter %r." % (self.title, self.is_on_this_shelf.shelf_letter))  
        
            print(" || Shelf %r contents: %r" % (self.is_on_this_shelf.shelf_letter, ", ".join(sorted(self.is_on_this_shelf.shelf_contents))))
            

                
def determine_if_this_is_a_valid_shelf_name(which_shelf_letter):
    
    
    which_shelf_letter = which_shelf_letter.lower()
        
    if not which_shelf_letter.isalpha():
            
        print("%r is not an alphanumeric string." % (which_shelf_letter))
        
    elif ( len(which_shelf_letter) != 1):
        
        print("%r is either too long or too short to be a single letter." % (which_shelf_letter))
            
    elif ( ord(which_shelf_letter) < 97 ) or ( ord(which_shelf_letter) > 122 ):
            
        print("%r is not a valid shelf letter." % (which_shelf_letter))
        
    else:
        
        return True

                
    
    def unshelf(self, no_shuffle_trace=True):
    
        ''' Ensure this Book is not in a Shelf by removing it from any Shelf it might be in and inserting it into the_dictionary_of_unshelved_books. '''       
        ## If this book is NOT in the pile of unshelved books...
        if self.is_on_this_shelf != self.reference_variable_for_the_library_this_book_is_inside.the_dictionary_of_unshelved_books:
        
            ## If the book was recently created, it might have None as its Shelf reference. foo.pop() wouldn't like that, so handle it with a simple conditional:
            if self.is_on_this_shelf != None:
            
            
                ## Cancelling the confusing half of the spamminess at the start:
                if no_shuffle_trace == False:
            
                    old_shelf_letter = self.is_on_this_shelf.shelf_letter
                    
                    old_shelf_contents = ", ".join(sorted(list(self.reference_variable_for_the_library_this_book_is_inside.the_card_catalogue[old_shelf_letter].shelf_contents)))
            
                    print(" || Shelf %r contents: %r" % (old_shelf_letter, old_shelf_contents))
                    
                    print(" <--- Book %r has been removed from shelf %r." % (self.title, self.is_on_this_shelf.shelf_letter))
                    
                    self.is_on_this_shelf.shelf_contents.pop(self.title)
            
                    old_shelf_contents = ", ".join(sorted(list(self.reference_variable_for_the_library_this_book_is_inside.the_card_catalogue[old_shelf_letter].shelf_contents)))
            
                    print(" || Shelf %r contents: %r" % (old_shelf_letter, old_shelf_contents))
              
                ## This else is necessary because before pop() the book is still on the old shelf and after pop() it's gone, and without taking that into account the print messages aren't as nifty.
                else:
            
                    ## Note: The syntax here understands the Book to be at the following location: the_library.the_card_catalogue[foo_shelf.shelf_letter][self.title] == self
                    self.is_on_this_shelf.shelf_contents.pop(self.title)
                
            ## Now put the book in the unshelved pile:
            self.reference_variable_for_the_library_this_book_is_inside.the_dictionary_of_unshelved_books[self.title] = self
            
            ## ... and make sure it knows it's there.
            self.is_on_this_shelf = self.reference_variable_for_the_library_this_book_is_inside.the_dictionary_of_unshelved_books
                
            
        else:
            
            ## Then the Book is already unshelved.
            pass

            
            
def capitalize_first_letter(input_string):
            ''' Helpfully ensure a string's first letter is capitalized regardless of user input. Good for manual book shelving. '''
            
            if len(input_string) > 1:
                output_string = input_string[0].upper() + input_string[1:]            
            else:
                output_string = remove_this_particular_book.upper()
            
            return output_string


            
def handle_input(input_string, supplied_reference_to_the_library):
    
    
    ## The leading number lets us use sorted() to list commands in this order. List slicing removes it for display to the user.
    the_dictionary_of_command_help_strings = {
    '0library': 'View the state of the library.',
    '1liberry': 'Spam the screen with a full list of all books in all shelves.',
    '2shelves': 'List all shelf titles.',
    '3shelved': 'List the contents of a shelf specified in a subsequent prompt.',
    '4enshelf': 'Put a book into a shelf using two subsequent prompts.',
    '5unshelf': 'Remove a currently-shelved book from its shelf using two subsequent prompts.',
    '6noshelf': 'List all books currently left unshelved.',
    '7quitelf': 'Summons an elf who will end the program for you.',
    '8shufelf': 'Watch the library elves mischievously shuffle books from one shelf to another for their own inscrutable purposes.'
    }     
    
    if input_string == 'help' or input_string == "'help'" or input_string == 'commands' or input_string == 'command':
    
        print("\n")
    
        for each_help_string in sorted(the_dictionary_of_command_help_strings):
        
            print(each_help_string[1:] + ": " + the_dictionary_of_command_help_strings[each_help_string])
    
    
    elif input_string == 'quit' or input_string == 'quitelf' or input_string == 'quit elf' or input_string == 'exit' or input_string == 'end':
    
        return 'quit'
            
            
    elif input_string == 'library':
        
        supplied_reference_to_the_library.report_library_state()
        
        
    elif input_string == 'liberry':
        
        supplied_reference_to_the_library.list_all_shelf_contents()
        
        
    elif input_string == 'shelves':
    
        supplied_reference_to_the_library.list_all_shelf_names()
        
        
    elif input_string == 'shelved':
        
        
        try:
        
            supplied_reference_to_the_library.list_all_shelf_names()
            
            this_shelf = raw_input("\n>> Enter a shelf letter to display the contents of:\n> ")[:1].lower()
    
            supplied_reference_to_the_library.list_the_contents_of_this_particular_shelf(this_shelf)
    
        except:
            
            print("\nShelf not found.")
            
        
        
    elif input_string == 'enshelf':
        
        if len(supplied_reference_to_the_library.the_dictionary_of_unshelved_books) > 0:
            
            
            try:
                    
                move_this_particular_book = raw_input("\n>> List of books currently unshelved: %r\n\n>> Enter a book title to place in a shelf:\n> " % (", ".join(sorted(supplied_reference_to_the_library.the_dictionary_of_unshelved_books))))
                    
                move_this_particular_book = capitalize_first_letter(move_this_particular_book)
                    
                to_this_particular_shelf = raw_input("\n>> List of shelves in the library: %r\n\n>> Enter a shelf letter to place the masterpiece %r inside:\n> " % (", ".join(sorted(supplied_reference_to_the_library.the_card_catalogue)), move_this_particular_book))[:1].lower()

                supplied_reference_to_the_library.the_dictionary_of_unshelved_books[move_this_particular_book].enshelf(which_shelf_letter=to_this_particular_shelf, no_shuffle_trace=True)
                    
                print("\n%r has been moved to shelf letter %r." % (move_this_particular_book, to_this_particular_shelf))
                
            except:
                
                print("\nError! Shelf or book not recognized.")
                
        else:
            
            print("\nThere are currently no books not on a shelf.")
            
            
    elif input_string == 'unshelf':
        
        
        try:
            
            
            supplied_reference_to_the_library.list_all_shelf_names()
            
            from_this_particular_shelf = raw_input("\n>> Enter a shelf letter to remove a book from:\n> ")[:1].lower()
            
            if len(supplied_reference_to_the_library.the_card_catalogue[from_this_particular_shelf].shelf_contents) > 0:
            
                remove_this_particular_book = raw_input("\n>> List of books on shelf letter %r: %r\n\n>> Enter a book title to remove from this shelf:\n> " % (from_this_particular_shelf, ", ".join(sorted(supplied_reference_to_the_library.the_card_catalogue[from_this_particular_shelf].shelf_contents))))
                
                remove_this_particular_book = capitalize_first_letter(remove_this_particular_book)
                
                supplied_reference_to_the_library.the_card_catalogue[from_this_particular_shelf].shelf_contents[remove_this_particular_book].unshelf(no_shuffle_trace=True)
                
                print("\n%r has been added to the list of unshelved books." % (remove_this_particular_book))
                
            else:
                
                print("\n  Shelf letter %r is currently empty." % (from_this_particular_shelf))
                
    
        except:
            
            print("\nError! Shelf or book not found.")
    
    
    elif input_string == 'noshelf':
        
        if len(supplied_reference_to_the_library.the_dictionary_of_unshelved_books) == 0:
        
            print("\nThere are currently no books not on a shelf.")
        
        else:
            
            print("\nBooks currently not on a shelf:\n" + ", ".join(sorted(supplied_reference_to_the_library.the_dictionary_of_unshelved_books)))
            

    elif input_string == 'shuffle' or input_string == 'shufelf' or input_string == 'shuffelf' or input_string == 'shuffel':
        
        shuffle_books(supplied_reference_to_the_library)
            
            
    else:
        
        print("\nCommand not recognized: %r" % (input_string))
 

 
def shuffle_books(supplied_library_reference):
                
    ''' Demonstrate the functionality of the enshelf() and unshelf() methods. '''
            
    ## One book per turn is plenty.
    #number_of_books_to_shuffle = random.randint(2, 5)
    number_of_books_to_shuffle = 1
    number_of_books_shuffled = 0
    
    while number_of_books_shuffled < number_of_books_to_shuffle:
        
        first_random_shelf_letter = chr(random.randint(97, 122))
        second_random_shelf_letter = chr(random.randint(97, 122))
        
        ## If there's nothing there, get another letter and try again.
        if len(supplied_library_reference.the_card_catalogue[first_random_shelf_letter].shelf_contents) == 0:
            
            pass
                
        else:
        
            random_book_key = random.choice(list(supplied_library_reference.the_card_catalogue[first_random_shelf_letter].shelf_contents.keys()))
            
            the_book_to_shuffle = supplied_library_reference.the_card_catalogue[first_random_shelf_letter].shelf_contents[random_book_key]
            
            the_book_to_shuffle.unshelf(no_shuffle_trace=False)
            the_book_to_shuffle.enshelf(which_shelf_letter=second_random_shelf_letter, no_shuffle_trace=False)
            
            number_of_books_shuffled += 1

            
            
def main():


    the_library = Library()
    
    print("\nWelcome to the library!")

    the_library.report_library_state()
       

    while True:
    
        next_command = 'shuffle'
    
        try:
        
            next_command = raw_input("\nEnter a specific command, press enter to shuffle a random book to a random shelf, or enter 'help' to view a list of commands.\n")
                
            ## Input sanitization and validation, from try:except to wringing of nonalphabetics.    
            next_command = next_command.lower()
            
            valid_letters = "abcdefghijklmnopqrstuvwxyz"
            
            ## This line runs through next_command and puts everything not in valid_letters into a little box, then connects all those things back into a single string.
            next_command = ''.join(each_character for each_character in next_command if each_character in valid_letters)    
                
            ## The default command: elven tomfoolery.
            if next_command == '':
                    
                next_command = 'shuffle'
       
        except:
        
            print("\n  Invalid input; this library does not allow numbers or symbols!")

            
        command_handler = handle_input(next_command, the_library)

        if command_handler == 'quit':
        
            break


            
if __name__ == '__main__':
    main()