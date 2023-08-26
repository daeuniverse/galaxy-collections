# daeuniverse general collection

The `daeuniverse-general-collection` includes a variety of Ansible content to help automate general workflow such as update, install for servers that are based on the `Debian` system. This collection is maintained by the @daeuniverse/infra team.

## Ansible version compatibility

Tested with the Ansible Core `2.8`, `2.12`, and `2.13` releases, and the current development version of Ansible.

## Install this collection

You can install the `daeuniverse.general` collection with the Ansible Galaxy CLI:

```bash
# galaxy
ansible-galaxy collection install daeuniverse.general
# git
ansible-galaxy collection install git+https://github.com/daeuniverse/galaxy-collections#/collections/general,master
```

You can also include it in a `requirements.yml` file and install it with `dae-galaxy collection install -r requirements.yml`, using the format:

```yaml
# requirements.yml
---
collections:
  - name: git+https://github.com/daeuniverse/galaxy-collections.git#/collections/general
    type: git
    version: master
```

To install a specific version of the collection, using the format:

```yaml
# requirements.yml
---
collections:
  - name: git+https://github.com/daeuniverse/galaxy-collections.git#/collections/general
    type: git
    version: daeuniverse.general.v1.1.0
```

Upgrade the exiting collection with the following command:

```bash
ansible-galaxy collection install -r requirements.yml --upgrade
```

## Use this collection

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

## Contribute to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [daeuniverse/galaxy-collections](https://github.com/daeuniverse/galaxy-collections) repository. See [How to Contribute](https://github.com/daeuniverse/galaxy-collections/blob/master/docs/contribute.md) for more details.

## Maintenance

### Build and pack a newer version of collection

```bash
ansible-galaxy collection build
```

### Publish an existing collection

```bash
ansible-galaxy collection publish --api <GALAXY_API_KEY> ./daeuniverse-general-<VERSION>.tar.gz
```

## License

[MIT (C) daeuniverse](https://github.com/yqlbu/daeuniverse/galaxy-collections/blob/master/LICENSE)
