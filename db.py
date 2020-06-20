import pymysql.cursors


# соединение с БД
def get_connection():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='db_bot',
                           cursorclass=pymysql.cursors.DictCursor)

    return conn


# добавить пользователя с выбранной категорией и локацией
def add_to_users(id_user, id_cat, loc):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO users (id_user, id_category, location) VALUES (%s, %s, %s)'
        cursor.execute(sql, (id_user, id_cat, loc))
        conn.commit()
    finally:
        conn.close()
    print("Success")


# получить список категорий и локаций одного пользователя или всех
def get_from_users(id_user=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        if id_user is None:
            sql = 'SELECT u.id_user, c.name, u.location FROM users u, categories c ' + \
                  'WHERE c.id = u.id_category'
            cursor.execute(sql)
        else:
            sql = 'SELECT u.id_user, c.name, u.location FROM users u, categories c ' + \
                  'WHERE u.id_user = %s AND c.id = u.id_category'
            cursor.execute(sql, (id_user,))
        # print(cursor.description)
        result = []
        for row in cursor:
            result.append(row)
    finally:
        conn.close()
    return result


# получить все категории
def get_categories():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'SELECT id, name FROM categories'
        cursor.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
    finally:
        conn.close()
    return result


# добавить новую ссылку на пост для пользователя
def add_to_posts(id_user, link):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO posts (id_user, link, status) VALUES (%s, %s, %s)'
        cursor.execute(sql, (id_user, link, 1))
        conn.commit()
    finally:
        conn.close()


# получить все ссылки пользователя
def get_from_posts(id_user):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'SELECT link FROM posts WHERE id_user = %s AND status = 1'
        cursor.execute(sql, (id_user,))
        result = []
        for row in cursor:
            result.append(row)
    finally:
        conn.close()
    return result


# add_to_db(3285241, 2, "Чертаново")
x = get_from_users()  # 19471248  3285241
print(x)
print(get_categories())
# add_to_posts(19471248, 'some_link_1')
# add_to_posts(19471248, 'some_link_2')
# add_to_posts(19471248, 'some_link_3')
print(get_from_posts(19471248))
