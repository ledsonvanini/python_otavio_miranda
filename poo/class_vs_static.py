
class Connection:
    # host = 'localhost'  # Class Attr
    def __init__(self, host='localhost'):
        self._host = host
        self._user = None
        self._password = None

    # Setter não 'Pytonico'
    def set_user(self, user):
        self._user = user


    def get_user(self):
        return self._user


    def get_host(self):
        return self._host


conn = Connection()
conn.set_user('Ledson')

print(conn.get_user())
print(conn.get_host())


