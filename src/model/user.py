class User:
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def valid(self):
        return self.username == 'root' and self.password == 'admin'

    def __str__(self):
        return (
            "User{username=%s, password=%s}" % 
            (self.username, self.password)
        )
