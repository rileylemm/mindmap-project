import networkx as nx

class MindMap:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node, parent=None):
        """Add a node and connect it to its parent if specified."""
        self.graph.add_node(node)
        if parent:
            self.graph.add_edge(parent, node)

    def get_cytoscape_elements(self):
        """Convert the graph to a list of Cytoscape elements."""
        elements = []
        for node in self.graph.nodes:
            elements.append({
                'data': {'id': node, 'label': node},
                'position': {'x': 0, 'y': 0}  # Initial position, will be draggable
            })
        
        for edge in self.graph.edges:
            elements.append({
                'data': {'source': edge[0], 'target': edge[1]}
            })
        
        return elements