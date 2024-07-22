from add_book import add_book
from get_book import get_book, get_encyclopedia
from user_add import add_user
from user_get import get_user, get_user_list
from rent_book import rent_book
from return_book import return_book
from borrowed import get_borrowed

def main():
    while True:
        main_menu = input('''
Welcome to Tampa Library, located in Tampa, FL!
How may I help you today?

1. Book Repository
2. Tampa Members Cult
3. Back to Reality
    ''')
        if main_menu == '1':
            book_repository()              
        elif main_menu == "2":
            Members_club()               
        elif main_menu == '3':
            print("Thanks for coming!")
            break
        else:
            print("Please enter a valid selection.")
            continue


def book_repository():
    while True:
        book_menu = input('''
Welcome to the Book Repository! what would you like to do:

1. Add a new book
2. Rent a book
3. Return a book
4. Search the Repository 
5. Display the Repository
6. Show rented books by member ID
7. Back to main menu
    ''')
        if book_menu == '1':
            add_book()
        elif book_menu == '2':
            rent_book()
        elif book_menu == '3': 
            return_book()
        elif book_menu == '4':
            get_book()
        elif book_menu == '5':
            get_encyclopedia()
        elif book_menu == '6':
            get_borrowed()
        elif book_menu == '7':
            break
        else:
            print("Please enter a valid selection! ")
            continue


def Members_club():
    while True: 
        club_menu = input('''
Welcome to the Tampa Library Members Cult! How can I help you?:

1. Become a member
2. Search for a member
3. Display full member list
4. Back to main menu                         
    ''')
        if club_menu == '1':
            add_user()
        elif club_menu == '2':
            get_user()
        elif club_menu == '3': 
            get_user_list()
        elif club_menu == '4':
            break
        else:
            print("Please enter a valid selection")
            continue


main()