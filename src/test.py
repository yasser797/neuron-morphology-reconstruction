# import numpy as np
# import open3d as o3d

# def generate_hyperbolic_coral_reef_3d(base_stitches, increase_rate, num_rows):
#     # Initialize lists to hold the coordinates
#     points = []
    
#     # Initial number of stitches
#     num_stitches = base_stitches
    
#     for row in range(num_rows):
#         for stitch in range(int(num_stitches)):
#             # Calculate the angle, radius, and height
#             angle = 2 * np.pi * stitch / base_stitches
#             radius = np.exp(row * increase_rate)
#             height = row * 0.1  # This adds depth to each row

#             # Convert polar coordinates to Cartesian and append the height for 3D
#             x = radius * np.cos(angle)
#             y = radius * np.sin(angle)
#             z = height
            
#             # Append the point to the list
#             points.append([x, y, z])
        
#         # Update the number of stitches for the next row
#         num_stitches *= (1 + increase_rate)
    
#     return points

# # Parameters
# base_stitches = 20   # Initial number of stitches in the base row
# increase_rate = 0.1  # Rate at which stitches increase per row
# num_rows = 100        # Total number of rows

# # Generate the 3D coral reef
# points = generate_hyperbolic_coral_reef_3d(base_stitches, increase_rate, num_rows)

# # Convert to Open3D point cloud
# point_cloud = o3d.geometry.PointCloud()
# point_cloud.points = o3d.utility.Vector3dVector(points)

# # Visualize the point cloud
# o3d.visualization.draw_geometries([point_cloud])


# import numpy as np
# import open3d as o3d

# def generate_hyperbolic_coral_reef_3d_with_folds(base_stitches, increase_rate, num_rows, fold_intensity):
#     # Initialize lists to hold the coordinates
#     points = []
    
#     # Initial number of stitches
#     num_stitches = base_stitches
    
#     for row in range(num_rows):
#         # Adding variability for folds
#         fold_variation = np.random.normal(1, fold_intensity, int(num_stitches))
        
#         for stitch in range(int(num_stitches)):
#             # Calculate the angle, radius, and height
#             angle = 2 * np.pi * stitch / base_stitches
#             radius = np.exp(row * increase_rate) * fold_variation[stitch]
#             height = row * 0.1  # This adds depth to each row

#             # Convert polar coordinates to Cartesian and append the height for 3D
#             x = radius * np.cos(angle)
#             y = radius * np.sin(angle)
#             z = height
            
#             # Append the point to the list
#             points.append([x, y, z])
        
#         # Update the number of stitches for the next row, adding randomness
#         num_stitches *= (1 + increase_rate) + np.random.normal(0, increase_rate * 0.1)

#     return points

# # Parameters
# base_stitches = 110   # Initial number of stitches in the base row
# increase_rate = 0.1  # Rate at which stitches increase per row
# num_rows = 50        # Total number of rows
# fold_intensity = 0.05  # Intensity of the folds, higher values mean more pronounced folds

# # Generate the 3D coral reef with folds
# points = generate_hyperbolic_coral_reef_3d_with_folds(base_stitches, increase_rate, num_rows, fold_intensity)

# # Convert to Open3D point cloud
# point_cloud = o3d.geometry.PointCloud()
# point_cloud.points = o3d.utility.Vector3dVector(points)

# # Visualize the point cloud
# o3d.visualization.draw_geometries([point_cloud])


# import numpy as np
# import open3d as o3d

# def generate_hyperbolic_coral_reef_mesh(base_stitches, increase_rate, num_rows, fold_intensity):
#     # Initialize lists to hold the coordinates and faces
#     points = []
#     faces = []
    
#     # Initial number of stitches
#     num_stitches = base_stitches
    
#     # Store the indices of the first point in each row to manage face creation
#     row_start_indices = []
    
#     for row in range(num_rows):
#         row_start_index = len(points)  # Index of the first point in this row
#         row_start_indices.append(row_start_index)
#         fold_variation = np.random.normal(1, fold_intensity, int(num_stitches))
        
#         for stitch in range(int(num_stitches)):
#             # Calculate the angle, radius, and height
#             angle = 2 * np.pi * stitch / base_stitches
#             radius = np.exp(row * increase_rate) * fold_variation[stitch]
#             height = row * 0.1  # Adds depth to each row

#             # Convert polar coordinates to Cartesian and append the height for 3D
#             x = radius * np.cos(angle)
#             y = radius * np.sin(angle)
#             z = height
            
#             # Append the point to the list
#             points.append([x, y, z])
        
#         # Update the number of stitches for the next row, adding randomness
#         num_stitches *= (1 + increase_rate) + np.random.normal(0, increase_rate * 0.1)

#     # Generate faces for the mesh
#     for i in range(1, len(row_start_indices) - 1):
#         current_row_count = row_start_indices[i+1] - row_start_indices[i]
#         previous_row_count = row_start_indices[i] - row_start_indices[i-1]
        
#         for j in range(previous_row_count):
#             current_index = row_start_indices[i] + j
#             previous_index = row_start_indices[i-1] + j
            
#             # Connect the current point to the previous point and the next point in the previous row
#             if j + 1 < previous_row_count:
#                 faces.append([previous_index, current_index, previous_index + 1])
#                 faces.append([current_index, previous_index + 1, current_index + 1 if (current_index + 1 - row_start_indices[i] < current_row_count) else row_start_indices[i]])
    
#     return points, faces

# # Parameters
# base_stitches = 10   # Initial number of stitches in the base row
# increase_rate = 0.1  # Rate at which stitches increase per row
# num_rows = 50        # Total number of rows
# fold_intensity = 0.05  # Intensity of the folds, higher values mean more pronounced folds

# # Generate the 3D coral reef with mesh
# points, faces = generate_hyperbolic_coral_reef_mesh(base_stitches, increase_rate, num_rows, fold_intensity)

# # Convert to Open3D mesh
# mesh = o3d.geometry.TriangleMesh()
# mesh.vertices = o3d.utility.Vector3dVector(points)
# mesh.triangles = o3d.utility.Vector3iVector(faces)
# mesh.compute_vertex_normals()

# # Visualize the mesh
# o3d.visualization.draw_geometries([mesh])

# import numpy as np
# import open3d as o3d

# def generate_hyperbolic_coral_reef_lines(base_stitches, increase_rate, num_rows, fold_intensity):
#     # Initialize lists to hold the coordinates and lines
#     points = []
#     lines = []
    
#     # Initial number of stitches
#     num_stitches = base_stitches
    
#     for row in range(num_rows):
#         row_start_index = len(points)  # Index of the first point in this row
#         fold_variation = np.random.normal(1, fold_intensity, int(num_stitches))
        
#         for stitch in range(int(num_stitches)):
#             # Calculate the angle, radius, and height
#             angle = 2 * np.pi * stitch / base_stitches
#             radius = np.exp(row * increase_rate) * fold_variation[stitch]
#             height = row * 0.1  # Adds depth to each row

#             # Convert polar coordinates to Cartesian and append the height for 3D
#             x = radius * np.cos(angle)
#             y = radius * np.sin(angle)
#             z = height
            
#             # Append the point to the list
#             points.append([x, y, z])
        
#             # Connect each point with the next, wrapping around at the end of the row
#             if stitch > 0:
#                 lines.append([len(points) - 2, len(points) - 1])
        
#         # Optionally connect end of row to start of row to complete the loop
#         if num_stitches > 1:
#             lines.append([row_start_index, len(points) - 1])

#         # Update the number of stitches for the next row, adding randomness
#         num_stitches *= (1 + increase_rate) + np.random.normal(0, increase_rate * 0.1)

#     return points, lines

# # Parameters
# base_stitches = 10   # Initial number of stitches in the base row
# increase_rate = 0.1  # Rate at which stitches increase per row
# num_rows = 50        # Total number of rows
# fold_intensity = 0.05  # Intensity of the folds, higher values mean more pronounced folds

# # Generate the 3D coral reef with line segments
# points, lines = generate_hyperbolic_coral_reef_lines(base_stitches, increase_rate, num_rows, fold_intensity)

# # Convert to Open3D line set
# line_set = o3d.geometry.LineSet()
# line_set.points = o3d.utility.Vector3dVector(points)
# line_set.lines = o3d.utility.Vector2iVector(lines)

# # Visualize the line set
# o3d.visualization.draw_geometries([line_set])



# import numpy as np
# import open3d as o3d

# def generate_hyperbolic_coral_reef_complex_lines(base_stitches, increase_rate, num_rows, fold_intensity):
#     # Initialize lists to hold the coordinates and lines
#     points = []
#     lines = []
    
#     # Initial number of stitches
#     num_stitches = base_stitches
#     point_indices = []  # Keep track of indices in each row
    
#     for row in range(num_rows):
#         row_indices = []
#         row_start_index = len(points)
#         fold_variation = np.random.normal(1, fold_intensity, int(num_stitches))
        
#         for stitch in range(int(num_stitches)):
#             # Calculate the angle, radius, and height
#             angle = 2 * np.pi * stitch / base_stitches
#             radius = np.exp(row * increase_rate) * fold_variation[stitch]
#             height = np.exp(row * 0.05) * np.cos(stitch * 0.1)  # Modulated height to introduce folds
            
#             # Convert polar coordinates to Cartesian and append the height for 3D
#             x = radius * np.cos(angle)
#             y = radius * np.sin(angle)
#             z = height
            
#             # Append the point to the list
#             points.append([x, y, z])
#             row_indices.append(len(points) - 1)
        
#             # Connect each point with the next, wrapping around at the end of the row
#             if stitch > 0:
#                 lines.append([len(points) - 2, len(points) - 1])
        
#         # Optionally connect end of row to start of row to complete the loop
#         if num_stitches > 1:
#             lines.append([row_start_index, len(points) - 1])

#         point_indices.append(row_indices)
#         # Update the number of stitches for the next row, adding randomness
#         num_stitches *= (1 + increase_rate) + np.random.normal(0, increase_rate * 0.1)

#     # Create cross-row connections for folds
#     for i in range(1, len(point_indices)):
#         for j in range(len(point_indices[i])):
#             # Connect to several points in the previous row to create a folded effect
#             if len(point_indices[i-1]) > j:
#                 lines.append([point_indices[i][j], point_indices[i-1][j]])
#             if len(point_indices[i-1]) > j+1:  # Connect diagonally as well
#                 lines.append([point_indices[i][j], point_indices[i-1][j+1]])

#     return points, lines

# # Parameters
# base_stitches = 5   # Initial number of stitches in the base row
# increase_rate = 0.2  # Rate at which stitches increase per row
# num_rows = 50        # Total number of rows
# fold_intensity = 0.1  # Intensity of the folds, higher values mean more pronounced folds

# # Generate the 3D coral reef with complex line segments
# points, lines = generate_hyperbolic_coral_reef_complex_lines(base_stitches, increase_rate, num_rows, fold_intensity)

# # Convert to Open3D line set
# line_set = o3d.geometry.LineSet()
# line_set.points = o3d.utility.Vector3dVector(points)
# line_set.lines = o3d.utility.Vector2iVector(lines)

# # Visualize the line set
# o3d.visualization.draw_geometries([line_set])



import numpy as np
import open3d as o3d

def generate_hyperbolic_coral_reef_point_cloud(base_stitches, increase_rate, num_rows, fold_intensity):
    # Initialize the list to hold the coordinates
    points = []
    
    # Initial number of stitches
    num_stitches = base_stitches
    
    for row in range(num_rows):
        fold_variation = np.random.normal(1, fold_intensity, int(num_stitches))
        
        for stitch in range(int(num_stitches)):
            # Calculate the angle, radius, and height
            angle = 2 * np.pi * stitch / base_stitches
            radius = np.exp(row * increase_rate) * fold_variation[stitch]
            height = np.exp(row * 0.05) * np.cos(stitch * 0.1)  # Modulated height to introduce folds

            # Convert polar coordinates to Cartesian
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            z = height
            
            # Append the point to the list
            points.append([x, y, z])
        
        # Update the number of stitches for the next row, adding randomness
        num_stitches *= (1 + increase_rate) + np.random.normal(0, increase_rate * 0.1)

    return points

# Parameters
base_stitches = 10   # Initial number of stitches in the base row
increase_rate = 0.2  # Rate at which stitches increase per row
num_rows = 50        # Total number of rows
fold_intensity = 0.1  # Intensity of the folds, higher values mean more pronounced folds

# Generate the 3D coral reef point cloud
points = generate_hyperbolic_coral_reef_point_cloud(base_stitches, increase_rate, num_rows, fold_intensity)

# Convert to Open3D point cloud
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])
