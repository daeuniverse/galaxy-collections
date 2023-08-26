# Ansible Collection Rule - daeuniverse.general.update

## Use this role

After installing the collection, you may directly use the roles in your playbook.

```yaml
# update.yml
---
- name: Update dae on remote hosts
  hosts: all
  become: yes

  vars:
    - action_url: "https://github.com/daeuniverse/dae/actions/runs/5977749239"

  roles:
    - role: daeuniverse.general.update
```
