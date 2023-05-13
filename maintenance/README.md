# daeuniverse Maintenance Collection

The `daeuniverse-maintenance-collection` includes a variety of Ansible content to help automate the general maintenance workflow for servers that are based on the `debian` system. This collection is maintained by the daeuniverse core team.

## Ansible version compatibility

Tested with the Ansible Core `2.8`, `2.12`, and `2.13` releases, and the current development version of Ansible.

## Install this collection

You can install the `daeuniverse.maintenance` collection with the Ansible Galaxy CLI:

```bash
dae-galaxy collection install git+https://github.com/daeuniverse/galaxy-collections#/collections/maintenance,master
```

You can also include it in a `requirements.yml` file and install it with `dae-galaxy collection install -r requirements.yml`, using the format:

```yaml
# requirements.yml
---
collections:
  - name: git+https://github.com/daeuniverse/galaxy-collections.git#/collections/maintenance
    type: git
    version: master
```

To install a specific version of the collection, using the format:

```yaml
# requirements.yml
---
collections:
  - name: git+https://github.com/daeuniverse/galaxy-collections.git#/collections/maintenance
    type: git
    version: daeuniverse.maintenance.v1.0.0
```

Upgrade the exiting collection with the following command:

```bash
ansible-galaxy collection install -r requirements.yml --upgrade
```

## Use this collection

After installing the collection, you may directly use the roles in your playbook.

```yaml
# add-user.yml
---
- name: Add user to remote server
  hosts: all
  become: yes

  vars:
    - public_keys:
        - ~/.ssh/id_rsa_yubikey.pub
        - ~/.ssh/id_rsa_awx.pub
  roles:
    - role: daeuniverse.maintenance.user
      username: packer
```

## Contribute to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [daeuniverse/dae-galaxy](https://github.com/daeuniverse/dae-galaxy) repository. See [How to Contribute](https://github.com/daeuniverse/galaxy-collections/blob/master/docs/contribute.md) for more details.

## License

[MIT (C) daeuniverse](https://github.com/yqlbu/daeuniverse/galaxy-collections/blob/master/LICENSE)
