import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('rdb-servers')


@pytest.mark.parametrize("name,version", [
    ("mysql-community-server", "5.6"),
])
def test_packages_is_installed(host, name, version):
    package = host.package(name)
    assert package.is_installed
    assert package.version.startswith(version)


@pytest.mark.parametrize("name", [
    ("mysqld"),
])
def test_service_running_and_enabled(host, name):
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("address", [
    ("tcp://0.0.0.0:3306"),
])
def test_service_is_listen(host, address):
    assert host.socket(address).is_listening
