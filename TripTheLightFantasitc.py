import pyvista as pv

# Create a sphere
sphere = pv.ParametricTorus()
twisted_torus = sphere.rotate_z(-180)  # Twist by 180 degrees

# Set up the plotter
plotter = pv.Plotter()

# Add the sphere mesh to the plotter
# plotter.add_mesh(sphere, color="silver", show_edges=True)
plotter.add_mesh(twisted_torus, color="gold", show_edges=True)

# Display the visualization
plotter.show()
