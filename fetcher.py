import sys
import os
import getopt

import gql


def fetch_issues(token, owner, repo):
    # we use GraphQL API here
    return gql.fetch_issues(token, owner, repo)


def usage():
    print('usage: {} OPTIONS'.format(sys.argv[0]))
    print('OPTIONS:')
    print('\t-t|--token\tgithub token for GraphQL')
    print('\t-o|--owner\trepo owner(login)')
    print('\t-r|--repo\trepo name to fetch issue')


def sample():
    # show how to use this tool

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ht:o:r:', ['help', 'token=', 'owner=', 'repo='])
    except getopt.GetoptError as err:
        print(err)
        usage()
        exit(2)
    token = None
    owner = None
    repo = None
    for o, a in opts:
        if o == '-h':
            usage()
            exit()
        elif o in ('-t', '--token'):
            token = a
        elif o in ('-o', '--owner'):
            owner = a
        elif o in ('-r', '--repo'):
            repo = a
        else:
            usage()
            assert False, 'unhandled option'
    if token is None:
        print('token is not specified, try to get it from ENV...')
        token_env = 'GITHUB_GQL_TOKEN'
        try:
            token = os.environ[token_env]
        except KeyError as err:
            print('{} is not in ENV? exit.'.format(token_env))
            exit(2)
    if owner is None:
        print('owner must be specified.')
        usage()
        exit(1)
    if repo is None:
        print('repo must be specified.')
        usage()
        exit(1)

    # here we go
    issue_list = fetch_issues(token, owner, repo)
    issue_num = len(issue_list)
    print('issue_num: {}'.format(issue_num))
    for issue in issue_list:
        print(issue)

    if issue_num == 0:
        print('fetch_issues() returned empty!')
        exit(1)


if __name__ == '__main__':
    sample()
    print('\nDone!\n')
