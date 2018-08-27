class Author:
    def __init__(self, json):
        self.login = json['login']
        self.avatarUrl = json['avatarUrl']

    def __str__(self):
        r = '{'
        r += 'login={}, '.format(self.login)
        r += 'avatarUrl={}'.format(self.avatarUrl)
        r += '}'
        return r
