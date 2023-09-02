#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from urllib import request
import json

DOCUMENTATION = """
---
module: daeuniverse.general.github_workflow_run
short_description: A custom Ansible module to fetch statistics accross GitHub workflow runs in @daeuniverse
description:
  - This module allows you to interact with GitHub workflow runs in @daeuniverse
version_added: "1.0.0"
author:
  - kev (@yqlbu)
tags:
  - daeuniverse
  - general
  - module
options:
  owner:
    description:
      - The owner of the repo
    required: true
  repo:
    description:
      - The repo name
    required: true
  build_type:
    description:
      - The workflow build type
    required: true
"""

EXAMPLES = """
- name: Ensure a GitHub workflow run is present
  daeuniverse.general.github_workflow_run:
    owner: "daeuniverse"
    repo: "dae"
    build_type: "pr-build"
"""


class Module:
    def __init__(self, module: AnsibleModule, repo_owner: str, repo_name: str) -> None:
        self.module = module
        self.repo = f'{repo_owner}/{repo_name}'
        self.supported_build_type = ['build', 'pr-build', 'daily-build']

    def get_latest_workflow_run_id(self, build_type: str) -> int | None:
        if build_type in self.supported_build_type:
            url = f'https://api.github.com/repos/{self.repo}/actions/workflows/{build_type}.yml/runs'
            req = request.Request(url)
            with request.urlopen(req) as response:
                data = json.loads(response.read())

                if data['total_count'] > 0:
                    latest_run_id = data['workflow_runs'][0]['id']
                    return latest_run_id
        else:
            self.module.fail_json(
                msg=f'Unsupported build_type. Available options are {self.supported_build_type}'
            )
            return None

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
        m = Module(module, module.params['owner'], module.params['repo'])
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
