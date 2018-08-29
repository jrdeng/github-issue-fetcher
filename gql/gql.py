import eventlet
eventlet.monkey_patch()
import requests

from .issue import Issue


def post(url, headers, payload):
    with eventlet.Timeout(20, False):
        r = requests.post(url, headers=headers, json=payload)
        if r.status_code != 200:
            return None 

        # debug
        #print(r.json())

        data = r.json()['data']
        if data is None:
            # should be error
            print('ERROR: {}'.format(r.json()))
            return None

        return data

    # timeout
    print('POST timeout, please try again later...')
    return None


def fetch_issues(token, repo_owner, repo_name):
    issue_list = []

    url = 'https://api.github.com/graphql'
    headers = {'Authorization': 'bearer ' + token}

    # NOTE: the maximum limit of nodes is 500,000.
    # modify the query_str to fetch data you need
    query_str_fmt = '''
    query
    {{
      repository(owner: {}, name: "{}") {{
        issues(first: 100, states: OPEN{}) {{
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
            cursor
          }}
          pageInfo {{
            endCursor
            hasNextPage
          }}
        }}
      }}
    }}
    '''
    cursor_fmt = ', after:"{}"'

    has_next_page = True
    end_cursor = ''
    index = 1
    while has_next_page:
        if len(end_cursor) == 0:
            query_first = query_str_fmt.format(repo_owner, repo_name, '')
            payload = { 'query': query_first }
        else:
            query_n = query_str_fmt.format(repo_owner, repo_name, cursor_fmt.format(end_cursor))
            payload = { 'query': query_n}
        print('>>>>>> fetching issues ... {}x100'.format(index))
        index += 1
        data = post(url, headers, payload)
        if data is None:
            print('POST failed...')
            return issue_list

        #print(data)

        repository = data['repository']
        issues = repository['issues']
     
        total_count = issues['totalCount']
        print('total_count: {}'.format(total_count))
       
        for edge in issues['edges']:
            node = edge['node']
            issue = Issue(node)
            issue_list.append(issue)

        page_info = issues['pageInfo']
        end_cursor = page_info['endCursor']
        has_next_page = page_info['hasNextPage']
        print('has_next_page: {}'.format(has_next_page))

    return issue_list

