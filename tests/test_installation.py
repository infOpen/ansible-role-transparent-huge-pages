"""
Role tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_service_file(host):
    """
    Test if transparent-huge-pages init file exists
    """

    service_file_path = '/etc/init.d/disable-transparent-huge-pages'

    assert host.file(service_file_path).exists
    assert host.file(service_file_path).is_file
    assert host.file(service_file_path).user == 'root'
    assert host.file(service_file_path).group == 'root'
    assert host.file(service_file_path).mode == 0o755


def test_service(host):
    """
    Test if transparent-huge-pages service enabled
    """

    assert host.service('disable-transparent-huge-pages').is_enabled


def test_sysfs_rules(host):
    """
    Check sysfs rules
    """

    rules = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        rules = [
            (
                '/sys/kernel/mm/transparent_hugepage/defrag',
                'always madvise [never]'
            ),
            (
                '/sys/kernel/mm/transparent_hugepage/enabled',
                'always madvise [never]'
            ),
        ]

    for rule in rules:
        assert host.check_output('cat {}'.format(rule[0])) == rule[1]
