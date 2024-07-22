from DB_connections import connect_db, Error

def get_borrowed():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query= 'SELECT * FROM borrowed_books;'

            cursor.execute(query)

            for id, user_id, book_id, title, borrow_date in cursor.fetchall():
                print(f'{id}. User ID: {user_id}, Book ID: {book_id}, Title: {title}, Borrow Date: {borrow_date}')
            
        except Error as e:
            print*f"Error: {e}"

        finally:
            cursor.close()
            conn.close()