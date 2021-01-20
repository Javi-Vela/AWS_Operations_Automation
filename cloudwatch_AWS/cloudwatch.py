import botocore.session
import botocore


def logGroup(group):
    # 24 hours from the last registration
    logsStream = client.describe_log_streams(logGroupName=group, orderBy='LastEventTime', descending=True)
    range_day = logsStream['logStreams'][0]['creationTime'] - 86400000
    # paginate log streams
    paginator = client.get_paginator("describe_log_streams")
    for paginateLog in paginator.paginate(logGroupName=group, orderBy='LastEventTime', descending=True):
        for log in paginateLog['logStreams']:
            if range_day > log['creationTime']:
                # remove log stream
                delStream = client.delete_log_stream(logGroupName=group, logStreamName=log['logStreamName'])


# start session
session = botocore.session.get_session()
client = session.create_client('logs', region_name='eu-west-3')
kwargs = {"PaginationConfig": {"PageSize": 50}}
# paginate log groups
for paginateGroup in client.get_paginator("describe_log_groups").paginate(**kwargs):
    for group in paginateGroup["logGroups"]:
        # send group name
        logGroup(group['logGroupName'])

