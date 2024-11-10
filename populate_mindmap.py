from mindmap import MindMap

def populate_mind_map():
    # Initialize the MindMap object
    mind_map = MindMap()
    
    # Root node
    root = "Understanding Earth’s Core-Mantle Boundary (CMB) Interactions"
    mind_map.add_node(root)

    # Central Goal
    central_goal = "Central Goal"
    mind_map.add_node(central_goal, root)
    mind_map.add_node("Analyze how fluctuations in Earth’s rotation (length of day) provide insights into core-mantle boundary properties.", central_goal)

    # Core Dynamics & Free Oscillations
    core_dynamics = "Core Dynamics & Free Oscillations"
    mind_map.add_node(core_dynamics, root)

    # Free Oscillations in Earth's Rotation
    free_oscillations = "Free Oscillations in Earth’s Rotation"
    mind_map.add_node(free_oscillations, core_dynamics)
    mind_map.add_node("Fluctuations in Earth's rotation rate over decades influenced by angular momentum exchange", free_oscillations)
    mind_map.add_node("Torsional oscillations in the fluid outer core cause periodic changes in the length of day", free_oscillations)

    # Mechanisms of Angular Momentum Transfer
    mechanisms = "Mechanisms of Angular Momentum Transfer"
    mind_map.add_node(mechanisms, core_dynamics)

    # Sub-nodes for Angular Momentum Transfer
    mind_map.add_node("Gravitational Torque: Influences due to mass distribution misalignments", mechanisms)
    mind_map.add_node("Electromagnetic Coupling: Lorentz forces near the core boundaries", mechanisms)
    mind_map.add_node("Topographic Coupling: Pressure variations due to CMB surface irregularities", mechanisms)

    # Key Components and Influences on Oscillations
    key_components = "Key Components and Influences on Oscillations"
    mind_map.add_node(key_components, root)

    # Torsional Oscillations
    torsional = "Torsional Oscillations"
    mind_map.add_node(torsional, key_components)
    mind_map.add_node("Described by rotations of fluid cylinders in the core", torsional)
    mind_map.add_node("Magnetic field lines act as restoring forces", torsional)
    mind_map.add_node("Core-mantle interactions influence rotational variations", torsional)

    # Coupling Mechanisms
    coupling = "Coupling Mechanisms"
    mind_map.add_node(coupling, key_components)
    mind_map.add_node("Electromagnetic: Forces based on magnetic field strength and conductivity", coupling)
    mind_map.add_node("Topographic: Pressure disturbances from CMB surface variations", coupling)
    mind_map.add_node("Gravitational: Misalignments between core and mantle create torques", coupling)

    # Modeling and Predictions
    modeling = "Modeling and Predictions"
    mind_map.add_node(modeling, root)
    mind_map.add_node("Mathematical Framework: Angular momentum equations model oscillations", modeling)
    mind_map.add_node("Insights from Observations: Geodetic measurements infer core properties", modeling)
    mind_map.add_node("Theoretical models predict oscillation frequencies", modeling)

    # Comparing Coupling Mechanisms
    comparing = "Comparing Coupling Mechanisms"
    mind_map.add_node(comparing, root)
    mind_map.add_node("Electromagnetic vs. Topographic: Differences in damping and influence", comparing)
    mind_map.add_node("Gravitational Coupling: Explains decade-scale fluctuations", comparing)

    # Conclusions & Implications
    conclusions = "Conclusions & Implications"
    mind_map.add_node(conclusions, root)
    mind_map.add_node("Gravitational coupling explains length-of-day oscillations", conclusions)
    mind_map.add_node("Future Studies: Refine models using geodetic and geomagnetic observations", conclusions)
    mind_map.add_node("Distinguishing between mechanisms via oscillation damping analysis", conclusions)

    # Generate elements for Cytoscape
    return mind_map.get_cytoscape_elements()