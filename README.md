# github issue fetcher

using [Github GraphQL API](https://developer.github.com/v4/) to fetch issues of the specified repository on github.

written in Python3, and depends on these modules:

- requests
- eventlet

## usage

1. install the dependencies

2. to use this script, you also need a `token` to access the GraphQL API, please take a look at [Authenticating with GraphQL](https://developer.github.com/v4/guides/forming-calls/#authenticating-with-graphql).

usage:

    import gql
  
    gql.fetch_issues(token, owner, repo)

the `owner` and `repo` specified whose/which repository you want.

you will get a list of object `Issue` which defined in [gql/issue.py](gql/issue.py).

mostly, you'll need to modify the `query_str` in [gql/gql.py](gql/gql.py) to fetch the data you want. and modify the class Issue to parse the result.

for convenience, there's a `sample()` in `fetcher.py`.

## known issues

1. the maximum number of nodes of one `query` is limited to 500,000
2. the max value of parameter `last` is limited to 100

## license

[WTFPL](https://en.wikipedia.org/wiki/WTFPL)
