#!/bin/env python
import pandas as pd
import jira as JIRA
import re

options = {
    'server': 'https://tools.hmcts.net/jira',}

#jira username and password should be pulled from environment / secrets
jira = JIRA.JIRA(options, basic_auth=('USERNAME', 'PASSWORD'))

#projects list should be abstracted
projects = ['RSE','CNP','RPE','RDO']

#run jquery across jira backend
project_data = []
total = []
for project in projects:
    for issues in jira.search_issues('project = {} AND resolution = Unresolved' .format(project), startAt=0,maxResults=0):
        total.append(str(issues))
    data = (len(total))
    project_data.append(data)
    total = []

#create dataframe from lists
d = {'Project':projects, 'Open Jira Issues':project_data}

df = pd.DataFrame(d)

df.to_csv (r'./export_jira_dataframe.csv', index = None, header=True)
