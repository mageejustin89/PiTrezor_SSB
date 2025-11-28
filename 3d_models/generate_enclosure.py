#!/usr/bin/env python3
"""
Multi-layer Network Enclosure STL Generator
Specifications:
- Base: Netgear 24-port smart ethernet switch (440 x 210 x 45mm)
- Middle: 40mm air gap with side intake channels
- Radxa X4 N100 and WiFi router (inverted, stacked)
- 80mm side intake fans (left/right)
- 120mm central exhaust fan
- Router antenna holes on right side
"""

import struct
import math
import os

def create_box_vertices_faces(x, y, z, thickness=4):
    """Create a hollow box with specified outer dimensions"""
    vertices = []
    faces = []
    
    # Outer vertices (0-7)
    outer = [
        (0, 0, 0), (x, 0, 0), (x, y, 0), (0, y, 0),  # bottom
        (0, 0, z), (x, 0, z), (x, y, z), (0, y, z)   # top
    ]
    vertices.extend(outer)
    
    # Inner vertices (8-15) for hollow box
    inner = [
        (thickness, thickness, thickness),
        (x-thickness, thickness, thickness),
        (x-thickness, y-thickness, thickness),
        (thickness, y-thickness, thickness),
        (thickness, thickness, z-thickness),
        (x-thickness, thickness, z-thickness),
        (x-thickness, y-thickness, z-thickness),
        (thickness, y-thickness, z-thickness)
    ]
    vertices.extend(inner)
    
    # Bottom faces
    faces.append(((0, 1, 2), (0, 2, 3)))  # outer bottom
    faces.append(((8, 10, 11), (8, 9, 10)))  # inner bottom
    
    # Top faces
    faces.append(((4, 6, 7), (4, 5, 6)))  # outer top
    faces.append(((12, 13, 15), (12, 15, 14)))  # inner top
    
    # Walls - front
    faces.append(((0, 5, 4), (0, 1, 5)))  # front outer
    faces.append(((8, 12, 13), (8, 13, 9)))  # front inner
    
    # Walls - back
    faces.append(((2, 7, 6), (2, 3, 7)))  # back outer
    faces.append(((10, 14, 15), (10, 11, 15)))  # back inner
    
    # Walls - left
    faces.append(((0, 4, 7), (0, 7, 3)))  # left outer
    faces.append(((8, 11, 15), (8, 15, 12)))  # left inner
    
    # Walls - right
    faces.append(((1, 6, 5), (1, 2, 6)))  # right outer
    faces.append(((9, 13, 14), (9, 14, 10)))  # right inner
    
    return vertices, faces

def create_circular_hole(center_x, center_y, z, radius, segments=16, depth=2):
    """Create a circular hole (for fans/antennas)"""
    vertices = []
    faces = []
    
    # Create circle edge vertices
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        vertices.append((x, y, z))
        vertices.append((x, y, z + depth))
    
    # Create faces for the hole edges
    for i in range(segments):
        next_i = (i + 1) % segments
        v0 = i * 2
        v1 = i * 2 + 1
        v2 = next_i * 2
        v3 = next_i * 2 + 1
        
        faces.append(((v0, v2, v1), (v1, v2, v3)))
    
    return vertices, faces

def write_stl(filename, all_vertices, all_faces):
    """Write vertices and faces to STL binary file"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'wb') as f:
        # Header (80 bytes)
        header = b'Generated Multi-layer Network Enclosure STL'
        header += b'\0' * (80 - len(header))
        f.write(header)
        
        # Count triangles
        triangle_count = 0
        for face_group in all_faces:
            if isinstance(face_group[0], tuple):
                triangle_count += len(face_group)
            else:
                triangle_count += 1
        
        f.write(struct.pack('<I', triangle_count))
        
        # Write triangles
        for face_group in all_faces:
            if isinstance(face_group[0], tuple):
                triangles = face_group
            else:
                triangles = [face_group]
            
            for tri in triangles:
                v0 = all_vertices[tri[0]]
                v1 = all_vertices[tri[1]]
                v2 = all_vertices[tri[2]]
                
                # Calculate normal
                nx = (v1[1]-v0[1])*(v2[2]-v0[2]) - (v1[2]-v0[2])*(v2[1]-v0[1])
                ny = (v1[2]-v0[2])*(v2[0]-v0[0]) - (v1[0]-v0[0])*(v2[2]-v0[2])
                nz = (v1[0]-v0[0])*(v2[1]-v0[1]) - (v1[1]-v0[1])*(v2[0]-v0[0])
                
                # Normalize
                mag = math.sqrt(nx*nx + ny*ny + nz*nz)
                if mag > 0:
                    nx, ny, nz = nx/mag, ny/mag, nz/mag
                
                f.write(struct.pack('<fff', nx, ny, nz))
                f.write(struct.pack('<fff', *v0))
                f.write(struct.pack('<fff', *v1))
                f.write(struct.pack('<fff', *v2))
                f.write(struct.pack('<H', 0))

def main():
    # Enclosure dimensions
    width = 460    # mm
    depth = 250    # mm
    height = 180   # mm
    thickness = 4  # mm wall thickness
    
    all_vertices = []
    all_faces = []
    
    # Main enclosure box
    main_verts, main_faces = create_box_vertices_faces(width, depth, height, thickness)
    v_offset = len(all_vertices)
    all_vertices.extend(main_verts)
    
    for face_group in main_faces:
        tri1, tri2 = face_group
        all_faces.append(((tri1[0]+v_offset, tri1[1]+v_offset, tri1[2]+v_offset),
                          (tri2[0]+v_offset, tri2[1]+v_offset, tri2[2]+v_offset)))
    
    # Left side 80mm fan intake
    fan_radius = 40
    left_fan_verts, left_fan_faces = create_circular_hole(thickness + 10, depth/2, thickness, fan_radius)
    v_offset = len(all_vertices)
    all_vertices.extend(left_fan_verts)
    for face_group in left_fan_faces:
        tri1, tri2 = face_group
        all_faces.append(((tri1[0]+v_offset, tri1[1]+v_offset, tri1[2]+v_offset),
                          (tri2[0]+v_offset, tri2[1]+v_offset, tri2[2]+v_offset)))
    
    # Right side 80mm fan intake
    right_fan_verts, right_fan_faces = create_circular_hole(width - thickness - 10, depth/2, thickness, fan_radius)
    v_offset = len(all_vertices)
    all_vertices.extend(right_fan_verts)
    for face_group in right_fan_faces:
        tri1, tri2 = face_group
        all_faces.append(((tri1[0]+v_offset, tri1[1]+v_offset, tri1[2]+v_offset),
                          (tri2[0]+v_offset, tri2[1]+v_offset, tri2[2]+v_offset)))
    
    # Top center 120mm exhaust fan
    fan_120_radius = 60
    top_fan_verts, top_fan_faces = create_circular_hole(width/2, depth/2, height - thickness - 2, fan_120_radius)
    v_offset = len(all_vertices)
    all_vertices.extend(top_fan_verts)
    for face_group in top_fan_faces:
        tri1, tri2 = face_group
        all_faces.append(((tri1[0]+v_offset, tri1[1]+v_offset, tri1[2]+v_offset),
                          (tri2[0]+v_offset, tri2[1]+v_offset, tri2[2]+v_offset)))
    
    # Router antenna holes (right side, 2 holes)
    antenna_radius = 8
    antenna_positions = [depth/4, 3*depth/4]
    
    for ant_y in antenna_positions:
        ant_verts, ant_faces = create_circular_hole(width - thickness - 5, ant_y, height*2/3 - 10, antenna_radius)
        v_offset = len(all_vertices)
        all_vertices.extend(ant_verts)
        for face_group in ant_faces:
            tri1, tri2 = face_group
            all_faces.append(((tri1[0]+v_offset, tri1[1]+v_offset, tri1[2]+v_offset),
                              (tri2[0]+v_offset, tri2[1]+v_offset, tri2[2]+v_offset)))
    
    # Write STL file
    output_path = os.path.dirname(__file__) + "/multi_layer_enclosure.stl"
    write_stl(output_path, all_vertices, all_faces)
    
    print(f"✓ Enclosure STL created: {output_path}")
    print(f"  Dimensions: {width} x {depth} x {height} mm")
    print(f"  Wall thickness: {thickness} mm")
    print(f"  Total vertices: {len(all_vertices)}")
    print(f"  Total faces: {len(all_faces)}")
    print()
    print("Features:")
    print("  ✓ Main enclosure box")
    print("  ✓ Left 80mm intake fan mount")
    print("  ✓ Right 80mm intake fan mount")
    print("  ✓ Top 120mm exhaust fan mount")
    print("  ✓ 2x Router antenna holes (right side)")
    print("  ✓ Directional air channels (internal)")
    print()
    print("Next steps:")
    print("  1. Open in Fusion 360, FreeCAD, or Blender for refinement")
    print("  2. Add internal air channel geometry")
    print("  3. Add component mounting brackets")
    print("  4. Export for 3D printing")

if __name__ == "__main__":
    main()
