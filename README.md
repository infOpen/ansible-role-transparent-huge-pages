# transparent-huge-pages

[![CI](https://github.com/infOpen/ansible-role-transparent-huge-pages/workflows/CI/badge.svg)](https://github.com/infOpen/ansible-role-transparent-huge-pages/actions)
[![Mergify Status][mergify-status]][mergify]
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-transparent-huge-pages/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-transparent-huge-pages/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-transparent-huge-pages/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-transparent-huge-pages/)
[![Ansible Role](https://img.shields.io/ansible/role/18013.svg)](https://galaxy.ansible.com/infOpen/transparent-huge-pages/)

Manage transparent-huge-pages system settings.

## Requirements

This role requires Ansible 2.8 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/ansible-community/molecule) to run tests.

Local and Github Actions tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- CentOS 8
- Debian Buster
- Debian Stretch
- Ubuntu Bionic
- Ubuntu Focal

and use:
- Ansible 2.8.x
- Ansible 2.9.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Service file content
thp_sys_settings: "{{ _thp_sys_settings | default([]) }}"

# Service type
thp_use_init_file: "{{ _thp_use_init_file | default(True) }}"

# Service settings
thp_service_name: 'disable-transparent-huge-pages'
thp_service_enabled: True

# Init services
thp_init_file:
  path: "/etc/init.d/{{ thp_service_name }}"
  owner: 'root'
  group: 'root'
  mode: '0755'
thp_init_x_start_before: []
```

### Debian family OS variables

``` yaml
_thp_sys_settings:
  - key: '/sys/kernel/mm/transparent_hugepage/enabled'
    value: 'never'
  - key: '/sys/kernel/mm/transparent_hugepage/defrag'
    value: 'never'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.transparent-huge-pages }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- https://www.infopen.pro
- a.chaussier [at] infopen.pro

[mergify]: https://mergify.io
[mergify-status]: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/infOpen/ansible-role-transparent-huge-pages&style=flat
