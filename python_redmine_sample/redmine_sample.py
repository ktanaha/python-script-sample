from redminelib import Redmine

'''
https://python-redmine.com/index.html
https://python-redmine.com/resources/issue.html
'''

redmine = Redmine('http://localhost:3000', key='37811bae54628b0c1eb331f61de7508a083cdb31')

# チケット登録サンプル
issue = redmine.issue.create(
    project_id = "sample-project",
    subject = "Test Issue",
    tracker_id = 1,
    description = 'Test Issue Description',
)
