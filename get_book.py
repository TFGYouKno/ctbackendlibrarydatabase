from DB_connections import connect_db, Error

def get_book():
    conn = connect_db()

    if conn is not None:
        try:
            title = input("Please enter the title of the book you are looking for:  ").title()

            cursor = conn.cursor()

            query = 'SELECT * FROM books WHERE title = %s'

            cursor.execute(query, (title, ))

            id, title, author, availability = cursor.fetchall()[0]
            print(f'{id}. {title} by {author}')
        
        except IndexError:
            print("Please enter a valid title and try again.")

        finally:
            cursor.close()
            conn.close()


def get_encyclopedia():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = 'SELECT * FROM books;'

            cursor.execute(query)

            for id, title, author, availability in cursor.fetchall():
                print(f"{id}. {title} by {author} is {availability}")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()