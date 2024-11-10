from dash import Dash, dcc, html
import dash_cytoscape as cyto
from populate_mindmap import populate_mind_map

# Generate Cytoscape elements from the populate function
elements = populate_mind_map()

# Initialize the Dash app
app = Dash(__name__)
server = app.server  # This is necessary for deploying on platforms like Render or Heroku

app.layout = html.Div([
    html.H1("Interactive Mind Map for Earth's Core Dynamics", style={'text-align': 'center'}),
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '800px'},
        layout={'name': 'breadthfirst'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',
                    'width': '70px',
                    'height': '70px',
                    'background-color': '#61bffc',
                    'color': '#000',
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'font-size': '14px'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': '#888',
                    'target-arrow-color': '#888',
                    'target-arrow-shape': 'triangle',
                    'curve-style': 'bezier'
                }
            }
        ],
        userZoomingEnabled=True,
        userPanningEnabled=True,
        boxSelectionEnabled=True,
        autoungrabify=False
    )
])

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)