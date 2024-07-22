from DB_connections import connect_db, Error
import re

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input('We are so glad you want to join our cult- err, libary!\n Please enter your name:  ').title()

            email = input("Please enter your email: ")
            found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
            if email == found.group():
                phone = input("please enter your phone number in the following format: _ _ _-_ _ _-_ _ _ _\n")
                found_phone = re.search(r"\(?\d{3}(\s|-|\))?\d{3}(\s|-)?\d{4}", phone)

                if phone == found_phone.group():    
                    new_member = (name, email, phone)
                    query = 'INSERT INTO users (user_name, email, phone) VALUES (%s, %s, %s)'
                    cursor.execute(query, new_member)
                    conn.commit()
                    print(f"Welcome {name} to the Tampa Library Members Cult!")
        except AttributeError:
                print("Please enter a valid email or phone number")
        except Error as e:
            print(f"{e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()