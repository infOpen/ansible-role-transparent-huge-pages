# transparent-huge-pages

[![Build Status](https://travis-ci.org/infOpen/ansible-role-transparent-huge-pages.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-transparent-huge-pages)

Manage transparent-huge-pages system settings.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
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
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
