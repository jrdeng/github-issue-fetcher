from .author import Author


class Comment:
    def __init__(self, json):
        self.author = Author(json['author'])
        self.createdAt = json['createdAt']
        self.body = json['body']

    def __str__(self):
        r = '{'
        r += 'author={}, '.format(self.author)
        r += 'createdAt={}, '.format(self.createdAt)
        r += 'body={}'.format(self.body)
        r += '}'
        return r
