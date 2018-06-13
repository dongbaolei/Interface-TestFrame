# -*- coding:utf-8 -*-
"""
@Time:2018/1/30 15:45
@Author:dongbaolei
"""

from jira import JIRA

import ReadConfig


class JiraUtil:
    def __init__(self):
        rf = ReadConfig.ReadConfig()
        self.server = rf.get_jiraUrl('url')
        self.basic_auth = (rf.get_jiraUrl('usrname'), rf.get_jiraUrl('pwd'))
        self.jiraClinet = None

    def login(self):
        self.jiraClinet = JIRA(server=self.server, basic_auth=self.basic_auth)

        if self.jiraClinet != None:
            return True
        else:
            return False

    def createIssue(self, project, summary, description, assignee):

        issue_dict = {

            'project': {'key': project},
            'issuetype': {'name': 'Bug'},
            'reporter': {'name': 'dongbaolei'},
            'summary': summary,
            'description': description,
            'assignee': {'name': assignee},
            'components': [{'name': '接口'}],
            'priority': {'name': 'Medium'},
            'fixVersions': [
                {
                    'name': 'v1.0.0.1'
                }
            ],

        }
        if self.jiraClinet == None:
            self.login()
        return self.jiraClinet.create_issue(issue_dict)

    # 更新issue状态
    def updateTransition(self, issueID, transition):
        if self.jiraClinet == None:
            self.login()
        return self.jiraClinet.transition_issue(issueID, transition)
        # 查询某个issue

    def searchIssue(self, jql_str, startAt, maxResults):
        if self.jiraClinet == None:
            self.login()
        return self.jiraClinet.search_issues(jql_str, startAt, maxResults)

    # 获取issue进程状态
    def GetIssueTransitionStatus(self, issueID):
        if self.jiraClinet == None:
            self.login()
        return self.jiraClinet.transitions(issueID)

    def GetIssueId(self):
        pass


if __name__ == '__main__':
    jira = JiraUtil()
    jira.login()
    # jira.createIssue('LZFINECAR', 'summary', '1212121', 'zhaozhaoxin', )
    jiraJson = jira.searchIssue("project=LZFINECAR and summary ~ 输入正确用户名密码登录失败", 0, 5)
    print(jiraJson[0])
    #print(jira.GetIssueTransitionStatus('LZFINECAR-206')[0]['id'])
    # jira.updateTransition('LZFINECAR-206',701)
# jira = JIRA('http://jira.lianzhongjr.com',basic_auth=('dongbaolei', 'blshiniye1985'))
#
# issue_dict= {
#     'project': {'key': 'LZFINECAR'},
#     'summary': 'issue概要',
#     'description': 'issue描述\n第二行',
#     'issuetype': {'name': 'Bug'},
#     'reporter':{'name': 'dongbaolei'},
#     'components':[{'name': '接口'}],
#     'priority': {'name': 'Medium'},
#     'assignee':{'name': 'zhaozhaoxin'},
#     }
#
# #jira.create_issue(fields=issue_dict)
# #print(new_issue.fields.worklog[0])
# #解决bug处理
# #jira.transition_issue('LZFINECAR-206',2)
#
# #判断bug流程状态
# print(jira.transitions('LZFINECAR-206'))
# print(jira.transitions('LZFINECAR-206')[0]['id'])
