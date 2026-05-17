
def scan_workflow_reliability(workflow_log):
    retries = workflow_log.count('retry')
    if retries > 1:
        return False
    return True
