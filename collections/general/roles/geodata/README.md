# Ansible role - daeuniverse.general.geodata

## Use this role

After installing the collection, you may directly use this role in your playbook.

### Update geodata

```yaml
# update.yml
---
- name: Update geodata on remote host
  hosts: all
  become: yes

  vars:
    - artifact_repo: "MetaCubeX/meta-rules-dat"
    - config_path: "/etc/dae"
    - daemon_service_name: "dae"
    - restart_daemon: yes

  roles:
    - role: daeuniverse.general.geodata
```
