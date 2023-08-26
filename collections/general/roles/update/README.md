# Ansible role - daeuniverse.general.update

## Use this role

After installing the collection, you may directly use this role in your playbook.

### Custom build

```yaml
# update.yml
---
- name: Update dae on remote hosts
  hosts: all
  become: yes

  vars:
    - app: dae
    - action_url: "https://github.com/daeuniverse/dae/actions/runs/5977749239"

  roles:
    - role: daeuniverse.general.update
```

### Latest {main,pr,daily}-build

```yaml
# update.yml
---
- name: Update dae on remote hosts
  hosts: all
  become: yes

  vars:
    - app: dae
    - build_type: pr-build # options: [daily-build,pr-build,main-build]
    - latest: true

  roles:
    - role: daeuniverse.general.update
```
