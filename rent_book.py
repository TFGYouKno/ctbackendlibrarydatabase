from DB_connections import connect_db, Error
from datetime import date

def rent_book():
    conn = connect_db()
    if conn is not None:
        try:
            title = input("Please enter the title of the book you would like to borrow: ").title()

            cursor = conn.cursor()

            query = 'SELECT * FROM books WHERE title = %s'

            cursor.execute(query, (title, ))

            id, title, author, availability = cursor.fetchall()[0]
            print(f'{id}. {title} by {author} is currently {availability}.')
            
            if availability == "available for loan":
                
                change_to_rented = "out on loan"
                
                availability_update = (change_to_rented, title)

                query2 = 'UPDATE books SET availability = %s WHERE title = %s;'

                cursor.execute(query2, availability_update)

                user_id = input("what is your member id:  ")
                book_id = id
                date_today = date.today()

                add_to_junct = (user_id, book_id, date_today) 

                query3 = 'INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)'

                cursor.execute(query3, add_to_junct)
                conn.commit()
                print(f'Here you are! Enjoy {title} and please return when you are done')

            elif availability == "out on loan":
                print(f"We are sorry, but {title} is currently out on loan. Check in at a later date when it is returned! ")
            
        except IndexError:
            print("Please enter a valid title and try again.")
        except Exception:
            print("Please enter a valid user from the repository")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()