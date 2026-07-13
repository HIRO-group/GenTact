import bpy
import mathutils
import os
import typing


def sub_sensor_visual_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Sub_Sensor_Visual node group"""
    sub_sensor_visual_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sub_Sensor_Visual")

    sub_sensor_visual_1.color_tag = 'NONE'
    sub_sensor_visual_1.description = ""
    sub_sensor_visual_1.default_group_node_width = 140
    sub_sensor_visual_1.show_modifier_manage_panel = True

    # sub_sensor_visual_1 interface

    # Socket Geometry
    geometry_socket = sub_sensor_visual_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Radii
    radii_socket = sub_sensor_visual_1.interface.new_socket(name="Radii", in_out='OUTPUT', socket_type='NodeSocketFloat')
    radii_socket.default_value = 0.0
    radii_socket.min_value = -3.4028234663852886e+38
    radii_socket.max_value = 3.4028234663852886e+38
    radii_socket.subtype = 'NONE'
    radii_socket.attribute_domain = 'POINT'
    radii_socket.default_input = 'VALUE'
    radii_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket = sub_sensor_visual_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = sub_sensor_visual_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Material
    material_socket = sub_sensor_visual_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    # Socket Overlap
    overlap_socket = sub_sensor_visual_1.interface.new_socket(name="Overlap", in_out='INPUT', socket_type='NodeSocketFloat')
    overlap_socket.default_value = 1.0
    overlap_socket.min_value = -10000.0
    overlap_socket.max_value = 10000.0
    overlap_socket.subtype = 'NONE'
    overlap_socket.attribute_domain = 'POINT'
    overlap_socket.default_input = 'VALUE'
    overlap_socket.structure_type = 'AUTO'

    # Socket Radius View
    radius_view_socket = sub_sensor_visual_1.interface.new_socket(name="Radius View", in_out='INPUT', socket_type='NodeSocketBool')
    radius_view_socket.default_value = True
    radius_view_socket.attribute_domain = 'POINT'
    radius_view_socket.hide_value = True
    radius_view_socket.default_input = 'VALUE'
    radius_view_socket.structure_type = 'AUTO'

    # Initialize sub_sensor_visual_1 nodes

    # Node Index of Nearest
    index_of_nearest = sub_sensor_visual_1.nodes.new("GeometryNodeIndexOfNearest")
    index_of_nearest.name = "Index of Nearest"
    index_of_nearest.show_options = True
    # Group ID
    index_of_nearest.inputs[1].default_value = 0

    # Node Position.001
    position_001 = sub_sensor_visual_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Position
    position = sub_sensor_visual_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Vector Math.001
    vector_math_001 = sub_sensor_visual_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'DISTANCE'

    # Node Set Material
    set_material = sub_sensor_visual_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node UV Sphere
    uv_sphere = sub_sensor_visual_1.nodes.new("GeometryNodeMeshUVSphere")
    uv_sphere.name = "UV Sphere"
    uv_sphere.show_options = True
    # Segments
    uv_sphere.inputs[0].default_value = 10
    # Rings
    uv_sphere.inputs[1].default_value = 6
    # Radius
    uv_sphere.inputs[2].default_value = 1.0

    # Node Group Input
    group_input = sub_sensor_visual_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Instance on Points
    instance_on_points = sub_sensor_visual_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Reroute
    reroute = sub_sensor_visual_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Reroute.001
    reroute_001 = sub_sensor_visual_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Group Output
    group_output = sub_sensor_visual_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Sample Index
    sample_index = sub_sensor_visual_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'INSTANCE'

    # Node Reroute.003
    reroute_003 = sub_sensor_visual_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Reroute.002
    reroute_002 = sub_sensor_visual_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Math
    math = sub_sensor_visual_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Separate Geometry
    separate_geometry = sub_sensor_visual_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.show_options = True
    separate_geometry.domain = 'POINT'

    # Node Scale Instances
    scale_instances = sub_sensor_visual_1.nodes.new("GeometryNodeScaleInstances")
    scale_instances.name = "Scale Instances"
    scale_instances.show_options = True
    # Selection
    scale_instances.inputs[1].default_value = True
    # Center
    scale_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Local Space
    scale_instances.inputs[4].default_value = True

    # Node Reroute.004
    reroute_004 = sub_sensor_visual_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketBool"
    # Node Group Input.001
    group_input_001 = sub_sensor_visual_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Set locations
    sub_sensor_visual_1.nodes["Index of Nearest"].location = (-160.58917236328125, -214.91156005859375)
    sub_sensor_visual_1.nodes["Position.001"].location = (-243.84747314453125, 55.50494384765625)
    sub_sensor_visual_1.nodes["Position"].location = (-420.0, -160.0)
    sub_sensor_visual_1.nodes["Vector Math.001"].location = (376.5555419921875, 54.27132034301758)
    sub_sensor_visual_1.nodes["Set Material"].location = (-910.72900390625, 241.3083953857422)
    sub_sensor_visual_1.nodes["UV Sphere"].location = (-1142.82373046875, 224.54180908203125)
    sub_sensor_visual_1.nodes["Group Input"].location = (-1394.7864990234375, 0.0)
    sub_sensor_visual_1.nodes["Instance on Points"].location = (-663.2575073242188, 170.41058349609375)
    sub_sensor_visual_1.nodes["Reroute"].location = (913.6024169921875, -266.07733154296875)
    sub_sensor_visual_1.nodes["Reroute.001"].location = (1317.3306884765625, -265.5663757324219)
    sub_sensor_visual_1.nodes["Group Output"].location = (1384.7864990234375, 0.0)
    sub_sensor_visual_1.nodes["Sample Index"].location = (66.7894287109375, -33.479949951171875)
    sub_sensor_visual_1.nodes["Reroute.003"].location = (797.806396484375, 125.88191986083984)
    sub_sensor_visual_1.nodes["Reroute.002"].location = (-19.396453857421875, 135.87399291992188)
    sub_sensor_visual_1.nodes["Math"].location = (606.7410888671875, 15.3592529296875)
    sub_sensor_visual_1.nodes["Separate Geometry"].location = (1158.2918701171875, 54.07794189453125)
    sub_sensor_visual_1.nodes["Scale Instances"].location = (918.2704467773438, 26.95090103149414)
    sub_sensor_visual_1.nodes["Reroute.004"].location = (1117.3731689453125, -290.69195556640625)
    sub_sensor_visual_1.nodes["Group Input.001"].location = (388.3890380859375, -163.9716796875)

    # Set dimensions
    sub_sensor_visual_1.nodes["Index of Nearest"].width  = 140.0
    sub_sensor_visual_1.nodes["Index of Nearest"].height = 100.0

    sub_sensor_visual_1.nodes["Position.001"].width  = 140.0
    sub_sensor_visual_1.nodes["Position.001"].height = 100.0

    sub_sensor_visual_1.nodes["Position"].width  = 140.0
    sub_sensor_visual_1.nodes["Position"].height = 100.0

    sub_sensor_visual_1.nodes["Vector Math.001"].width  = 140.0
    sub_sensor_visual_1.nodes["Vector Math.001"].height = 100.0

    sub_sensor_visual_1.nodes["Set Material"].width  = 140.0
    sub_sensor_visual_1.nodes["Set Material"].height = 100.0

    sub_sensor_visual_1.nodes["UV Sphere"].width  = 140.0
    sub_sensor_visual_1.nodes["UV Sphere"].height = 100.0

    sub_sensor_visual_1.nodes["Group Input"].width  = 140.0
    sub_sensor_visual_1.nodes["Group Input"].height = 100.0

    sub_sensor_visual_1.nodes["Instance on Points"].width  = 140.0
    sub_sensor_visual_1.nodes["Instance on Points"].height = 100.0

    sub_sensor_visual_1.nodes["Reroute"].width  = 20.0
    sub_sensor_visual_1.nodes["Reroute"].height = 100.0

    sub_sensor_visual_1.nodes["Reroute.001"].width  = 20.0
    sub_sensor_visual_1.nodes["Reroute.001"].height = 100.0

    sub_sensor_visual_1.nodes["Group Output"].width  = 140.0
    sub_sensor_visual_1.nodes["Group Output"].height = 100.0

    sub_sensor_visual_1.nodes["Sample Index"].width  = 140.0
    sub_sensor_visual_1.nodes["Sample Index"].height = 100.0

    sub_sensor_visual_1.nodes["Reroute.003"].width  = 20.0
    sub_sensor_visual_1.nodes["Reroute.003"].height = 100.0

    sub_sensor_visual_1.nodes["Reroute.002"].width  = 20.0
    sub_sensor_visual_1.nodes["Reroute.002"].height = 100.0

    sub_sensor_visual_1.nodes["Math"].width  = 140.0
    sub_sensor_visual_1.nodes["Math"].height = 100.0

    sub_sensor_visual_1.nodes["Separate Geometry"].width  = 140.0
    sub_sensor_visual_1.nodes["Separate Geometry"].height = 100.0

    sub_sensor_visual_1.nodes["Scale Instances"].width  = 140.0
    sub_sensor_visual_1.nodes["Scale Instances"].height = 100.0

    sub_sensor_visual_1.nodes["Reroute.004"].width  = 20.0
    sub_sensor_visual_1.nodes["Reroute.004"].height = 100.0

    sub_sensor_visual_1.nodes["Group Input.001"].width  = 140.0
    sub_sensor_visual_1.nodes["Group Input.001"].height = 100.0


    # Initialize sub_sensor_visual_1 links

    # index_of_nearest.Index -> sample_index.Index
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Index of Nearest"].outputs[0],
        sub_sensor_visual_1.nodes["Sample Index"].inputs[2]
    )
    # position.Position -> sample_index.Value
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Position"].outputs[0],
        sub_sensor_visual_1.nodes["Sample Index"].inputs[1]
    )
    # uv_sphere.Mesh -> set_material.Geometry
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["UV Sphere"].outputs[0],
        sub_sensor_visual_1.nodes["Set Material"].inputs[0]
    )
    # set_material.Geometry -> instance_on_points.Instance
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Set Material"].outputs[0],
        sub_sensor_visual_1.nodes["Instance on Points"].inputs[2]
    )
    # position_001.Position -> vector_math_001.Vector
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Position.001"].outputs[0],
        sub_sensor_visual_1.nodes["Vector Math.001"].inputs[0]
    )
    # sample_index.Value -> vector_math_001.Vector
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Sample Index"].outputs[0],
        sub_sensor_visual_1.nodes["Vector Math.001"].inputs[1]
    )
    # math.Value -> scale_instances.Scale
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Math"].outputs[0],
        sub_sensor_visual_1.nodes["Scale Instances"].inputs[2]
    )
    # vector_math_001.Value -> math.Value
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Vector Math.001"].outputs[1],
        sub_sensor_visual_1.nodes["Math"].inputs[0]
    )
    # position.Position -> index_of_nearest.Position
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Position"].outputs[0],
        sub_sensor_visual_1.nodes["Index of Nearest"].inputs[0]
    )
    # reroute_003.Output -> scale_instances.Instances
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Reroute.003"].outputs[0],
        sub_sensor_visual_1.nodes["Scale Instances"].inputs[0]
    )
    # group_input.Points -> instance_on_points.Points
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Group Input"].outputs[0],
        sub_sensor_visual_1.nodes["Instance on Points"].inputs[0]
    )
    # group_input.Material -> set_material.Material
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Group Input"].outputs[2],
        sub_sensor_visual_1.nodes["Set Material"].inputs[2]
    )
    # group_input_001.Overlap -> math.Value
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Group Input.001"].outputs[3],
        sub_sensor_visual_1.nodes["Math"].inputs[1]
    )
    # reroute_001.Output -> group_output.Radii
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Reroute.001"].outputs[0],
        sub_sensor_visual_1.nodes["Group Output"].inputs[1]
    )
    # math.Value -> reroute.Input
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Math"].outputs[0],
        sub_sensor_visual_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> reroute_001.Input
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Reroute"].outputs[0],
        sub_sensor_visual_1.nodes["Reroute.001"].inputs[0]
    )
    # instance_on_points.Instances -> reroute_002.Input
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Instance on Points"].outputs[0],
        sub_sensor_visual_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_002.Output -> sample_index.Geometry
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Reroute.002"].outputs[0],
        sub_sensor_visual_1.nodes["Sample Index"].inputs[0]
    )
    # reroute_002.Output -> reroute_003.Input
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Reroute.002"].outputs[0],
        sub_sensor_visual_1.nodes["Reroute.003"].inputs[0]
    )
    # scale_instances.Instances -> separate_geometry.Geometry
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Scale Instances"].outputs[0],
        sub_sensor_visual_1.nodes["Separate Geometry"].inputs[0]
    )
    # separate_geometry.Selection -> group_output.Geometry
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Separate Geometry"].outputs[0],
        sub_sensor_visual_1.nodes["Group Output"].inputs[0]
    )
    # reroute_004.Output -> separate_geometry.Selection
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Reroute.004"].outputs[0],
        sub_sensor_visual_1.nodes["Separate Geometry"].inputs[1]
    )
    # group_input_001.Radius View -> reroute_004.Input
    sub_sensor_visual_1.links.new(
        sub_sensor_visual_1.nodes["Group Input.001"].outputs[4],
        sub_sensor_visual_1.nodes["Reroute.004"].inputs[0]
    )

    return sub_sensor_visual_1


def poisson_slice_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Poisson Slice node group"""
    poisson_slice_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Poisson Slice")

    poisson_slice_1.color_tag = 'NONE'
    poisson_slice_1.description = ""
    poisson_slice_1.default_group_node_width = 140
    poisson_slice_1.show_modifier_manage_panel = True

    # poisson_slice_1 interface

    # Socket Points
    points_socket = poisson_slice_1.interface.new_socket(name="Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Euler Rotation
    euler_rotation_socket = poisson_slice_1.interface.new_socket(name="Euler Rotation", in_out='OUTPUT', socket_type='NodeSocketVector')
    euler_rotation_socket.default_value = (0.0, 0.0, 0.0)
    euler_rotation_socket.min_value = -3.4028234663852886e+38
    euler_rotation_socket.max_value = 3.4028234663852886e+38
    euler_rotation_socket.subtype = 'EULER'
    euler_rotation_socket.attribute_domain = 'POINT'
    euler_rotation_socket.default_input = 'VALUE'
    euler_rotation_socket.structure_type = 'AUTO'

    # Socket Normal
    normal_socket = poisson_slice_1.interface.new_socket(name="Normal", in_out='OUTPUT', socket_type='NodeSocketVector')
    normal_socket.default_value = (0.0, 0.0, 0.0)
    normal_socket.min_value = -3.4028234663852886e+38
    normal_socket.max_value = 3.4028234663852886e+38
    normal_socket.subtype = 'NONE'
    normal_socket.attribute_domain = 'POINT'
    normal_socket.default_input = 'VALUE'
    normal_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket = poisson_slice_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = poisson_slice_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket.default_value = 128
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Base Min Dist
    base_min_dist_socket = poisson_slice_1.interface.new_socket(name="Base Min Dist", in_out='INPUT', socket_type='NodeSocketFloat')
    base_min_dist_socket.default_value = 0.5
    base_min_dist_socket.min_value = -10000.0
    base_min_dist_socket.max_value = 10000.0
    base_min_dist_socket.subtype = 'NONE'
    base_min_dist_socket.attribute_domain = 'POINT'
    base_min_dist_socket.default_input = 'VALUE'
    base_min_dist_socket.structure_type = 'AUTO'

    # Socket Density Map
    density_map_socket = poisson_slice_1.interface.new_socket(name="Density Map", in_out='INPUT', socket_type='NodeSocketFloat')
    density_map_socket.default_value = 0.0
    density_map_socket.min_value = -10000.0
    density_map_socket.max_value = 10000.0
    density_map_socket.subtype = 'NONE'
    density_map_socket.attribute_domain = 'POINT'
    density_map_socket.default_input = 'VALUE'
    density_map_socket.structure_type = 'AUTO'

    # Socket Density Max
    density_max_socket = poisson_slice_1.interface.new_socket(name="Density Max", in_out='INPUT', socket_type='NodeSocketFloat')
    density_max_socket.default_value = 586.7999877929688
    density_max_socket.min_value = 0.0
    density_max_socket.max_value = 3.4028234663852886e+38
    density_max_socket.subtype = 'NONE'
    density_max_socket.attribute_domain = 'POINT'
    density_max_socket.default_input = 'VALUE'
    density_max_socket.structure_type = 'AUTO'

    # Socket Density Factor
    density_factor_socket = poisson_slice_1.interface.new_socket(name="Density Factor", in_out='INPUT', socket_type='NodeSocketFloat')
    density_factor_socket.default_value = 1.0
    density_factor_socket.min_value = 0.0
    density_factor_socket.max_value = 1.0
    density_factor_socket.subtype = 'FACTOR'
    density_factor_socket.attribute_domain = 'POINT'
    density_factor_socket.default_input = 'VALUE'
    density_factor_socket.structure_type = 'AUTO'

    # Socket Upper Bound
    upper_bound_socket = poisson_slice_1.interface.new_socket(name="Upper Bound", in_out='INPUT', socket_type='NodeSocketFloat')
    upper_bound_socket.default_value = 0.0
    upper_bound_socket.min_value = -10000.0
    upper_bound_socket.max_value = 10000.0
    upper_bound_socket.subtype = 'NONE'
    upper_bound_socket.attribute_domain = 'POINT'
    upper_bound_socket.default_input = 'VALUE'
    upper_bound_socket.structure_type = 'AUTO'

    # Socket Lower Bound
    lower_bound_socket = poisson_slice_1.interface.new_socket(name="Lower Bound", in_out='INPUT', socket_type='NodeSocketFloat')
    lower_bound_socket.default_value = 0.0
    lower_bound_socket.min_value = -10000.0
    lower_bound_socket.max_value = 10000.0
    lower_bound_socket.subtype = 'NONE'
    lower_bound_socket.attribute_domain = 'POINT'
    lower_bound_socket.default_input = 'VALUE'
    lower_bound_socket.structure_type = 'AUTO'

    # Socket Distance Multiplier
    distance_multiplier_socket = poisson_slice_1.interface.new_socket(name="Distance Multiplier", in_out='INPUT', socket_type='NodeSocketFloat')
    distance_multiplier_socket.default_value = 4.0
    distance_multiplier_socket.min_value = -10000.0
    distance_multiplier_socket.max_value = 10000.0
    distance_multiplier_socket.subtype = 'NONE'
    distance_multiplier_socket.attribute_domain = 'POINT'
    distance_multiplier_socket.default_input = 'VALUE'
    distance_multiplier_socket.structure_type = 'AUTO'

    # Initialize poisson_slice_1 nodes

    # Node Group Output
    group_output = poisson_slice_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = poisson_slice_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Distribute Points on Faces.002
    distribute_points_on_faces_002 = poisson_slice_1.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces_002.name = "Distribute Points on Faces.002"
    distribute_points_on_faces_002.show_options = True
    distribute_points_on_faces_002.distribute_method = 'POISSON'
    distribute_points_on_faces_002.use_legacy_normal = False

    # Node Math.006
    math_006 = poisson_slice_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False

    # Node Compare.004
    compare_004 = poisson_slice_1.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.show_options = True
    compare_004.data_type = 'FLOAT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'LESS_EQUAL'

    # Node Rotation to Euler.002
    rotation_to_euler_002 = poisson_slice_1.nodes.new("FunctionNodeRotationToEuler")
    rotation_to_euler_002.name = "Rotation to Euler.002"
    rotation_to_euler_002.show_options = True

    # Node Compare.005
    compare_005 = poisson_slice_1.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.show_options = True
    compare_005.data_type = 'FLOAT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'GREATER_THAN'

    # Node Boolean Math
    boolean_math = poisson_slice_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.show_options = True
    boolean_math.operation = 'AND'

    # Node Remove Named Attribute
    remove_named_attribute = poisson_slice_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute.name = "Remove Named Attribute"
    remove_named_attribute.show_options = True
    # Pattern Mode
    remove_named_attribute.inputs[1].default_value = 'Exact'
    # Name
    remove_named_attribute.inputs[2].default_value = ""

    # Set locations
    poisson_slice_1.nodes["Group Output"].location = (500.0, 40.0)
    poisson_slice_1.nodes["Group Input"].location = (-672.8167114257812, -18.523757934570312)
    poisson_slice_1.nodes["Distribute Points on Faces.002"].location = (99.1583023071289, 94.57749938964844)
    poisson_slice_1.nodes["Math.006"].location = (-353.10662841796875, -211.0105743408203)
    poisson_slice_1.nodes["Compare.004"].location = (-354.4921875, 316.5439453125)
    poisson_slice_1.nodes["Rotation to Euler.002"].location = (313.3600769042969, -49.281837463378906)
    poisson_slice_1.nodes["Compare.005"].location = (-356.2641296386719, 143.95718383789062)
    poisson_slice_1.nodes["Boolean Math"].location = (-180.29493713378906, 265.3675231933594)
    poisson_slice_1.nodes["Remove Named Attribute"].location = (540.0, 200.0)

    # Set dimensions
    poisson_slice_1.nodes["Group Output"].width  = 140.0
    poisson_slice_1.nodes["Group Output"].height = 100.0

    poisson_slice_1.nodes["Group Input"].width  = 140.0
    poisson_slice_1.nodes["Group Input"].height = 100.0

    poisson_slice_1.nodes["Distribute Points on Faces.002"].width  = 170.0
    poisson_slice_1.nodes["Distribute Points on Faces.002"].height = 100.0

    poisson_slice_1.nodes["Math.006"].width  = 140.0
    poisson_slice_1.nodes["Math.006"].height = 100.0

    poisson_slice_1.nodes["Compare.004"].width  = 140.0
    poisson_slice_1.nodes["Compare.004"].height = 100.0

    poisson_slice_1.nodes["Rotation to Euler.002"].width  = 140.0
    poisson_slice_1.nodes["Rotation to Euler.002"].height = 100.0

    poisson_slice_1.nodes["Compare.005"].width  = 140.0
    poisson_slice_1.nodes["Compare.005"].height = 100.0

    poisson_slice_1.nodes["Boolean Math"].width  = 140.0
    poisson_slice_1.nodes["Boolean Math"].height = 100.0

    poisson_slice_1.nodes["Remove Named Attribute"].width  = 170.0
    poisson_slice_1.nodes["Remove Named Attribute"].height = 100.0


    # Initialize poisson_slice_1 links

    # math_006.Value -> distribute_points_on_faces_002.Distance Min
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Math.006"].outputs[0],
        poisson_slice_1.nodes["Distribute Points on Faces.002"].inputs[2]
    )
    # distribute_points_on_faces_002.Rotation -> rotation_to_euler_002.Rotation
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Distribute Points on Faces.002"].outputs[2],
        poisson_slice_1.nodes["Rotation to Euler.002"].inputs[0]
    )
    # boolean_math.Boolean -> distribute_points_on_faces_002.Selection
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Boolean Math"].outputs[0],
        poisson_slice_1.nodes["Distribute Points on Faces.002"].inputs[1]
    )
    # group_input.Base Min Dist -> math_006.Value
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[2],
        poisson_slice_1.nodes["Math.006"].inputs[0]
    )
    # group_input.Mesh -> distribute_points_on_faces_002.Mesh
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[0],
        poisson_slice_1.nodes["Distribute Points on Faces.002"].inputs[0]
    )
    # group_input.Density Factor -> distribute_points_on_faces_002.Density Factor
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[5],
        poisson_slice_1.nodes["Distribute Points on Faces.002"].inputs[5]
    )
    # group_input.Seed -> distribute_points_on_faces_002.Seed
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[1],
        poisson_slice_1.nodes["Distribute Points on Faces.002"].inputs[6]
    )
    # group_input.Density Max -> distribute_points_on_faces_002.Density Max
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[4],
        poisson_slice_1.nodes["Distribute Points on Faces.002"].inputs[3]
    )
    # distribute_points_on_faces_002.Points -> group_output.Points
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Distribute Points on Faces.002"].outputs[0],
        poisson_slice_1.nodes["Group Output"].inputs[0]
    )
    # rotation_to_euler_002.Euler -> group_output.Euler Rotation
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Rotation to Euler.002"].outputs[0],
        poisson_slice_1.nodes["Group Output"].inputs[1]
    )
    # compare_004.Result -> boolean_math.Boolean
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Compare.004"].outputs[0],
        poisson_slice_1.nodes["Boolean Math"].inputs[0]
    )
    # compare_005.Result -> boolean_math.Boolean
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Compare.005"].outputs[0],
        poisson_slice_1.nodes["Boolean Math"].inputs[1]
    )
    # group_input.Lower Bound -> compare_005.B
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[7],
        poisson_slice_1.nodes["Compare.005"].inputs[1]
    )
    # group_input.Upper Bound -> compare_004.B
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[6],
        poisson_slice_1.nodes["Compare.004"].inputs[1]
    )
    # group_input.Density Map -> compare_004.A
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[3],
        poisson_slice_1.nodes["Compare.004"].inputs[0]
    )
    # group_input.Density Map -> compare_005.A
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[3],
        poisson_slice_1.nodes["Compare.005"].inputs[0]
    )
    # group_input.Distance Multiplier -> math_006.Value
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Group Input"].outputs[8],
        poisson_slice_1.nodes["Math.006"].inputs[1]
    )
    # distribute_points_on_faces_002.Normal -> group_output.Normal
    poisson_slice_1.links.new(
        poisson_slice_1.nodes["Distribute Points on Faces.002"].outputs[1],
        poisson_slice_1.nodes["Group Output"].inputs[2]
    )

    return poisson_slice_1


def poisson_placement_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Poisson Placement node group"""
    poisson_placement_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Poisson Placement")

    poisson_placement_1.color_tag = 'NONE'
    poisson_placement_1.description = ""
    poisson_placement_1.default_group_node_width = 140
    poisson_placement_1.show_modifier_manage_panel = True

    # poisson_placement_1 interface

    # Socket Points
    points_socket = poisson_placement_1.interface.new_socket(name="Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Euler Rotations
    euler_rotations_socket = poisson_placement_1.interface.new_socket(name="Euler Rotations", in_out='OUTPUT', socket_type='NodeSocketVector')
    euler_rotations_socket.default_value = (0.0, 0.0, 0.0)
    euler_rotations_socket.min_value = -3.4028234663852886e+38
    euler_rotations_socket.max_value = 3.4028234663852886e+38
    euler_rotations_socket.subtype = 'EULER'
    euler_rotations_socket.attribute_domain = 'POINT'
    euler_rotations_socket.default_input = 'VALUE'
    euler_rotations_socket.structure_type = 'AUTO'

    # Socket Normals
    normals_socket = poisson_placement_1.interface.new_socket(name="Normals", in_out='OUTPUT', socket_type='NodeSocketVector')
    normals_socket.default_value = (0.0, 0.0, 0.0)
    normals_socket.min_value = -3.4028234663852886e+38
    normals_socket.max_value = 3.4028234663852886e+38
    normals_socket.subtype = 'NONE'
    normals_socket.attribute_domain = 'POINT'
    normals_socket.default_input = 'VALUE'
    normals_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket = poisson_placement_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = poisson_placement_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket.default_value = 128
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Distance Min
    distance_min_socket = poisson_placement_1.interface.new_socket(name="Distance Min", in_out='INPUT', socket_type='NodeSocketFloat')
    distance_min_socket.default_value = 0.009999999776482582
    distance_min_socket.min_value = 0.0
    distance_min_socket.max_value = 3.4028234663852886e+38
    distance_min_socket.subtype = 'DISTANCE'
    distance_min_socket.attribute_domain = 'POINT'
    distance_min_socket.default_input = 'VALUE'
    distance_min_socket.structure_type = 'AUTO'

    # Socket Max Density
    max_density_socket = poisson_placement_1.interface.new_socket(name="Max Density", in_out='INPUT', socket_type='NodeSocketFloat')
    max_density_socket.default_value = 0.5
    max_density_socket.min_value = -10000.0
    max_density_socket.max_value = 10000.0
    max_density_socket.subtype = 'NONE'
    max_density_socket.attribute_domain = 'POINT'
    max_density_socket.default_input = 'VALUE'
    max_density_socket.structure_type = 'AUTO'

    # Socket Density Multiplier
    density_multiplier_socket = poisson_placement_1.interface.new_socket(name="Density Multiplier", in_out='INPUT', socket_type='NodeSocketFloat')
    density_multiplier_socket.default_value = 0.5
    density_multiplier_socket.min_value = -10000.0
    density_multiplier_socket.max_value = 10000.0
    density_multiplier_socket.subtype = 'NONE'
    density_multiplier_socket.attribute_domain = 'POINT'
    density_multiplier_socket.default_input = 'VALUE'
    density_multiplier_socket.structure_type = 'AUTO'

    # Socket Name
    name_socket = poisson_placement_1.interface.new_socket(name="Name", in_out='INPUT', socket_type='NodeSocketString')
    name_socket.default_value = ""
    name_socket.subtype = 'NONE'
    name_socket.attribute_domain = 'POINT'
    name_socket.default_input = 'VALUE'
    name_socket.structure_type = 'AUTO'

    # Socket True
    true_socket = poisson_placement_1.interface.new_socket(name="True", in_out='INPUT', socket_type='NodeSocketGeometry')
    true_socket.attribute_domain = 'POINT'
    true_socket.default_input = 'VALUE'
    true_socket.structure_type = 'AUTO'

    # Initialize poisson_placement_1 nodes

    # Node Group Output
    group_output = poisson_placement_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = poisson_placement_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Math
    math = poisson_placement_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.hide = True
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Clamp
    clamp = poisson_placement_1.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.hide = True
    clamp.show_options = True
    clamp.clamp_type = 'RANGE'
    # Min
    clamp.inputs[1].default_value = 0.0

    # Node Color Ramp
    color_ramp = poisson_placement_1.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.show_options = True
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'

    # Initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.090908944606781
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(1.0)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    # Node Math.002
    math_002 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'LESS_THAN'
    math_002.use_clamp = False

    # Node Math.001
    math_001 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.hide = True
    math_001.show_options = True
    math_001.operation = 'DIVIDE'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 100.0

    # Node Named Attribute
    named_attribute = poisson_placement_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'FLOAT'

    # Node Math.003
    math_003 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'SUBTRACT'
    math_003.use_clamp = False
    # Value
    math_003.inputs[0].default_value = 1.0

    # Node Math.004
    math_004 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = 0.8999999761581421

    # Node Frame
    frame = poisson_placement_1.nodes.new("NodeFrame")
    frame.label = "Tolerance"
    frame.name = "Frame"
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Reroute.001
    reroute_001 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Frame.001
    frame_001 = poisson_placement_1.nodes.new("NodeFrame")
    frame_001.label = "Density Multiplier"
    frame_001.name = "Frame.001"
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Reroute.002
    reroute_002 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketInt"
    # Node Reroute.004
    reroute_004 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketInt"
    # Node Reroute.005
    reroute_005 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.006
    reroute_006 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.008
    reroute_008 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketFloat"
    # Node Join Geometry
    join_geometry = poisson_placement_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Delete Geometry.001
    delete_geometry_001 = poisson_placement_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.hide = True
    delete_geometry_001.show_options = True
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'

    # Node Compare.005
    compare_005 = poisson_placement_1.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.show_options = True
    compare_005.data_type = 'FLOAT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'LESS_THAN'

    # Node Geometry Proximity.001
    geometry_proximity_001 = poisson_placement_1.nodes.new("GeometryNodeProximity")
    geometry_proximity_001.name = "Geometry Proximity.001"
    geometry_proximity_001.hide = True
    geometry_proximity_001.show_options = True
    geometry_proximity_001.target_element = 'POINTS'
    # Group ID
    geometry_proximity_001.inputs[1].default_value = 0
    # Source Position
    geometry_proximity_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    geometry_proximity_001.inputs[3].default_value = 0

    # Node Reroute.007
    reroute_007 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketFloat"
    # Node Vector Math.002
    vector_math_002 = poisson_placement_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.hide = True
    vector_math_002.show_options = True
    vector_math_002.operation = 'ADD'

    # Node Reroute
    reroute = poisson_placement_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Reroute.003
    reroute_003 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Frame.002
    frame_002 = poisson_placement_1.nodes.new("NodeFrame")
    frame_002.label = "Remove Edge Cases"
    frame_002.name = "Frame.002"
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Group.001
    group_001 = poisson_placement_1.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.show_options = True
    group_001.node_tree = bpy.data.node_groups[node_tree_names[poisson_slice_1_node_group]]
    # Socket_7
    group_001.inputs[6].default_value = 1.0

    # Node Group.002
    group_002 = poisson_placement_1.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.show_options = True
    group_002.node_tree = bpy.data.node_groups[node_tree_names[poisson_slice_1_node_group]]

    # Node Reroute.009
    reroute_009 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloat"
    # Node Reroute.010
    reroute_010 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketFloat"
    # Node Reroute.011
    reroute_011 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketFloat"
    # Node Reroute.012
    reroute_012 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketGeometry"
    # Node Reroute.013
    reroute_013 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketFloat"
    # Node Delete Geometry.002
    delete_geometry_002 = poisson_placement_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.hide = True
    delete_geometry_002.show_options = True
    delete_geometry_002.domain = 'POINT'
    delete_geometry_002.mode = 'ALL'

    # Node Compare.006
    compare_006 = poisson_placement_1.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.hide = True
    compare_006.show_options = True
    compare_006.data_type = 'FLOAT'
    compare_006.mode = 'ELEMENT'
    compare_006.operation = 'LESS_THAN'

    # Node Geometry Proximity.002
    geometry_proximity_002 = poisson_placement_1.nodes.new("GeometryNodeProximity")
    geometry_proximity_002.name = "Geometry Proximity.002"
    geometry_proximity_002.hide = True
    geometry_proximity_002.show_options = True
    geometry_proximity_002.target_element = 'POINTS'
    # Group ID
    geometry_proximity_002.inputs[1].default_value = 0
    # Source Position
    geometry_proximity_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    geometry_proximity_002.inputs[3].default_value = 0

    # Node Vector Math.003
    vector_math_003 = poisson_placement_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.hide = True
    vector_math_003.show_options = True
    vector_math_003.operation = 'ADD'

    # Node Frame.003
    frame_003 = poisson_placement_1.nodes.new("NodeFrame")
    frame_003.label = "Remove Edge Cases"
    frame_003.name = "Frame.003"
    frame_003.show_options = True
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Group.003
    group_003 = poisson_placement_1.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.show_options = True
    group_003.node_tree = bpy.data.node_groups[node_tree_names[poisson_slice_1_node_group]]

    # Node Group.004
    group_004 = poisson_placement_1.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.show_options = True
    group_004.node_tree = bpy.data.node_groups[node_tree_names[poisson_slice_1_node_group]]
    # Socket_8
    group_004.inputs[7].default_value = 0.0

    # Node Delete Geometry.003
    delete_geometry_003 = poisson_placement_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_003.name = "Delete Geometry.003"
    delete_geometry_003.hide = True
    delete_geometry_003.show_options = True
    delete_geometry_003.domain = 'POINT'
    delete_geometry_003.mode = 'ALL'

    # Node Compare.007
    compare_007 = poisson_placement_1.nodes.new("FunctionNodeCompare")
    compare_007.name = "Compare.007"
    compare_007.hide = True
    compare_007.show_options = True
    compare_007.data_type = 'FLOAT'
    compare_007.mode = 'ELEMENT'
    compare_007.operation = 'LESS_THAN'

    # Node Geometry Proximity.003
    geometry_proximity_003 = poisson_placement_1.nodes.new("GeometryNodeProximity")
    geometry_proximity_003.name = "Geometry Proximity.003"
    geometry_proximity_003.hide = True
    geometry_proximity_003.show_options = True
    geometry_proximity_003.target_element = 'POINTS'
    # Group ID
    geometry_proximity_003.inputs[1].default_value = 0
    # Source Position
    geometry_proximity_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    geometry_proximity_003.inputs[3].default_value = 0

    # Node Frame.004
    frame_004 = poisson_placement_1.nodes.new("NodeFrame")
    frame_004.label = "Remove Edge Cases"
    frame_004.name = "Frame.004"
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Vector Math.004
    vector_math_004 = poisson_placement_1.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.hide = True
    vector_math_004.show_options = True
    vector_math_004.operation = 'ADD'

    # Node Reroute.014
    reroute_014 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    reroute_014.socket_idname = "NodeSocketVector"
    # Node Reroute.015
    reroute_015 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketInt"
    # Node Reroute.016
    reroute_016 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    reroute_016.socket_idname = "NodeSocketGeometry"
    # Node Reroute.017
    reroute_017 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.show_options = True
    reroute_017.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.018
    reroute_018 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    reroute_018.socket_idname = "NodeSocketFloat"
    # Node Reroute.019
    reroute_019 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    reroute_019.socket_idname = "NodeSocketFloat"
    # Node Reroute.020
    reroute_020 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.show_options = True
    reroute_020.socket_idname = "NodeSocketColor"
    # Node Reroute.021
    reroute_021 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.show_options = True
    reroute_021.socket_idname = "NodeSocketColor"
    # Node Reroute.022
    reroute_022 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    reroute_022.show_options = True
    reroute_022.socket_idname = "NodeSocketGeometry"
    # Node Reroute.023
    reroute_023 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.show_options = True
    reroute_023.socket_idname = "NodeSocketInt"
    # Node Reroute.024
    reroute_024 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.show_options = True
    reroute_024.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.025
    reroute_025 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.show_options = True
    reroute_025.socket_idname = "NodeSocketFloat"
    # Node Value
    value = poisson_placement_1.nodes.new("ShaderNodeValue")
    value.label = "Upper Bound 3"
    value.name = "Value"
    value.show_options = True

    value.outputs[0].default_value = 0.20000001788139343
    # Node Reroute.026
    reroute_026 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.show_options = True
    reroute_026.socket_idname = "NodeSocketFloat"
    # Node Value.001
    value_001 = poisson_placement_1.nodes.new("ShaderNodeValue")
    value_001.label = "Upper Bound 2"
    value_001.name = "Value.001"
    value_001.show_options = True

    value_001.outputs[0].default_value = 0.4000000059604645
    # Node Reroute.029
    reroute_029 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_029.name = "Reroute.029"
    reroute_029.show_options = True
    reroute_029.socket_idname = "NodeSocketFloat"
    # Node Value.002
    value_002 = poisson_placement_1.nodes.new("ShaderNodeValue")
    value_002.label = "Upper Bound 1"
    value_002.name = "Value.002"
    value_002.show_options = True

    value_002.outputs[0].default_value = 0.8999999761581421
    # Node Reroute.030
    reroute_030 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_030.name = "Reroute.030"
    reroute_030.show_options = True
    reroute_030.socket_idname = "NodeSocketFloat"
    # Node Math.005
    math_005 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.hide = True
    math_005.show_options = True
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False

    # Node Reroute.027
    reroute_027 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    reroute_027.show_options = True
    reroute_027.socket_idname = "NodeSocketFloatDistance"
    # Node Value.005
    value_005 = poisson_placement_1.nodes.new("ShaderNodeValue")
    value_005.label = "Distance Multiplier 1"
    value_005.name = "Value.005"
    value_005.show_options = True

    value_005.outputs[0].default_value = 1.0
    # Node Math.006
    math_006 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.hide = True
    math_006.show_options = True
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False

    # Node Value.006
    value_006 = poisson_placement_1.nodes.new("ShaderNodeValue")
    value_006.label = "Distance Multiplier 2"
    value_006.name = "Value.006"
    value_006.show_options = True

    value_006.outputs[0].default_value = 2.0
    # Node Math.007
    math_007 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.hide = True
    math_007.show_options = True
    math_007.operation = 'MULTIPLY'
    math_007.use_clamp = False

    # Node Value.007
    value_007 = poisson_placement_1.nodes.new("ShaderNodeValue")
    value_007.label = "Distance Multiplier 3"
    value_007.name = "Value.007"
    value_007.show_options = True

    value_007.outputs[0].default_value = 4.0
    # Node Reroute.028
    reroute_028 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    reroute_028.show_options = True
    reroute_028.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.031
    reroute_031 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_031.name = "Reroute.031"
    reroute_031.show_options = True
    reroute_031.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.033
    reroute_033 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_033.name = "Reroute.033"
    reroute_033.show_options = True
    reroute_033.socket_idname = "NodeSocketFloat"
    # Node Reroute.034
    reroute_034 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_034.name = "Reroute.034"
    reroute_034.show_options = True
    reroute_034.socket_idname = "NodeSocketFloat"
    # Node Reroute.035
    reroute_035 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_035.name = "Reroute.035"
    reroute_035.show_options = True
    reroute_035.socket_idname = "NodeSocketFloat"
    # Node Value.008
    value_008 = poisson_placement_1.nodes.new("ShaderNodeValue")
    value_008.label = "Distance Multiplier 4"
    value_008.name = "Value.008"
    value_008.show_options = True

    value_008.outputs[0].default_value = 8.0
    # Node Math.008
    math_008 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.hide = True
    math_008.show_options = True
    math_008.operation = 'ADD'
    math_008.use_clamp = False
    # Value_001
    math_008.inputs[1].default_value = 0.10000000149011612

    # Node Math.009
    math_009 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.hide = True
    math_009.show_options = True
    math_009.operation = 'ADD'
    math_009.use_clamp = False
    # Value_001
    math_009.inputs[1].default_value = 0.10000000149011612

    # Node Math.010
    math_010 = poisson_placement_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.hide = True
    math_010.show_options = True
    math_010.operation = 'ADD'
    math_010.use_clamp = False
    # Value_001
    math_010.inputs[1].default_value = 0.10000000149011612

    # Node Vector Math.005
    vector_math_005 = poisson_placement_1.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.hide = True
    vector_math_005.show_options = True
    vector_math_005.operation = 'ADD'

    # Node Vector Math.006
    vector_math_006 = poisson_placement_1.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.hide = True
    vector_math_006.show_options = True
    vector_math_006.operation = 'ADD'
    # Vector
    vector_math_006.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Vector_001
    vector_math_006.inputs[1].default_value = (0.0, 0.0, 0.0)

    # Node Vector Math.007
    vector_math_007 = poisson_placement_1.nodes.new("ShaderNodeVectorMath")
    vector_math_007.name = "Vector Math.007"
    vector_math_007.hide = True
    vector_math_007.show_options = True
    vector_math_007.operation = 'ADD'

    # Node Vector Math.008
    vector_math_008 = poisson_placement_1.nodes.new("ShaderNodeVectorMath")
    vector_math_008.name = "Vector Math.008"
    vector_math_008.hide = True
    vector_math_008.show_options = True
    vector_math_008.operation = 'ADD'

    # Node Reroute.032
    reroute_032 = poisson_placement_1.nodes.new("NodeReroute")
    reroute_032.name = "Reroute.032"
    reroute_032.show_options = True
    reroute_032.socket_idname = "NodeSocketVector"
    # Node Viewer
    viewer = poisson_placement_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")
    viewer.viewer_items.new('FLOAT', "Value")
    # Value
    viewer.inputs[1].default_value = 0.0

    # Set parents
    poisson_placement_1.nodes["Math"].parent = poisson_placement_1.nodes["Frame.001"]
    poisson_placement_1.nodes["Clamp"].parent = poisson_placement_1.nodes["Frame.001"]
    poisson_placement_1.nodes["Color Ramp"].parent = poisson_placement_1.nodes["Frame"]
    poisson_placement_1.nodes["Math.002"].parent = poisson_placement_1.nodes["Frame"]
    poisson_placement_1.nodes["Math.003"].parent = poisson_placement_1.nodes["Frame"]
    poisson_placement_1.nodes["Math.004"].parent = poisson_placement_1.nodes["Frame"]
    poisson_placement_1.nodes["Reroute.001"].parent = poisson_placement_1.nodes["Frame.001"]
    poisson_placement_1.nodes["Delete Geometry.001"].parent = poisson_placement_1.nodes["Frame.002"]
    poisson_placement_1.nodes["Compare.005"].parent = poisson_placement_1.nodes["Frame.002"]
    poisson_placement_1.nodes["Geometry Proximity.001"].parent = poisson_placement_1.nodes["Frame.002"]
    poisson_placement_1.nodes["Reroute.009"].parent = poisson_placement_1.nodes["Frame"]
    poisson_placement_1.nodes["Delete Geometry.002"].parent = poisson_placement_1.nodes["Frame.003"]
    poisson_placement_1.nodes["Compare.006"].parent = poisson_placement_1.nodes["Frame.003"]
    poisson_placement_1.nodes["Geometry Proximity.002"].parent = poisson_placement_1.nodes["Frame.003"]
    poisson_placement_1.nodes["Delete Geometry.003"].parent = poisson_placement_1.nodes["Frame.004"]
    poisson_placement_1.nodes["Compare.007"].parent = poisson_placement_1.nodes["Frame.004"]
    poisson_placement_1.nodes["Geometry Proximity.003"].parent = poisson_placement_1.nodes["Frame.004"]

    # Set locations
    poisson_placement_1.nodes["Group Output"].location = (2252.991455078125, 76.17880249023438)
    poisson_placement_1.nodes["Group Input"].location = (-2296.390869140625, 14.094621658325195)
    poisson_placement_1.nodes["Math"].location = (108.6212158203125, -93.56890869140625)
    poisson_placement_1.nodes["Clamp"].location = (310.5789794921875, -44.332611083984375)
    poisson_placement_1.nodes["Color Ramp"].location = (630.1890869140625, -36.07157897949219)
    poisson_placement_1.nodes["Math.002"].location = (455.1639404296875, -50.673919677734375)
    poisson_placement_1.nodes["Math.001"].location = (-2136.099365234375, -107.94114685058594)
    poisson_placement_1.nodes["Named Attribute"].location = (-2094.569091796875, -224.30255126953125)
    poisson_placement_1.nodes["Math.003"].location = (254.6981201171875, -45.9217529296875)
    poisson_placement_1.nodes["Math.004"].location = (76.771484375, -44.074188232421875)
    poisson_placement_1.nodes["Frame"].location = (-1691.6279296875, 250.4666748046875)
    poisson_placement_1.nodes["Reroute.001"].location = (33.8333740234375, -62.5491943359375)
    poisson_placement_1.nodes["Frame.001"].location = (-1613.7864990234375, 415.1666564941406)
    poisson_placement_1.nodes["Reroute.002"].location = (-807.1942138671875, -58.561737060546875)
    poisson_placement_1.nodes["Reroute.004"].location = (-1696.522216796875, -56.40123748779297)
    poisson_placement_1.nodes["Reroute.005"].location = (-807.1763305664062, -75.89035034179688)
    poisson_placement_1.nodes["Reroute.006"].location = (-1705.562255859375, -76.0916519165039)
    poisson_placement_1.nodes["Reroute.008"].location = (-796.1201171875, 355.99029541015625)
    poisson_placement_1.nodes["Join Geometry"].location = (2003.086669921875, 110.77774047851562)
    poisson_placement_1.nodes["Delete Geometry.001"].location = (397.260986328125, -86.08203125)
    poisson_placement_1.nodes["Compare.005"].location = (230.6317138671875, -42.656494140625)
    poisson_placement_1.nodes["Geometry Proximity.001"].location = (28.8328857421875, -49.24639892578125)
    poisson_placement_1.nodes["Reroute.007"].location = (-1353.487060546875, -95.79159545898438)
    poisson_placement_1.nodes["Vector Math.002"].location = (738.9694213867188, 212.875244140625)
    poisson_placement_1.nodes["Reroute"].location = (-806.4228515625, -41.56085205078125)
    poisson_placement_1.nodes["Reroute.003"].location = (-1695.1103515625, -38.46118927001953)
    poisson_placement_1.nodes["Frame.002"].location = (1064.3333740234375, 334.0)
    poisson_placement_1.nodes["Group.001"].location = (474.2406005859375, 396.00653076171875)
    poisson_placement_1.nodes["Group.002"].location = (520.0, 20.0)
    poisson_placement_1.nodes["Reroute.009"].location = (33.8333740234375, -89.0985107421875)
    poisson_placement_1.nodes["Reroute.010"].location = (-1814.236328125, -99.65582275390625)
    poisson_placement_1.nodes["Reroute.011"].location = (-809.1395263671875, -95.76837921142578)
    poisson_placement_1.nodes["Reroute.012"].location = (1653.50390625, 362.17095947265625)
    poisson_placement_1.nodes["Reroute.013"].location = (-29.214752197265625, 47.180381774902344)
    poisson_placement_1.nodes["Delete Geometry.002"].location = (397.2894287109375, -86.32601928710938)
    poisson_placement_1.nodes["Compare.006"].location = (230.66015625, -42.900482177734375)
    poisson_placement_1.nodes["Geometry Proximity.002"].location = (28.8614501953125, -49.490386962890625)
    poisson_placement_1.nodes["Vector Math.003"].location = (998.3311767578125, -476.035400390625)
    poisson_placement_1.nodes["Frame.003"].location = (1323.6666259765625, -354.6666564941406)
    poisson_placement_1.nodes["Group.003"].location = (733.6022338867188, -292.90411376953125)
    poisson_placement_1.nodes["Group.004"].location = (473.0001220703125, -640.04638671875)
    poisson_placement_1.nodes["Delete Geometry.003"].location = (397.3287353515625, -86.3124008178711)
    poisson_placement_1.nodes["Compare.007"].location = (230.699462890625, -42.88685989379883)
    poisson_placement_1.nodes["Geometry Proximity.003"].location = (28.9007568359375, -49.47676467895508)
    poisson_placement_1.nodes["Frame.004"].location = (1330.3333740234375, 9.333333015441895)
    poisson_placement_1.nodes["Vector Math.004"].location = (1173.298095703125, -132.89608764648438)
    poisson_placement_1.nodes["Reroute.014"].location = (2055.296875, -156.5221710205078)
    poisson_placement_1.nodes["Reroute.015"].location = (-1498.758544921875, -56.87989044189453)
    poisson_placement_1.nodes["Reroute.016"].location = (-1498.758544921875, -39.142333984375)
    poisson_placement_1.nodes["Reroute.017"].location = (-1500.261474609375, -76.04566955566406)
    poisson_placement_1.nodes["Reroute.018"].location = (-1500.261474609375, -97.01470947265625)
    poisson_placement_1.nodes["Reroute.019"].location = (-165.62857055664062, -541.525390625)
    poisson_placement_1.nodes["Reroute.020"].location = (-26.6895751953125, 3.8181838989257812)
    poisson_placement_1.nodes["Reroute.021"].location = (-164.10916137695312, -586.0267944335938)
    poisson_placement_1.nodes["Reroute.022"].location = (-814.3773193359375, -507.9164733886719)
    poisson_placement_1.nodes["Reroute.023"].location = (-814.0401611328125, -525.4027099609375)
    poisson_placement_1.nodes["Reroute.024"].location = (-813.5087890625, -544.9868774414062)
    poisson_placement_1.nodes["Reroute.025"].location = (-813.6690673828125, -568.5579833984375)
    poisson_placement_1.nodes["Value"].location = (-913.5899047851562, -348.88031005859375)
    poisson_placement_1.nodes["Reroute.026"].location = (-191.89718627929688, -581.6975708007812)
    poisson_placement_1.nodes["Value.001"].location = (-913.56298828125, -249.63009643554688)
    poisson_placement_1.nodes["Reroute.029"].location = (425.1026916503906, -270.27020263671875)
    poisson_placement_1.nodes["Value.002"].location = (-915.092529296875, -151.83181762695312)
    poisson_placement_1.nodes["Reroute.030"].location = (-89.80072021484375, 36.490882873535156)
    poisson_placement_1.nodes["Math.005"].location = (540.0, 40.0)
    poisson_placement_1.nodes["Reroute.027"].location = (444.18939208984375, -83.8433837890625)
    poisson_placement_1.nodes["Value.005"].location = (256.9215393066406, 89.22665405273438)
    poisson_placement_1.nodes["Math.006"].location = (534.0384521484375, -250.89764404296875)
    poisson_placement_1.nodes["Value.006"].location = (260.1625061035156, -187.4114990234375)
    poisson_placement_1.nodes["Math.007"].location = (535.8397827148438, -598.902587890625)
    poisson_placement_1.nodes["Value.007"].location = (272.4151611328125, -563.5302124023438)
    poisson_placement_1.nodes["Reroute.028"].location = (437.1025390625, -441.42718505859375)
    poisson_placement_1.nodes["Reroute.031"].location = (449.398681640625, -785.75146484375)
    poisson_placement_1.nodes["Reroute.033"].location = (1265.0369873046875, 89.85745239257812)
    poisson_placement_1.nodes["Reroute.034"].location = (1249.273681640625, -229.05369567871094)
    poisson_placement_1.nodes["Reroute.035"].location = (1263.216796875, -593.0169067382812)
    poisson_placement_1.nodes["Value.008"].location = (260.2165832519531, -883.1010131835938)
    poisson_placement_1.nodes["Math.008"].location = (262.895751953125, -153.6063995361328)
    poisson_placement_1.nodes["Math.009"].location = (532.0933837890625, -304.0968017578125)
    poisson_placement_1.nodes["Math.010"].location = (261.34185791015625, -851.8719482421875)
    poisson_placement_1.nodes["Vector Math.005"].location = (736.5426635742188, 167.6517333984375)
    poisson_placement_1.nodes["Vector Math.006"].location = (805.527099609375, 91.939453125)
    poisson_placement_1.nodes["Vector Math.007"].location = (1173.079345703125, -175.46286010742188)
    poisson_placement_1.nodes["Vector Math.008"].location = (996.780029296875, -522.220458984375)
    poisson_placement_1.nodes["Reroute.032"].location = (2059.32861328125, -189.8099365234375)
    poisson_placement_1.nodes["Viewer"].location = (765.1318359375, 55.0)

    # Set dimensions
    poisson_placement_1.nodes["Group Output"].width  = 140.0
    poisson_placement_1.nodes["Group Output"].height = 100.0

    poisson_placement_1.nodes["Group Input"].width  = 140.0
    poisson_placement_1.nodes["Group Input"].height = 100.0

    poisson_placement_1.nodes["Math"].width  = 140.0
    poisson_placement_1.nodes["Math"].height = 100.0

    poisson_placement_1.nodes["Clamp"].width  = 140.0
    poisson_placement_1.nodes["Clamp"].height = 100.0

    poisson_placement_1.nodes["Color Ramp"].width  = 240.0
    poisson_placement_1.nodes["Color Ramp"].height = 100.0

    poisson_placement_1.nodes["Math.002"].width  = 140.0
    poisson_placement_1.nodes["Math.002"].height = 100.0

    poisson_placement_1.nodes["Math.001"].width  = 140.0
    poisson_placement_1.nodes["Math.001"].height = 100.0

    poisson_placement_1.nodes["Named Attribute"].width  = 140.0
    poisson_placement_1.nodes["Named Attribute"].height = 100.0

    poisson_placement_1.nodes["Math.003"].width  = 140.0
    poisson_placement_1.nodes["Math.003"].height = 100.0

    poisson_placement_1.nodes["Math.004"].width  = 140.0
    poisson_placement_1.nodes["Math.004"].height = 100.0

    poisson_placement_1.nodes["Frame"].width  = 899.2946166992188
    poisson_placement_1.nodes["Frame"].height = 262.8000183105469

    poisson_placement_1.nodes["Reroute.001"].width  = 14.5
    poisson_placement_1.nodes["Reroute.001"].height = 100.0

    poisson_placement_1.nodes["Frame.001"].width  = 479.453125
    poisson_placement_1.nodes["Frame.001"].height = 146.0333251953125

    poisson_placement_1.nodes["Reroute.002"].width  = 14.5
    poisson_placement_1.nodes["Reroute.002"].height = 100.0

    poisson_placement_1.nodes["Reroute.004"].width  = 14.5
    poisson_placement_1.nodes["Reroute.004"].height = 100.0

    poisson_placement_1.nodes["Reroute.005"].width  = 14.5
    poisson_placement_1.nodes["Reroute.005"].height = 100.0

    poisson_placement_1.nodes["Reroute.006"].width  = 14.5
    poisson_placement_1.nodes["Reroute.006"].height = 100.0

    poisson_placement_1.nodes["Reroute.008"].width  = 14.5
    poisson_placement_1.nodes["Reroute.008"].height = 100.0

    poisson_placement_1.nodes["Join Geometry"].width  = 140.0
    poisson_placement_1.nodes["Join Geometry"].height = 100.0

    poisson_placement_1.nodes["Delete Geometry.001"].width  = 140.0
    poisson_placement_1.nodes["Delete Geometry.001"].height = 100.0

    poisson_placement_1.nodes["Compare.005"].width  = 140.0
    poisson_placement_1.nodes["Compare.005"].height = 100.0

    poisson_placement_1.nodes["Geometry Proximity.001"].width  = 140.0
    poisson_placement_1.nodes["Geometry Proximity.001"].height = 100.0

    poisson_placement_1.nodes["Reroute.007"].width  = 14.5
    poisson_placement_1.nodes["Reroute.007"].height = 100.0

    poisson_placement_1.nodes["Vector Math.002"].width  = 140.0
    poisson_placement_1.nodes["Vector Math.002"].height = 100.0

    poisson_placement_1.nodes["Reroute"].width  = 14.5
    poisson_placement_1.nodes["Reroute"].height = 100.0

    poisson_placement_1.nodes["Reroute.003"].width  = 14.5
    poisson_placement_1.nodes["Reroute.003"].height = 100.0

    poisson_placement_1.nodes["Frame.002"].width  = 566.0
    poisson_placement_1.nodes["Frame.002"].height = 214.33334350585938

    poisson_placement_1.nodes["Group.001"].width  = 205.1318359375
    poisson_placement_1.nodes["Group.001"].height = 100.0

    poisson_placement_1.nodes["Group.002"].width  = 205.1318359375
    poisson_placement_1.nodes["Group.002"].height = 100.0

    poisson_placement_1.nodes["Reroute.009"].width  = 14.5
    poisson_placement_1.nodes["Reroute.009"].height = 100.0

    poisson_placement_1.nodes["Reroute.010"].width  = 14.5
    poisson_placement_1.nodes["Reroute.010"].height = 100.0

    poisson_placement_1.nodes["Reroute.011"].width  = 14.5
    poisson_placement_1.nodes["Reroute.011"].height = 100.0

    poisson_placement_1.nodes["Reroute.012"].width  = 14.5
    poisson_placement_1.nodes["Reroute.012"].height = 100.0

    poisson_placement_1.nodes["Reroute.013"].width  = 14.5
    poisson_placement_1.nodes["Reroute.013"].height = 100.0

    poisson_placement_1.nodes["Delete Geometry.002"].width  = 140.0
    poisson_placement_1.nodes["Delete Geometry.002"].height = 100.0

    poisson_placement_1.nodes["Compare.006"].width  = 140.0
    poisson_placement_1.nodes["Compare.006"].height = 100.0

    poisson_placement_1.nodes["Geometry Proximity.002"].width  = 140.0
    poisson_placement_1.nodes["Geometry Proximity.002"].height = 100.0

    poisson_placement_1.nodes["Vector Math.003"].width  = 140.0
    poisson_placement_1.nodes["Vector Math.003"].height = 100.0

    poisson_placement_1.nodes["Frame.003"].width  = 566.0
    poisson_placement_1.nodes["Frame.003"].height = 138.20001220703125

    poisson_placement_1.nodes["Group.003"].width  = 205.1318359375
    poisson_placement_1.nodes["Group.003"].height = 100.0

    poisson_placement_1.nodes["Group.004"].width  = 205.1318359375
    poisson_placement_1.nodes["Group.004"].height = 100.0

    poisson_placement_1.nodes["Delete Geometry.003"].width  = 140.0
    poisson_placement_1.nodes["Delete Geometry.003"].height = 100.0

    poisson_placement_1.nodes["Compare.007"].width  = 140.0
    poisson_placement_1.nodes["Compare.007"].height = 100.0

    poisson_placement_1.nodes["Geometry Proximity.003"].width  = 140.0
    poisson_placement_1.nodes["Geometry Proximity.003"].height = 100.0

    poisson_placement_1.nodes["Frame.004"].width  = 566.0
    poisson_placement_1.nodes["Frame.004"].height = 138.1999969482422

    poisson_placement_1.nodes["Vector Math.004"].width  = 140.0
    poisson_placement_1.nodes["Vector Math.004"].height = 100.0

    poisson_placement_1.nodes["Reroute.014"].width  = 14.5
    poisson_placement_1.nodes["Reroute.014"].height = 100.0

    poisson_placement_1.nodes["Reroute.015"].width  = 14.5
    poisson_placement_1.nodes["Reroute.015"].height = 100.0

    poisson_placement_1.nodes["Reroute.016"].width  = 14.5
    poisson_placement_1.nodes["Reroute.016"].height = 100.0

    poisson_placement_1.nodes["Reroute.017"].width  = 14.5
    poisson_placement_1.nodes["Reroute.017"].height = 100.0

    poisson_placement_1.nodes["Reroute.018"].width  = 14.5
    poisson_placement_1.nodes["Reroute.018"].height = 100.0

    poisson_placement_1.nodes["Reroute.019"].width  = 14.5
    poisson_placement_1.nodes["Reroute.019"].height = 100.0

    poisson_placement_1.nodes["Reroute.020"].width  = 14.5
    poisson_placement_1.nodes["Reroute.020"].height = 100.0

    poisson_placement_1.nodes["Reroute.021"].width  = 14.5
    poisson_placement_1.nodes["Reroute.021"].height = 100.0

    poisson_placement_1.nodes["Reroute.022"].width  = 14.5
    poisson_placement_1.nodes["Reroute.022"].height = 100.0

    poisson_placement_1.nodes["Reroute.023"].width  = 14.5
    poisson_placement_1.nodes["Reroute.023"].height = 100.0

    poisson_placement_1.nodes["Reroute.024"].width  = 14.5
    poisson_placement_1.nodes["Reroute.024"].height = 100.0

    poisson_placement_1.nodes["Reroute.025"].width  = 14.5
    poisson_placement_1.nodes["Reroute.025"].height = 100.0

    poisson_placement_1.nodes["Value"].width  = 140.0
    poisson_placement_1.nodes["Value"].height = 100.0

    poisson_placement_1.nodes["Reroute.026"].width  = 14.5
    poisson_placement_1.nodes["Reroute.026"].height = 100.0

    poisson_placement_1.nodes["Value.001"].width  = 140.0
    poisson_placement_1.nodes["Value.001"].height = 100.0

    poisson_placement_1.nodes["Reroute.029"].width  = 14.5
    poisson_placement_1.nodes["Reroute.029"].height = 100.0

    poisson_placement_1.nodes["Value.002"].width  = 140.0
    poisson_placement_1.nodes["Value.002"].height = 100.0

    poisson_placement_1.nodes["Reroute.030"].width  = 14.5
    poisson_placement_1.nodes["Reroute.030"].height = 100.0

    poisson_placement_1.nodes["Math.005"].width  = 140.0
    poisson_placement_1.nodes["Math.005"].height = 100.0

    poisson_placement_1.nodes["Reroute.027"].width  = 14.5
    poisson_placement_1.nodes["Reroute.027"].height = 100.0

    poisson_placement_1.nodes["Value.005"].width  = 140.0
    poisson_placement_1.nodes["Value.005"].height = 100.0

    poisson_placement_1.nodes["Math.006"].width  = 140.0
    poisson_placement_1.nodes["Math.006"].height = 100.0

    poisson_placement_1.nodes["Value.006"].width  = 140.0
    poisson_placement_1.nodes["Value.006"].height = 100.0

    poisson_placement_1.nodes["Math.007"].width  = 140.0
    poisson_placement_1.nodes["Math.007"].height = 100.0

    poisson_placement_1.nodes["Value.007"].width  = 140.0
    poisson_placement_1.nodes["Value.007"].height = 100.0

    poisson_placement_1.nodes["Reroute.028"].width  = 14.5
    poisson_placement_1.nodes["Reroute.028"].height = 100.0

    poisson_placement_1.nodes["Reroute.031"].width  = 14.5
    poisson_placement_1.nodes["Reroute.031"].height = 100.0

    poisson_placement_1.nodes["Reroute.033"].width  = 14.5
    poisson_placement_1.nodes["Reroute.033"].height = 100.0

    poisson_placement_1.nodes["Reroute.034"].width  = 14.5
    poisson_placement_1.nodes["Reroute.034"].height = 100.0

    poisson_placement_1.nodes["Reroute.035"].width  = 14.5
    poisson_placement_1.nodes["Reroute.035"].height = 100.0

    poisson_placement_1.nodes["Value.008"].width  = 140.0
    poisson_placement_1.nodes["Value.008"].height = 100.0

    poisson_placement_1.nodes["Math.008"].width  = 140.0
    poisson_placement_1.nodes["Math.008"].height = 100.0

    poisson_placement_1.nodes["Math.009"].width  = 140.0
    poisson_placement_1.nodes["Math.009"].height = 100.0

    poisson_placement_1.nodes["Math.010"].width  = 140.0
    poisson_placement_1.nodes["Math.010"].height = 100.0

    poisson_placement_1.nodes["Vector Math.005"].width  = 140.0
    poisson_placement_1.nodes["Vector Math.005"].height = 100.0

    poisson_placement_1.nodes["Vector Math.006"].width  = 140.0
    poisson_placement_1.nodes["Vector Math.006"].height = 100.0

    poisson_placement_1.nodes["Vector Math.007"].width  = 140.0
    poisson_placement_1.nodes["Vector Math.007"].height = 100.0

    poisson_placement_1.nodes["Vector Math.008"].width  = 140.0
    poisson_placement_1.nodes["Vector Math.008"].height = 100.0

    poisson_placement_1.nodes["Reroute.032"].width  = 14.5
    poisson_placement_1.nodes["Reroute.032"].height = 100.0

    poisson_placement_1.nodes["Viewer"].width  = 140.0
    poisson_placement_1.nodes["Viewer"].height = 100.0


    # Initialize poisson_placement_1 links

    # math_002.Value -> color_ramp.Factor
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.002"].outputs[0],
        poisson_placement_1.nodes["Color Ramp"].inputs[0]
    )
    # math_003.Value -> math_002.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.003"].outputs[0],
        poisson_placement_1.nodes["Math.002"].inputs[0]
    )
    # math_004.Value -> math_003.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.004"].outputs[0],
        poisson_placement_1.nodes["Math.003"].inputs[1]
    )
    # math.Value -> clamp.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math"].outputs[0],
        poisson_placement_1.nodes["Clamp"].inputs[0]
    )
    # reroute_009.Output -> math_004.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.009"].outputs[0],
        poisson_placement_1.nodes["Math.004"].inputs[0]
    )
    # group_input.Name -> named_attribute.Name
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group Input"].outputs[5],
        poisson_placement_1.nodes["Named Attribute"].inputs[0]
    )
    # reroute_001.Output -> math.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.001"].outputs[0],
        poisson_placement_1.nodes["Math"].inputs[1]
    )
    # group_input.Density Multiplier -> math_001.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group Input"].outputs[4],
        poisson_placement_1.nodes["Math.001"].inputs[0]
    )
    # group_input.Max Density -> reroute_001.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group Input"].outputs[3],
        poisson_placement_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_001.Output -> clamp.Max
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.001"].outputs[0],
        poisson_placement_1.nodes["Clamp"].inputs[2]
    )
    # reroute_015.Output -> reroute_002.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.015"].outputs[0],
        poisson_placement_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Seed -> reroute_004.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group Input"].outputs[1],
        poisson_placement_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_017.Output -> reroute_005.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.017"].outputs[0],
        poisson_placement_1.nodes["Reroute.005"].inputs[0]
    )
    # group_input.Distance Min -> reroute_006.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group Input"].outputs[2],
        poisson_placement_1.nodes["Reroute.006"].inputs[0]
    )
    # clamp.Result -> reroute_008.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Clamp"].outputs[0],
        poisson_placement_1.nodes["Reroute.008"].inputs[0]
    )
    # compare_005.Result -> delete_geometry_001.Selection
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Compare.005"].outputs[0],
        poisson_placement_1.nodes["Delete Geometry.001"].inputs[1]
    )
    # geometry_proximity_001.Distance -> compare_005.A
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Geometry Proximity.001"].outputs[1],
        poisson_placement_1.nodes["Compare.005"].inputs[0]
    )
    # reroute_007.Output -> math_002.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.007"].outputs[0],
        poisson_placement_1.nodes["Math.002"].inputs[1]
    )
    # reroute_018.Output -> reroute_007.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.018"].outputs[0],
        poisson_placement_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_016.Output -> reroute.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.016"].outputs[0],
        poisson_placement_1.nodes["Reroute"].inputs[0]
    )
    # group_input.Mesh -> reroute_003.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group Input"].outputs[0],
        poisson_placement_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_002.Output -> group_001.Seed
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.002"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[1]
    )
    # reroute.Output -> group_001.Mesh
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[0]
    )
    # reroute_013.Output -> group_001.Density Max
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.013"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[4]
    )
    # reroute_020.Output -> group_001.Density Factor
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.020"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[5]
    )
    # reroute_011.Output -> group_001.Density Map
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.011"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[3]
    )
    # group_001.Points -> geometry_proximity_001.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.001"].outputs[0],
        poisson_placement_1.nodes["Geometry Proximity.001"].inputs[0]
    )
    # group_002.Points -> delete_geometry_001.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.002"].outputs[0],
        poisson_placement_1.nodes["Delete Geometry.001"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Points
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Join Geometry"].outputs[0],
        poisson_placement_1.nodes["Group Output"].inputs[0]
    )
    # group_002.Euler Rotation -> vector_math_002.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.002"].outputs[1],
        poisson_placement_1.nodes["Vector Math.002"].inputs[1]
    )
    # group_001.Euler Rotation -> vector_math_002.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.001"].outputs[1],
        poisson_placement_1.nodes["Vector Math.002"].inputs[0]
    )
    # math_001.Value -> reroute_009.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.001"].outputs[0],
        poisson_placement_1.nodes["Reroute.009"].inputs[0]
    )
    # reroute_009.Output -> math.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.009"].outputs[0],
        poisson_placement_1.nodes["Math"].inputs[0]
    )
    # named_attribute.Attribute -> reroute_010.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Named Attribute"].outputs[0],
        poisson_placement_1.nodes["Reroute.010"].inputs[0]
    )
    # reroute_007.Output -> reroute_011.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.007"].outputs[0],
        poisson_placement_1.nodes["Reroute.011"].inputs[0]
    )
    # group_001.Points -> reroute_012.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.001"].outputs[0],
        poisson_placement_1.nodes["Reroute.012"].inputs[0]
    )
    # reroute_002.Output -> group_002.Seed
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.002"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[1]
    )
    # reroute.Output -> group_002.Mesh
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[0]
    )
    # reroute_011.Output -> group_002.Density Map
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.011"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[3]
    )
    # reroute_008.Output -> reroute_013.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.008"].outputs[0],
        poisson_placement_1.nodes["Reroute.013"].inputs[0]
    )
    # reroute_013.Output -> group_002.Density Max
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.013"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[4]
    )
    # compare_006.Result -> delete_geometry_002.Selection
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Compare.006"].outputs[0],
        poisson_placement_1.nodes["Delete Geometry.002"].inputs[1]
    )
    # geometry_proximity_002.Distance -> compare_006.A
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Geometry Proximity.002"].outputs[1],
        poisson_placement_1.nodes["Compare.006"].inputs[0]
    )
    # group_003.Points -> geometry_proximity_002.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.003"].outputs[0],
        poisson_placement_1.nodes["Geometry Proximity.002"].inputs[0]
    )
    # group_004.Points -> delete_geometry_002.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.004"].outputs[0],
        poisson_placement_1.nodes["Delete Geometry.002"].inputs[0]
    )
    # group_004.Euler Rotation -> vector_math_003.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.004"].outputs[1],
        poisson_placement_1.nodes["Vector Math.003"].inputs[1]
    )
    # group_003.Euler Rotation -> vector_math_003.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.003"].outputs[1],
        poisson_placement_1.nodes["Vector Math.003"].inputs[0]
    )
    # compare_007.Result -> delete_geometry_003.Selection
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Compare.007"].outputs[0],
        poisson_placement_1.nodes["Delete Geometry.003"].inputs[1]
    )
    # geometry_proximity_003.Distance -> compare_007.A
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Geometry Proximity.003"].outputs[1],
        poisson_placement_1.nodes["Compare.007"].inputs[0]
    )
    # group_002.Points -> geometry_proximity_003.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.002"].outputs[0],
        poisson_placement_1.nodes["Geometry Proximity.003"].inputs[0]
    )
    # group_003.Points -> delete_geometry_003.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.003"].outputs[0],
        poisson_placement_1.nodes["Delete Geometry.003"].inputs[0]
    )
    # delete_geometry_002.Geometry -> join_geometry.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Delete Geometry.002"].outputs[0],
        poisson_placement_1.nodes["Join Geometry"].inputs[0]
    )
    # vector_math_002.Vector -> vector_math_004.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Vector Math.002"].outputs[0],
        poisson_placement_1.nodes["Vector Math.004"].inputs[0]
    )
    # vector_math_003.Vector -> vector_math_004.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Vector Math.003"].outputs[0],
        poisson_placement_1.nodes["Vector Math.004"].inputs[1]
    )
    # reroute_014.Output -> group_output.Euler Rotations
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.014"].outputs[0],
        poisson_placement_1.nodes["Group Output"].inputs[1]
    )
    # vector_math_004.Vector -> reroute_014.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Vector Math.004"].outputs[0],
        poisson_placement_1.nodes["Reroute.014"].inputs[0]
    )
    # reroute_004.Output -> reroute_015.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.004"].outputs[0],
        poisson_placement_1.nodes["Reroute.015"].inputs[0]
    )
    # reroute_003.Output -> reroute_016.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.003"].outputs[0],
        poisson_placement_1.nodes["Reroute.016"].inputs[0]
    )
    # reroute_006.Output -> reroute_017.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.006"].outputs[0],
        poisson_placement_1.nodes["Reroute.017"].inputs[0]
    )
    # reroute_010.Output -> reroute_018.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.010"].outputs[0],
        poisson_placement_1.nodes["Reroute.018"].inputs[0]
    )
    # reroute_019.Output -> group_003.Density Max
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.019"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[4]
    )
    # reroute_008.Output -> reroute_019.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.008"].outputs[0],
        poisson_placement_1.nodes["Reroute.019"].inputs[0]
    )
    # reroute_019.Output -> group_004.Density Max
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.019"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[4]
    )
    # color_ramp.Color -> reroute_020.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Color Ramp"].outputs[0],
        poisson_placement_1.nodes["Reroute.020"].inputs[0]
    )
    # reroute_020.Output -> group_002.Density Factor
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.020"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[5]
    )
    # reroute_021.Output -> group_003.Density Factor
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.021"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[5]
    )
    # color_ramp.Color -> reroute_021.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Color Ramp"].outputs[0],
        poisson_placement_1.nodes["Reroute.021"].inputs[0]
    )
    # reroute_021.Output -> group_004.Density Factor
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.021"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[5]
    )
    # reroute_022.Output -> group_003.Mesh
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.022"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[0]
    )
    # reroute_016.Output -> reroute_022.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.016"].outputs[0],
        poisson_placement_1.nodes["Reroute.022"].inputs[0]
    )
    # reroute_023.Output -> group_003.Seed
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.023"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[1]
    )
    # reroute_015.Output -> reroute_023.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.015"].outputs[0],
        poisson_placement_1.nodes["Reroute.023"].inputs[0]
    )
    # reroute_005.Output -> group_001.Base Min Dist
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.005"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[2]
    )
    # reroute_027.Output -> group_002.Base Min Dist
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.027"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[2]
    )
    # reroute_028.Output -> group_003.Base Min Dist
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.028"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[2]
    )
    # reroute_017.Output -> reroute_024.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.017"].outputs[0],
        poisson_placement_1.nodes["Reroute.024"].inputs[0]
    )
    # reroute_025.Output -> group_003.Density Map
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.025"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[3]
    )
    # reroute_018.Output -> reroute_025.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.018"].outputs[0],
        poisson_placement_1.nodes["Reroute.025"].inputs[0]
    )
    # reroute_025.Output -> group_004.Density Map
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.025"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[3]
    )
    # reroute_031.Output -> group_004.Base Min Dist
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.031"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[2]
    )
    # reroute_023.Output -> group_004.Seed
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.023"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[1]
    )
    # reroute_022.Output -> group_004.Mesh
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.022"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[0]
    )
    # value.Value -> reroute_026.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value"].outputs[0],
        poisson_placement_1.nodes["Reroute.026"].inputs[0]
    )
    # value_001.Value -> reroute_029.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.001"].outputs[0],
        poisson_placement_1.nodes["Reroute.029"].inputs[0]
    )
    # reroute_029.Output -> group_002.Lower Bound
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.029"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[7]
    )
    # math_009.Value -> group_003.Upper Bound
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.009"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[6]
    )
    # math_010.Value -> group_004.Upper Bound
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.010"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[6]
    )
    # reroute_026.Output -> group_003.Lower Bound
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.026"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[7]
    )
    # math_008.Value -> group_002.Upper Bound
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.008"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[6]
    )
    # value_002.Value -> reroute_030.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.002"].outputs[0],
        poisson_placement_1.nodes["Reroute.030"].inputs[0]
    )
    # reroute_030.Output -> group_001.Lower Bound
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.030"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[7]
    )
    # reroute_005.Output -> reroute_027.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.005"].outputs[0],
        poisson_placement_1.nodes["Reroute.027"].inputs[0]
    )
    # reroute_027.Output -> math_005.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.027"].outputs[0],
        poisson_placement_1.nodes["Math.005"].inputs[1]
    )
    # value_005.Value -> math_005.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.005"].outputs[0],
        poisson_placement_1.nodes["Math.005"].inputs[0]
    )
    # value_005.Value -> group_001.Distance Multiplier
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.005"].outputs[0],
        poisson_placement_1.nodes["Group.001"].inputs[8]
    )
    # value_006.Value -> math_006.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.006"].outputs[0],
        poisson_placement_1.nodes["Math.006"].inputs[0]
    )
    # value_007.Value -> math_007.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.007"].outputs[0],
        poisson_placement_1.nodes["Math.007"].inputs[0]
    )
    # reroute_024.Output -> reroute_028.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.024"].outputs[0],
        poisson_placement_1.nodes["Reroute.028"].inputs[0]
    )
    # reroute_028.Output -> math_006.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.028"].outputs[0],
        poisson_placement_1.nodes["Math.006"].inputs[1]
    )
    # reroute_024.Output -> reroute_031.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.024"].outputs[0],
        poisson_placement_1.nodes["Reroute.031"].inputs[0]
    )
    # reroute_031.Output -> math_007.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.031"].outputs[0],
        poisson_placement_1.nodes["Math.007"].inputs[1]
    )
    # value_006.Value -> group_002.Distance Multiplier
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.006"].outputs[0],
        poisson_placement_1.nodes["Group.002"].inputs[8]
    )
    # value_007.Value -> group_003.Distance Multiplier
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.007"].outputs[0],
        poisson_placement_1.nodes["Group.003"].inputs[8]
    )
    # math_005.Value -> reroute_033.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.005"].outputs[0],
        poisson_placement_1.nodes["Reroute.033"].inputs[0]
    )
    # math_006.Value -> reroute_034.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.006"].outputs[0],
        poisson_placement_1.nodes["Reroute.034"].inputs[0]
    )
    # math_007.Value -> reroute_035.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Math.007"].outputs[0],
        poisson_placement_1.nodes["Reroute.035"].inputs[0]
    )
    # value_008.Value -> group_004.Distance Multiplier
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Value.008"].outputs[0],
        poisson_placement_1.nodes["Group.004"].inputs[8]
    )
    # reroute_033.Output -> compare_005.B
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.033"].outputs[0],
        poisson_placement_1.nodes["Compare.005"].inputs[1]
    )
    # reroute_034.Output -> compare_007.B
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.034"].outputs[0],
        poisson_placement_1.nodes["Compare.007"].inputs[1]
    )
    # reroute_035.Output -> compare_006.B
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.035"].outputs[0],
        poisson_placement_1.nodes["Compare.006"].inputs[1]
    )
    # reroute_030.Output -> math_008.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.030"].outputs[0],
        poisson_placement_1.nodes["Math.008"].inputs[0]
    )
    # reroute_029.Output -> math_009.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.029"].outputs[0],
        poisson_placement_1.nodes["Math.009"].inputs[0]
    )
    # reroute_026.Output -> math_010.Value
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.026"].outputs[0],
        poisson_placement_1.nodes["Math.010"].inputs[0]
    )
    # group_001.Normal -> vector_math_005.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.001"].outputs[2],
        poisson_placement_1.nodes["Vector Math.005"].inputs[0]
    )
    # group_002.Normal -> vector_math_005.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.002"].outputs[2],
        poisson_placement_1.nodes["Vector Math.005"].inputs[1]
    )
    # vector_math_005.Vector -> vector_math_007.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Vector Math.005"].outputs[0],
        poisson_placement_1.nodes["Vector Math.007"].inputs[0]
    )
    # group_003.Normal -> vector_math_008.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.003"].outputs[2],
        poisson_placement_1.nodes["Vector Math.008"].inputs[0]
    )
    # group_004.Normal -> vector_math_008.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.004"].outputs[2],
        poisson_placement_1.nodes["Vector Math.008"].inputs[1]
    )
    # vector_math_008.Vector -> vector_math_007.Vector
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Vector Math.008"].outputs[0],
        poisson_placement_1.nodes["Vector Math.007"].inputs[1]
    )
    # reroute_032.Output -> group_output.Normals
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.032"].outputs[0],
        poisson_placement_1.nodes["Group Output"].inputs[2]
    )
    # vector_math_007.Vector -> reroute_032.Input
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Vector Math.007"].outputs[0],
        poisson_placement_1.nodes["Reroute.032"].inputs[0]
    )
    # group_002.Points -> viewer.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Group.002"].outputs[0],
        poisson_placement_1.nodes["Viewer"].inputs[0]
    )
    # delete_geometry_003.Geometry -> join_geometry.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Delete Geometry.003"].outputs[0],
        poisson_placement_1.nodes["Join Geometry"].inputs[0]
    )
    # delete_geometry_001.Geometry -> join_geometry.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Delete Geometry.001"].outputs[0],
        poisson_placement_1.nodes["Join Geometry"].inputs[0]
    )
    # reroute_012.Output -> join_geometry.Geometry
    poisson_placement_1.links.new(
        poisson_placement_1.nodes["Reroute.012"].outputs[0],
        poisson_placement_1.nodes["Join Geometry"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return poisson_placement_1


def distribute_surface_points_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Distribute Surface Points node group"""
    distribute_surface_points_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Distribute Surface Points")

    distribute_surface_points_1.color_tag = 'NONE'
    distribute_surface_points_1.description = ""
    distribute_surface_points_1.default_group_node_width = 140
    distribute_surface_points_1.is_modifier = True
    distribute_surface_points_1.show_modifier_manage_panel = True

    # distribute_surface_points_1 interface

    # Socket Sensor Points
    sensor_points_socket = distribute_surface_points_1.interface.new_socket(name="Sensor Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_points_socket.attribute_domain = 'POINT'
    sensor_points_socket.default_input = 'VALUE'
    sensor_points_socket.structure_type = 'AUTO'

    # Socket Euler Rotations
    euler_rotations_socket = distribute_surface_points_1.interface.new_socket(name="Euler Rotations", in_out='OUTPUT', socket_type='NodeSocketVector')
    euler_rotations_socket.default_value = (0.0, 0.0, 0.0)
    euler_rotations_socket.min_value = -3.4028234663852886e+38
    euler_rotations_socket.max_value = 3.4028234663852886e+38
    euler_rotations_socket.subtype = 'NONE'
    euler_rotations_socket.attribute_domain = 'POINT'
    euler_rotations_socket.default_input = 'VALUE'
    euler_rotations_socket.structure_type = 'AUTO'

    # Socket Radii
    radii_socket = distribute_surface_points_1.interface.new_socket(name="Radii", in_out='OUTPUT', socket_type='NodeSocketFloat')
    radii_socket.default_value = 0.0
    radii_socket.min_value = -3.4028234663852886e+38
    radii_socket.max_value = 3.4028234663852886e+38
    radii_socket.subtype = 'NONE'
    radii_socket.attribute_domain = 'POINT'
    radii_socket.default_input = 'VALUE'
    radii_socket.structure_type = 'AUTO'

    # Socket Sampling Type
    sampling_type_socket = distribute_surface_points_1.interface.new_socket(name="Sampling Type", in_out='INPUT', socket_type='NodeSocketMenu')
    sampling_type_socket.attribute_domain = 'POINT'
    sampling_type_socket.default_input = 'VALUE'
    sampling_type_socket.structure_type = 'AUTO'
    sampling_type_socket.optional_label = True

    # Socket Max Density
    max_density_socket = distribute_surface_points_1.interface.new_socket(name="Max Density", in_out='INPUT', socket_type='NodeSocketFloat')
    max_density_socket.default_value = 0.0
    max_density_socket.min_value = -3.4028234663852886e+38
    max_density_socket.max_value = 3.4028234663852886e+38
    max_density_socket.subtype = 'NONE'
    max_density_socket.attribute_domain = 'POINT'
    max_density_socket.default_input = 'VALUE'
    max_density_socket.structure_type = 'AUTO'

    # Socket Dermis Top Cut
    dermis_top_cut_socket = distribute_surface_points_1.interface.new_socket(name="Dermis Top Cut", in_out='INPUT', socket_type='NodeSocketGeometry')
    dermis_top_cut_socket.attribute_domain = 'POINT'
    dermis_top_cut_socket.default_input = 'VALUE'
    dermis_top_cut_socket.structure_type = 'AUTO'

    # Socket Min Distance
    min_distance_socket = distribute_surface_points_1.interface.new_socket(name="Min Distance", in_out='INPUT', socket_type='NodeSocketFloat')
    min_distance_socket.default_value = 0.019999999552965164
    min_distance_socket.min_value = 0.0
    min_distance_socket.max_value = 3.4028234663852886e+38
    min_distance_socket.subtype = 'DISTANCE'
    min_distance_socket.attribute_domain = 'POINT'
    min_distance_socket.description = "Minimum placement distance between sensors"
    min_distance_socket.default_input = 'VALUE'
    min_distance_socket.structure_type = 'AUTO'

    # Socket Density Multiplier
    density_multiplier_socket = distribute_surface_points_1.interface.new_socket(name="Density Multiplier", in_out='INPUT', socket_type='NodeSocketFloat')
    density_multiplier_socket.default_value = 50.0
    density_multiplier_socket.min_value = 0.0
    density_multiplier_socket.max_value = 100.0
    density_multiplier_socket.subtype = 'PERCENTAGE'
    density_multiplier_socket.attribute_domain = 'POINT'
    density_multiplier_socket.default_input = 'VALUE'
    density_multiplier_socket.structure_type = 'AUTO'

    # Socket Overlap
    overlap_socket = distribute_surface_points_1.interface.new_socket(name="Overlap", in_out='INPUT', socket_type='NodeSocketFloat')
    overlap_socket.default_value = 1.0
    overlap_socket.min_value = -10000.0
    overlap_socket.max_value = 10000.0
    overlap_socket.subtype = 'NONE'
    overlap_socket.attribute_domain = 'POINT'
    overlap_socket.default_input = 'VALUE'
    overlap_socket.structure_type = 'AUTO'

    # Socket Density Paint
    density_paint_socket = distribute_surface_points_1.interface.new_socket(name="Density Paint", in_out='INPUT', socket_type='NodeSocketString')
    density_paint_socket.default_value = "Group"
    density_paint_socket.subtype = 'NONE'
    density_paint_socket.default_attribute_name = "Point>Group"
    density_paint_socket.attribute_domain = 'POINT'
    density_paint_socket.hide_value = True
    density_paint_socket.default_input = 'VALUE'
    density_paint_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = distribute_surface_points_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket.default_value = 128
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Initialize distribute_surface_points_1 nodes

    # Node Frame.001
    frame_001 = distribute_surface_points_1.nodes.new("NodeFrame")
    frame_001.label = "Store Sensor Positions"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.2452997863292694, 0.4419439136981964, 0.2922254502773285)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Frame.003
    frame_003 = distribute_surface_points_1.nodes.new("NodeFrame")
    frame_003.label = "Radius Calculation and View"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.6079999804496765, 0.20478303730487823, 0.21565717458724976)
    frame_003.show_options = True
    frame_003.label_size = 13
    frame_003.shrink = False

    # Node Frame.002
    frame_002 = distribute_surface_points_1.nodes.new("NodeFrame")
    frame_002.label = "Store Radius Data"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.2904207408428192, 0.6079999804496765, 0.33591747283935547)
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = False

    # Node Frame
    frame = distribute_surface_points_1.nodes.new("NodeFrame")
    frame.label = "Poisson Sensor Distribution Option"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.374528169631958, 0.20898117125034332, 0.33026742935180664)
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.005
    frame_005 = distribute_surface_points_1.nodes.new("NodeFrame")
    frame_005.label = "Radius Spheres (Optional)"
    frame_005.name = "Frame.005"
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Frame.007
    frame_007 = distribute_surface_points_1.nodes.new("NodeFrame")
    frame_007.label = "Sensor Positions as Vertices"
    frame_007.name = "Frame.007"
    frame_007.show_options = True
    frame_007.label_size = 20
    frame_007.shrink = True

    # Node Store Named Attribute
    store_named_attribute = distribute_surface_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT_VECTOR'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True

    # Node Position.002
    position_002 = distribute_surface_points_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node String
    string = distribute_surface_points_1.nodes.new("FunctionNodeInputString")
    string.name = "String"
    string.show_options = True
    string.string = "sensor_pos"

    # Node Reroute
    reroute = distribute_surface_points_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketVector"
    # Node Reroute.001
    reroute_001 = distribute_surface_points_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Group Output
    group_output = distribute_surface_points_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input.001
    group_input_001 = distribute_surface_points_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Group Input
    group_input = distribute_surface_points_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group
    group = distribute_surface_points_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[sub_sensor_visual_1_node_group]]
    # Socket_6
    group.inputs[4].default_value = True

    # Node Store Named Attribute.002
    store_named_attribute_002 = distribute_surface_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'FLOAT'
    store_named_attribute_002.domain = 'POINT'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "radii"

    # Node Store Named Attribute.003
    store_named_attribute_003 = distribute_surface_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.show_options = True
    store_named_attribute_003.data_type = 'BOOLEAN'
    store_named_attribute_003.domain = 'POINT'
    # Selection
    store_named_attribute_003.inputs[1].default_value = True
    # Name
    store_named_attribute_003.inputs[2].default_value = "is_sensor"
    # Value
    store_named_attribute_003.inputs[3].default_value = True

    # Node Frame.009
    frame_009 = distribute_surface_points_1.nodes.new("NodeFrame")
    frame_009.label = "Random Distribution Option"
    frame_009.name = "Frame.009"
    frame_009.use_custom_color = True
    frame_009.color = (0.374528169631958, 0.14459507167339325, 0.10789040476083755)
    frame_009.show_options = True
    frame_009.label_size = 20
    frame_009.shrink = True

    # Node Distribute Points on Faces.001
    distribute_points_on_faces_001 = distribute_surface_points_1.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces_001.name = "Distribute Points on Faces.001"
    distribute_points_on_faces_001.show_options = True
    distribute_points_on_faces_001.distribute_method = 'RANDOM'
    distribute_points_on_faces_001.use_legacy_normal = False
    # Selection
    distribute_points_on_faces_001.inputs[1].default_value = True

    # Node Group Input.003
    group_input_003 = distribute_surface_points_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.show_options = True

    # Node Math.007
    math_007 = distribute_surface_points_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.hide = True
    math_007.show_options = True
    math_007.operation = 'DIVIDE'
    math_007.use_clamp = False
    # Value_001
    math_007.inputs[1].default_value = 100.0

    # Node Named Attribute.001
    named_attribute_001 = distribute_surface_points_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'FLOAT'

    # Node Rotation to Euler.001
    rotation_to_euler_001 = distribute_surface_points_1.nodes.new("FunctionNodeRotationToEuler")
    rotation_to_euler_001.name = "Rotation to Euler.001"
    rotation_to_euler_001.show_options = True

    # Node Reroute.010
    reroute_010 = distribute_surface_points_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketFloat"
    # Node Switch.002
    switch_002 = distribute_surface_points_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.show_options = True
    switch_002.input_type = 'GEOMETRY'

    # Node Switch.003
    switch_003 = distribute_surface_points_1.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.show_options = True
    switch_003.input_type = 'VECTOR'

    # Node Reroute.011
    reroute_011 = distribute_surface_points_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketGeometry"
    # Node Math.006
    math_006 = distribute_surface_points_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.hide = True
    math_006.show_options = True
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False

    # Node Math.008
    math_008 = distribute_surface_points_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.show_options = True
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False

    # Node Reroute.013
    reroute_013 = distribute_surface_points_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketBool"
    # Node Group.001
    group_001 = distribute_surface_points_1.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.show_options = True
    group_001.node_tree = bpy.data.node_groups[node_tree_names[poisson_placement_1_node_group]]

    # Node Store Named Attribute.004
    store_named_attribute_004 = distribute_surface_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_004.name = "Store Named Attribute.004"
    store_named_attribute_004.show_options = True
    store_named_attribute_004.data_type = 'FLOAT_VECTOR'
    store_named_attribute_004.domain = 'POINT'
    # Selection
    store_named_attribute_004.inputs[1].default_value = True

    # Node String.002
    string_002 = distribute_surface_points_1.nodes.new("FunctionNodeInputString")
    string_002.name = "String.002"
    string_002.show_options = True
    string_002.string = "sensor_normal"

    # Node Frame.013
    frame_013 = distribute_surface_points_1.nodes.new("NodeFrame")
    frame_013.label = "Save Normals"
    frame_013.name = "Frame.013"
    frame_013.show_options = True
    frame_013.label_size = 20
    frame_013.shrink = True

    # Node Viewer.001
    viewer_001 = distribute_surface_points_1.nodes.new("GeometryNodeViewer")
    viewer_001.name = "Viewer.001"
    viewer_001.show_options = True
    viewer_001.active_index = 0
    viewer_001.domain = 'AUTO'
    viewer_001.ui_shortcut = 0
    viewer_001.viewer_items.clear()
    viewer_001.viewer_items.new('GEOMETRY', "Geometry")
    viewer_001.viewer_items.new('FLOAT', "Value")
    # Value
    viewer_001.inputs[1].default_value = 0.0

    # Node Store Named Attribute.005
    store_named_attribute_005 = distribute_surface_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_005.name = "Store Named Attribute.005"
    store_named_attribute_005.show_options = True
    store_named_attribute_005.data_type = 'FLOAT_VECTOR'
    store_named_attribute_005.domain = 'POINT'
    # Selection
    store_named_attribute_005.inputs[1].default_value = True
    # Name
    store_named_attribute_005.inputs[2].default_value = "sensor_rpy"

    # Node Set Point Radius
    set_point_radius = distribute_surface_points_1.nodes.new("GeometryNodeSetPointRadius")
    set_point_radius.name = "Set Point Radius"
    set_point_radius.show_options = True
    # Selection
    set_point_radius.inputs[1].default_value = True
    # Radius
    set_point_radius.inputs[2].default_value = 0.0010000000474974513

    # Node Menu Switch
    menu_switch = distribute_surface_points_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.show_options = True
    menu_switch.active_index = 1
    menu_switch.data_type = 'BOOLEAN'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Poisson Disk")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Random")
    menu_switch.enum_items[1].description = ""
    # Item_0
    menu_switch.inputs[1].default_value = True
    # Item_1
    menu_switch.inputs[2].default_value = False

    # Set parents
    distribute_surface_points_1.nodes["Store Named Attribute"].parent = distribute_surface_points_1.nodes["Frame.001"]
    distribute_surface_points_1.nodes["Position.002"].parent = distribute_surface_points_1.nodes["Frame.001"]
    distribute_surface_points_1.nodes["String"].parent = distribute_surface_points_1.nodes["Frame.001"]
    distribute_surface_points_1.nodes["Group Input"].parent = distribute_surface_points_1.nodes["Frame"]
    distribute_surface_points_1.nodes["Group"].parent = distribute_surface_points_1.nodes["Frame.003"]
    distribute_surface_points_1.nodes["Store Named Attribute.002"].parent = distribute_surface_points_1.nodes["Frame.002"]
    distribute_surface_points_1.nodes["Store Named Attribute.003"].parent = distribute_surface_points_1.nodes["Frame.002"]
    distribute_surface_points_1.nodes["Distribute Points on Faces.001"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Group Input.003"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Math.007"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Named Attribute.001"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Rotation to Euler.001"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Reroute.010"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Math.006"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Math.008"].parent = distribute_surface_points_1.nodes["Frame.009"]
    distribute_surface_points_1.nodes["Group.001"].parent = distribute_surface_points_1.nodes["Frame"]
    distribute_surface_points_1.nodes["Store Named Attribute.004"].parent = distribute_surface_points_1.nodes["Frame.013"]
    distribute_surface_points_1.nodes["String.002"].parent = distribute_surface_points_1.nodes["Frame.013"]

    # Set locations
    distribute_surface_points_1.nodes["Frame.001"].location = (372.7742004394531, 485.6129150390625)
    distribute_surface_points_1.nodes["Frame.003"].location = (1340.0, 320.5)
    distribute_surface_points_1.nodes["Frame.002"].location = (1609.5, 743.5870971679688)
    distribute_surface_points_1.nodes["Frame"].location = (-2394.193603515625, -24.580646514892578)
    distribute_surface_points_1.nodes["Frame.005"].location = (2356.520751953125, 347.3067321777344)
    distribute_surface_points_1.nodes["Frame.007"].location = (2505.079833984375, 513.4829711914062)
    distribute_surface_points_1.nodes["Store Named Attribute"].location = (200.42648315429688, -35.77679443359375)
    distribute_surface_points_1.nodes["Position.002"].location = (28.908660888671875, -276.8806457519531)
    distribute_surface_points_1.nodes["String"].location = (29.2125244140625, -188.815185546875)
    distribute_surface_points_1.nodes["Reroute"].location = (411.4287109375, -476.6747131347656)
    distribute_surface_points_1.nodes["Reroute.001"].location = (1306.0411376953125, 418.57098388671875)
    distribute_surface_points_1.nodes["Group Output"].location = (2420.0, -80.0)
    distribute_surface_points_1.nodes["Group Input.001"].location = (640.0, 40.0)
    distribute_surface_points_1.nodes["Group Input"].location = (28.817626953125, -73.26641845703125)
    distribute_surface_points_1.nodes["Group"].location = (30.0, -49.776611328125)
    distribute_surface_points_1.nodes["Store Named Attribute.002"].location = (30.00634765625, -72.522216796875)
    distribute_surface_points_1.nodes["Store Named Attribute.003"].location = (268.591064453125, -79.1868896484375)
    distribute_surface_points_1.nodes["Frame.009"].location = (-2386.45166015625, -633.8709716796875)
    distribute_surface_points_1.nodes["Distribute Points on Faces.001"].location = (1374.1826171875, -35.7049560546875)
    distribute_surface_points_1.nodes["Group Input.003"].location = (28.9287109375, -159.095947265625)
    distribute_surface_points_1.nodes["Math.007"].location = (206.45166015625, -266.1290283203125)
    distribute_surface_points_1.nodes["Named Attribute.001"].location = (413.2091064453125, -510.853271484375)
    distribute_surface_points_1.nodes["Rotation to Euler.001"].location = (1577.17822265625, -93.22613525390625)
    distribute_surface_points_1.nodes["Reroute.010"].location = (795.689697265625, -513.845947265625)
    distribute_surface_points_1.nodes["Switch.002"].location = (-479.53729248046875, -313.0189514160156)
    distribute_surface_points_1.nodes["Switch.003"].location = (-480.0, -500.0)
    distribute_surface_points_1.nodes["Reroute.011"].location = (-302.1346435546875, 91.88330841064453)
    distribute_surface_points_1.nodes["Math.006"].location = (919.84375, -395.4788818359375)
    distribute_surface_points_1.nodes["Math.008"].location = (1103.3856201171875, -245.6005859375)
    distribute_surface_points_1.nodes["Reroute.013"].location = (-837.2044067382812, -619.3040161132812)
    distribute_surface_points_1.nodes["Group.001"].location = (594.193603515625, -35.41935348510742)
    distribute_surface_points_1.nodes["Store Named Attribute.004"].location = (273.867431640625, -35.71661376953125)
    distribute_surface_points_1.nodes["String.002"].location = (29.2606201171875, -239.256591796875)
    distribute_surface_points_1.nodes["Frame.013"].location = (-1347.48388671875, -105.8709716796875)
    distribute_surface_points_1.nodes["Viewer.001"].location = (-688.6666870117188, -33.33333206176758)
    distribute_surface_points_1.nodes["Store Named Attribute.005"].location = (-855.1258544921875, -154.55775451660156)
    distribute_surface_points_1.nodes["Set Point Radius"].location = (1880.0, 880.0)
    distribute_surface_points_1.nodes["Menu Switch"].location = (-1320.0, -440.0)

    # Set dimensions
    distribute_surface_points_1.nodes["Frame.001"].width  = 369.1612854003906
    distribute_surface_points_1.nodes["Frame.001"].height = 353.6129150390625

    distribute_surface_points_1.nodes["Frame.003"].width  = 438.0
    distribute_surface_points_1.nodes["Frame.003"].height = 286.9110412597656

    distribute_surface_points_1.nodes["Frame.002"].width  = 677.694091796875
    distribute_surface_points_1.nodes["Frame.002"].height = 385.1257629394531

    distribute_surface_points_1.nodes["Frame"].width  = 803.225830078125
    distribute_surface_points_1.nodes["Frame"].height = 324.9677429199219

    distribute_surface_points_1.nodes["Frame.005"].width  = 273.5859375
    distribute_surface_points_1.nodes["Frame.005"].height = 44.999908447265625

    distribute_surface_points_1.nodes["Frame.007"].width  = 293.73046875
    distribute_surface_points_1.nodes["Frame.007"].height = 44.999969482421875

    distribute_surface_points_1.nodes["Store Named Attribute"].width  = 140.0
    distribute_surface_points_1.nodes["Store Named Attribute"].height = 100.0

    distribute_surface_points_1.nodes["Position.002"].width  = 140.0
    distribute_surface_points_1.nodes["Position.002"].height = 100.0

    distribute_surface_points_1.nodes["String"].width  = 140.0
    distribute_surface_points_1.nodes["String"].height = 100.0

    distribute_surface_points_1.nodes["Reroute"].width  = 12.5
    distribute_surface_points_1.nodes["Reroute"].height = 100.0

    distribute_surface_points_1.nodes["Reroute.001"].width  = 12.5
    distribute_surface_points_1.nodes["Reroute.001"].height = 100.0

    distribute_surface_points_1.nodes["Group Output"].width  = 140.0
    distribute_surface_points_1.nodes["Group Output"].height = 100.0

    distribute_surface_points_1.nodes["Group Input.001"].width  = 140.0
    distribute_surface_points_1.nodes["Group Input.001"].height = 100.0

    distribute_surface_points_1.nodes["Group Input"].width  = 140.0
    distribute_surface_points_1.nodes["Group Input"].height = 100.0

    distribute_surface_points_1.nodes["Group"].width  = 200.0
    distribute_surface_points_1.nodes["Group"].height = 100.0

    distribute_surface_points_1.nodes["Store Named Attribute.002"].width  = 140.0
    distribute_surface_points_1.nodes["Store Named Attribute.002"].height = 100.0

    distribute_surface_points_1.nodes["Store Named Attribute.003"].width  = 140.0
    distribute_surface_points_1.nodes["Store Named Attribute.003"].height = 100.0

    distribute_surface_points_1.nodes["Frame.009"].width  = 1746.45166015625
    distribute_surface_points_1.nodes["Frame.009"].height = 657.0968017578125

    distribute_surface_points_1.nodes["Distribute Points on Faces.001"].width  = 170.0
    distribute_surface_points_1.nodes["Distribute Points on Faces.001"].height = 100.0

    distribute_surface_points_1.nodes["Group Input.003"].width  = 140.0
    distribute_surface_points_1.nodes["Group Input.003"].height = 100.0

    distribute_surface_points_1.nodes["Math.007"].width  = 140.0
    distribute_surface_points_1.nodes["Math.007"].height = 100.0

    distribute_surface_points_1.nodes["Named Attribute.001"].width  = 140.0
    distribute_surface_points_1.nodes["Named Attribute.001"].height = 100.0

    distribute_surface_points_1.nodes["Rotation to Euler.001"].width  = 140.0
    distribute_surface_points_1.nodes["Rotation to Euler.001"].height = 100.0

    distribute_surface_points_1.nodes["Reroute.010"].width  = 12.5
    distribute_surface_points_1.nodes["Reroute.010"].height = 100.0

    distribute_surface_points_1.nodes["Switch.002"].width  = 140.0
    distribute_surface_points_1.nodes["Switch.002"].height = 100.0

    distribute_surface_points_1.nodes["Switch.003"].width  = 140.0
    distribute_surface_points_1.nodes["Switch.003"].height = 100.0

    distribute_surface_points_1.nodes["Reroute.011"].width  = 12.5
    distribute_surface_points_1.nodes["Reroute.011"].height = 100.0

    distribute_surface_points_1.nodes["Math.006"].width  = 140.0
    distribute_surface_points_1.nodes["Math.006"].height = 100.0

    distribute_surface_points_1.nodes["Math.008"].width  = 140.0
    distribute_surface_points_1.nodes["Math.008"].height = 100.0

    distribute_surface_points_1.nodes["Reroute.013"].width  = 12.5
    distribute_surface_points_1.nodes["Reroute.013"].height = 100.0

    distribute_surface_points_1.nodes["Group.001"].width  = 180.0
    distribute_surface_points_1.nodes["Group.001"].height = 100.0

    distribute_surface_points_1.nodes["Store Named Attribute.004"].width  = 140.0
    distribute_surface_points_1.nodes["Store Named Attribute.004"].height = 100.0

    distribute_surface_points_1.nodes["String.002"].width  = 140.0
    distribute_surface_points_1.nodes["String.002"].height = 100.0

    distribute_surface_points_1.nodes["Frame.013"].width  = 442.709716796875
    distribute_surface_points_1.nodes["Frame.013"].height = 316.4516296386719

    distribute_surface_points_1.nodes["Viewer.001"].width  = 140.0
    distribute_surface_points_1.nodes["Viewer.001"].height = 100.0

    distribute_surface_points_1.nodes["Store Named Attribute.005"].width  = 140.0
    distribute_surface_points_1.nodes["Store Named Attribute.005"].height = 100.0

    distribute_surface_points_1.nodes["Set Point Radius"].width  = 140.0
    distribute_surface_points_1.nodes["Set Point Radius"].height = 100.0

    distribute_surface_points_1.nodes["Menu Switch"].width  = 140.0
    distribute_surface_points_1.nodes["Menu Switch"].height = 100.0


    # Initialize distribute_surface_points_1 links

    # reroute_011.Output -> store_named_attribute.Geometry
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Reroute.011"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute"].inputs[0]
    )
    # string.String -> store_named_attribute.Name
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["String"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute"].inputs[2]
    )
    # position_002.Position -> store_named_attribute.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Position.002"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute"].inputs[3]
    )
    # group_input_001.Dermis Top Cut -> group.Geometry
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.001"].outputs[2],
        distribute_surface_points_1.nodes["Group"].inputs[1]
    )
    # group_input_001.Overlap -> group.Overlap
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.001"].outputs[5],
        distribute_surface_points_1.nodes["Group"].inputs[3]
    )
    # group.Radii -> store_named_attribute_002.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group"].outputs[1],
        distribute_surface_points_1.nodes["Store Named Attribute.002"].inputs[3]
    )
    # reroute_001.Output -> group.Points
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Reroute.001"].outputs[0],
        distribute_surface_points_1.nodes["Group"].inputs[0]
    )
    # store_named_attribute_002.Geometry -> store_named_attribute_003.Geometry
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Store Named Attribute.002"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute.003"].inputs[0]
    )
    # group_input_003.Seed -> distribute_points_on_faces_001.Seed
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.003"].outputs[7],
        distribute_surface_points_1.nodes["Distribute Points on Faces.001"].inputs[6]
    )
    # group_input_003.Density Paint -> named_attribute_001.Name
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.003"].outputs[6],
        distribute_surface_points_1.nodes["Named Attribute.001"].inputs[0]
    )
    # group_input_003.Density Multiplier -> math_007.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.003"].outputs[4],
        distribute_surface_points_1.nodes["Math.007"].inputs[0]
    )
    # distribute_points_on_faces_001.Rotation -> rotation_to_euler_001.Rotation
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Distribute Points on Faces.001"].outputs[2],
        distribute_surface_points_1.nodes["Rotation to Euler.001"].inputs[0]
    )
    # named_attribute_001.Attribute -> reroute_010.Input
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Named Attribute.001"].outputs[0],
        distribute_surface_points_1.nodes["Reroute.010"].inputs[0]
    )
    # group_input_003.Min Distance -> distribute_points_on_faces_001.Distance Min
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.003"].outputs[3],
        distribute_surface_points_1.nodes["Distribute Points on Faces.001"].inputs[2]
    )
    # switch_002.Output -> reroute_011.Input
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Switch.002"].outputs[0],
        distribute_surface_points_1.nodes["Reroute.011"].inputs[0]
    )
    # switch_003.Output -> reroute.Input
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Switch.003"].outputs[0],
        distribute_surface_points_1.nodes["Reroute"].inputs[0]
    )
    # math_007.Value -> math_006.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Math.007"].outputs[0],
        distribute_surface_points_1.nodes["Math.006"].inputs[0]
    )
    # reroute_010.Output -> math_006.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Reroute.010"].outputs[0],
        distribute_surface_points_1.nodes["Math.006"].inputs[1]
    )
    # math_006.Value -> math_008.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Math.006"].outputs[0],
        distribute_surface_points_1.nodes["Math.008"].inputs[1]
    )
    # math_008.Value -> distribute_points_on_faces_001.Density
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Math.008"].outputs[0],
        distribute_surface_points_1.nodes["Distribute Points on Faces.001"].inputs[4]
    )
    # reroute_013.Output -> switch_003.Switch
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Reroute.013"].outputs[0],
        distribute_surface_points_1.nodes["Switch.003"].inputs[0]
    )
    # reroute_013.Output -> switch_002.Switch
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Reroute.013"].outputs[0],
        distribute_surface_points_1.nodes["Switch.002"].inputs[0]
    )
    # distribute_points_on_faces_001.Points -> switch_002.False
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Distribute Points on Faces.001"].outputs[0],
        distribute_surface_points_1.nodes["Switch.002"].inputs[1]
    )
    # rotation_to_euler_001.Euler -> switch_003.False
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Rotation to Euler.001"].outputs[0],
        distribute_surface_points_1.nodes["Switch.003"].inputs[1]
    )
    # group_001.Euler Rotations -> switch_003.True
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group.001"].outputs[1],
        distribute_surface_points_1.nodes["Switch.003"].inputs[2]
    )
    # group_input_003.Max Density -> math_008.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.003"].outputs[1],
        distribute_surface_points_1.nodes["Math.008"].inputs[0]
    )
    # group_input.Density Paint -> group_001.Name
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input"].outputs[6],
        distribute_surface_points_1.nodes["Group.001"].inputs[5]
    )
    # group_input.Max Density -> group_001.Max Density
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input"].outputs[1],
        distribute_surface_points_1.nodes["Group.001"].inputs[3]
    )
    # group_input.Seed -> group_001.Seed
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input"].outputs[7],
        distribute_surface_points_1.nodes["Group.001"].inputs[1]
    )
    # group_input.Density Multiplier -> group_001.Density Multiplier
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input"].outputs[4],
        distribute_surface_points_1.nodes["Group.001"].inputs[4]
    )
    # reroute_001.Output -> store_named_attribute_002.Geometry
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Reroute.001"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # store_named_attribute.Geometry -> reroute_001.Input
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Store Named Attribute"].outputs[0],
        distribute_surface_points_1.nodes["Reroute.001"].inputs[0]
    )
    # store_named_attribute_005.Geometry -> switch_002.True
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Store Named Attribute.005"].outputs[0],
        distribute_surface_points_1.nodes["Switch.002"].inputs[2]
    )
    # group_001.Points -> store_named_attribute_004.Geometry
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group.001"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute.004"].inputs[0]
    )
    # group_001.Normals -> store_named_attribute_004.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group.001"].outputs[2],
        distribute_surface_points_1.nodes["Store Named Attribute.004"].inputs[3]
    )
    # string_002.String -> store_named_attribute_004.Name
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["String.002"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute.004"].inputs[2]
    )
    # store_named_attribute_004.Geometry -> store_named_attribute_005.Geometry
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Store Named Attribute.004"].outputs[0],
        distribute_surface_points_1.nodes["Store Named Attribute.005"].inputs[0]
    )
    # group_001.Euler Rotations -> store_named_attribute_005.Value
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group.001"].outputs[1],
        distribute_surface_points_1.nodes["Store Named Attribute.005"].inputs[3]
    )
    # store_named_attribute_002.Geometry -> set_point_radius.Points
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Store Named Attribute.002"].outputs[0],
        distribute_surface_points_1.nodes["Set Point Radius"].inputs[0]
    )
    # store_named_attribute_005.Geometry -> viewer_001.Geometry
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Store Named Attribute.005"].outputs[0],
        distribute_surface_points_1.nodes["Viewer.001"].inputs[0]
    )
    # store_named_attribute_003.Geometry -> group_output.Sensor Points
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Store Named Attribute.003"].outputs[0],
        distribute_surface_points_1.nodes["Group Output"].inputs[0]
    )
    # reroute.Output -> group_output.Euler Rotations
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Reroute"].outputs[0],
        distribute_surface_points_1.nodes["Group Output"].inputs[1]
    )
    # menu_switch.Output -> reroute_013.Input
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Menu Switch"].outputs[0],
        distribute_surface_points_1.nodes["Reroute.013"].inputs[0]
    )
    # group_input_003.Sampling Type -> menu_switch.Menu
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.003"].outputs[0],
        distribute_surface_points_1.nodes["Menu Switch"].inputs[0]
    )
    # group_input_003.Dermis Top Cut -> distribute_points_on_faces_001.Mesh
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input.003"].outputs[2],
        distribute_surface_points_1.nodes["Distribute Points on Faces.001"].inputs[0]
    )
    # group_input.Dermis Top Cut -> group_001.Mesh
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input"].outputs[2],
        distribute_surface_points_1.nodes["Group.001"].inputs[0]
    )
    # group_input.Min Distance -> group_001.Distance Min
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group Input"].outputs[3],
        distribute_surface_points_1.nodes["Group.001"].inputs[2]
    )
    # group.Radii -> group_output.Radii
    distribute_surface_points_1.links.new(
        distribute_surface_points_1.nodes["Group"].outputs[1],
        distribute_surface_points_1.nodes["Group Output"].inputs[2]
    )
    sampling_type_socket.default_value = 'Poisson Disk'
    viewer_001.viewer_items[0].auto_remove = True
    viewer_001.viewer_items[1].auto_remove = False

    return distribute_surface_points_1


def custom_points_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Custom Points node group"""
    custom_points_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Custom Points")

    custom_points_1.color_tag = 'NONE'
    custom_points_1.description = ""
    custom_points_1.default_group_node_width = 140
    custom_points_1.show_modifier_manage_panel = True

    # custom_points_1 interface

    # Socket Selection
    selection_socket = custom_points_1.interface.new_socket(name="Selection", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    selection_socket.attribute_domain = 'POINT'
    selection_socket.description = "The parts of the geometry in the selection"
    selection_socket.default_input = 'VALUE'
    selection_socket.structure_type = 'AUTO'

    # Socket Instances
    instances_socket = custom_points_1.interface.new_socket(name="Instances", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    instances_socket.attribute_domain = 'POINT'
    instances_socket.default_input = 'VALUE'
    instances_socket.structure_type = 'AUTO'

    # Socket Sensor Points
    sensor_points_socket = custom_points_1.interface.new_socket(name="Sensor Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_points_socket.attribute_domain = 'POINT'
    sensor_points_socket.default_input = 'VALUE'
    sensor_points_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket = custom_points_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.description = "Geometry to split into two parts"
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Point Label
    point_label_socket = custom_points_1.interface.new_socket(name="Point Label", in_out='INPUT', socket_type='NodeSocketString')
    point_label_socket.default_value = ""
    point_label_socket.subtype = 'NONE'
    point_label_socket.attribute_domain = 'POINT'
    point_label_socket.default_input = 'VALUE'
    point_label_socket.structure_type = 'AUTO'
    point_label_socket.optional_label = True

    # Socket Offset
    offset_socket = custom_points_1.interface.new_socket(name="Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    offset_socket.default_value = 0.0
    offset_socket.min_value = 0.0
    offset_socket.max_value = 0.10000000149011612
    offset_socket.subtype = 'FACTOR'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'

    # Initialize custom_points_1 nodes

    # Node Group Output
    group_output = custom_points_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = custom_points_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Separate Geometry
    separate_geometry = custom_points_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.show_options = True
    separate_geometry.domain = 'POINT'

    # Node Named Attribute
    named_attribute = custom_points_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'BOOLEAN'

    # Node Join Geometry
    join_geometry = custom_points_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Viewer
    viewer = custom_points_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Mesh")

    # Node Mesh to Points
    mesh_to_points = custom_points_1.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points.name = "Mesh to Points"
    mesh_to_points.show_options = True
    mesh_to_points.mode = 'VERTICES'
    # Selection
    mesh_to_points.inputs[1].default_value = True
    # Position
    mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    mesh_to_points.inputs[3].default_value = 0.05000000074505806

    # Node Translate Instances
    translate_instances = custom_points_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances.name = "Translate Instances"
    translate_instances.show_options = True
    # Selection
    translate_instances.inputs[1].default_value = True
    # Local Space
    translate_instances.inputs[3].default_value = True

    # Node Instance on Points
    instance_on_points = custom_points_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node UV Sphere
    uv_sphere = custom_points_1.nodes.new("GeometryNodeMeshUVSphere")
    uv_sphere.name = "UV Sphere"
    uv_sphere.show_options = True
    # Segments
    uv_sphere.inputs[0].default_value = 32
    # Rings
    uv_sphere.inputs[1].default_value = 16
    # Radius
    uv_sphere.inputs[2].default_value = 0.009999999776482582

    # Node Combine XYZ
    combine_xyz = custom_points_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # Node Instances to Points
    instances_to_points = custom_points_1.nodes.new("GeometryNodeInstancesToPoints")
    instances_to_points.name = "Instances to Points"
    instances_to_points.show_options = True
    # Selection
    instances_to_points.inputs[1].default_value = True
    # Position
    instances_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    instances_to_points.inputs[3].default_value = 0.05000000074505806

    # Node Points to Vertices
    points_to_vertices = custom_points_1.nodes.new("GeometryNodePointsToVertices")
    points_to_vertices.name = "Points to Vertices"
    points_to_vertices.show_options = True
    # Selection
    points_to_vertices.inputs[1].default_value = True

    # Node Join Geometry.001
    join_geometry_001 = custom_points_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Reroute
    reroute = custom_points_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Named Attribute.001
    named_attribute_001 = custom_points_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'FLOAT_VECTOR'
    # Name
    named_attribute_001.inputs[0].default_value = "sensor_rpy"

    # Node Euler to Rotation
    euler_to_rotation = custom_points_1.nodes.new("FunctionNodeEulerToRotation")
    euler_to_rotation.name = "Euler to Rotation"
    euler_to_rotation.show_options = True

    # Node Sample Index
    sample_index = custom_points_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Index
    index = custom_points_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Reroute.001
    reroute_001 = custom_points_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Menu Switch
    menu_switch = custom_points_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.show_options = True
    menu_switch.active_index = 1
    menu_switch.data_type = 'GEOMETRY'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Sampling")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Custom")
    menu_switch.enum_items[1].description = ""
    # Menu
    menu_switch.inputs[0].default_value = 'Sampling'

    # Node Viewer.001
    viewer_001 = custom_points_1.nodes.new("GeometryNodeViewer")
    viewer_001.name = "Viewer.001"
    viewer_001.show_options = True
    viewer_001.active_index = 0
    viewer_001.domain = 'AUTO'
    viewer_001.ui_shortcut = 0
    viewer_001.viewer_items.clear()
    viewer_001.viewer_items.new('GEOMETRY', "Instances")

    # Node Viewer.002
    viewer_002 = custom_points_1.nodes.new("GeometryNodeViewer")
    viewer_002.name = "Viewer.002"
    viewer_002.show_options = True
    viewer_002.active_index = 0
    viewer_002.domain = 'AUTO'
    viewer_002.ui_shortcut = 0
    viewer_002.viewer_items.clear()
    viewer_002.viewer_items.new('GEOMETRY', "Inverted")

    # Node Viewer.003
    viewer_003 = custom_points_1.nodes.new("GeometryNodeViewer")
    viewer_003.name = "Viewer.003"
    viewer_003.show_options = True
    viewer_003.active_index = 0
    viewer_003.domain = 'AUTO'
    viewer_003.ui_shortcut = 0
    viewer_003.viewer_items.clear()

    # Set locations
    custom_points_1.nodes["Group Output"].location = (2100.0, 120.0)
    custom_points_1.nodes["Group Input"].location = (-290.0, 0.0)
    custom_points_1.nodes["Separate Geometry"].location = (100.0, 160.0)
    custom_points_1.nodes["Named Attribute"].location = (-100.0, 200.0)
    custom_points_1.nodes["Join Geometry"].location = (1720.0, -140.0)
    custom_points_1.nodes["Viewer"].location = (2060.0, -100.0)
    custom_points_1.nodes["Mesh to Points"].location = (300.0, 100.0)
    custom_points_1.nodes["Translate Instances"].location = (1180.0, 40.0)
    custom_points_1.nodes["Instance on Points"].location = (960.0, 240.0)
    custom_points_1.nodes["UV Sphere"].location = (300.0, 260.0)
    custom_points_1.nodes["Combine XYZ"].location = (920.0, -220.0)
    custom_points_1.nodes["Instances to Points"].location = (1360.0, -20.0)
    custom_points_1.nodes["Points to Vertices"].location = (1540.0, -60.0)
    custom_points_1.nodes["Join Geometry.001"].location = (1740.0, 80.0)
    custom_points_1.nodes["Reroute"].location = (1680.0, -180.0)
    custom_points_1.nodes["Named Attribute.001"].location = (300.0, -280.0)
    custom_points_1.nodes["Euler to Rotation"].location = (660.0, -220.0)
    custom_points_1.nodes["Sample Index"].location = (480.0, -220.0)
    custom_points_1.nodes["Index"].location = (280.0, -420.0)
    custom_points_1.nodes["Reroute.001"].location = (300.0, -140.0)
    custom_points_1.nodes["Menu Switch"].location = (2040.0, -300.0)
    custom_points_1.nodes["Viewer.001"].location = (1350.8387451171875, 122.32258605957031)
    custom_points_1.nodes["Viewer.002"].location = (300.0, 440.0)
    custom_points_1.nodes["Viewer.003"].location = (-100.0, 280.0)

    # Set dimensions
    custom_points_1.nodes["Group Output"].width  = 140.0
    custom_points_1.nodes["Group Output"].height = 100.0

    custom_points_1.nodes["Group Input"].width  = 140.0
    custom_points_1.nodes["Group Input"].height = 100.0

    custom_points_1.nodes["Separate Geometry"].width  = 140.0
    custom_points_1.nodes["Separate Geometry"].height = 100.0

    custom_points_1.nodes["Named Attribute"].width  = 140.0
    custom_points_1.nodes["Named Attribute"].height = 100.0

    custom_points_1.nodes["Join Geometry"].width  = 140.0
    custom_points_1.nodes["Join Geometry"].height = 100.0

    custom_points_1.nodes["Viewer"].width  = 140.0
    custom_points_1.nodes["Viewer"].height = 100.0

    custom_points_1.nodes["Mesh to Points"].width  = 140.0
    custom_points_1.nodes["Mesh to Points"].height = 100.0

    custom_points_1.nodes["Translate Instances"].width  = 140.0
    custom_points_1.nodes["Translate Instances"].height = 100.0

    custom_points_1.nodes["Instance on Points"].width  = 140.0
    custom_points_1.nodes["Instance on Points"].height = 100.0

    custom_points_1.nodes["UV Sphere"].width  = 140.0
    custom_points_1.nodes["UV Sphere"].height = 100.0

    custom_points_1.nodes["Combine XYZ"].width  = 140.0
    custom_points_1.nodes["Combine XYZ"].height = 100.0

    custom_points_1.nodes["Instances to Points"].width  = 140.0
    custom_points_1.nodes["Instances to Points"].height = 100.0

    custom_points_1.nodes["Points to Vertices"].width  = 140.0
    custom_points_1.nodes["Points to Vertices"].height = 100.0

    custom_points_1.nodes["Join Geometry.001"].width  = 140.0
    custom_points_1.nodes["Join Geometry.001"].height = 100.0

    custom_points_1.nodes["Reroute"].width  = 12.5
    custom_points_1.nodes["Reroute"].height = 100.0

    custom_points_1.nodes["Named Attribute.001"].width  = 140.0
    custom_points_1.nodes["Named Attribute.001"].height = 100.0

    custom_points_1.nodes["Euler to Rotation"].width  = 140.0
    custom_points_1.nodes["Euler to Rotation"].height = 100.0

    custom_points_1.nodes["Sample Index"].width  = 140.0
    custom_points_1.nodes["Sample Index"].height = 100.0

    custom_points_1.nodes["Index"].width  = 140.0
    custom_points_1.nodes["Index"].height = 100.0

    custom_points_1.nodes["Reroute.001"].width  = 12.5
    custom_points_1.nodes["Reroute.001"].height = 100.0

    custom_points_1.nodes["Menu Switch"].width  = 140.0
    custom_points_1.nodes["Menu Switch"].height = 100.0

    custom_points_1.nodes["Viewer.001"].width  = 140.0
    custom_points_1.nodes["Viewer.001"].height = 100.0

    custom_points_1.nodes["Viewer.002"].width  = 140.0
    custom_points_1.nodes["Viewer.002"].height = 100.0

    custom_points_1.nodes["Viewer.003"].width  = 140.0
    custom_points_1.nodes["Viewer.003"].height = 100.0


    # Initialize custom_points_1 links

    # named_attribute.Attribute -> separate_geometry.Selection
    custom_points_1.links.new(
        custom_points_1.nodes["Named Attribute"].outputs[0],
        custom_points_1.nodes["Separate Geometry"].inputs[1]
    )
    # group_input.Point Label -> named_attribute.Name
    custom_points_1.links.new(
        custom_points_1.nodes["Group Input"].outputs[1],
        custom_points_1.nodes["Named Attribute"].inputs[0]
    )
    # group_input.Geometry -> separate_geometry.Geometry
    custom_points_1.links.new(
        custom_points_1.nodes["Group Input"].outputs[0],
        custom_points_1.nodes["Separate Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Selection
    custom_points_1.links.new(
        custom_points_1.nodes["Join Geometry"].outputs[0],
        custom_points_1.nodes["Group Output"].inputs[0]
    )
    # reroute.Output -> join_geometry.Geometry
    custom_points_1.links.new(
        custom_points_1.nodes["Reroute"].outputs[0],
        custom_points_1.nodes["Join Geometry"].inputs[0]
    )
    # points_to_vertices.Mesh -> viewer.Mesh
    custom_points_1.links.new(
        custom_points_1.nodes["Points to Vertices"].outputs[0],
        custom_points_1.nodes["Viewer"].inputs[0]
    )
    # separate_geometry.Selection -> mesh_to_points.Mesh
    custom_points_1.links.new(
        custom_points_1.nodes["Separate Geometry"].outputs[0],
        custom_points_1.nodes["Mesh to Points"].inputs[0]
    )
    # mesh_to_points.Points -> instance_on_points.Points
    custom_points_1.links.new(
        custom_points_1.nodes["Mesh to Points"].outputs[0],
        custom_points_1.nodes["Instance on Points"].inputs[0]
    )
    # instance_on_points.Instances -> translate_instances.Instances
    custom_points_1.links.new(
        custom_points_1.nodes["Instance on Points"].outputs[0],
        custom_points_1.nodes["Translate Instances"].inputs[0]
    )
    # uv_sphere.Mesh -> instance_on_points.Instance
    custom_points_1.links.new(
        custom_points_1.nodes["UV Sphere"].outputs[0],
        custom_points_1.nodes["Instance on Points"].inputs[2]
    )
    # group_input.Offset -> combine_xyz.Z
    custom_points_1.links.new(
        custom_points_1.nodes["Group Input"].outputs[2],
        custom_points_1.nodes["Combine XYZ"].inputs[2]
    )
    # translate_instances.Instances -> instances_to_points.Instances
    custom_points_1.links.new(
        custom_points_1.nodes["Translate Instances"].outputs[0],
        custom_points_1.nodes["Instances to Points"].inputs[0]
    )
    # instances_to_points.Points -> points_to_vertices.Points
    custom_points_1.links.new(
        custom_points_1.nodes["Instances to Points"].outputs[0],
        custom_points_1.nodes["Points to Vertices"].inputs[0]
    )
    # join_geometry_001.Geometry -> group_output.Instances
    custom_points_1.links.new(
        custom_points_1.nodes["Join Geometry.001"].outputs[0],
        custom_points_1.nodes["Group Output"].inputs[1]
    )
    # reroute_001.Output -> reroute.Input
    custom_points_1.links.new(
        custom_points_1.nodes["Reroute.001"].outputs[0],
        custom_points_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> join_geometry_001.Geometry
    custom_points_1.links.new(
        custom_points_1.nodes["Reroute"].outputs[0],
        custom_points_1.nodes["Join Geometry.001"].inputs[0]
    )
    # euler_to_rotation.Rotation -> instance_on_points.Rotation
    custom_points_1.links.new(
        custom_points_1.nodes["Euler to Rotation"].outputs[0],
        custom_points_1.nodes["Instance on Points"].inputs[5]
    )
    # named_attribute_001.Attribute -> sample_index.Value
    custom_points_1.links.new(
        custom_points_1.nodes["Named Attribute.001"].outputs[0],
        custom_points_1.nodes["Sample Index"].inputs[1]
    )
    # mesh_to_points.Points -> sample_index.Geometry
    custom_points_1.links.new(
        custom_points_1.nodes["Mesh to Points"].outputs[0],
        custom_points_1.nodes["Sample Index"].inputs[0]
    )
    # index.Index -> sample_index.Index
    custom_points_1.links.new(
        custom_points_1.nodes["Index"].outputs[0],
        custom_points_1.nodes["Sample Index"].inputs[2]
    )
    # sample_index.Value -> euler_to_rotation.Euler
    custom_points_1.links.new(
        custom_points_1.nodes["Sample Index"].outputs[0],
        custom_points_1.nodes["Euler to Rotation"].inputs[0]
    )
    # combine_xyz.Vector -> translate_instances.Translation
    custom_points_1.links.new(
        custom_points_1.nodes["Combine XYZ"].outputs[0],
        custom_points_1.nodes["Translate Instances"].inputs[2]
    )
    # separate_geometry.Inverted -> reroute_001.Input
    custom_points_1.links.new(
        custom_points_1.nodes["Separate Geometry"].outputs[1],
        custom_points_1.nodes["Reroute.001"].inputs[0]
    )
    # points_to_vertices.Mesh -> group_output.Sensor Points
    custom_points_1.links.new(
        custom_points_1.nodes["Points to Vertices"].outputs[0],
        custom_points_1.nodes["Group Output"].inputs[2]
    )
    # translate_instances.Instances -> viewer_001.Instances
    custom_points_1.links.new(
        custom_points_1.nodes["Translate Instances"].outputs[0],
        custom_points_1.nodes["Viewer.001"].inputs[0]
    )
    # separate_geometry.Inverted -> viewer_002.Inverted
    custom_points_1.links.new(
        custom_points_1.nodes["Separate Geometry"].outputs[1],
        custom_points_1.nodes["Viewer.002"].inputs[0]
    )
    # points_to_vertices.Mesh -> join_geometry.Geometry
    custom_points_1.links.new(
        custom_points_1.nodes["Points to Vertices"].outputs[0],
        custom_points_1.nodes["Join Geometry"].inputs[0]
    )
    # translate_instances.Instances -> join_geometry_001.Geometry
    custom_points_1.links.new(
        custom_points_1.nodes["Translate Instances"].outputs[0],
        custom_points_1.nodes["Join Geometry.001"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True
    viewer_001.viewer_items[0].auto_remove = True
    viewer_002.viewer_items[0].auto_remove = True

    return custom_points_1


def sample_points_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Sample Points node group"""
    sample_points_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sample Points")

    sample_points_1.color_tag = 'NONE'
    sample_points_1.description = ""
    sample_points_1.default_group_node_width = 140
    sample_points_1.is_modifier = True
    sample_points_1.show_modifier_manage_panel = True

    # sample_points_1 interface

    # Socket Geometry
    geometry_socket = sample_points_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Sensor Points
    sensor_points_socket = sample_points_1.interface.new_socket(name="Sensor Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_points_socket.attribute_domain = 'POINT'
    sensor_points_socket.default_input = 'VALUE'
    sensor_points_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = sample_points_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Isolate Points
    isolate_points_socket = sample_points_1.interface.new_socket(name="Isolate Points", in_out='INPUT', socket_type='NodeSocketBool')
    isolate_points_socket.default_value = False
    isolate_points_socket.attribute_domain = 'POINT'
    isolate_points_socket.default_input = 'VALUE'
    isolate_points_socket.structure_type = 'AUTO'

    # Socket Distribution Type
    distribution_type_socket = sample_points_1.interface.new_socket(name="Distribution Type", in_out='INPUT', socket_type='NodeSocketMenu')
    distribution_type_socket.attribute_domain = 'POINT'
    distribution_type_socket.default_input = 'VALUE'
    distribution_type_socket.structure_type = 'AUTO'
    distribution_type_socket.optional_label = True

    # Socket Density Paint
    density_paint_socket = sample_points_1.interface.new_socket(name="Density Paint", in_out='INPUT', socket_type='NodeSocketString')
    density_paint_socket.default_value = "Nodes"
    density_paint_socket.subtype = 'NONE'
    density_paint_socket.default_attribute_name = "Point>Group"
    density_paint_socket.attribute_domain = 'POINT'
    density_paint_socket.hide_value = True
    density_paint_socket.default_input = 'VALUE'
    density_paint_socket.structure_type = 'AUTO'

    # Socket Sampling Type
    sampling_type_socket = sample_points_1.interface.new_socket(name="Sampling Type", in_out='INPUT', socket_type='NodeSocketMenu')
    sampling_type_socket.attribute_domain = 'POINT'
    sampling_type_socket.default_input = 'VALUE'
    sampling_type_socket.structure_type = 'AUTO'
    sampling_type_socket.optional_label = True

    # Socket Min Distance
    min_distance_socket = sample_points_1.interface.new_socket(name="Min Distance", in_out='INPUT', socket_type='NodeSocketFloat')
    min_distance_socket.default_value = 0.019999999552965164
    min_distance_socket.min_value = 0.0
    min_distance_socket.max_value = 3.4028234663852886e+38
    min_distance_socket.subtype = 'DISTANCE'
    min_distance_socket.attribute_domain = 'POINT'
    min_distance_socket.description = "Minimum placement distance between sensors"
    min_distance_socket.default_input = 'VALUE'
    min_distance_socket.structure_type = 'AUTO'

    # Socket Max Density
    max_density_socket = sample_points_1.interface.new_socket(name="Max Density", in_out='INPUT', socket_type='NodeSocketFloat')
    max_density_socket.default_value = 50000.0
    max_density_socket.min_value = 0.0
    max_density_socket.max_value = 3.4028234663852886e+38
    max_density_socket.subtype = 'NONE'
    max_density_socket.attribute_domain = 'POINT'
    max_density_socket.default_input = 'VALUE'
    max_density_socket.structure_type = 'AUTO'

    # Socket Density Multiplier
    density_multiplier_socket = sample_points_1.interface.new_socket(name="Density Multiplier", in_out='INPUT', socket_type='NodeSocketFloat')
    density_multiplier_socket.default_value = 50.0
    density_multiplier_socket.min_value = 0.0
    density_multiplier_socket.max_value = 100.0
    density_multiplier_socket.subtype = 'PERCENTAGE'
    density_multiplier_socket.attribute_domain = 'POINT'
    density_multiplier_socket.default_input = 'VALUE'
    density_multiplier_socket.structure_type = 'AUTO'

    # Socket Size
    size_socket = sample_points_1.interface.new_socket(name="Size", in_out='INPUT', socket_type='NodeSocketFloat')
    size_socket.default_value = 1.0
    size_socket.min_value = -10000.0
    size_socket.max_value = 10000.0
    size_socket.subtype = 'NONE'
    size_socket.attribute_domain = 'POINT'
    size_socket.default_input = 'VALUE'
    size_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = sample_points_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket.default_value = 128
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Offset
    offset_socket = sample_points_1.interface.new_socket(name="Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    offset_socket.default_value = 0.0
    offset_socket.min_value = 0.0
    offset_socket.max_value = 10000.0
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'

    # Panel Options
    options_panel = sample_points_1.interface.new_panel("Options")
    # Socket Options
    options_socket = sample_points_1.interface.new_socket(name="Options", in_out='INPUT', socket_type='NodeSocketMenu', parent = options_panel)
    options_socket.attribute_domain = 'POINT'
    options_socket.default_input = 'VALUE'
    options_socket.structure_type = 'AUTO'

    # Socket Sampling Surface Name
    sampling_surface_name_socket = sample_points_1.interface.new_socket(name="Sampling Surface Name", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    sampling_surface_name_socket.default_value = "dermis"
    sampling_surface_name_socket.subtype = 'NONE'
    sampling_surface_name_socket.attribute_domain = 'POINT'
    sampling_surface_name_socket.default_input = 'VALUE'
    sampling_surface_name_socket.structure_type = 'AUTO'
    sampling_surface_name_socket.optional_label = True

    # Socket Point Label
    point_label_socket = sample_points_1.interface.new_socket(name="Point Label", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    point_label_socket.default_value = "sensor_point"
    point_label_socket.subtype = 'NONE'
    point_label_socket.attribute_domain = 'POINT'
    point_label_socket.default_input = 'VALUE'
    point_label_socket.structure_type = 'AUTO'


    # Initialize sample_points_1 nodes

    # Node Group Input
    group_input = sample_points_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = sample_points_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Distribute Surface Points
    distribute_surface_points = sample_points_1.nodes.new("GeometryNodeGroup")
    distribute_surface_points.name = "Distribute Surface Points"
    distribute_surface_points.show_options = True
    distribute_surface_points.node_tree = bpy.data.node_groups[node_tree_names[distribute_surface_points_1_node_group]]

    # Node Separate Geometry
    separate_geometry = sample_points_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.show_options = True
    separate_geometry.domain = 'POINT'

    # Node Named Attribute
    named_attribute = sample_points_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'FLOAT'

    # Node Join Geometry
    join_geometry = sample_points_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Store Named Attribute
    store_named_attribute = sample_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT_VECTOR'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "eulers"

    # Node Menu Switch
    menu_switch = sample_points_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.show_options = True
    menu_switch.active_index = 1
    menu_switch.data_type = 'BOOLEAN'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Default")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Advanced")
    menu_switch.enum_items[1].description = ""
    # Item_0
    menu_switch.inputs[1].default_value = True
    # Item_1
    menu_switch.inputs[2].default_value = False

    # Node Store Named Attribute.001
    store_named_attribute_001 = sample_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Value
    store_named_attribute_001.inputs[3].default_value = True

    # Node String
    string = sample_points_1.nodes.new("FunctionNodeInputString")
    string.name = "String"
    string.show_options = True
    string.string = "sensor_point"

    # Node Switch
    switch = sample_points_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'STRING'

    # Node Points to Vertices
    points_to_vertices = sample_points_1.nodes.new("GeometryNodePointsToVertices")
    points_to_vertices.name = "Points to Vertices"
    points_to_vertices.show_options = True
    # Selection
    points_to_vertices.inputs[1].default_value = True

    # Node Viewer
    viewer = sample_points_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")

    # Node Store Named Attribute.002
    store_named_attribute_002 = sample_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'INT'
    store_named_attribute_002.domain = 'POINT'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "sensor_idx"

    # Node Index
    index = sample_points_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Math
    math = sample_points_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'ADD'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # Node Frame
    frame = sample_points_1.nodes.new("NodeFrame")
    frame.label = "Cant be 0"
    frame.name = "Frame"
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Switch.001
    switch_001 = sample_points_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'STRING'
    # True
    switch_001.inputs[2].default_value = "dermis"

    # Node Switch.002
    switch_002 = sample_points_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.show_options = True
    switch_002.input_type = 'GEOMETRY'

    # Node Reroute
    reroute = sample_points_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Separate Geometry.001
    separate_geometry_001 = sample_points_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_001.name = "Separate Geometry.001"
    separate_geometry_001.show_options = True
    separate_geometry_001.domain = 'POINT'

    # Node Named Attribute.001
    named_attribute_001 = sample_points_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'BOOLEAN'

    # Node Group
    group = sample_points_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[custom_points_1_node_group]]

    # Node Menu Switch.001
    menu_switch_001 = sample_points_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch_001.name = "Menu Switch.001"
    menu_switch_001.show_options = True
    menu_switch_001.active_index = 1
    menu_switch_001.data_type = 'GEOMETRY'
    menu_switch_001.enum_items.clear()
    menu_switch_001.enum_items.new("Sampling")
    menu_switch_001.enum_items[0].description = ""
    menu_switch_001.enum_items.new("Custom")
    menu_switch_001.enum_items[1].description = ""

    # Node Switch.003
    switch_003 = sample_points_1.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.show_options = True
    switch_003.input_type = 'GEOMETRY'

    # Node Group Input.001
    group_input_001 = sample_points_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Set parents
    sample_points_1.nodes["Index"].parent = sample_points_1.nodes["Frame"]
    sample_points_1.nodes["Math"].parent = sample_points_1.nodes["Frame"]

    # Set locations
    sample_points_1.nodes["Group Input"].location = (-2580.0, 40.0)
    sample_points_1.nodes["Group Output"].location = (1500.0, 0.0)
    sample_points_1.nodes["Distribute Surface Points"].location = (-600.0, 260.0)
    sample_points_1.nodes["Separate Geometry"].location = (-899.9999389648438, 320.0)
    sample_points_1.nodes["Named Attribute"].location = (-1120.0, 300.0)
    sample_points_1.nodes["Join Geometry"].location = (500.0, -200.0)
    sample_points_1.nodes["Store Named Attribute"].location = (-100.0000228881836, 260.0)
    sample_points_1.nodes["Menu Switch"].location = (-1760.0, -440.0)
    sample_points_1.nodes["Store Named Attribute.001"].location = (80.0, 80.0)
    sample_points_1.nodes["String"].location = (-1520.0, -580.0)
    sample_points_1.nodes["Switch"].location = (-1180.0, -400.0)
    sample_points_1.nodes["Points to Vertices"].location = (-280.0, 240.0)
    sample_points_1.nodes["Viewer"].location = (526.6666870117188, -479.3333435058594)
    sample_points_1.nodes["Store Named Attribute.002"].location = (260.0, 40.0)
    sample_points_1.nodes["Index"].location = (29.161300659179688, -55.93547058105469)
    sample_points_1.nodes["Math"].location = (209.1613006591797, -35.93547058105469)
    sample_points_1.nodes["Frame"].location = (-169.1613006591797, -184.0645294189453)
    sample_points_1.nodes["Switch.001"].location = (-1480.0, -180.0)
    sample_points_1.nodes["Switch.002"].location = (760.0, 0.0)
    sample_points_1.nodes["Reroute"].location = (-1920.96826171875, 29.3447322845459)
    sample_points_1.nodes["Separate Geometry.001"].location = (-2120.0, 160.0)
    sample_points_1.nodes["Named Attribute.001"].location = (-2340.0, 180.0)
    sample_points_1.nodes["Group"].location = (700.0, -460.0)
    sample_points_1.nodes["Menu Switch.001"].location = (1000.0, -200.0)
    sample_points_1.nodes["Switch.003"].location = (1200.0, -340.0)
    sample_points_1.nodes["Group Input.001"].location = (360.0, -560.0)

    # Set dimensions
    sample_points_1.nodes["Group Input"].width  = 140.0
    sample_points_1.nodes["Group Input"].height = 100.0

    sample_points_1.nodes["Group Output"].width  = 140.0
    sample_points_1.nodes["Group Output"].height = 100.0

    sample_points_1.nodes["Distribute Surface Points"].width  = 280.0
    sample_points_1.nodes["Distribute Surface Points"].height = 100.0

    sample_points_1.nodes["Separate Geometry"].width  = 140.0
    sample_points_1.nodes["Separate Geometry"].height = 100.0

    sample_points_1.nodes["Named Attribute"].width  = 140.0
    sample_points_1.nodes["Named Attribute"].height = 100.0

    sample_points_1.nodes["Join Geometry"].width  = 140.0
    sample_points_1.nodes["Join Geometry"].height = 100.0

    sample_points_1.nodes["Store Named Attribute"].width  = 140.0
    sample_points_1.nodes["Store Named Attribute"].height = 100.0

    sample_points_1.nodes["Menu Switch"].width  = 140.0
    sample_points_1.nodes["Menu Switch"].height = 100.0

    sample_points_1.nodes["Store Named Attribute.001"].width  = 140.0
    sample_points_1.nodes["Store Named Attribute.001"].height = 100.0

    sample_points_1.nodes["String"].width  = 140.0
    sample_points_1.nodes["String"].height = 100.0

    sample_points_1.nodes["Switch"].width  = 140.0
    sample_points_1.nodes["Switch"].height = 100.0

    sample_points_1.nodes["Points to Vertices"].width  = 140.0
    sample_points_1.nodes["Points to Vertices"].height = 100.0

    sample_points_1.nodes["Viewer"].width  = 140.0
    sample_points_1.nodes["Viewer"].height = 100.0

    sample_points_1.nodes["Store Named Attribute.002"].width  = 140.0
    sample_points_1.nodes["Store Named Attribute.002"].height = 100.0

    sample_points_1.nodes["Index"].width  = 140.0
    sample_points_1.nodes["Index"].height = 100.0

    sample_points_1.nodes["Math"].width  = 140.0
    sample_points_1.nodes["Math"].height = 100.0

    sample_points_1.nodes["Frame"].width  = 378.45159912109375
    sample_points_1.nodes["Frame"].height = 207.2903289794922

    sample_points_1.nodes["Switch.001"].width  = 140.0
    sample_points_1.nodes["Switch.001"].height = 100.0

    sample_points_1.nodes["Switch.002"].width  = 140.0
    sample_points_1.nodes["Switch.002"].height = 100.0

    sample_points_1.nodes["Reroute"].width  = 12.5
    sample_points_1.nodes["Reroute"].height = 100.0

    sample_points_1.nodes["Separate Geometry.001"].width  = 140.0
    sample_points_1.nodes["Separate Geometry.001"].height = 100.0

    sample_points_1.nodes["Named Attribute.001"].width  = 140.0
    sample_points_1.nodes["Named Attribute.001"].height = 100.0

    sample_points_1.nodes["Group"].width  = 220.0
    sample_points_1.nodes["Group"].height = 100.0

    sample_points_1.nodes["Menu Switch.001"].width  = 140.0
    sample_points_1.nodes["Menu Switch.001"].height = 100.0

    sample_points_1.nodes["Switch.003"].width  = 140.0
    sample_points_1.nodes["Switch.003"].height = 100.0

    sample_points_1.nodes["Group Input.001"].width  = 140.0
    sample_points_1.nodes["Group Input.001"].height = 100.0


    # Initialize sample_points_1 links

    # named_attribute.Attribute -> separate_geometry.Selection
    sample_points_1.links.new(
        sample_points_1.nodes["Named Attribute"].outputs[0],
        sample_points_1.nodes["Separate Geometry"].inputs[1]
    )
    # reroute.Output -> separate_geometry.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Reroute"].outputs[0],
        sample_points_1.nodes["Separate Geometry"].inputs[0]
    )
    # separate_geometry.Selection -> distribute_surface_points.Dermis Top Cut
    sample_points_1.links.new(
        sample_points_1.nodes["Separate Geometry"].outputs[0],
        sample_points_1.nodes["Distribute Surface Points"].inputs[2]
    )
    # reroute.Output -> join_geometry.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Reroute"].outputs[0],
        sample_points_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Sampling Type -> distribute_surface_points.Sampling Type
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[4],
        sample_points_1.nodes["Distribute Surface Points"].inputs[0]
    )
    # group_input.Max Density -> distribute_surface_points.Max Density
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[6],
        sample_points_1.nodes["Distribute Surface Points"].inputs[1]
    )
    # group_input.Min Distance -> distribute_surface_points.Min Distance
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[5],
        sample_points_1.nodes["Distribute Surface Points"].inputs[3]
    )
    # group_input.Density Multiplier -> distribute_surface_points.Density Multiplier
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[7],
        sample_points_1.nodes["Distribute Surface Points"].inputs[4]
    )
    # group_input.Size -> distribute_surface_points.Overlap
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[8],
        sample_points_1.nodes["Distribute Surface Points"].inputs[5]
    )
    # group_input.Density Paint -> distribute_surface_points.Density Paint
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[3],
        sample_points_1.nodes["Distribute Surface Points"].inputs[6]
    )
    # group_input.Seed -> distribute_surface_points.Seed
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[9],
        sample_points_1.nodes["Distribute Surface Points"].inputs[7]
    )
    # points_to_vertices.Mesh -> store_named_attribute.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Points to Vertices"].outputs[0],
        sample_points_1.nodes["Store Named Attribute"].inputs[0]
    )
    # distribute_surface_points.Euler Rotations -> store_named_attribute.Value
    sample_points_1.links.new(
        sample_points_1.nodes["Distribute Surface Points"].outputs[1],
        sample_points_1.nodes["Store Named Attribute"].inputs[3]
    )
    # group_input.Options -> menu_switch.Menu
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[11],
        sample_points_1.nodes["Menu Switch"].inputs[0]
    )
    # store_named_attribute.Geometry -> store_named_attribute_001.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Store Named Attribute"].outputs[0],
        sample_points_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # menu_switch.Default -> switch.Switch
    sample_points_1.links.new(
        sample_points_1.nodes["Menu Switch"].outputs[1],
        sample_points_1.nodes["Switch"].inputs[0]
    )
    # string.String -> switch.True
    sample_points_1.links.new(
        sample_points_1.nodes["String"].outputs[0],
        sample_points_1.nodes["Switch"].inputs[2]
    )
    # group_input.Point Label -> switch.False
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[13],
        sample_points_1.nodes["Switch"].inputs[1]
    )
    # switch.Output -> store_named_attribute_001.Name
    sample_points_1.links.new(
        sample_points_1.nodes["Switch"].outputs[0],
        sample_points_1.nodes["Store Named Attribute.001"].inputs[2]
    )
    # distribute_surface_points.Sensor Points -> points_to_vertices.Points
    sample_points_1.links.new(
        sample_points_1.nodes["Distribute Surface Points"].outputs[0],
        sample_points_1.nodes["Points to Vertices"].inputs[0]
    )
    # group_input_001.Geometry -> viewer.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input.001"].outputs[0],
        sample_points_1.nodes["Viewer"].inputs[0]
    )
    # store_named_attribute_001.Geometry -> store_named_attribute_002.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Store Named Attribute.001"].outputs[0],
        sample_points_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # math.Value -> store_named_attribute_002.Value
    sample_points_1.links.new(
        sample_points_1.nodes["Math"].outputs[0],
        sample_points_1.nodes["Store Named Attribute.002"].inputs[3]
    )
    # index.Index -> math.Value
    sample_points_1.links.new(
        sample_points_1.nodes["Index"].outputs[0],
        sample_points_1.nodes["Math"].inputs[0]
    )
    # menu_switch.Default -> switch_001.Switch
    sample_points_1.links.new(
        sample_points_1.nodes["Menu Switch"].outputs[1],
        sample_points_1.nodes["Switch.001"].inputs[0]
    )
    # group_input.Sampling Surface Name -> switch_001.False
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[12],
        sample_points_1.nodes["Switch.001"].inputs[1]
    )
    # switch_001.Output -> named_attribute.Name
    sample_points_1.links.new(
        sample_points_1.nodes["Switch.001"].outputs[0],
        sample_points_1.nodes["Named Attribute"].inputs[0]
    )
    # join_geometry.Geometry -> switch_002.False
    sample_points_1.links.new(
        sample_points_1.nodes["Join Geometry"].outputs[0],
        sample_points_1.nodes["Switch.002"].inputs[1]
    )
    # store_named_attribute_002.Geometry -> switch_002.True
    sample_points_1.links.new(
        sample_points_1.nodes["Store Named Attribute.002"].outputs[0],
        sample_points_1.nodes["Switch.002"].inputs[2]
    )
    # group_input.Isolate Points -> switch_002.Switch
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[1],
        sample_points_1.nodes["Switch.002"].inputs[0]
    )
    # group_input.Geometry -> separate_geometry_001.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[0],
        sample_points_1.nodes["Separate Geometry.001"].inputs[0]
    )
    # group_input.Point Label -> named_attribute_001.Name
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[13],
        sample_points_1.nodes["Named Attribute.001"].inputs[0]
    )
    # named_attribute_001.Attribute -> separate_geometry_001.Selection
    sample_points_1.links.new(
        sample_points_1.nodes["Named Attribute.001"].outputs[0],
        sample_points_1.nodes["Separate Geometry.001"].inputs[1]
    )
    # separate_geometry_001.Inverted -> reroute.Input
    sample_points_1.links.new(
        sample_points_1.nodes["Separate Geometry.001"].outputs[1],
        sample_points_1.nodes["Reroute"].inputs[0]
    )
    # menu_switch_001.Custom -> switch_003.Switch
    sample_points_1.links.new(
        sample_points_1.nodes["Menu Switch.001"].outputs[2],
        sample_points_1.nodes["Switch.003"].inputs[0]
    )
    # group.Sensor Points -> switch_003.True
    sample_points_1.links.new(
        sample_points_1.nodes["Group"].outputs[2],
        sample_points_1.nodes["Switch.003"].inputs[2]
    )
    # store_named_attribute_002.Geometry -> switch_003.False
    sample_points_1.links.new(
        sample_points_1.nodes["Store Named Attribute.002"].outputs[0],
        sample_points_1.nodes["Switch.003"].inputs[1]
    )
    # switch_003.Output -> group_output.Sensor Points
    sample_points_1.links.new(
        sample_points_1.nodes["Switch.003"].outputs[0],
        sample_points_1.nodes["Group Output"].inputs[1]
    )
    # menu_switch_001.Output -> group_output.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Menu Switch.001"].outputs[0],
        sample_points_1.nodes["Group Output"].inputs[0]
    )
    # switch_002.Output -> menu_switch_001.Sampling
    sample_points_1.links.new(
        sample_points_1.nodes["Switch.002"].outputs[0],
        sample_points_1.nodes["Menu Switch.001"].inputs[1]
    )
    # group.Selection -> menu_switch_001.Custom
    sample_points_1.links.new(
        sample_points_1.nodes["Group"].outputs[0],
        sample_points_1.nodes["Menu Switch.001"].inputs[2]
    )
    # group_input.Distribution Type -> menu_switch_001.Menu
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input"].outputs[2],
        sample_points_1.nodes["Menu Switch.001"].inputs[0]
    )
    # group_input_001.Geometry -> group.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input.001"].outputs[0],
        sample_points_1.nodes["Group"].inputs[0]
    )
    # group_input_001.Point Label -> group.Point Label
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input.001"].outputs[13],
        sample_points_1.nodes["Group"].inputs[1]
    )
    # group_input_001.Offset -> group.Offset
    sample_points_1.links.new(
        sample_points_1.nodes["Group Input.001"].outputs[10],
        sample_points_1.nodes["Group"].inputs[2]
    )
    # store_named_attribute_002.Geometry -> join_geometry.Geometry
    sample_points_1.links.new(
        sample_points_1.nodes["Store Named Attribute.002"].outputs[0],
        sample_points_1.nodes["Join Geometry"].inputs[0]
    )
    distribution_type_socket.default_value = 'Sampling'
    sampling_type_socket.default_value = 'Poisson Disk'
    options_socket.default_value = 'Default'
    viewer.viewer_items[0].auto_remove = True

    return sample_points_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    sub_sensor_visual = sub_sensor_visual_1_node_group(node_tree_names)
    node_tree_names[sub_sensor_visual_1_node_group] = sub_sensor_visual.name

    poisson_slice = poisson_slice_1_node_group(node_tree_names)
    node_tree_names[poisson_slice_1_node_group] = poisson_slice.name

    poisson_placement = poisson_placement_1_node_group(node_tree_names)
    node_tree_names[poisson_placement_1_node_group] = poisson_placement.name

    distribute_surface_points = distribute_surface_points_1_node_group(node_tree_names)
    node_tree_names[distribute_surface_points_1_node_group] = distribute_surface_points.name

    custom_points = custom_points_1_node_group(node_tree_names)
    node_tree_names[custom_points_1_node_group] = custom_points.name

    sample_points = sample_points_1_node_group(node_tree_names)
    node_tree_names[sample_points_1_node_group] = sample_points.name

