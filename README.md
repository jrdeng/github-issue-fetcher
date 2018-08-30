# github issue fetcher

use [Github GraphQL API](https://developer.github.com/v4/) to fetch issues of the specified repository on github.

I'm using these scripts to fetch issues then generate static website(by using [Hugo](https://gohugo.io/)). see  [blog-hugo](https://github.com/jrdeng/blog-hugo)`/generate_and_deploy.py`

written in Python3, and depends on these modules:

- requests
- eventlet

## usage

1. install the dependencies

2. to use this script, you also need a `token` to access the GraphQL API, please take a look at [Authenticating with GraphQL](https://developer.github.com/v4/guides/forming-calls/#authenticating-with-graphql).

usage:

    $ git clone https://github.com/jrdeng/github-issue-fetcher.git
    # or use as submodule
    
    # import to your project
    import sys
    sys.path.append('github-issue-fetcher')
    import fetcher
    issue_list = fetcher.fetch_issues(token, owner, repo)

the `owner` and `repo` specified whose/which repository you want.

you will get a list of object `Issue` which defined in [gql/issue.py](gql/issue.py).

mostly, you'll need to modify the `query_str` in [gql/gql.py](gql/gql.py) to fetch the data you want. and modify the class Issue to parse the result.

for convenience, there's a `sample()` in `fetcher.py`.

## license

[WTFPL](https://en.wikipedia.org/wiki/WTFPL)
