import eventlet
eventlet.monkey_patch()
import requests

from .issue import Issue


def fetch_issues(token, repo_owner, repo_name):
    issue_list = []

    url = 'https://api.github.com/graphql'
    headers = {'Authorization': 'bearer ' + token}

    # NOTE: the maximum limit of nodes is 500,000.
    # TODO: the `last` limit to 100...

    # modify the query_str to fetch data you need
    query_str = '''
    query
    {{
      repository(owner: {}, name: "{}") {{
        issues(last: 100, states: OPEN) {{
          totalCount
          edges {{
            node {{
              url
              title
              author {{
                login
                avatarUrl
              }}
              createdAt
              body
              labels(first: 10) {{
                totalCount
                edges {{
                  node {{
                    name
                  }}
                }}
              }}
              comments(last: 100) {{
                totalCount
                edges {{
                  node {{
                    author {{
                      login
                      avatarUrl
                    }}
                    createdAt
                    body
                  }}
                }}
              }}
            }}
          }}
        }}
      }}
    }}
    '''.format(repo_owner, repo_name)

    payload = {
        'query': query_str
    }

    with eventlet.Timeout(10, False):
        r = requests.post(url, headers=headers, json=payload)
        if r.status_code != 200:
            return issue_list

        # debug
        #print(r.json())

        data = r.json()['data']
        if data is None:
            # should be error
            print('ERROR: {}'.format(r.json()))
            return issue_list

        repository = data['repository']
        issues = repository['issues']
     
        #count = issues['totalCount']
        #print('count: {}'.format(count))
       
        for edge in issues['edges']:
            node = edge['node']
            issue = Issue(node)
            issue_list.append(issue)

        return issue_list
    
    print('POST timeout, please try again later...')
    return issue_list

