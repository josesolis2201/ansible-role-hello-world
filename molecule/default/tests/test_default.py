def test_command(host):
    cmd = 'curl -s http://localhost:3333 | grep "Hello World!"'
    assert host.command(cmd).rc == 0
