from DB_connections import connect_db, Error

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            title = input("Please enter the title of the book you are trying to return:\n").title()

            cursor = conn.cursor()

            query = 'SELECT * FROM books WHERE title = %s'

            cursor.execute(query, (title, ))

            id, title, author, availability = cursor.fetchall()[0]
            print(f'{id}. {title} by {author} is currently {availability}.')

            if availability == "out on loan":

                change_availability = "available to borrow"

                availability_update = (change_availability, title)

                query2 = 'UPDATE books SET availability = %s WHERE title = %s;'

                cursor.execute(query2, availability_update)
                
                book_id = id

                cursor = conn.cursor()

                query3 = 'DELETE FROM borrowed_books WHERE book_id = %s'

                cursor.execute(query3, (book_id, ))
                conn.commit()
                print(f"Thank you for returning {title}, we hope you enjoyed the read!")

            elif availability == "available for loan":
                print("We are always happy to take donations, but that is not our book.")
        except IndexError:
            print("Please enter a valid title and try again.")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()