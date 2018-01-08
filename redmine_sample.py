from redminelib import Redmine

'''
https://python-redmine.com/index.html
https://python-redmine.com/resources/issue.html
'''

redmine = Redmine('http://localhost:3000', key='24288d0e0dd9e2b113fea86d8aabbeac27d8692b')

# チケット登録サンプル
issue = redmine.issue.create(
    project_id = "sample-project",
    subject = "Test Issue",
    tracker_id = 1,
    description = 'Test Issue Description',
)
