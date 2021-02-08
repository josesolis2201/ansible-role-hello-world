def test_command(host):
    cmd = 'echo "Hello world" | grep "Hello world"'
    assert host.command(cmd).rc == 0
