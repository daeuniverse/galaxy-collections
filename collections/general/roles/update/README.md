# Ansible role - daeuniverse.general.update

## Use this role

After installing the collection, you may directly use this role in your playbook.

### Custom Build

```yaml
# update.yml
---
- name: Update dae on remote hosts
  hosts: all
  become: yes

  vars:
    - app: dae
    - action_url: "https://github.com/daeuniverse/dae/actions/runs/5977749239"
    - build_type: custom # options: [daily-build,pr-build,build,release,custom]

  roles:
    - role: daeuniverse.general.update
```

### Latest Build

```yaml
# update.yml
---
- name: Update dae on remote hosts
  hosts: all
  become: yes

  vars:
    - app: dae
    - build_type: pr-build # options: [daily-build,pr-build,build,release,custom]
    - latest: yes

  roles:
    - role: daeuniverse.general.update
```

### Release Build

```yaml
# update.yml
---
- name: Update dae on remote hosts
  hosts: all
  become: yes

  vars:
    - app: dae
    - build_type: release # options: [daily-build,pr-build,build,release,custom]
    - release_tag: v0.2.5rc2

  roles:
    - role: daeuniverse.general.update
```
