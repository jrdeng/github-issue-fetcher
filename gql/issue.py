from .author import Author
from .label import Label
from .comment import Comment


class Issue:
    def __init__(self, json):
        self.url = json['url']
        self.id = self.url.split('/')[-1]
        self.title = json['title']
        self.author = Author(json['author'])
        self.createdAt = json['createdAt']
        self.body = json['body']
        # labels
        self.labels = []
        labels = json['labels']
        for edge in labels['edges']:
            node = edge['node']
            label = Label(node)
            self.labels.append(label)
        # comments
        self.comments = []
        comments = json['comments']
        for edge in comments['edges']:
            node = edge['node']
            comment = Comment(node)
            self.comments.append(comment)

    def __str__(self):
        r = '========== POST ==========\n'
        r += 'id={}\n'.format(self.id)
        r += 'url={}\n'.format(self.url)
        r += 'title={}\n'.format(self.title)
        r += 'author={}\n'.format(self.author)
        r += 'createdAt={}\n'.format(self.createdAt)
        r += 'labels={'
        for label in self.labels:
            r += '{}, '.format(label)
        r += '}\n'
        r += '<<<<<<body begin>>>>>>\n{}\n<<<<<<body end>>>>>>\n'.format(self.body)
        r += '---------- COMMENTS -----\n'
        if len(self.comments) == 0:
            r += '(None)\n'
        else:
            for comment in self.comments:
                r += '{}\n'.format(comment)
        r += '\n'
        return r
