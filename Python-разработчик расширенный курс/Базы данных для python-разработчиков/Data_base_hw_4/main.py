import psycopg2

# Задание
# Создайте программу для управления клиентами на Python.Требуется хранить персональную информацию о клиентах:
# имя
# фамилия
# email
# телефон
# Сложность в том, что телефон у клиента может быть не один, а два, три и даже больше. А может и вообще не быть телефона, например, он не захотел его оставлять.
# Вам необходимо разработать структуру БД для хранения информации и несколько функций на Python для управления данными.
# Функция, создающая структуру БД (таблицы).
# Функция, позволяющая добавить нового клиента.
# Функция, позволяющая добавить телефон для существующего клиента.
# Функция, позволяющая изменить данные о клиенте.
# Функция, позволяющая удалить телефон для существующего клиента.
# Функция, позволяющая удалить существующего клиента.
# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
# Функции выше являются обязательными, но это не значит, что должны быть только они. При необходимости можете создавать дополнительные функции и классы.
# Также предоставьте код, демонстрирующий работу всех написанных функций.
# Результатом работы будет .py файл.

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS phonenumbers;")
        cur.execute("DROP TABLE IF EXISTS clients;")
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            surname VARCHAR(100) NOT NULL,
            email VARCHAR(100)
            );
                 """)
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS phonenumbers(
            client_id INTEGER NOT NULL REFERENCES clients(id), 
            phonenumber VARCHAR(10)
            );
                """)
        conn.commit()
    print(f'Create tables in database')

def add_client(conn, name: str, surname: str, email: str, phonenumber: str):
    with conn.cursor() as cur:
        cur.execute(""" 
                    INSERT INTO clients(name, surname, email)
                    VALUES(%s, %s, %s)
                    RETURNING id;
                """, (name, surname, email))
        client_id = cur.fetchone()
    print(f'Client {name} {surname} added to database with ID: {client_id[0]}')
    add_phone(conn, client_id[0], phonenumber)

def add_phone(conn, client_id: int, phonenumber: str):
    with conn.cursor() as cur:
        cur.execute(""" 
                    INSERT INTO phonenumbers(client_id, phonenumber)
                    VALUES(%s, %s);
                """, (client_id, phonenumber))
        conn.commit()
    print(f'Phone number {phonenumber} added to database for client: {client_id}')

def change_client(conn, client_id, name=None, surname=None, email=None, phonenumber=None):
    result =f'Change client number {client_id}: '
    with conn.cursor() as cur:
        if name is not None:
            cur.execute(""" 
                        UPDATE clients
                        SET name = %s
                        WHERE id = %s;
                    """, (name, client_id))
            result += f'new name - {name} '
        if surname is not None:
            cur.execute(""" 
                        UPDATE clients
                        SET surname = %s
                        WHERE id = %s;
                    """, (surname, client_id))
            result += f' | new surname - {surname}'
        if email is not None:
            cur.execute(""" 
                        UPDATE clients
                        SET email = %s
                        WHERE id = %s;
                    """, (email, client_id))
            result += f' | new email - {email} '
        if phonenumber is not None:
            cur.execute(""" 
                        UPDATE phonenumbers
                        SET phonenumber = %s
                        WHERE client_id = %s;
                    """, (phonenumber, client_id))
            result += f' | new phonenumber - {phonenumber} '
        conn.commit()
        print(result)

def delete_phone(conn, client_id, phonenumber: str):
    with conn.cursor() as cur:
        cur.execute(""" 
                    DELETE FROM phonenumbers
                    WHERE client_id = %s AND phonenumber = %s;
                """,(client_id, phonenumber))
        conn.commit()
    print(f'Phone number {phonenumber} of client number {client_id} deleted from database')

def delete_client(conn, client_id: int):
    with conn.cursor() as cur:
        cur.execute(""" 
                    DELETE FROM phonenumbers
                    WHERE client_id = %s;
                """,(client_id,))
        cur.execute(""" 
                    DELETE FROM clients
                    WHERE id = %s;
                """,(client_id,))
        conn.commit()
    print(f'Client number {client_id} deleted from database')

def find_client(conn, name=None, surname=None, email=None, phonenumber=None):
    result = ''
    with conn.cursor() as cur:
        if name is not None:
            cur.execute(""" 
                        SELECT * from clients
                        WHERE name = %s;
                    """, (name,))
            client_name = cur.fetchone()
            cur.execute(""" 
                        SELECT phonenumber from phonenumbers
                        WHERE client_id = %s;
                    """, (client_name[0],))
            client_phonenumber = cur.fetchone()
            print(f'Name: {client_name[1]} | surname: {client_name[2]} | email: {client_name[3]} | phonenumber: {client_phonenumber[0]}')
        elif surname is not None:
            cur.execute(""" 
                        SELECT * from clients
                        WHERE surname = %s;
                    """, (surname,))
            client_name = cur.fetchone()
            cur.execute(""" 
                        SELECT phonenumber from phonenumbers
                        WHERE client_id = %s;
                    """, (client_name[0],))
            client_phonenumber = cur.fetchone()
            print(f'Name: {client_name[1]} | surname: {client_name[2]} | email: {client_name[3]} | phonenumber: {client_phonenumber[0]}')
        elif email is not None:
            cur.execute(""" 
                        SELECT * from clients
                        WHERE email = %s;
                    """, (email,))
            client_name = cur.fetchone()
            cur.execute(""" 
                        SELECT phonenumber from phonenumbers
                        WHERE client_id = %s;
                    """, (client_name[0],))
            client_phonenumber = cur.fetchone()
            print(f'Name: {client_name[1]} | surname: {client_name[2]} | email: {client_name[3]} | phonenumber: {client_phonenumber[0]}')
        elif phonenumber is not None:
            cur.execute(""" 
                        SELECT * from phonenumbers
                        WHERE phonenumber = %s;
                    """, (phonenumber,))
            client_phonenumber = cur.fetchone()
            cur.execute(""" 
                        SELECT * from clients
                        WHERE id = %s;
                    """, (client_phonenumber[0],))
            client_name = cur.fetchone()
            print(f'Name: {client_name[1]} | surname: {client_name[2]} | email: {client_name[3]} | phonenumber: {client_phonenumber[1]}')


with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    create_db(conn)
    add_client(conn,'Vito', 'Spatafore', 'Vito@mail.com', '95555')
    add_client(conn, 'John', 'Sacrimoni', 'Sack@mail.com', '91487')
    add_client(conn, 'Patrick', 'Parisi', 'Patrick_Star@mail.com', '966677')
    add_client(conn, 'Ralph', 'Cifaretto', 'Ralphie@mail.com', '95635636')
    add_client(conn, 'Giacomo', 'Aprile', 'Jackie@mail.com', '9563564664')
    add_client(conn, 'Richard', 'Aprile', 'Richie@mail.com', '9554677')
    add_client(conn, 'Robert', 'Baccalieri', 'Bobby_Bacala@mail.com', '9156027')
    add_client(conn, 'Silvio', 'Dante', 'Sil@mail.com', '9532200')
    add_client(conn, 'Paul', 'Gualtieri', 'Paulie_Walnuts@mail.com', '9112331')
    add_phone(conn, 3, '9154951111')
    add_phone(conn, 5, '111111111')
    change_client(conn, 1, name = 'Pasquale', email = 'Patsy@mail.com')
    change_client(conn, 5, 'Corrado', 'Soprano', 'Junior@mail.com', '5656553')
    delete_phone(conn, 5, '9554677')
    delete_client(conn, 6)
    find_client(conn, name = 'Ralph')
    find_client(conn, surname = 'Gualtieri')
    find_client(conn, email = 'Junior@mail.com')
    find_client(conn, phonenumber = '9532200')
