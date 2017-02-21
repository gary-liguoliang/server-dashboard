from model import ConfigSet


class ServerGateway:
    request_repo = []

    def __init__(self):
        pass

    def fetch_server_status(self, config_set):
        self.request_repo.append(config_set)

        for node in config_set.nodes:
            print "node: %s " % node
            for component in config_set.component_keys:
                print "component: %s" % component

if __name__ == '__main__':
    gateway = ServerGateway()
    config_set = ConfigSet(['localhost'], 'Service', ['Power'])
    gateway.fetch_server_status(config_set)
