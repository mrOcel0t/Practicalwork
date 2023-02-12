import sqlite3
# global data, columns
# data = []
columns = ('ID','Authore','Name','Country','Age')


def get(filename):
    """Считывает книги из указанного файла и добавляет данные в список data"""
    data = []
    with open(filename,'r') as file:
        for line in file:
            values = line.rstrip().split(',')
            data.append((int(values[0]),values[1],values[2],values[3],int(values[4])))
    return data        


def put(data, filename):
    """Записывает книги из списка data в указанный файл"""
    with open(filename,'w') as file:
        for value in data:
            print(','.join(map(str, value)), file=file)


def print_data(data):
    """Выводит список книг на экран"""
    # m = 0
    # for book in data:
    #     m = max([m] + [len(str(i)) for i in book])
    # m = max(max([len(i) for i in columns]), m)
    # for i in columns:
    #     print(str(i).ljust(m + 1, ''), end='')
    # print()
    # for line in data:
    #     for i in line:
    #         print(str(i).ljust(m + 1, ' '), end='')
    #         print()
    for book in data:
        print(f'{book[0]:<2} {book[1]:<27} {book[2]:<32} {book[3]:<7} {book[4]}')


data = get('books.txt')
print_data(data)
connection = sqlite3.connect('Books.db')
cursor = connection.execute('''CREATE TABLE IF NOT EXISTS
books(
    ID INTEGER NOT NULL UNIQUE,
    Author TEXT,
    Name TEXT,
    Country TEXT,
    Age INTEGER,
    PRIMARY KEY(ID)
)''')
for n in data:
    cursor.execute(f'INSERT OR IGNORE INTO books VALUES(?,?,?,?,?)', n)
    connection.commit()
    print(f'Added {n}')
    # print(f'Book {n} is already in the database')
    # for n in list(cursor.execute('SELECT*from books')):
    #     print(n)
