#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from urllib import request
import json


class Module:
    def __init__(self, repo_owner: str, repo_name: str) -> None:
        self.repo = f'{repo_owner}/{repo_name}'

    def get_latest_workflow_run_id(self, build_type: str) -> int | None:
        url = f'https://api.github.com/repos/{self.repo}/actions/workflows/{build_type}.yml/runs'
        req = request.Request(url)
        with request.urlopen(req) as response:
            data = json.loads(response.read())

            if data['total_count'] > 0:
                latest_run_id = data['workflow_runs'][0]['id']
                return latest_run_id

        return None


def main():
    module_args = dict(
        owner=dict(type='str', required=True),
        repo=dict(type='str', required=True),
        build_type=dict(type='str', required=True),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    result = dict(changed=False, run_id=0, error='')

    try:
        m = Module(module.params['owner'], module.params['repo'])
        latest_run_id = m.get_latest_workflow_run_id(module.params['build_type'])
        if latest_run_id is not None:
            result['run_id'] = latest_run_id
        else:
            result['error'] = 'No runs found for the specified workflow'
    except Exception as e:
        result['error'] = str(e)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
