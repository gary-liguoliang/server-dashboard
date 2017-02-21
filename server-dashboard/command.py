import winrm


def get_service_status(node="WIN-10-DEV", service_name=""):
    session = winrm.Session(node, auth=('root', 'P@ssw0rD'))
    r = session.run_cmd('ipconfig', ['/all'])
    print r.std_out


if __name__ == '__main__':
    get_service_status()
