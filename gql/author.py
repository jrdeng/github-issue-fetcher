class Author:
    def __init__(self, json):
        # we may get None for 'author'...
        if json is None:
            self.login = 'None'
            self.avatarUrl = 'https://avatars0.githubusercontent.com/u/170314?v=4' # just hardcode it ...
        else:
            self.login = json['login']
            self.avatarUrl = json['avatarUrl']

    def __str__(self):
        r = '{'
        r += 'login={}, '.format(self.login)
        r += 'avatarUrl={}'.format(self.avatarUrl)
        r += '}'
        return r

