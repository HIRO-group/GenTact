import bpy
import mathutils
import os
import typing


def distribute_custom_sensors_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Distribute Custom Sensors node group"""
    distribute_custom_sensors_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Distribute Custom Sensors")

    distribute_custom_sensors_1.color_tag = 'NONE'
    distribute_custom_sensors_1.description = ""
    distribute_custom_sensors_1.default_group_node_width = 140
    distribute_custom_sensors_1.is_modifier = True
    distribute_custom_sensors_1.show_modifier_manage_panel = True

    # distribute_custom_sensors_1 interface

    # Socket Geometry
    geometry_socket = distribute_custom_sensors_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Negative Geometry
    negative_geometry_socket = distribute_custom_sensors_1.interface.new_socket(name="Negative Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    negative_geometry_socket.attribute_domain = 'POINT'
    negative_geometry_socket.default_input = 'VALUE'
    negative_geometry_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket = distribute_custom_sensors_1.interface.new_socket(name="Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket_1 = distribute_custom_sensors_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry')
    points_socket_1.attribute_domain = 'POINT'
    points_socket_1.default_input = 'VALUE'
    points_socket_1.structure_type = 'AUTO'

    # Socket Euler
    euler_socket = distribute_custom_sensors_1.interface.new_socket(name="Euler", in_out='INPUT', socket_type='NodeSocketVector')
    euler_socket.default_value = (0.0, 0.0, 0.0)
    euler_socket.min_value = -3.4028234663852886e+38
    euler_socket.max_value = 3.4028234663852886e+38
    euler_socket.subtype = 'EULER'
    euler_socket.attribute_domain = 'POINT'
    euler_socket.default_input = 'VALUE'
    euler_socket.structure_type = 'AUTO'

    # Socket Sensor Mesh
    sensor_mesh_socket = distribute_custom_sensors_1.interface.new_socket(name="Sensor Mesh", in_out='INPUT', socket_type='NodeSocketObject')
    sensor_mesh_socket.attribute_domain = 'POINT'
    sensor_mesh_socket.default_input = 'VALUE'
    sensor_mesh_socket.structure_type = 'AUTO'

    # Socket Sensor Negative Mesh
    sensor_negative_mesh_socket = distribute_custom_sensors_1.interface.new_socket(name="Sensor Negative Mesh", in_out='INPUT', socket_type='NodeSocketObject')
    sensor_negative_mesh_socket.attribute_domain = 'POINT'
    sensor_negative_mesh_socket.default_input = 'VALUE'
    sensor_negative_mesh_socket.structure_type = 'AUTO'

    # Socket Node Offset
    node_offset_socket = distribute_custom_sensors_1.interface.new_socket(name="Node Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    node_offset_socket.default_value = 0.0
    node_offset_socket.min_value = -10000.0
    node_offset_socket.max_value = 10000.0
    node_offset_socket.subtype = 'NONE'
    node_offset_socket.attribute_domain = 'POINT'
    node_offset_socket.default_input = 'VALUE'
    node_offset_socket.structure_type = 'AUTO'

    # Socket Reference Thickness
    reference_thickness_socket = distribute_custom_sensors_1.interface.new_socket(name="Reference Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    reference_thickness_socket.default_value = 0.0
    reference_thickness_socket.min_value = -3.4028234663852886e+38
    reference_thickness_socket.max_value = 3.4028234663852886e+38
    reference_thickness_socket.subtype = 'NONE'
    reference_thickness_socket.attribute_domain = 'POINT'
    reference_thickness_socket.default_input = 'VALUE'
    reference_thickness_socket.structure_type = 'AUTO'

    # Initialize distribute_custom_sensors_1 nodes

    # Node Group Input
    group_input = distribute_custom_sensors_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = distribute_custom_sensors_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Object Info
    object_info = distribute_custom_sensors_1.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.show_options = True
    object_info.transform_space = 'ORIGINAL'
    # As Instance
    object_info.inputs[1].default_value = False

    # Node Combine XYZ
    combine_xyz = distribute_custom_sensors_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # Node Instance on Points
    instance_on_points = distribute_custom_sensors_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0

    # Node Reroute
    reroute = distribute_custom_sensors_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Instance on Points.001
    instance_on_points_001 = distribute_custom_sensors_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.show_options = True
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0
    # Scale
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Euler to Rotation
    euler_to_rotation = distribute_custom_sensors_1.nodes.new("FunctionNodeEulerToRotation")
    euler_to_rotation.name = "Euler to Rotation"
    euler_to_rotation.show_options = True

    # Node Set Material
    set_material = distribute_custom_sensors_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True
    if "Sensor Mat" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["Sensor Mat"]

    # Node Object Info.001
    object_info_001 = distribute_custom_sensors_1.nodes.new("GeometryNodeObjectInfo")
    object_info_001.name = "Object Info.001"
    object_info_001.show_options = True
    object_info_001.transform_space = 'ORIGINAL'
    # As Instance
    object_info_001.inputs[1].default_value = False

    # Node Translate Instances
    translate_instances = distribute_custom_sensors_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances.name = "Translate Instances"
    translate_instances.show_options = True
    # Selection
    translate_instances.inputs[1].default_value = True
    # Local Space
    translate_instances.inputs[3].default_value = True

    # Node Rotate Instances
    rotate_instances = distribute_custom_sensors_1.nodes.new("GeometryNodeRotateInstances")
    rotate_instances.name = "Rotate Instances"
    rotate_instances.show_options = True
    # Selection
    rotate_instances.inputs[1].default_value = True
    # Rotation
    rotate_instances.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Pivot Point
    rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Local Space
    rotate_instances.inputs[4].default_value = True

    # Node Realize Instances
    realize_instances = distribute_custom_sensors_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    realize_instances.realize_to_point_domain = True
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Set Material.001
    set_material_001 = distribute_custom_sensors_1.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    set_material_001.show_options = True
    # Selection
    set_material_001.inputs[1].default_value = True
    if "Sensor Mat" in bpy.data.materials:
        set_material_001.inputs[2].default_value = bpy.data.materials["Sensor Mat"]

    # Node Translate Instances.001
    translate_instances_001 = distribute_custom_sensors_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances_001.name = "Translate Instances.001"
    translate_instances_001.show_options = True
    # Selection
    translate_instances_001.inputs[1].default_value = True
    # Local Space
    translate_instances_001.inputs[3].default_value = True

    # Node Rotate Instances.001
    rotate_instances_001 = distribute_custom_sensors_1.nodes.new("GeometryNodeRotateInstances")
    rotate_instances_001.name = "Rotate Instances.001"
    rotate_instances_001.show_options = True
    # Selection
    rotate_instances_001.inputs[1].default_value = True
    # Rotation
    rotate_instances_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Pivot Point
    rotate_instances_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Local Space
    rotate_instances_001.inputs[4].default_value = True

    # Node Realize Instances.001
    realize_instances_001 = distribute_custom_sensors_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.show_options = True
    realize_instances_001.realize_to_point_domain = True
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Reroute.001
    reroute_001 = distribute_custom_sensors_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketVector"
    # Node Reroute.002
    reroute_002 = distribute_custom_sensors_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketVector"
    # Node Math
    math = distribute_custom_sensors_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'DIVIDE'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 100.0

    # Node Math.001
    math_001 = distribute_custom_sensors_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    # Node Remove Named Attribute
    remove_named_attribute = distribute_custom_sensors_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute.name = "Remove Named Attribute"
    remove_named_attribute.show_options = True
    # Pattern Mode
    remove_named_attribute.inputs[1].default_value = 'Exact'
    # Name
    remove_named_attribute.inputs[2].default_value = "is_sensor"

    # Node Instances to Points
    instances_to_points = distribute_custom_sensors_1.nodes.new("GeometryNodeInstancesToPoints")
    instances_to_points.name = "Instances to Points"
    instances_to_points.show_options = True
    # Selection
    instances_to_points.inputs[1].default_value = True
    # Position
    instances_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    instances_to_points.inputs[3].default_value = 0.05000000074505806

    # Node Store Named Attribute
    store_named_attribute = distribute_custom_sensors_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT_VECTOR'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "sensor_pos"

    # Node Points to Vertices
    points_to_vertices = distribute_custom_sensors_1.nodes.new("GeometryNodePointsToVertices")
    points_to_vertices.name = "Points to Vertices"
    points_to_vertices.show_options = True
    # Selection
    points_to_vertices.inputs[1].default_value = True

    # Node Sample Index
    sample_index = distribute_custom_sensors_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Index
    index = distribute_custom_sensors_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Position
    position = distribute_custom_sensors_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Set locations
    distribute_custom_sensors_1.nodes["Group Input"].location = (-2660.0, -40.0)
    distribute_custom_sensors_1.nodes["Group Output"].location = (900.0, 60.0)
    distribute_custom_sensors_1.nodes["Object Info"].location = (-1420.0, 280.0)
    distribute_custom_sensors_1.nodes["Combine XYZ"].location = (-1420.0, -80.0)
    distribute_custom_sensors_1.nodes["Instance on Points"].location = (-700.0, 340.0)
    distribute_custom_sensors_1.nodes["Reroute"].location = (-933.091552734375, -45.59730529785156)
    distribute_custom_sensors_1.nodes["Instance on Points.001"].location = (-700.0, -60.0)
    distribute_custom_sensors_1.nodes["Euler to Rotation"].location = (-1020.0, 100.0)
    distribute_custom_sensors_1.nodes["Set Material"].location = (-1020.0, 280.0)
    distribute_custom_sensors_1.nodes["Object Info.001"].location = (-1420.0, -260.0)
    distribute_custom_sensors_1.nodes["Translate Instances"].location = (-500.0, 420.0)
    distribute_custom_sensors_1.nodes["Rotate Instances"].location = (-280.0, 420.0)
    distribute_custom_sensors_1.nodes["Realize Instances"].location = (-20.0, 400.0)
    distribute_custom_sensors_1.nodes["Set Material.001"].location = (-1040.0, -220.0)
    distribute_custom_sensors_1.nodes["Translate Instances.001"].location = (-500.0, -300.0)
    distribute_custom_sensors_1.nodes["Rotate Instances.001"].location = (-280.0, -100.0)
    distribute_custom_sensors_1.nodes["Realize Instances.001"].location = (-20.0, -100.0)
    distribute_custom_sensors_1.nodes["Reroute.001"].location = (-1180.0, 360.0)
    distribute_custom_sensors_1.nodes["Reroute.002"].location = (-1200.0, -380.0)
    distribute_custom_sensors_1.nodes["Math"].location = (-2120.0, -300.0)
    distribute_custom_sensors_1.nodes["Math.001"].location = (-1840.0, -100.0)
    distribute_custom_sensors_1.nodes["Remove Named Attribute"].location = (-2400.0, 20.0)
    distribute_custom_sensors_1.nodes["Instances to Points"].location = (-20.0, 80.0)
    distribute_custom_sensors_1.nodes["Store Named Attribute"].location = (420.0, 140.0)
    distribute_custom_sensors_1.nodes["Points to Vertices"].location = (160.0, 100.0)
    distribute_custom_sensors_1.nodes["Sample Index"].location = (340.0, -140.0)
    distribute_custom_sensors_1.nodes["Index"].location = (-20.0, 140.0)
    distribute_custom_sensors_1.nodes["Position"].location = (120.0, -300.0)

    # Set dimensions
    distribute_custom_sensors_1.nodes["Group Input"].width  = 140.0
    distribute_custom_sensors_1.nodes["Group Input"].height = 100.0

    distribute_custom_sensors_1.nodes["Group Output"].width  = 140.0
    distribute_custom_sensors_1.nodes["Group Output"].height = 100.0

    distribute_custom_sensors_1.nodes["Object Info"].width  = 140.0
    distribute_custom_sensors_1.nodes["Object Info"].height = 100.0

    distribute_custom_sensors_1.nodes["Combine XYZ"].width  = 140.0
    distribute_custom_sensors_1.nodes["Combine XYZ"].height = 100.0

    distribute_custom_sensors_1.nodes["Instance on Points"].width  = 140.0
    distribute_custom_sensors_1.nodes["Instance on Points"].height = 100.0

    distribute_custom_sensors_1.nodes["Reroute"].width  = 14.5
    distribute_custom_sensors_1.nodes["Reroute"].height = 100.0

    distribute_custom_sensors_1.nodes["Instance on Points.001"].width  = 140.0
    distribute_custom_sensors_1.nodes["Instance on Points.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Euler to Rotation"].width  = 140.0
    distribute_custom_sensors_1.nodes["Euler to Rotation"].height = 100.0

    distribute_custom_sensors_1.nodes["Set Material"].width  = 140.0
    distribute_custom_sensors_1.nodes["Set Material"].height = 100.0

    distribute_custom_sensors_1.nodes["Object Info.001"].width  = 140.0
    distribute_custom_sensors_1.nodes["Object Info.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Translate Instances"].width  = 140.0
    distribute_custom_sensors_1.nodes["Translate Instances"].height = 100.0

    distribute_custom_sensors_1.nodes["Rotate Instances"].width  = 140.0
    distribute_custom_sensors_1.nodes["Rotate Instances"].height = 100.0

    distribute_custom_sensors_1.nodes["Realize Instances"].width  = 140.0
    distribute_custom_sensors_1.nodes["Realize Instances"].height = 100.0

    distribute_custom_sensors_1.nodes["Set Material.001"].width  = 140.0
    distribute_custom_sensors_1.nodes["Set Material.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Translate Instances.001"].width  = 140.0
    distribute_custom_sensors_1.nodes["Translate Instances.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Rotate Instances.001"].width  = 140.0
    distribute_custom_sensors_1.nodes["Rotate Instances.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Realize Instances.001"].width  = 140.0
    distribute_custom_sensors_1.nodes["Realize Instances.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Reroute.001"].width  = 14.5
    distribute_custom_sensors_1.nodes["Reroute.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Reroute.002"].width  = 14.5
    distribute_custom_sensors_1.nodes["Reroute.002"].height = 100.0

    distribute_custom_sensors_1.nodes["Math"].width  = 140.0
    distribute_custom_sensors_1.nodes["Math"].height = 100.0

    distribute_custom_sensors_1.nodes["Math.001"].width  = 140.0
    distribute_custom_sensors_1.nodes["Math.001"].height = 100.0

    distribute_custom_sensors_1.nodes["Remove Named Attribute"].width  = 170.0
    distribute_custom_sensors_1.nodes["Remove Named Attribute"].height = 100.0

    distribute_custom_sensors_1.nodes["Instances to Points"].width  = 140.0
    distribute_custom_sensors_1.nodes["Instances to Points"].height = 100.0

    distribute_custom_sensors_1.nodes["Store Named Attribute"].width  = 140.0
    distribute_custom_sensors_1.nodes["Store Named Attribute"].height = 100.0

    distribute_custom_sensors_1.nodes["Points to Vertices"].width  = 140.0
    distribute_custom_sensors_1.nodes["Points to Vertices"].height = 100.0

    distribute_custom_sensors_1.nodes["Sample Index"].width  = 140.0
    distribute_custom_sensors_1.nodes["Sample Index"].height = 100.0

    distribute_custom_sensors_1.nodes["Index"].width  = 140.0
    distribute_custom_sensors_1.nodes["Index"].height = 100.0

    distribute_custom_sensors_1.nodes["Position"].width  = 140.0
    distribute_custom_sensors_1.nodes["Position"].height = 100.0


    # Initialize distribute_custom_sensors_1 links

    # math_001.Value -> combine_xyz.Z
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Math.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Combine XYZ"].inputs[2]
    )
    # group_input.Sensor Mesh -> object_info.Object
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Group Input"].outputs[2],
        distribute_custom_sensors_1.nodes["Object Info"].inputs[0]
    )
    # remove_named_attribute.Geometry -> reroute.Input
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Remove Named Attribute"].outputs[0],
        distribute_custom_sensors_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> instance_on_points.Points
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Reroute"].outputs[0],
        distribute_custom_sensors_1.nodes["Instance on Points"].inputs[0]
    )
    # reroute.Output -> instance_on_points_001.Points
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Reroute"].outputs[0],
        distribute_custom_sensors_1.nodes["Instance on Points.001"].inputs[0]
    )
    # group_input.Euler -> euler_to_rotation.Euler
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Group Input"].outputs[1],
        distribute_custom_sensors_1.nodes["Euler to Rotation"].inputs[0]
    )
    # euler_to_rotation.Rotation -> instance_on_points.Rotation
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Euler to Rotation"].outputs[0],
        distribute_custom_sensors_1.nodes["Instance on Points"].inputs[5]
    )
    # euler_to_rotation.Rotation -> instance_on_points_001.Rotation
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Euler to Rotation"].outputs[0],
        distribute_custom_sensors_1.nodes["Instance on Points.001"].inputs[5]
    )
    # object_info.Scale -> instance_on_points.Scale
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Object Info"].outputs[3],
        distribute_custom_sensors_1.nodes["Instance on Points"].inputs[6]
    )
    # object_info.Geometry -> set_material.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Object Info"].outputs[4],
        distribute_custom_sensors_1.nodes["Set Material"].inputs[0]
    )
    # set_material.Geometry -> instance_on_points.Instance
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Set Material"].outputs[0],
        distribute_custom_sensors_1.nodes["Instance on Points"].inputs[2]
    )
    # group_input.Sensor Negative Mesh -> object_info_001.Object
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Group Input"].outputs[3],
        distribute_custom_sensors_1.nodes["Object Info.001"].inputs[0]
    )
    # instance_on_points.Instances -> translate_instances.Instances
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Instance on Points"].outputs[0],
        distribute_custom_sensors_1.nodes["Translate Instances"].inputs[0]
    )
    # translate_instances.Instances -> rotate_instances.Instances
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Translate Instances"].outputs[0],
        distribute_custom_sensors_1.nodes["Rotate Instances"].inputs[0]
    )
    # rotate_instances.Instances -> realize_instances.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Rotate Instances"].outputs[0],
        distribute_custom_sensors_1.nodes["Realize Instances"].inputs[0]
    )
    # realize_instances.Geometry -> group_output.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Realize Instances"].outputs[0],
        distribute_custom_sensors_1.nodes["Group Output"].inputs[0]
    )
    # set_material_001.Geometry -> instance_on_points_001.Instance
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Set Material.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Instance on Points.001"].inputs[2]
    )
    # object_info_001.Geometry -> set_material_001.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Object Info.001"].outputs[4],
        distribute_custom_sensors_1.nodes["Set Material.001"].inputs[0]
    )
    # instance_on_points_001.Instances -> translate_instances_001.Instances
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Instance on Points.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Translate Instances.001"].inputs[0]
    )
    # translate_instances_001.Instances -> rotate_instances_001.Instances
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Translate Instances.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Rotate Instances.001"].inputs[0]
    )
    # rotate_instances_001.Instances -> realize_instances_001.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Rotate Instances.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Realize Instances.001"].inputs[0]
    )
    # realize_instances_001.Geometry -> group_output.Negative Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Realize Instances.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Group Output"].inputs[1]
    )
    # reroute_001.Output -> translate_instances.Translation
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Reroute.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Translate Instances"].inputs[2]
    )
    # combine_xyz.Vector -> reroute_001.Input
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Combine XYZ"].outputs[0],
        distribute_custom_sensors_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_002.Output -> translate_instances_001.Translation
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Reroute.002"].outputs[0],
        distribute_custom_sensors_1.nodes["Translate Instances.001"].inputs[2]
    )
    # combine_xyz.Vector -> reroute_002.Input
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Combine XYZ"].outputs[0],
        distribute_custom_sensors_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Node Offset -> math.Value
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Group Input"].outputs[4],
        distribute_custom_sensors_1.nodes["Math"].inputs[0]
    )
    # math.Value -> math_001.Value
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Math"].outputs[0],
        distribute_custom_sensors_1.nodes["Math.001"].inputs[0]
    )
    # group_input.Reference Thickness -> math_001.Value
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Group Input"].outputs[5],
        distribute_custom_sensors_1.nodes["Math.001"].inputs[1]
    )
    # group_input.Points -> remove_named_attribute.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Group Input"].outputs[0],
        distribute_custom_sensors_1.nodes["Remove Named Attribute"].inputs[0]
    )
    # rotate_instances_001.Instances -> instances_to_points.Instances
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Rotate Instances.001"].outputs[0],
        distribute_custom_sensors_1.nodes["Instances to Points"].inputs[0]
    )
    # store_named_attribute.Geometry -> group_output.Points
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Store Named Attribute"].outputs[0],
        distribute_custom_sensors_1.nodes["Group Output"].inputs[2]
    )
    # points_to_vertices.Mesh -> store_named_attribute.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Points to Vertices"].outputs[0],
        distribute_custom_sensors_1.nodes["Store Named Attribute"].inputs[0]
    )
    # instances_to_points.Points -> points_to_vertices.Points
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Instances to Points"].outputs[0],
        distribute_custom_sensors_1.nodes["Points to Vertices"].inputs[0]
    )
    # index.Index -> sample_index.Index
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Index"].outputs[0],
        distribute_custom_sensors_1.nodes["Sample Index"].inputs[2]
    )
    # points_to_vertices.Mesh -> sample_index.Geometry
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Points to Vertices"].outputs[0],
        distribute_custom_sensors_1.nodes["Sample Index"].inputs[0]
    )
    # position.Position -> sample_index.Value
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Position"].outputs[0],
        distribute_custom_sensors_1.nodes["Sample Index"].inputs[1]
    )
    # sample_index.Value -> store_named_attribute.Value
    distribute_custom_sensors_1.links.new(
        distribute_custom_sensors_1.nodes["Sample Index"].outputs[0],
        distribute_custom_sensors_1.nodes["Store Named Attribute"].inputs[3]
    )

    return distribute_custom_sensors_1


def cutout_thickness_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Cutout Thickness node group"""
    cutout_thickness_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Cutout Thickness")

    cutout_thickness_1.color_tag = 'NONE'
    cutout_thickness_1.description = ""
    cutout_thickness_1.default_group_node_width = 140
    cutout_thickness_1.show_modifier_manage_panel = True

    # cutout_thickness_1 interface

    # Socket Geometry
    geometry_socket = cutout_thickness_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Top Cut
    top_cut_socket = cutout_thickness_1.interface.new_socket(name="Top Cut", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    top_cut_socket.attribute_domain = 'POINT'
    top_cut_socket.default_input = 'VALUE'
    top_cut_socket.structure_type = 'AUTO'

    # Socket Extruded Mesh
    extruded_mesh_socket = cutout_thickness_1.interface.new_socket(name="Extruded Mesh", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    extruded_mesh_socket.attribute_domain = 'POINT'
    extruded_mesh_socket.default_input = 'VALUE'
    extruded_mesh_socket.structure_type = 'AUTO'

    # Socket Bottom Cut
    bottom_cut_socket = cutout_thickness_1.interface.new_socket(name="Bottom Cut", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    bottom_cut_socket.attribute_domain = 'POINT'
    bottom_cut_socket.default_input = 'VALUE'
    bottom_cut_socket.structure_type = 'AUTO'

    # Socket Side
    side_socket = cutout_thickness_1.interface.new_socket(name="Side", in_out='OUTPUT', socket_type='NodeSocketBool')
    side_socket.default_value = False
    side_socket.attribute_domain = 'POINT'
    side_socket.default_input = 'VALUE'
    side_socket.structure_type = 'AUTO'

    # Socket Input
    input_socket = cutout_thickness_1.interface.new_socket(name="Input", in_out='INPUT', socket_type='NodeSocketGeometry')
    input_socket.attribute_domain = 'POINT'
    input_socket.default_input = 'VALUE'
    input_socket.structure_type = 'AUTO'

    # Socket Offset Scale
    offset_scale_socket = cutout_thickness_1.interface.new_socket(name="Offset Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    offset_scale_socket.default_value = 0.019999999552965164
    offset_scale_socket.min_value = -3.4028234663852886e+38
    offset_scale_socket.max_value = 3.4028234663852886e+38
    offset_scale_socket.subtype = 'NONE'
    offset_scale_socket.attribute_domain = 'POINT'
    offset_scale_socket.default_input = 'VALUE'
    offset_scale_socket.structure_type = 'AUTO'

    # Socket Top Material
    top_material_socket = cutout_thickness_1.interface.new_socket(name="Top Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    top_material_socket.attribute_domain = 'POINT'
    top_material_socket.default_input = 'VALUE'
    top_material_socket.structure_type = 'AUTO'

    # Socket Side Material
    side_material_socket = cutout_thickness_1.interface.new_socket(name="Side Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    side_material_socket.attribute_domain = 'POINT'
    side_material_socket.default_input = 'VALUE'
    side_material_socket.structure_type = 'AUTO'

    # Socket Name
    name_socket = cutout_thickness_1.interface.new_socket(name="Name", in_out='INPUT', socket_type='NodeSocketString')
    name_socket.default_value = ""
    name_socket.subtype = 'NONE'
    name_socket.attribute_domain = 'POINT'
    name_socket.default_input = 'VALUE'
    name_socket.structure_type = 'AUTO'

    # Initialize cutout_thickness_1 nodes

    # Node Group Output
    group_output = cutout_thickness_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = cutout_thickness_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Set Material
    set_material = cutout_thickness_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True

    # Node Set Material.001
    set_material_001 = cutout_thickness_1.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    set_material_001.show_options = True

    # Node Reroute.010
    reroute_010 = cutout_thickness_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketGeometry"
    # Node Reroute.003
    reroute_003 = cutout_thickness_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Set Material.002
    set_material_002 = cutout_thickness_1.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    set_material_002.show_options = True
    # Selection
    set_material_002.inputs[1].default_value = True

    # Node Join Geometry
    join_geometry = cutout_thickness_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Frame.007
    frame_007 = cutout_thickness_1.nodes.new("NodeFrame")
    frame_007.label = "Join Top, Bottom, and Side Cutouts"
    frame_007.name = "Frame.007"
    frame_007.use_custom_color = True
    frame_007.color = (0.4318181574344635, 0.6079999804496765, 0.2556363642215729)
    frame_007.show_options = True
    frame_007.label_size = 30
    frame_007.shrink = True

    # Node Merge by Distance
    merge_by_distance = cutout_thickness_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.show_options = True
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance.inputs[3].default_value = 0.0010000000474974513

    # Node Extrude Mesh
    extrude_mesh = cutout_thickness_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.show_options = True
    extrude_mesh.mode = 'FACES'
    # Selection
    extrude_mesh.inputs[1].default_value = True
    # Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh.inputs[4].default_value = False

    # Node Flip Faces
    flip_faces = cutout_thickness_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    flip_faces.show_options = True
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Reroute
    reroute = cutout_thickness_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketMaterial"
    # Node Store Named Attribute
    store_named_attribute = cutout_thickness_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    # Value
    store_named_attribute.inputs[3].default_value = True

    # Node Boolean Math
    boolean_math = cutout_thickness_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.show_options = True
    boolean_math.operation = 'NOT'

    # Node Viewer
    viewer = cutout_thickness_1.nodes.new("GeometryNodeViewer")
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
    cutout_thickness_1.nodes["Set Material"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Set Material.001"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Reroute.010"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Reroute.003"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Set Material.002"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Join Geometry"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Merge by Distance"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Extrude Mesh"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Flip Faces"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Reroute"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Store Named Attribute"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Boolean Math"].parent = cutout_thickness_1.nodes["Frame.007"]
    cutout_thickness_1.nodes["Viewer"].parent = cutout_thickness_1.nodes["Frame.007"]

    # Set locations
    cutout_thickness_1.nodes["Group Output"].location = (889.3176879882812, 261.690673828125)
    cutout_thickness_1.nodes["Group Input"].location = (-791.9739990234375, 322.9139099121094)
    cutout_thickness_1.nodes["Set Material"].location = (402.9366455078125, -51.0)
    cutout_thickness_1.nodes["Set Material.001"].location = (619.6802978515625, -139.01393127441406)
    cutout_thickness_1.nodes["Reroute.010"].location = (101.4052734375, -548.8909301757812)
    cutout_thickness_1.nodes["Reroute.003"].location = (35.0, -325.13604736328125)
    cutout_thickness_1.nodes["Set Material.002"].location = (806.81640625, -466.34368896484375)
    cutout_thickness_1.nodes["Join Geometry"].location = (1025.804931640625, -315.816650390625)
    cutout_thickness_1.nodes["Frame.007"].location = (-562.9366455078125, 331.0)
    cutout_thickness_1.nodes["Merge by Distance"].location = (1238.96923828125, -271.84100341796875)
    cutout_thickness_1.nodes["Extrude Mesh"].location = (142.9366455078125, -191.0)
    cutout_thickness_1.nodes["Flip Faces"].location = (425.39599609375, -495.77880859375)
    cutout_thickness_1.nodes["Reroute"].location = (478.3724365234375, -194.03118896484375)
    cutout_thickness_1.nodes["Store Named Attribute"].location = (842.9366455078125, -191.0)
    cutout_thickness_1.nodes["Boolean Math"].location = (439.00494384765625, -287.50274658203125)
    cutout_thickness_1.nodes["Viewer"].location = (1022.9366455078125, -71.0)

    # Set dimensions
    cutout_thickness_1.nodes["Group Output"].width  = 140.0
    cutout_thickness_1.nodes["Group Output"].height = 100.0

    cutout_thickness_1.nodes["Group Input"].width  = 140.0
    cutout_thickness_1.nodes["Group Input"].height = 100.0

    cutout_thickness_1.nodes["Set Material"].width  = 140.0
    cutout_thickness_1.nodes["Set Material"].height = 100.0

    cutout_thickness_1.nodes["Set Material.001"].width  = 149.686767578125
    cutout_thickness_1.nodes["Set Material.001"].height = 100.0

    cutout_thickness_1.nodes["Reroute.010"].width  = 10.0
    cutout_thickness_1.nodes["Reroute.010"].height = 100.0

    cutout_thickness_1.nodes["Reroute.003"].width  = 10.0
    cutout_thickness_1.nodes["Reroute.003"].height = 100.0

    cutout_thickness_1.nodes["Set Material.002"].width  = 140.0
    cutout_thickness_1.nodes["Set Material.002"].height = 100.0

    cutout_thickness_1.nodes["Join Geometry"].width  = 140.0
    cutout_thickness_1.nodes["Join Geometry"].height = 100.0

    cutout_thickness_1.nodes["Frame.007"].width  = 1408.9366455078125
    cutout_thickness_1.nodes["Frame.007"].height = 596.0

    cutout_thickness_1.nodes["Merge by Distance"].width  = 140.0
    cutout_thickness_1.nodes["Merge by Distance"].height = 100.0

    cutout_thickness_1.nodes["Extrude Mesh"].width  = 140.0
    cutout_thickness_1.nodes["Extrude Mesh"].height = 100.0

    cutout_thickness_1.nodes["Flip Faces"].width  = 140.0
    cutout_thickness_1.nodes["Flip Faces"].height = 100.0

    cutout_thickness_1.nodes["Reroute"].width  = 10.0
    cutout_thickness_1.nodes["Reroute"].height = 100.0

    cutout_thickness_1.nodes["Store Named Attribute"].width  = 140.0
    cutout_thickness_1.nodes["Store Named Attribute"].height = 100.0

    cutout_thickness_1.nodes["Boolean Math"].width  = 140.0
    cutout_thickness_1.nodes["Boolean Math"].height = 100.0

    cutout_thickness_1.nodes["Viewer"].width  = 140.0
    cutout_thickness_1.nodes["Viewer"].height = 100.0


    # Initialize cutout_thickness_1 links

    # join_geometry.Geometry -> merge_by_distance.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Join Geometry"].outputs[0],
        cutout_thickness_1.nodes["Merge by Distance"].inputs[0]
    )
    # extrude_mesh.Top -> set_material.Selection
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Extrude Mesh"].outputs[1],
        cutout_thickness_1.nodes["Set Material"].inputs[1]
    )
    # set_material_002.Geometry -> join_geometry.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Set Material.002"].outputs[0],
        cutout_thickness_1.nodes["Join Geometry"].inputs[0]
    )
    # reroute_003.Output -> extrude_mesh.Mesh
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Reroute.003"].outputs[0],
        cutout_thickness_1.nodes["Extrude Mesh"].inputs[0]
    )
    # reroute_010.Output -> flip_faces.Mesh
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Reroute.010"].outputs[0],
        cutout_thickness_1.nodes["Flip Faces"].inputs[0]
    )
    # reroute_003.Output -> reroute_010.Input
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Reroute.003"].outputs[0],
        cutout_thickness_1.nodes["Reroute.010"].inputs[0]
    )
    # extrude_mesh.Side -> set_material_001.Selection
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Extrude Mesh"].outputs[2],
        cutout_thickness_1.nodes["Set Material.001"].inputs[1]
    )
    # set_material.Geometry -> set_material_001.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Set Material"].outputs[0],
        cutout_thickness_1.nodes["Set Material.001"].inputs[0]
    )
    # extrude_mesh.Mesh -> set_material.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Extrude Mesh"].outputs[0],
        cutout_thickness_1.nodes["Set Material"].inputs[0]
    )
    # flip_faces.Mesh -> set_material_002.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Flip Faces"].outputs[0],
        cutout_thickness_1.nodes["Set Material.002"].inputs[0]
    )
    # group_input.Input -> reroute_003.Input
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Group Input"].outputs[0],
        cutout_thickness_1.nodes["Reroute.003"].inputs[0]
    )
    # group_input.Offset Scale -> extrude_mesh.Offset Scale
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Group Input"].outputs[1],
        cutout_thickness_1.nodes["Extrude Mesh"].inputs[3]
    )
    # set_material.Geometry -> group_output.Top Cut
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Set Material"].outputs[0],
        cutout_thickness_1.nodes["Group Output"].inputs[1]
    )
    # merge_by_distance.Geometry -> group_output.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Merge by Distance"].outputs[0],
        cutout_thickness_1.nodes["Group Output"].inputs[0]
    )
    # extrude_mesh.Mesh -> group_output.Extruded Mesh
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Extrude Mesh"].outputs[0],
        cutout_thickness_1.nodes["Group Output"].inputs[2]
    )
    # extrude_mesh.Side -> group_output.Side
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Extrude Mesh"].outputs[2],
        cutout_thickness_1.nodes["Group Output"].inputs[4]
    )
    # group_input.Top Material -> set_material.Material
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Group Input"].outputs[2],
        cutout_thickness_1.nodes["Set Material"].inputs[2]
    )
    # reroute.Output -> set_material_001.Material
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Reroute"].outputs[0],
        cutout_thickness_1.nodes["Set Material.001"].inputs[2]
    )
    # group_input.Side Material -> reroute.Input
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Group Input"].outputs[3],
        cutout_thickness_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> set_material_002.Material
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Reroute"].outputs[0],
        cutout_thickness_1.nodes["Set Material.002"].inputs[2]
    )
    # set_material_002.Geometry -> group_output.Bottom Cut
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Set Material.002"].outputs[0],
        cutout_thickness_1.nodes["Group Output"].inputs[3]
    )
    # set_material_001.Geometry -> store_named_attribute.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Set Material.001"].outputs[0],
        cutout_thickness_1.nodes["Store Named Attribute"].inputs[0]
    )
    # group_input.Name -> store_named_attribute.Name
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Group Input"].outputs[4],
        cutout_thickness_1.nodes["Store Named Attribute"].inputs[2]
    )
    # boolean_math.Boolean -> store_named_attribute.Selection
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Boolean Math"].outputs[0],
        cutout_thickness_1.nodes["Store Named Attribute"].inputs[1]
    )
    # extrude_mesh.Side -> boolean_math.Boolean
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Extrude Mesh"].outputs[2],
        cutout_thickness_1.nodes["Boolean Math"].inputs[0]
    )
    # store_named_attribute.Geometry -> viewer.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Store Named Attribute"].outputs[0],
        cutout_thickness_1.nodes["Viewer"].inputs[0]
    )
    # store_named_attribute.Geometry -> join_geometry.Geometry
    cutout_thickness_1.links.new(
        cutout_thickness_1.nodes["Store Named Attribute"].outputs[0],
        cutout_thickness_1.nodes["Join Geometry"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return cutout_thickness_1


def plate_volume_reduced_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Plate Volume Reduced node group"""
    plate_volume_reduced_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Plate Volume Reduced")

    plate_volume_reduced_1.color_tag = 'NONE'
    plate_volume_reduced_1.description = ""
    plate_volume_reduced_1.default_group_node_width = 140
    plate_volume_reduced_1.show_modifier_manage_panel = True

    # plate_volume_reduced_1 interface

    # Socket Geometry
    geometry_socket = plate_volume_reduced_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Bottom Plate
    bottom_plate_socket = plate_volume_reduced_1.interface.new_socket(name="Bottom Plate", in_out='INPUT', socket_type='NodeSocketGeometry')
    bottom_plate_socket.attribute_domain = 'POINT'
    bottom_plate_socket.default_input = 'VALUE'
    bottom_plate_socket.structure_type = 'AUTO'

    # Socket Plate Offset
    plate_offset_socket = plate_volume_reduced_1.interface.new_socket(name="Plate Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    plate_offset_socket.default_value = 0.5
    plate_offset_socket.min_value = -10000.0
    plate_offset_socket.max_value = 10000.0
    plate_offset_socket.subtype = 'NONE'
    plate_offset_socket.attribute_domain = 'POINT'
    plate_offset_socket.default_input = 'VALUE'
    plate_offset_socket.structure_type = 'AUTO'

    # Socket Limit Thickness
    limit_thickness_socket = plate_volume_reduced_1.interface.new_socket(name="Limit Thickness", in_out='INPUT', socket_type='NodeSocketBool')
    limit_thickness_socket.default_value = False
    limit_thickness_socket.attribute_domain = 'POINT'
    limit_thickness_socket.default_input = 'VALUE'
    limit_thickness_socket.structure_type = 'AUTO'

    # Socket Reference Thickness
    reference_thickness_socket = plate_volume_reduced_1.interface.new_socket(name="Reference Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    reference_thickness_socket.default_value = 0.0
    reference_thickness_socket.min_value = -3.4028234663852886e+38
    reference_thickness_socket.max_value = 3.4028234663852886e+38
    reference_thickness_socket.subtype = 'NONE'
    reference_thickness_socket.attribute_domain = 'POINT'
    reference_thickness_socket.default_input = 'VALUE'
    reference_thickness_socket.structure_type = 'AUTO'

    # Socket New Thickness
    new_thickness_socket = plate_volume_reduced_1.interface.new_socket(name="New Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    new_thickness_socket.default_value = 50.0
    new_thickness_socket.min_value = 0.0
    new_thickness_socket.max_value = 200.0
    new_thickness_socket.subtype = 'PERCENTAGE'
    new_thickness_socket.attribute_domain = 'POINT'
    new_thickness_socket.default_input = 'VALUE'
    new_thickness_socket.structure_type = 'AUTO'

    # Socket Top Material
    top_material_socket = plate_volume_reduced_1.interface.new_socket(name="Top Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    top_material_socket.attribute_domain = 'POINT'
    top_material_socket.default_input = 'VALUE'
    top_material_socket.structure_type = 'AUTO'

    # Initialize plate_volume_reduced_1 nodes

    # Node Plate
    plate = plate_volume_reduced_1.nodes.new("NodeGroupOutput")
    plate.label = "Plate"
    plate.name = "Plate"
    plate.show_options = True
    plate.is_active_output = True

    # Node Group Input
    group_input = plate_volume_reduced_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Extrude Mesh.002
    extrude_mesh_002 = plate_volume_reduced_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.show_options = True
    extrude_mesh_002.mode = 'FACES'
    # Selection
    extrude_mesh_002.inputs[1].default_value = True
    # Offset
    extrude_mesh_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh_002.inputs[4].default_value = False

    # Node Math.009
    math_009 = plate_volume_reduced_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.hide = True
    math_009.show_options = True
    math_009.operation = 'MULTIPLY'
    math_009.use_clamp = True

    # Node Delete Geometry.002
    delete_geometry_002 = plate_volume_reduced_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.show_options = True
    delete_geometry_002.domain = 'FACE'
    delete_geometry_002.mode = 'ALL'

    # Node Math.010
    math_010 = plate_volume_reduced_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.hide = True
    math_010.show_options = True
    math_010.operation = 'DIVIDE'
    math_010.use_clamp = False
    # Value_001
    math_010.inputs[1].default_value = 100.0

    # Node Group.003
    group_003 = plate_volume_reduced_1.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.show_options = True
    group_003.node_tree = bpy.data.node_groups[node_tree_names[cutout_thickness_1_node_group]]
    # Socket_9
    group_003.inputs[4].default_value = ""

    # Node Reroute.024
    reroute_024 = plate_volume_reduced_1.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.show_options = True
    reroute_024.socket_idname = "NodeSocketFloat"
    # Node Math.012
    math_012 = plate_volume_reduced_1.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.hide = True
    math_012.show_options = True
    math_012.operation = 'DIVIDE'
    math_012.use_clamp = False
    # Value_001
    math_012.inputs[1].default_value = 100.0

    # Node Math.014
    math_014 = plate_volume_reduced_1.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.show_options = True
    math_014.operation = 'MULTIPLY'
    math_014.use_clamp = False

    # Node Plate\
    plate_ = plate_volume_reduced_1.nodes.new("NodeFrame")
    plate_.label = "Create a Plate"
    plate_.name = "Plate\\"
    plate_.show_options = True
    plate_.label_size = 20
    plate_.shrink = True

    # Node Math.007
    math_007 = plate_volume_reduced_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'SUBTRACT'
    math_007.use_clamp = False

    # Node Math.006
    math_006 = plate_volume_reduced_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'MINIMUM'
    math_006.use_clamp = False

    # Node Switch
    switch = plate_volume_reduced_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'FLOAT'

    # Node Reroute
    reroute = plate_volume_reduced_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketBool"
    # Node Reroute.001
    reroute_001 = plate_volume_reduced_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketBool"
    # Node Viewer
    viewer = plate_volume_reduced_1.nodes.new("GeometryNodeViewer")
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

    # Node Reroute.002
    reroute_002 = plate_volume_reduced_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketMaterial"
    # Set parents
    plate_volume_reduced_1.nodes["Extrude Mesh.002"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Math.009"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Delete Geometry.002"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Math.010"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Group.003"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Reroute.024"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Math.012"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Math.014"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Math.007"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Math.006"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Switch"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Reroute"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Reroute.001"].parent = plate_volume_reduced_1.nodes["Plate\\"]
    plate_volume_reduced_1.nodes["Reroute.002"].parent = plate_volume_reduced_1.nodes["Plate\\"]

    # Set locations
    plate_volume_reduced_1.nodes["Plate"].location = (1026.4322509765625, 314.9958801269531)
    plate_volume_reduced_1.nodes["Group Input"].location = (-1282.3311767578125, 56.3474235534668)
    plate_volume_reduced_1.nodes["Extrude Mesh.002"].location = (1239.4237060546875, -69.34725952148438)
    plate_volume_reduced_1.nodes["Math.009"].location = (1068.3040771484375, -247.78500366210938)
    plate_volume_reduced_1.nodes["Delete Geometry.002"].location = (1498.4700927734375, -36.876068115234375)
    plate_volume_reduced_1.nodes["Math.010"].location = (884.6500244140625, -275.2738952636719)
    plate_volume_reduced_1.nodes["Group.003"].location = (1756.6292724609375, -35.659515380859375)
    plate_volume_reduced_1.nodes["Reroute.024"].location = (690.6966552734375, -238.45370483398438)
    plate_volume_reduced_1.nodes["Math.012"].location = (911.9052124023438, -693.6356201171875)
    plate_volume_reduced_1.nodes["Math.014"].location = (1255.6878662109375, -586.0584716796875)
    plate_volume_reduced_1.nodes["Plate\\"].location = (-940.7990112304688, 289.1333312988281)
    plate_volume_reduced_1.nodes["Math.007"].location = (1253.60205078125, -349.48504638671875)
    plate_volume_reduced_1.nodes["Math.006"].location = (1485.6099853515625, -337.94580078125)
    plate_volume_reduced_1.nodes["Switch"].location = (1669.8916015625, -406.83892822265625)
    plate_volume_reduced_1.nodes["Reroute"].location = (33.8333740234375, -827.2783203125)
    plate_volume_reduced_1.nodes["Reroute.001"].location = (1582.299072265625, -823.520263671875)
    plate_volume_reduced_1.nodes["Viewer"].location = (1048.094482421875, 211.27883911132812)
    plate_volume_reduced_1.nodes["Reroute.002"].location = (1653.351806640625, -254.40301513671875)

    # Set dimensions
    plate_volume_reduced_1.nodes["Plate"].width  = 140.0
    plate_volume_reduced_1.nodes["Plate"].height = 100.0

    plate_volume_reduced_1.nodes["Group Input"].width  = 140.0
    plate_volume_reduced_1.nodes["Group Input"].height = 100.0

    plate_volume_reduced_1.nodes["Extrude Mesh.002"].width  = 140.0
    plate_volume_reduced_1.nodes["Extrude Mesh.002"].height = 100.0

    plate_volume_reduced_1.nodes["Math.009"].width  = 140.0
    plate_volume_reduced_1.nodes["Math.009"].height = 100.0

    plate_volume_reduced_1.nodes["Delete Geometry.002"].width  = 140.0
    plate_volume_reduced_1.nodes["Delete Geometry.002"].height = 100.0

    plate_volume_reduced_1.nodes["Math.010"].width  = 140.0
    plate_volume_reduced_1.nodes["Math.010"].height = 100.0

    plate_volume_reduced_1.nodes["Group.003"].width  = 200.0
    plate_volume_reduced_1.nodes["Group.003"].height = 100.0

    plate_volume_reduced_1.nodes["Reroute.024"].width  = 14.5
    plate_volume_reduced_1.nodes["Reroute.024"].height = 100.0

    plate_volume_reduced_1.nodes["Math.012"].width  = 140.0
    plate_volume_reduced_1.nodes["Math.012"].height = 100.0

    plate_volume_reduced_1.nodes["Math.014"].width  = 140.0
    plate_volume_reduced_1.nodes["Math.014"].height = 100.0

    plate_volume_reduced_1.nodes["Plate\\"].width  = 1985.799072265625
    plate_volume_reduced_1.nodes["Plate\\"].height = 861.111572265625

    plate_volume_reduced_1.nodes["Math.007"].width  = 140.0
    plate_volume_reduced_1.nodes["Math.007"].height = 100.0

    plate_volume_reduced_1.nodes["Math.006"].width  = 140.0
    plate_volume_reduced_1.nodes["Math.006"].height = 100.0

    plate_volume_reduced_1.nodes["Switch"].width  = 140.0
    plate_volume_reduced_1.nodes["Switch"].height = 100.0

    plate_volume_reduced_1.nodes["Reroute"].width  = 14.5
    plate_volume_reduced_1.nodes["Reroute"].height = 100.0

    plate_volume_reduced_1.nodes["Reroute.001"].width  = 14.5
    plate_volume_reduced_1.nodes["Reroute.001"].height = 100.0

    plate_volume_reduced_1.nodes["Viewer"].width  = 140.0
    plate_volume_reduced_1.nodes["Viewer"].height = 100.0

    plate_volume_reduced_1.nodes["Reroute.002"].width  = 14.5
    plate_volume_reduced_1.nodes["Reroute.002"].height = 100.0


    # Initialize plate_volume_reduced_1 links

    # math_012.Value -> math_014.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.012"].outputs[0],
        plate_volume_reduced_1.nodes["Math.014"].inputs[1]
    )
    # reroute_024.Output -> math_009.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Reroute.024"].outputs[0],
        plate_volume_reduced_1.nodes["Math.009"].inputs[0]
    )
    # math_010.Value -> math_009.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.010"].outputs[0],
        plate_volume_reduced_1.nodes["Math.009"].inputs[1]
    )
    # reroute_024.Output -> math_014.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Reroute.024"].outputs[0],
        plate_volume_reduced_1.nodes["Math.014"].inputs[0]
    )
    # math_009.Value -> extrude_mesh_002.Offset Scale
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.009"].outputs[0],
        plate_volume_reduced_1.nodes["Extrude Mesh.002"].inputs[3]
    )
    # extrude_mesh_002.Mesh -> delete_geometry_002.Geometry
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Extrude Mesh.002"].outputs[0],
        plate_volume_reduced_1.nodes["Delete Geometry.002"].inputs[0]
    )
    # delete_geometry_002.Geometry -> group_003.Input
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Delete Geometry.002"].outputs[0],
        plate_volume_reduced_1.nodes["Group.003"].inputs[0]
    )
    # extrude_mesh_002.Side -> delete_geometry_002.Selection
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Extrude Mesh.002"].outputs[2],
        plate_volume_reduced_1.nodes["Delete Geometry.002"].inputs[1]
    )
    # group_input.Reference Thickness -> reroute_024.Input
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group Input"].outputs[3],
        plate_volume_reduced_1.nodes["Reroute.024"].inputs[0]
    )
    # group_input.New Thickness -> math_012.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group Input"].outputs[4],
        plate_volume_reduced_1.nodes["Math.012"].inputs[0]
    )
    # group_input.Plate Offset -> math_010.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group Input"].outputs[1],
        plate_volume_reduced_1.nodes["Math.010"].inputs[0]
    )
    # group_003.Geometry -> plate.Geometry
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group.003"].outputs[0],
        plate_volume_reduced_1.nodes["Plate"].inputs[0]
    )
    # math_007.Value -> math_006.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.007"].outputs[0],
        plate_volume_reduced_1.nodes["Math.006"].inputs[0]
    )
    # math_014.Value -> math_006.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.014"].outputs[0],
        plate_volume_reduced_1.nodes["Math.006"].inputs[1]
    )
    # math_009.Value -> math_007.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.009"].outputs[0],
        plate_volume_reduced_1.nodes["Math.007"].inputs[1]
    )
    # reroute_024.Output -> math_007.Value
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Reroute.024"].outputs[0],
        plate_volume_reduced_1.nodes["Math.007"].inputs[0]
    )
    # reroute_001.Output -> switch.Switch
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Reroute.001"].outputs[0],
        plate_volume_reduced_1.nodes["Switch"].inputs[0]
    )
    # math_006.Value -> switch.True
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.006"].outputs[0],
        plate_volume_reduced_1.nodes["Switch"].inputs[2]
    )
    # math_014.Value -> switch.False
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Math.014"].outputs[0],
        plate_volume_reduced_1.nodes["Switch"].inputs[1]
    )
    # switch.Output -> group_003.Offset Scale
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Switch"].outputs[0],
        plate_volume_reduced_1.nodes["Group.003"].inputs[1]
    )
    # group_input.Limit Thickness -> reroute.Input
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group Input"].outputs[2],
        plate_volume_reduced_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> reroute_001.Input
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Reroute"].outputs[0],
        plate_volume_reduced_1.nodes["Reroute.001"].inputs[0]
    )
    # group_003.Geometry -> viewer.Geometry
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group.003"].outputs[0],
        plate_volume_reduced_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Bottom Plate -> extrude_mesh_002.Mesh
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group Input"].outputs[0],
        plate_volume_reduced_1.nodes["Extrude Mesh.002"].inputs[0]
    )
    # reroute_002.Output -> group_003.Top Material
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Reroute.002"].outputs[0],
        plate_volume_reduced_1.nodes["Group.003"].inputs[2]
    )
    # group_input.Top Material -> reroute_002.Input
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Group Input"].outputs[5],
        plate_volume_reduced_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_002.Output -> group_003.Side Material
    plate_volume_reduced_1.links.new(
        plate_volume_reduced_1.nodes["Reroute.002"].outputs[0],
        plate_volume_reduced_1.nodes["Group.003"].inputs[3]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return plate_volume_reduced_1


def cut_disk_custom_sensor_layer_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Cut Disk Custom Sensor Layer node group"""
    cut_disk_custom_sensor_layer_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Cut Disk Custom Sensor Layer")

    cut_disk_custom_sensor_layer_1.color_tag = 'NONE'
    cut_disk_custom_sensor_layer_1.description = ""
    cut_disk_custom_sensor_layer_1.default_group_node_width = 140
    cut_disk_custom_sensor_layer_1.show_modifier_manage_panel = True

    # cut_disk_custom_sensor_layer_1 interface

    # Socket Geometry
    geometry_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Stem Points
    stem_points_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Stem Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    stem_points_socket.attribute_domain = 'POINT'
    stem_points_socket.default_input = 'VALUE'
    stem_points_socket.structure_type = 'AUTO'

    # Socket Shape
    shape_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Shape", in_out='INPUT', socket_type='NodeSocketGeometry')
    shape_socket.attribute_domain = 'POINT'
    shape_socket.default_input = 'VALUE'
    shape_socket.structure_type = 'AUTO'

    # Socket Bottom Plate
    bottom_plate_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Bottom Plate", in_out='INPUT', socket_type='NodeSocketGeometry')
    bottom_plate_socket.attribute_domain = 'POINT'
    bottom_plate_socket.default_input = 'VALUE'
    bottom_plate_socket.structure_type = 'AUTO'

    # Socket Reference Thickness
    reference_thickness_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Reference Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    reference_thickness_socket.default_value = 0.0
    reference_thickness_socket.min_value = 0.0
    reference_thickness_socket.max_value = 3.4028234663852886e+38
    reference_thickness_socket.subtype = 'NONE'
    reference_thickness_socket.attribute_domain = 'POINT'
    reference_thickness_socket.description = "Match this to the dermis"
    reference_thickness_socket.default_input = 'VALUE'
    reference_thickness_socket.structure_type = 'AUTO'

    # Panel Shape Settings
    shape_settings_panel = cut_disk_custom_sensor_layer_1.interface.new_panel("Shape Settings")
    # Socket Material
    material_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = shape_settings_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    # Socket Node Offset
    node_offset_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Node Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    node_offset_socket.default_value = 0.5
    node_offset_socket.min_value = -10000.0
    node_offset_socket.max_value = 10000.0
    node_offset_socket.subtype = 'NONE'
    node_offset_socket.attribute_domain = 'POINT'
    node_offset_socket.default_input = 'VALUE'
    node_offset_socket.structure_type = 'AUTO'

    # Socket Node Thickness
    node_thickness_socket = cut_disk_custom_sensor_layer_1.interface.new_socket(name="Node Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    node_thickness_socket.default_value = 0.5
    node_thickness_socket.min_value = -10000.0
    node_thickness_socket.max_value = 10000.0
    node_thickness_socket.subtype = 'NONE'
    node_thickness_socket.attribute_domain = 'POINT'
    node_thickness_socket.default_input = 'VALUE'
    node_thickness_socket.structure_type = 'AUTO'


    # Initialize cut_disk_custom_sensor_layer_1 nodes

    # Node Group Output
    group_output = cut_disk_custom_sensor_layer_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = cut_disk_custom_sensor_layer_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Mesh Boolean.005
    mesh_boolean_005 = cut_disk_custom_sensor_layer_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_005.name = "Mesh Boolean.005"
    mesh_boolean_005.show_options = True
    mesh_boolean_005.operation = 'INTERSECT'
    mesh_boolean_005.solver = 'EXACT'
    # Self Intersection
    mesh_boolean_005.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_005.inputs[3].default_value = False

    # Node Flip Faces
    flip_faces = cut_disk_custom_sensor_layer_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    flip_faces.show_options = True
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Set Material
    set_material = cut_disk_custom_sensor_layer_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Plate Volume Reduced
    plate_volume_reduced = cut_disk_custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    plate_volume_reduced.name = "Plate Volume Reduced"
    plate_volume_reduced.show_options = True
    plate_volume_reduced.node_tree = bpy.data.node_groups[node_tree_names[plate_volume_reduced_1_node_group]]
    # Socket_9
    plate_volume_reduced.inputs[2].default_value = False
    if "Sensor Mat" in bpy.data.materials:
        plate_volume_reduced.inputs[5].default_value = bpy.data.materials["Sensor Mat"]

    # Set locations
    cut_disk_custom_sensor_layer_1.nodes["Group Output"].location = (120.0, 60.0)
    cut_disk_custom_sensor_layer_1.nodes["Group Input"].location = (-1500.0, 20.0)
    cut_disk_custom_sensor_layer_1.nodes["Mesh Boolean.005"].location = (-120.0, 80.0)
    cut_disk_custom_sensor_layer_1.nodes["Flip Faces"].location = (-1080.0, -20.0)
    cut_disk_custom_sensor_layer_1.nodes["Set Material"].location = (-480.0, 80.0)
    cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].location = (-700.0, -99.99999237060547)

    # Set dimensions
    cut_disk_custom_sensor_layer_1.nodes["Group Output"].width  = 140.0
    cut_disk_custom_sensor_layer_1.nodes["Group Output"].height = 100.0

    cut_disk_custom_sensor_layer_1.nodes["Group Input"].width  = 140.0
    cut_disk_custom_sensor_layer_1.nodes["Group Input"].height = 100.0

    cut_disk_custom_sensor_layer_1.nodes["Mesh Boolean.005"].width  = 140.0
    cut_disk_custom_sensor_layer_1.nodes["Mesh Boolean.005"].height = 100.0

    cut_disk_custom_sensor_layer_1.nodes["Flip Faces"].width  = 140.0
    cut_disk_custom_sensor_layer_1.nodes["Flip Faces"].height = 100.0

    cut_disk_custom_sensor_layer_1.nodes["Set Material"].width  = 140.0
    cut_disk_custom_sensor_layer_1.nodes["Set Material"].height = 100.0

    cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].width  = 280.0
    cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].height = 100.0


    # Initialize cut_disk_custom_sensor_layer_1 links

    # group_input.Bottom Plate -> flip_faces.Mesh
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Group Input"].outputs[1],
        cut_disk_custom_sensor_layer_1.nodes["Flip Faces"].inputs[0]
    )
    # mesh_boolean_005.Mesh -> group_output.Geometry
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Mesh Boolean.005"].outputs[0],
        cut_disk_custom_sensor_layer_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Shape -> set_material.Geometry
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Group Input"].outputs[0],
        cut_disk_custom_sensor_layer_1.nodes["Set Material"].inputs[0]
    )
    # group_input.Material -> set_material.Material
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Group Input"].outputs[3],
        cut_disk_custom_sensor_layer_1.nodes["Set Material"].inputs[2]
    )
    # set_material.Geometry -> mesh_boolean_005.Mesh
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Set Material"].outputs[0],
        cut_disk_custom_sensor_layer_1.nodes["Mesh Boolean.005"].inputs[1]
    )
    # flip_faces.Mesh -> plate_volume_reduced.Bottom Plate
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Flip Faces"].outputs[0],
        cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].inputs[0]
    )
    # group_input.Reference Thickness -> plate_volume_reduced.Reference Thickness
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Group Input"].outputs[2],
        cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].inputs[3]
    )
    # group_input.Node Offset -> plate_volume_reduced.Plate Offset
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Group Input"].outputs[4],
        cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].inputs[1]
    )
    # group_input.Node Thickness -> plate_volume_reduced.New Thickness
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Group Input"].outputs[5],
        cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].inputs[4]
    )
    # plate_volume_reduced.Geometry -> mesh_boolean_005.Mesh
    cut_disk_custom_sensor_layer_1.links.new(
        cut_disk_custom_sensor_layer_1.nodes["Plate Volume Reduced"].outputs[0],
        cut_disk_custom_sensor_layer_1.nodes["Mesh Boolean.005"].inputs[1]
    )

    return cut_disk_custom_sensor_layer_1


def separate_and_remove_att_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Separate and Remove Att node group"""
    separate_and_remove_att_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Separate and Remove Att")

    separate_and_remove_att_1.color_tag = 'NONE'
    separate_and_remove_att_1.description = ""
    separate_and_remove_att_1.default_group_node_width = 140
    separate_and_remove_att_1.show_modifier_manage_panel = True

    # separate_and_remove_att_1 interface

    # Socket Selection
    selection_socket = separate_and_remove_att_1.interface.new_socket(name="Selection", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    selection_socket.attribute_domain = 'POINT'
    selection_socket.description = "The parts of the geometry in the selection"
    selection_socket.default_input = 'VALUE'
    selection_socket.structure_type = 'AUTO'

    # Socket Inverted
    inverted_socket = separate_and_remove_att_1.interface.new_socket(name="Inverted", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    inverted_socket.attribute_domain = 'POINT'
    inverted_socket.description = "The parts of the geometry not in the selection"
    inverted_socket.default_input = 'VALUE'
    inverted_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket = separate_and_remove_att_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Attribute
    attribute_socket = separate_and_remove_att_1.interface.new_socket(name="Attribute", in_out='INPUT', socket_type='NodeSocketString')
    attribute_socket.default_value = ""
    attribute_socket.subtype = 'NONE'
    attribute_socket.attribute_domain = 'POINT'
    attribute_socket.default_input = 'VALUE'
    attribute_socket.structure_type = 'AUTO'

    # Socket Additional Remove
    additional_remove_socket = separate_and_remove_att_1.interface.new_socket(name="Additional Remove", in_out='INPUT', socket_type='NodeSocketString')
    additional_remove_socket.default_value = ""
    additional_remove_socket.subtype = 'NONE'
    additional_remove_socket.attribute_domain = 'POINT'
    additional_remove_socket.default_input = 'VALUE'
    additional_remove_socket.structure_type = 'AUTO'

    # Socket Additional Remove
    additional_remove_socket_1 = separate_and_remove_att_1.interface.new_socket(name="Additional Remove", in_out='INPUT', socket_type='NodeSocketString')
    additional_remove_socket_1.default_value = ""
    additional_remove_socket_1.subtype = 'NONE'
    additional_remove_socket_1.attribute_domain = 'POINT'
    additional_remove_socket_1.default_input = 'VALUE'
    additional_remove_socket_1.structure_type = 'AUTO'

    # Initialize separate_and_remove_att_1 nodes

    # Node Group Output
    group_output = separate_and_remove_att_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = separate_and_remove_att_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Separate Geometry.001
    separate_geometry_001 = separate_and_remove_att_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_001.name = "Separate Geometry.001"
    separate_geometry_001.hide = True
    separate_geometry_001.show_options = True
    separate_geometry_001.domain = 'POINT'

    # Node Named Attribute.002
    named_attribute_002 = separate_and_remove_att_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.show_options = True
    named_attribute_002.data_type = 'BOOLEAN'

    # Node Remove Named Attribute
    remove_named_attribute = separate_and_remove_att_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute.name = "Remove Named Attribute"
    remove_named_attribute.show_options = True
    # Pattern Mode
    remove_named_attribute.inputs[1].default_value = 'Exact'

    # Node Remove Named Attribute.001
    remove_named_attribute_001 = separate_and_remove_att_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute_001.name = "Remove Named Attribute.001"
    remove_named_attribute_001.show_options = True
    # Pattern Mode
    remove_named_attribute_001.inputs[1].default_value = 'Exact'

    # Node Reroute
    reroute = separate_and_remove_att_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketString"
    # Node Reroute.001
    reroute_001 = separate_and_remove_att_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketString"
    # Node Remove Named Attribute.002
    remove_named_attribute_002 = separate_and_remove_att_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute_002.name = "Remove Named Attribute.002"
    remove_named_attribute_002.show_options = True
    # Pattern Mode
    remove_named_attribute_002.inputs[1].default_value = 'Exact'

    # Node Remove Named Attribute.003
    remove_named_attribute_003 = separate_and_remove_att_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute_003.name = "Remove Named Attribute.003"
    remove_named_attribute_003.show_options = True
    # Pattern Mode
    remove_named_attribute_003.inputs[1].default_value = 'Exact'

    # Node Remove Named Attribute.004
    remove_named_attribute_004 = separate_and_remove_att_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute_004.name = "Remove Named Attribute.004"
    remove_named_attribute_004.show_options = True
    # Pattern Mode
    remove_named_attribute_004.inputs[1].default_value = 'Exact'

    # Node Remove Named Attribute.005
    remove_named_attribute_005 = separate_and_remove_att_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute_005.name = "Remove Named Attribute.005"
    remove_named_attribute_005.show_options = True
    # Pattern Mode
    remove_named_attribute_005.inputs[1].default_value = 'Exact'

    # Node Reroute.002
    reroute_002 = separate_and_remove_att_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketString"
    # Node Reroute.003
    reroute_003 = separate_and_remove_att_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketString"
    # Set locations
    separate_and_remove_att_1.nodes["Group Output"].location = (540.0, 0.0)
    separate_and_remove_att_1.nodes["Group Input"].location = (-1260.0, 0.0)
    separate_and_remove_att_1.nodes["Separate Geometry.001"].location = (-500.0, -40.0)
    separate_and_remove_att_1.nodes["Named Attribute.002"].location = (-640.0, -200.0)
    separate_and_remove_att_1.nodes["Remove Named Attribute"].location = (-300.0, 100.0)
    separate_and_remove_att_1.nodes["Remove Named Attribute.001"].location = (-300.0, -40.0)
    separate_and_remove_att_1.nodes["Reroute"].location = (-688.8182373046875, -176.64776611328125)
    separate_and_remove_att_1.nodes["Reroute.001"].location = (-331.44000244140625, -124.05705261230469)
    separate_and_remove_att_1.nodes["Remove Named Attribute.002"].location = (-20.0, -40.0)
    separate_and_remove_att_1.nodes["Remove Named Attribute.003"].location = (-20.0, 100.0)
    separate_and_remove_att_1.nodes["Remove Named Attribute.004"].location = (200.0, -40.0)
    separate_and_remove_att_1.nodes["Remove Named Attribute.005"].location = (200.0, 100.0)
    separate_and_remove_att_1.nodes["Reroute.002"].location = (-80.0, -200.0)
    separate_and_remove_att_1.nodes["Reroute.003"].location = (160.0, -240.0)

    # Set dimensions
    separate_and_remove_att_1.nodes["Group Output"].width  = 140.0
    separate_and_remove_att_1.nodes["Group Output"].height = 100.0

    separate_and_remove_att_1.nodes["Group Input"].width  = 140.0
    separate_and_remove_att_1.nodes["Group Input"].height = 100.0

    separate_and_remove_att_1.nodes["Separate Geometry.001"].width  = 140.0
    separate_and_remove_att_1.nodes["Separate Geometry.001"].height = 100.0

    separate_and_remove_att_1.nodes["Named Attribute.002"].width  = 140.0
    separate_and_remove_att_1.nodes["Named Attribute.002"].height = 100.0

    separate_and_remove_att_1.nodes["Remove Named Attribute"].width  = 170.0
    separate_and_remove_att_1.nodes["Remove Named Attribute"].height = 100.0

    separate_and_remove_att_1.nodes["Remove Named Attribute.001"].width  = 170.0
    separate_and_remove_att_1.nodes["Remove Named Attribute.001"].height = 100.0

    separate_and_remove_att_1.nodes["Reroute"].width  = 10.0
    separate_and_remove_att_1.nodes["Reroute"].height = 100.0

    separate_and_remove_att_1.nodes["Reroute.001"].width  = 10.0
    separate_and_remove_att_1.nodes["Reroute.001"].height = 100.0

    separate_and_remove_att_1.nodes["Remove Named Attribute.002"].width  = 170.0
    separate_and_remove_att_1.nodes["Remove Named Attribute.002"].height = 100.0

    separate_and_remove_att_1.nodes["Remove Named Attribute.003"].width  = 170.0
    separate_and_remove_att_1.nodes["Remove Named Attribute.003"].height = 100.0

    separate_and_remove_att_1.nodes["Remove Named Attribute.004"].width  = 170.0
    separate_and_remove_att_1.nodes["Remove Named Attribute.004"].height = 100.0

    separate_and_remove_att_1.nodes["Remove Named Attribute.005"].width  = 170.0
    separate_and_remove_att_1.nodes["Remove Named Attribute.005"].height = 100.0

    separate_and_remove_att_1.nodes["Reroute.002"].width  = 10.0
    separate_and_remove_att_1.nodes["Reroute.002"].height = 100.0

    separate_and_remove_att_1.nodes["Reroute.003"].width  = 10.0
    separate_and_remove_att_1.nodes["Reroute.003"].height = 100.0


    # Initialize separate_and_remove_att_1 links

    # reroute.Output -> named_attribute_002.Name
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute"].outputs[0],
        separate_and_remove_att_1.nodes["Named Attribute.002"].inputs[0]
    )
    # named_attribute_002.Attribute -> separate_geometry_001.Selection
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Named Attribute.002"].outputs[0],
        separate_and_remove_att_1.nodes["Separate Geometry.001"].inputs[1]
    )
    # group_input.Geometry -> separate_geometry_001.Geometry
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Group Input"].outputs[0],
        separate_and_remove_att_1.nodes["Separate Geometry.001"].inputs[0]
    )
    # remove_named_attribute_005.Geometry -> group_output.Selection
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Remove Named Attribute.005"].outputs[0],
        separate_and_remove_att_1.nodes["Group Output"].inputs[0]
    )
    # remove_named_attribute_004.Geometry -> group_output.Inverted
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Remove Named Attribute.004"].outputs[0],
        separate_and_remove_att_1.nodes["Group Output"].inputs[1]
    )
    # separate_geometry_001.Selection -> remove_named_attribute.Geometry
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Separate Geometry.001"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute"].inputs[0]
    )
    # separate_geometry_001.Inverted -> remove_named_attribute_001.Geometry
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Separate Geometry.001"].outputs[1],
        separate_and_remove_att_1.nodes["Remove Named Attribute.001"].inputs[0]
    )
    # reroute_001.Output -> remove_named_attribute_001.Name
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute.001"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.001"].inputs[2]
    )
    # reroute.Output -> reroute_001.Input
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute"].outputs[0],
        separate_and_remove_att_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_001.Output -> remove_named_attribute.Name
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute.001"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute"].inputs[2]
    )
    # group_input.Attribute -> reroute.Input
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Group Input"].outputs[1],
        separate_and_remove_att_1.nodes["Reroute"].inputs[0]
    )
    # remove_named_attribute_001.Geometry -> remove_named_attribute_002.Geometry
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Remove Named Attribute.001"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.002"].inputs[0]
    )
    # remove_named_attribute.Geometry -> remove_named_attribute_003.Geometry
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Remove Named Attribute"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.003"].inputs[0]
    )
    # remove_named_attribute_002.Geometry -> remove_named_attribute_004.Geometry
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Remove Named Attribute.002"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.004"].inputs[0]
    )
    # remove_named_attribute_003.Geometry -> remove_named_attribute_005.Geometry
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Remove Named Attribute.003"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.005"].inputs[0]
    )
    # reroute_002.Output -> remove_named_attribute_002.Name
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute.002"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.002"].inputs[2]
    )
    # group_input.Additional Remove -> reroute_002.Input
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Group Input"].outputs[2],
        separate_and_remove_att_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_002.Output -> remove_named_attribute_003.Name
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute.002"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.003"].inputs[2]
    )
    # reroute_003.Output -> remove_named_attribute_004.Name
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute.003"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.004"].inputs[2]
    )
    # group_input.Additional Remove -> reroute_003.Input
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Group Input"].outputs[3],
        separate_and_remove_att_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_003.Output -> remove_named_attribute_005.Name
    separate_and_remove_att_1.links.new(
        separate_and_remove_att_1.nodes["Reroute.003"].outputs[0],
        separate_and_remove_att_1.nodes["Remove Named Attribute.005"].inputs[2]
    )

    return separate_and_remove_att_1


def custom_sensor_layer_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Custom Sensor Layer node group"""
    custom_sensor_layer_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Custom Sensor Layer")

    custom_sensor_layer_1.color_tag = 'NONE'
    custom_sensor_layer_1.description = ""
    custom_sensor_layer_1.default_group_node_width = 140
    custom_sensor_layer_1.is_modifier = True
    custom_sensor_layer_1.show_modifier_manage_panel = True

    # custom_sensor_layer_1 interface

    # Socket Geometry
    geometry_socket = custom_sensor_layer_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Sensor Mounts
    sensor_mounts_socket = custom_sensor_layer_1.interface.new_socket(name="Sensor Mounts", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_mounts_socket.attribute_domain = 'POINT'
    sensor_mounts_socket.default_input = 'VALUE'
    sensor_mounts_socket.structure_type = 'AUTO'

    # Socket Negative Geometry
    negative_geometry_socket = custom_sensor_layer_1.interface.new_socket(name="Negative Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    negative_geometry_socket.attribute_domain = 'POINT'
    negative_geometry_socket.default_input = 'VALUE'
    negative_geometry_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket = custom_sensor_layer_1.interface.new_socket(name="Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = custom_sensor_layer_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Isolate
    isolate_socket = custom_sensor_layer_1.interface.new_socket(name="Isolate", in_out='INPUT', socket_type='NodeSocketBool')
    isolate_socket.default_value = False
    isolate_socket.attribute_domain = 'POINT'
    isolate_socket.default_input = 'VALUE'
    isolate_socket.structure_type = 'AUTO'

    # Socket Include Original Geometry
    include_original_geometry_socket = custom_sensor_layer_1.interface.new_socket(name="Include Original Geometry", in_out='INPUT', socket_type='NodeSocketBool')
    include_original_geometry_socket.default_value = True
    include_original_geometry_socket.attribute_domain = 'POINT'
    include_original_geometry_socket.default_input = 'VALUE'
    include_original_geometry_socket.structure_type = 'AUTO'

    # Socket Mesh Union
    mesh_union_socket = custom_sensor_layer_1.interface.new_socket(name="Mesh Union", in_out='INPUT', socket_type='NodeSocketBool')
    mesh_union_socket.default_value = False
    mesh_union_socket.attribute_domain = 'POINT'
    mesh_union_socket.description = "Computationally expensive. Helps if the sensors are disjointed"
    mesh_union_socket.default_input = 'VALUE'
    mesh_union_socket.structure_type = 'AUTO'

    # Panel Node Shape
    node_shape_panel = custom_sensor_layer_1.interface.new_panel("Node Shape")
    # Socket Sensor Mesh
    sensor_mesh_socket = custom_sensor_layer_1.interface.new_socket(name="Sensor Mesh", in_out='INPUT', socket_type='NodeSocketObject', parent = node_shape_panel)
    sensor_mesh_socket.attribute_domain = 'POINT'
    sensor_mesh_socket.default_input = 'VALUE'
    sensor_mesh_socket.structure_type = 'AUTO'

    # Socket Sensor Negative Mesh
    sensor_negative_mesh_socket = custom_sensor_layer_1.interface.new_socket(name="Sensor Negative Mesh", in_out='INPUT', socket_type='NodeSocketObject', parent = node_shape_panel)
    sensor_negative_mesh_socket.attribute_domain = 'POINT'
    sensor_negative_mesh_socket.default_input = 'VALUE'
    sensor_negative_mesh_socket.structure_type = 'AUTO'

    # Socket Node Offset
    node_offset_socket = custom_sensor_layer_1.interface.new_socket(name="Node Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = node_shape_panel)
    node_offset_socket.default_value = 50.0
    node_offset_socket.min_value = -200.0
    node_offset_socket.max_value = 200.0
    node_offset_socket.subtype = 'PERCENTAGE'
    node_offset_socket.attribute_domain = 'POINT'
    node_offset_socket.default_input = 'VALUE'
    node_offset_socket.structure_type = 'AUTO'

    # Socket Node Thickness
    node_thickness_socket = custom_sensor_layer_1.interface.new_socket(name="Node Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = node_shape_panel)
    node_thickness_socket.default_value = 300.0
    node_thickness_socket.min_value = 0.0
    node_thickness_socket.max_value = 500.0
    node_thickness_socket.subtype = 'PERCENTAGE'
    node_thickness_socket.attribute_domain = 'POINT'
    node_thickness_socket.default_input = 'VALUE'
    node_thickness_socket.structure_type = 'AUTO'

    # Socket Material
    material_socket = custom_sensor_layer_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = node_shape_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'


    # Panel Options
    options_panel = custom_sensor_layer_1.interface.new_panel("Options", default_closed=True)
    # Socket Options
    options_socket = custom_sensor_layer_1.interface.new_socket(name="Options", in_out='INPUT', socket_type='NodeSocketMenu', parent = options_panel)
    options_socket.attribute_domain = 'POINT'
    options_socket.default_input = 'VALUE'
    options_socket.structure_type = 'AUTO'
    options_socket.optional_label = True

    # Socket Application Surface
    application_surface_socket = custom_sensor_layer_1.interface.new_socket(name="Application Surface", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    application_surface_socket.default_value = "dermis_top"
    application_surface_socket.subtype = 'NONE'
    application_surface_socket.attribute_domain = 'POINT'
    application_surface_socket.default_input = 'VALUE'
    application_surface_socket.structure_type = 'AUTO'

    # Socket Dermis
    dermis_socket = custom_sensor_layer_1.interface.new_socket(name="Dermis", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    dermis_socket.default_value = "dermis"
    dermis_socket.subtype = 'NONE'
    dermis_socket.attribute_domain = 'POINT'
    dermis_socket.default_input = 'VALUE'
    dermis_socket.structure_type = 'AUTO'

    # Socket Dermis Bottom
    dermis_bottom_socket = custom_sensor_layer_1.interface.new_socket(name="Dermis Bottom", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    dermis_bottom_socket.default_value = "dermis_bottom"
    dermis_bottom_socket.subtype = 'NONE'
    dermis_bottom_socket.attribute_domain = 'POINT'
    dermis_bottom_socket.default_input = 'VALUE'
    dermis_bottom_socket.structure_type = 'AUTO'

    # Socket Sensor Point Label
    sensor_point_label_socket = custom_sensor_layer_1.interface.new_socket(name="Sensor Point Label", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    sensor_point_label_socket.default_value = "sensor_point"
    sensor_point_label_socket.subtype = 'NONE'
    sensor_point_label_socket.attribute_domain = 'POINT'
    sensor_point_label_socket.default_input = 'VALUE'
    sensor_point_label_socket.structure_type = 'AUTO'


    # Initialize custom_sensor_layer_1 nodes

    # Node Group Input
    group_input = custom_sensor_layer_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = custom_sensor_layer_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Join Geometry
    join_geometry = custom_sensor_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Switch
    switch = custom_sensor_layer_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'GEOMETRY'

    # Node Menu Switch
    menu_switch = custom_sensor_layer_1.nodes.new("GeometryNodeMenuSwitch")
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
    menu_switch.inputs[1].default_value = False
    # Item_1
    menu_switch.inputs[2].default_value = True

    # Node Reroute.003
    reroute_003 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.005
    reroute_005 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.009
    reroute_009 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.011
    reroute_011 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketFloatPercentage"
    # Node Distribute Custom Sensors
    distribute_custom_sensors = custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    distribute_custom_sensors.name = "Distribute Custom Sensors"
    distribute_custom_sensors.show_options = True
    distribute_custom_sensors.node_tree = bpy.data.node_groups[node_tree_names[distribute_custom_sensors_1_node_group]]

    # Node Sample Index
    sample_index = custom_sensor_layer_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT'
    sample_index.domain = 'POINT'
    # Index
    sample_index.inputs[2].default_value = 0

    # Node Named Attribute.001
    named_attribute_001 = custom_sensor_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'FLOAT'
    # Name
    named_attribute_001.inputs[0].default_value = "thickness"

    # Node Mesh Boolean
    mesh_boolean = custom_sensor_layer_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.show_options = True
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'FLOAT'

    # Node Reroute.001
    reroute_001 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Switch.001
    switch_001 = custom_sensor_layer_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'STRING'
    # False
    switch_001.inputs[1].default_value = "dermis_top"

    # Node Switch.002
    switch_002 = custom_sensor_layer_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.show_options = True
    switch_002.input_type = 'STRING'
    # False
    switch_002.inputs[1].default_value = "dermis"

    # Node Reroute
    reroute = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketString"
    # Node Remove Named Attribute
    remove_named_attribute = custom_sensor_layer_1.nodes.new("GeometryNodeRemoveAttribute")
    remove_named_attribute.name = "Remove Named Attribute"
    remove_named_attribute.show_options = True
    # Pattern Mode
    remove_named_attribute.inputs[1].default_value = 'Exact'

    # Node Store Named Attribute
    store_named_attribute = custom_sensor_layer_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "is_sensor"
    # Value
    store_named_attribute.inputs[3].default_value = True

    # Node Set Point Radius
    set_point_radius = custom_sensor_layer_1.nodes.new("GeometryNodeSetPointRadius")
    set_point_radius.name = "Set Point Radius"
    set_point_radius.show_options = True
    # Selection
    set_point_radius.inputs[1].default_value = True
    # Radius
    set_point_radius.inputs[2].default_value = 0.00800000037997961

    # Node Index
    index = custom_sensor_layer_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Cut Disk Custom Layer
    cut_disk_custom_layer = custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    cut_disk_custom_layer.name = "Cut Disk Custom Layer"
    cut_disk_custom_layer.show_options = True
    cut_disk_custom_layer.node_tree = bpy.data.node_groups[node_tree_names[cut_disk_custom_sensor_layer_1_node_group]]

    # Node Switch.003
    switch_003 = custom_sensor_layer_1.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.show_options = True
    switch_003.input_type = 'STRING'
    # False
    switch_003.inputs[1].default_value = "dermis_bottom"

    # Node Math
    math = custom_sensor_layer_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # Node Reroute.006
    reroute_006 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketBool"
    # Node Reroute.007
    reroute_007 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketBool"
    # Node Frame
    frame = custom_sensor_layer_1.nodes.new("NodeFrame")
    frame.label = "Isolate in viewer for sensor data"
    frame.name = "Frame"
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Reroute.004
    reroute_004 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketGeometry"
    # Node Reroute.008
    reroute_008 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketFloat"
    # Node Switch.004
    switch_004 = custom_sensor_layer_1.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.show_options = True
    switch_004.input_type = 'GEOMETRY'

    # Node Reroute.002
    reroute_002 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketBool"
    # Node Switch.005
    switch_005 = custom_sensor_layer_1.nodes.new("GeometryNodeSwitch")
    switch_005.name = "Switch.005"
    switch_005.show_options = True
    switch_005.input_type = 'STRING'
    # False
    switch_005.inputs[1].default_value = "sensor_point"

    # Node Sample Index.001
    sample_index_001 = custom_sensor_layer_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'

    # Node Named Attribute
    named_attribute = custom_sensor_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'FLOAT_VECTOR'
    # Name
    named_attribute.inputs[0].default_value = "eulers"

    # Node Index.001
    index_001 = custom_sensor_layer_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Viewer
    viewer = custom_sensor_layer_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Negative Geometry")

    # Node Join Geometry.001
    join_geometry_001 = custom_sensor_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Mesh Boolean.001
    mesh_boolean_001 = custom_sensor_layer_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.name = "Mesh Boolean.001"
    mesh_boolean_001.show_options = True
    mesh_boolean_001.operation = 'UNION'
    mesh_boolean_001.solver = 'EXACT'
    # Self Intersection
    mesh_boolean_001.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_001.inputs[3].default_value = False

    # Node Reroute.010
    reroute_010 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketGeometry"
    # Node Reroute.012
    reroute_012 = custom_sensor_layer_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketGeometry"
    # Node Switch.006
    switch_006 = custom_sensor_layer_1.nodes.new("GeometryNodeSwitch")
    switch_006.name = "Switch.006"
    switch_006.show_options = True
    switch_006.input_type = 'GEOMETRY'

    # Node Store Named Attribute.001
    store_named_attribute_001 = custom_sensor_layer_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Value
    store_named_attribute_001.inputs[3].default_value = True

    # Node Separate and Remove Att
    separate_and_remove_att = custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att.name = "Separate and Remove Att"
    separate_and_remove_att.show_options = True
    separate_and_remove_att.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]
    # Socket_6
    separate_and_remove_att.inputs[2].default_value = ""
    # Socket_7
    separate_and_remove_att.inputs[3].default_value = ""

    # Node Separate and Remove Att.001
    separate_and_remove_att_001 = custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att_001.name = "Separate and Remove Att.001"
    separate_and_remove_att_001.show_options = True
    separate_and_remove_att_001.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]
    # Socket_6
    separate_and_remove_att_001.inputs[2].default_value = ""
    # Socket_7
    separate_and_remove_att_001.inputs[3].default_value = ""

    # Node Separate and Remove Att.002
    separate_and_remove_att_002 = custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att_002.name = "Separate and Remove Att.002"
    separate_and_remove_att_002.show_options = True
    separate_and_remove_att_002.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]
    # Socket_6
    separate_and_remove_att_002.inputs[2].default_value = ""
    # Socket_7
    separate_and_remove_att_002.inputs[3].default_value = ""

    # Node Separate and Remove Att.003
    separate_and_remove_att_003 = custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att_003.name = "Separate and Remove Att.003"
    separate_and_remove_att_003.show_options = True
    separate_and_remove_att_003.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]
    # Socket_6
    separate_and_remove_att_003.inputs[2].default_value = ""
    # Socket_7
    separate_and_remove_att_003.inputs[3].default_value = ""

    # Node Separate and Remove Att.004
    separate_and_remove_att_004 = custom_sensor_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att_004.name = "Separate and Remove Att.004"
    separate_and_remove_att_004.show_options = True
    separate_and_remove_att_004.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]
    # Socket_6
    separate_and_remove_att_004.inputs[2].default_value = ""
    # Socket_7
    separate_and_remove_att_004.inputs[3].default_value = ""

    # Set parents
    custom_sensor_layer_1.nodes["Store Named Attribute"].parent = custom_sensor_layer_1.nodes["Frame"]
    custom_sensor_layer_1.nodes["Set Point Radius"].parent = custom_sensor_layer_1.nodes["Frame"]
    custom_sensor_layer_1.nodes["Index"].parent = custom_sensor_layer_1.nodes["Frame"]

    # Set locations
    custom_sensor_layer_1.nodes["Group Input"].location = (-1640.0, 20.0)
    custom_sensor_layer_1.nodes["Group Output"].location = (2900.0, -100.0)
    custom_sensor_layer_1.nodes["Join Geometry"].location = (2520.0, -100.0)
    custom_sensor_layer_1.nodes["Switch"].location = (1300.0, 560.0)
    custom_sensor_layer_1.nodes["Menu Switch"].location = (-1360.0, 340.05792236328125)
    custom_sensor_layer_1.nodes["Reroute.003"].location = (200.0, -760.0)
    custom_sensor_layer_1.nodes["Reroute.005"].location = (200.0, -740.0)
    custom_sensor_layer_1.nodes["Reroute.009"].location = (-1340.0, -780.0)
    custom_sensor_layer_1.nodes["Reroute.011"].location = (-1340.0, -760.0)
    custom_sensor_layer_1.nodes["Distribute Custom Sensors"].location = (360.0, 40.0)
    custom_sensor_layer_1.nodes["Sample Index"].location = (60.0, 280.0)
    custom_sensor_layer_1.nodes["Named Attribute.001"].location = (-120.0, 340.0)
    custom_sensor_layer_1.nodes["Mesh Boolean"].location = (760.0, 500.0)
    custom_sensor_layer_1.nodes["Reroute.001"].location = (-899.9999389648438, 0.0)
    custom_sensor_layer_1.nodes["Switch.001"].location = (-1140.0, 300.0)
    custom_sensor_layer_1.nodes["Switch.002"].location = (-1140.0, 460.0)
    custom_sensor_layer_1.nodes["Reroute"].location = (-760.0, 20.0)
    custom_sensor_layer_1.nodes["Remove Named Attribute"].location = (-300.0, 120.0)
    custom_sensor_layer_1.nodes["Store Named Attribute"].location = (28.6451416015625, -56.06451416015625)
    custom_sensor_layer_1.nodes["Set Point Radius"].location = (208.6451416015625, -36.06451416015625)
    custom_sensor_layer_1.nodes["Index"].location = (208.6451416015625, -156.06451416015625)
    custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].location = (920.0, -260.0)
    custom_sensor_layer_1.nodes["Switch.003"].location = (-1140.0, 140.0)
    custom_sensor_layer_1.nodes["Math"].location = (305.84698486328125, -859.6641845703125)
    custom_sensor_layer_1.nodes["Reroute.006"].location = (-1300.0, 680.0)
    custom_sensor_layer_1.nodes["Reroute.007"].location = (1140.0, 660.0)
    custom_sensor_layer_1.nodes["Frame"].location = (1831.3548583984375, 316.06451416015625)
    custom_sensor_layer_1.nodes["Reroute.004"].location = (-1000.0, 0.0)
    custom_sensor_layer_1.nodes["Reroute.008"].location = (360.0, -380.0)
    custom_sensor_layer_1.nodes["Switch.004"].location = (1360.0, 1100.0)
    custom_sensor_layer_1.nodes["Reroute.002"].location = (-1220.0, 660.0)
    custom_sensor_layer_1.nodes["Switch.005"].location = (-1140.0, -40.0)
    custom_sensor_layer_1.nodes["Sample Index.001"].location = (-340.0, -40.0)
    custom_sensor_layer_1.nodes["Named Attribute"].location = (-560.0, -140.0)
    custom_sensor_layer_1.nodes["Index.001"].location = (-560.0, -280.0)
    custom_sensor_layer_1.nodes["Viewer"].location = (2306.666748046875, -19.33333396911621)
    custom_sensor_layer_1.nodes["Join Geometry.001"].location = (1880.0, -140.0)
    custom_sensor_layer_1.nodes["Mesh Boolean.001"].location = (1780.0, -340.0)
    custom_sensor_layer_1.nodes["Reroute.010"].location = (1687.885498046875, -145.91966247558594)
    custom_sensor_layer_1.nodes["Reroute.012"].location = (1687.885498046875, -27.06967544555664)
    custom_sensor_layer_1.nodes["Switch.006"].location = (2180.0, -140.0)
    custom_sensor_layer_1.nodes["Store Named Attribute.001"].location = (1960.0, -280.0)
    custom_sensor_layer_1.nodes["Separate and Remove Att"].location = (-799.9999389648438, 640.0)
    custom_sensor_layer_1.nodes["Separate and Remove Att.001"].location = (-799.9999389648438, 360.0)
    custom_sensor_layer_1.nodes["Separate and Remove Att.002"].location = (-799.9999389648438, -360.0)
    custom_sensor_layer_1.nodes["Separate and Remove Att.003"].location = (-799.9999389648438, -840.0)
    custom_sensor_layer_1.nodes["Separate and Remove Att.004"].location = (940.0001220703125, 940.0)

    # Set dimensions
    custom_sensor_layer_1.nodes["Group Input"].width  = 140.0
    custom_sensor_layer_1.nodes["Group Input"].height = 100.0

    custom_sensor_layer_1.nodes["Group Output"].width  = 140.0
    custom_sensor_layer_1.nodes["Group Output"].height = 100.0

    custom_sensor_layer_1.nodes["Join Geometry"].width  = 140.0
    custom_sensor_layer_1.nodes["Join Geometry"].height = 100.0

    custom_sensor_layer_1.nodes["Switch"].width  = 140.0
    custom_sensor_layer_1.nodes["Switch"].height = 100.0

    custom_sensor_layer_1.nodes["Menu Switch"].width  = 140.0
    custom_sensor_layer_1.nodes["Menu Switch"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.003"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.003"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.005"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.005"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.009"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.009"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.011"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.011"].height = 100.0

    custom_sensor_layer_1.nodes["Distribute Custom Sensors"].width  = 260.0
    custom_sensor_layer_1.nodes["Distribute Custom Sensors"].height = 100.0

    custom_sensor_layer_1.nodes["Sample Index"].width  = 140.0
    custom_sensor_layer_1.nodes["Sample Index"].height = 100.0

    custom_sensor_layer_1.nodes["Named Attribute.001"].width  = 140.0
    custom_sensor_layer_1.nodes["Named Attribute.001"].height = 100.0

    custom_sensor_layer_1.nodes["Mesh Boolean"].width  = 140.0
    custom_sensor_layer_1.nodes["Mesh Boolean"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.001"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.001"].height = 100.0

    custom_sensor_layer_1.nodes["Switch.001"].width  = 140.0
    custom_sensor_layer_1.nodes["Switch.001"].height = 100.0

    custom_sensor_layer_1.nodes["Switch.002"].width  = 140.0
    custom_sensor_layer_1.nodes["Switch.002"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute"].height = 100.0

    custom_sensor_layer_1.nodes["Remove Named Attribute"].width  = 170.0
    custom_sensor_layer_1.nodes["Remove Named Attribute"].height = 100.0

    custom_sensor_layer_1.nodes["Store Named Attribute"].width  = 140.0
    custom_sensor_layer_1.nodes["Store Named Attribute"].height = 100.0

    custom_sensor_layer_1.nodes["Set Point Radius"].width  = 140.0
    custom_sensor_layer_1.nodes["Set Point Radius"].height = 100.0

    custom_sensor_layer_1.nodes["Index"].width  = 140.0
    custom_sensor_layer_1.nodes["Index"].height = 100.0

    custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].width  = 260.0
    custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].height = 100.0

    custom_sensor_layer_1.nodes["Switch.003"].width  = 140.0
    custom_sensor_layer_1.nodes["Switch.003"].height = 100.0

    custom_sensor_layer_1.nodes["Math"].width  = 140.0
    custom_sensor_layer_1.nodes["Math"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.006"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.006"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.007"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.007"].height = 100.0

    custom_sensor_layer_1.nodes["Frame"].width  = 377.6773681640625
    custom_sensor_layer_1.nodes["Frame"].height = 246.0

    custom_sensor_layer_1.nodes["Reroute.004"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.004"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.008"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.008"].height = 100.0

    custom_sensor_layer_1.nodes["Switch.004"].width  = 140.0
    custom_sensor_layer_1.nodes["Switch.004"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.002"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.002"].height = 100.0

    custom_sensor_layer_1.nodes["Switch.005"].width  = 140.0
    custom_sensor_layer_1.nodes["Switch.005"].height = 100.0

    custom_sensor_layer_1.nodes["Sample Index.001"].width  = 140.0
    custom_sensor_layer_1.nodes["Sample Index.001"].height = 100.0

    custom_sensor_layer_1.nodes["Named Attribute"].width  = 140.0
    custom_sensor_layer_1.nodes["Named Attribute"].height = 100.0

    custom_sensor_layer_1.nodes["Index.001"].width  = 140.0
    custom_sensor_layer_1.nodes["Index.001"].height = 100.0

    custom_sensor_layer_1.nodes["Viewer"].width  = 140.0
    custom_sensor_layer_1.nodes["Viewer"].height = 100.0

    custom_sensor_layer_1.nodes["Join Geometry.001"].width  = 140.0
    custom_sensor_layer_1.nodes["Join Geometry.001"].height = 100.0

    custom_sensor_layer_1.nodes["Mesh Boolean.001"].width  = 140.0
    custom_sensor_layer_1.nodes["Mesh Boolean.001"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.010"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.010"].height = 100.0

    custom_sensor_layer_1.nodes["Reroute.012"].width  = 12.5
    custom_sensor_layer_1.nodes["Reroute.012"].height = 100.0

    custom_sensor_layer_1.nodes["Switch.006"].width  = 140.0
    custom_sensor_layer_1.nodes["Switch.006"].height = 100.0

    custom_sensor_layer_1.nodes["Store Named Attribute.001"].width  = 140.0
    custom_sensor_layer_1.nodes["Store Named Attribute.001"].height = 100.0

    custom_sensor_layer_1.nodes["Separate and Remove Att"].width  = 200.0
    custom_sensor_layer_1.nodes["Separate and Remove Att"].height = 100.0

    custom_sensor_layer_1.nodes["Separate and Remove Att.001"].width  = 200.0
    custom_sensor_layer_1.nodes["Separate and Remove Att.001"].height = 100.0

    custom_sensor_layer_1.nodes["Separate and Remove Att.002"].width  = 200.0
    custom_sensor_layer_1.nodes["Separate and Remove Att.002"].height = 100.0

    custom_sensor_layer_1.nodes["Separate and Remove Att.003"].width  = 200.0
    custom_sensor_layer_1.nodes["Separate and Remove Att.003"].height = 100.0

    custom_sensor_layer_1.nodes["Separate and Remove Att.004"].width  = 200.0
    custom_sensor_layer_1.nodes["Separate and Remove Att.004"].height = 100.0


    # Initialize custom_sensor_layer_1 links

    # join_geometry.Geometry -> group_output.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Join Geometry"].outputs[0],
        custom_sensor_layer_1.nodes["Group Output"].inputs[0]
    )
    # reroute_007.Output -> switch.Switch
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.007"].outputs[0],
        custom_sensor_layer_1.nodes["Switch"].inputs[0]
    )
    # group_input.Options -> menu_switch.Menu
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[9],
        custom_sensor_layer_1.nodes["Menu Switch"].inputs[0]
    )
    # reroute_009.Output -> reroute_003.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.009"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_011.Output -> reroute_005.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.011"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.005"].inputs[0]
    )
    # group_input.Node Thickness -> reroute_009.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[7],
        custom_sensor_layer_1.nodes["Reroute.009"].inputs[0]
    )
    # group_input.Node Offset -> reroute_011.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[6],
        custom_sensor_layer_1.nodes["Reroute.011"].inputs[0]
    )
    # group_input.Sensor Mesh -> distribute_custom_sensors.Sensor Mesh
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[4],
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].inputs[2]
    )
    # group_input.Sensor Negative Mesh -> distribute_custom_sensors.Sensor Negative Mesh
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[5],
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].inputs[3]
    )
    # reroute_005.Output -> distribute_custom_sensors.Node Offset
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.005"].outputs[0],
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].inputs[4]
    )
    # named_attribute_001.Attribute -> sample_index.Value
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Named Attribute.001"].outputs[0],
        custom_sensor_layer_1.nodes["Sample Index"].inputs[1]
    )
    # reroute_008.Output -> distribute_custom_sensors.Reference Thickness
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.008"].outputs[0],
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].inputs[5]
    )
    # reroute_004.Output -> reroute_001.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.004"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.001"].inputs[0]
    )
    # distribute_custom_sensors.Negative Geometry -> mesh_boolean.Mesh 2
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].outputs[1],
        custom_sensor_layer_1.nodes["Mesh Boolean"].inputs[1]
    )
    # menu_switch.Output -> switch_001.Switch
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Menu Switch"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.001"].inputs[0]
    )
    # group_input.Application Surface -> switch_001.True
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[10],
        custom_sensor_layer_1.nodes["Switch.001"].inputs[2]
    )
    # group_input.Dermis -> switch_002.True
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[11],
        custom_sensor_layer_1.nodes["Switch.002"].inputs[2]
    )
    # menu_switch.Output -> switch_002.Switch
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Menu Switch"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.002"].inputs[0]
    )
    # switch_002.Output -> reroute.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.002"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> remove_named_attribute.Name
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute"].outputs[0],
        custom_sensor_layer_1.nodes["Remove Named Attribute"].inputs[2]
    )
    # store_named_attribute.Geometry -> set_point_radius.Points
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Store Named Attribute"].outputs[0],
        custom_sensor_layer_1.nodes["Set Point Radius"].inputs[0]
    )
    # distribute_custom_sensors.Geometry -> cut_disk_custom_layer.Shape
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].outputs[0],
        custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].inputs[0]
    )
    # reroute_005.Output -> cut_disk_custom_layer.Node Offset
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.005"].outputs[0],
        custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].inputs[4]
    )
    # reroute_003.Output -> math.Value
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.003"].outputs[0],
        custom_sensor_layer_1.nodes["Math"].inputs[0]
    )
    # math.Value -> cut_disk_custom_layer.Node Thickness
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Math"].outputs[0],
        custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].inputs[5]
    )
    # mesh_boolean.Mesh -> switch.False
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Mesh Boolean"].outputs[0],
        custom_sensor_layer_1.nodes["Switch"].inputs[1]
    )
    # group_input.Isolate -> reroute_006.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[1],
        custom_sensor_layer_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_006.Output -> reroute_007.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.006"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.007"].inputs[0]
    )
    # group_input.Geometry -> reroute_004.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.004"].inputs[0]
    )
    # group_input.Material -> cut_disk_custom_layer.Material
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[8],
        custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].inputs[3]
    )
    # sample_index.Value -> reroute_008.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Sample Index"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.008"].inputs[0]
    )
    # reroute_008.Output -> cut_disk_custom_layer.Reference Thickness
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.008"].outputs[0],
        custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].inputs[2]
    )
    # reroute_002.Output -> switch_004.Switch
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.002"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.004"].inputs[0]
    )
    # group_input.Include Original Geometry -> reroute_002.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[2],
        custom_sensor_layer_1.nodes["Reroute.002"].inputs[0]
    )
    # menu_switch.Output -> switch_003.Switch
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Menu Switch"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.003"].inputs[0]
    )
    # group_input.Dermis Bottom -> switch_003.True
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[12],
        custom_sensor_layer_1.nodes["Switch.003"].inputs[2]
    )
    # menu_switch.Output -> switch_005.Switch
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Menu Switch"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.005"].inputs[0]
    )
    # group_input.Sensor Point Label -> switch_005.True
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[13],
        custom_sensor_layer_1.nodes["Switch.005"].inputs[2]
    )
    # named_attribute.Attribute -> sample_index_001.Value
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Named Attribute"].outputs[0],
        custom_sensor_layer_1.nodes["Sample Index.001"].inputs[1]
    )
    # index_001.Index -> sample_index_001.Index
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Index.001"].outputs[0],
        custom_sensor_layer_1.nodes["Sample Index.001"].inputs[2]
    )
    # distribute_custom_sensors.Negative Geometry -> viewer.Negative Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].outputs[1],
        custom_sensor_layer_1.nodes["Viewer"].inputs[0]
    )
    # sample_index_001.Value -> distribute_custom_sensors.Euler
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Sample Index.001"].outputs[0],
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].inputs[1]
    )
    # reroute_010.Output -> join_geometry_001.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.010"].outputs[0],
        custom_sensor_layer_1.nodes["Join Geometry.001"].inputs[0]
    )
    # switch_006.Output -> join_geometry.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.006"].outputs[0],
        custom_sensor_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # cut_disk_custom_layer.Geometry -> reroute_010.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.010"].inputs[0]
    )
    # switch.Output -> reroute_012.Input
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch"].outputs[0],
        custom_sensor_layer_1.nodes["Reroute.012"].inputs[0]
    )
    # reroute_010.Output -> mesh_boolean_001.Mesh
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.010"].outputs[0],
        custom_sensor_layer_1.nodes["Mesh Boolean.001"].inputs[1]
    )
    # join_geometry_001.Geometry -> switch_006.False
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Join Geometry.001"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.006"].inputs[1]
    )
    # store_named_attribute_001.Geometry -> switch_006.True
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Store Named Attribute.001"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.006"].inputs[2]
    )
    # group_input.Mesh Union -> switch_006.Switch
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Group Input"].outputs[3],
        custom_sensor_layer_1.nodes["Switch.006"].inputs[0]
    )
    # mesh_boolean_001.Mesh -> store_named_attribute_001.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Mesh Boolean.001"].outputs[0],
        custom_sensor_layer_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # switch_002.Output -> store_named_attribute_001.Name
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.002"].outputs[0],
        custom_sensor_layer_1.nodes["Store Named Attribute.001"].inputs[2]
    )
    # reroute_010.Output -> group_output.Sensor Mounts
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.010"].outputs[0],
        custom_sensor_layer_1.nodes["Group Output"].inputs[1]
    )
    # distribute_custom_sensors.Negative Geometry -> group_output.Negative Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].outputs[1],
        custom_sensor_layer_1.nodes["Group Output"].inputs[2]
    )
    # distribute_custom_sensors.Points -> group_output.Points
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].outputs[2],
        custom_sensor_layer_1.nodes["Group Output"].inputs[3]
    )
    # reroute_001.Output -> separate_and_remove_att.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.001"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att"].inputs[0]
    )
    # reroute_001.Output -> separate_and_remove_att_001.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.001"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.001"].inputs[0]
    )
    # reroute_001.Output -> separate_and_remove_att_002.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.001"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.002"].inputs[0]
    )
    # reroute_001.Output -> separate_and_remove_att_003.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.001"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.003"].inputs[0]
    )
    # switch_002.Output -> separate_and_remove_att.Attribute
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.002"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att"].inputs[1]
    )
    # switch_001.Output -> separate_and_remove_att_001.Attribute
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.001"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.001"].inputs[1]
    )
    # switch_003.Output -> separate_and_remove_att_003.Attribute
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.003"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.003"].inputs[1]
    )
    # switch_005.Output -> separate_and_remove_att_002.Attribute
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.005"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.002"].inputs[1]
    )
    # separate_and_remove_att.Selection -> mesh_boolean.Mesh 1
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Separate and Remove Att"].outputs[0],
        custom_sensor_layer_1.nodes["Mesh Boolean"].inputs[0]
    )
    # separate_and_remove_att_001.Selection -> sample_index.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Separate and Remove Att.001"].outputs[0],
        custom_sensor_layer_1.nodes["Sample Index"].inputs[0]
    )
    # separate_and_remove_att_002.Selection -> sample_index_001.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Separate and Remove Att.002"].outputs[0],
        custom_sensor_layer_1.nodes["Sample Index.001"].inputs[0]
    )
    # separate_and_remove_att_002.Selection -> distribute_custom_sensors.Points
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Separate and Remove Att.002"].outputs[0],
        custom_sensor_layer_1.nodes["Distribute Custom Sensors"].inputs[0]
    )
    # separate_and_remove_att_003.Selection -> cut_disk_custom_layer.Bottom Plate
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Separate and Remove Att.003"].outputs[0],
        custom_sensor_layer_1.nodes["Cut Disk Custom Layer"].inputs[1]
    )
    # switch_002.Output -> separate_and_remove_att_004.Attribute
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.002"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.004"].inputs[1]
    )
    # reroute_001.Output -> separate_and_remove_att_004.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.001"].outputs[0],
        custom_sensor_layer_1.nodes["Separate and Remove Att.004"].inputs[0]
    )
    # separate_and_remove_att_004.Selection -> switch_004.True
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Separate and Remove Att.004"].outputs[0],
        custom_sensor_layer_1.nodes["Switch.004"].inputs[2]
    )
    # switch_004.Output -> join_geometry.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Switch.004"].outputs[0],
        custom_sensor_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # reroute_012.Output -> join_geometry_001.Geometry
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.012"].outputs[0],
        custom_sensor_layer_1.nodes["Join Geometry.001"].inputs[0]
    )
    # reroute_012.Output -> mesh_boolean_001.Mesh
    custom_sensor_layer_1.links.new(
        custom_sensor_layer_1.nodes["Reroute.012"].outputs[0],
        custom_sensor_layer_1.nodes["Mesh Boolean.001"].inputs[1]
    )
    options_socket.default_value = 'Default'
    viewer.viewer_items[0].auto_remove = True

    return custom_sensor_layer_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    distribute_custom_sensors = distribute_custom_sensors_1_node_group(node_tree_names)
    node_tree_names[distribute_custom_sensors_1_node_group] = distribute_custom_sensors.name

    cutout_thickness = cutout_thickness_1_node_group(node_tree_names)
    node_tree_names[cutout_thickness_1_node_group] = cutout_thickness.name

    plate_volume_reduced = plate_volume_reduced_1_node_group(node_tree_names)
    node_tree_names[plate_volume_reduced_1_node_group] = plate_volume_reduced.name

    cut_disk_custom_sensor_layer = cut_disk_custom_sensor_layer_1_node_group(node_tree_names)
    node_tree_names[cut_disk_custom_sensor_layer_1_node_group] = cut_disk_custom_sensor_layer.name

    separate_and_remove_att = separate_and_remove_att_1_node_group(node_tree_names)
    node_tree_names[separate_and_remove_att_1_node_group] = separate_and_remove_att.name

    custom_sensor_layer = custom_sensor_layer_1_node_group(node_tree_names)
    node_tree_names[custom_sensor_layer_1_node_group] = custom_sensor_layer.name

