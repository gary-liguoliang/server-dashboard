
class ConfigSet:
    nodes = []
    component_type = ''
    component_keys = []

    def __init__(self, nodes, component_type, component_keys):
        self.nodes = nodes
        self.component_type = component_type
        self.component_keys = component_keys

    def __repr__(self):
        return 'ConfigSet: nodes: %s, type: %s, keys: %s' % (self.nodes, self.component_type, self.component_keys)
