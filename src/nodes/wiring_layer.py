import bpy
import mathutils
import os
import typing


def remove_curve_attributes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Remove Curve Attributes node group"""
    remove_curve_attributes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Remove Curve Attributes")

    remove_curve_attributes_1.color_tag = 'NONE'
    remove_curve_attributes_1.description = ""
    remove_curve_attributes_1.default_group_node_width = 140
    remove_curve_attributes_1.show_modifier_manage_panel = True

    # remove_curve_attributes_1 interface

    # Socket Geometry
    geometry_socket = remove_curve_attributes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = remove_curve_attributes_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Initialize remove_curve_attributes_1 nodes

    # Node Group Output
    group_output = remove_curve_attributes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = remove_curve_attributes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Domain Size
    domain_size = remove_curve_attributes_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.show_options = True
    domain_size.component = 'CURVE'

    # Node Mesh Line
    mesh_line = remove_curve_attributes_1.nodes.new("GeometryNodeMeshLine")
    mesh_line.name = "Mesh Line"
    mesh_line.show_options = True
    mesh_line.count_mode = 'TOTAL'
    mesh_line.mode = 'OFFSET'
    # Start Location
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset
    mesh_line.inputs[3].default_value = (0.0, 0.0, 1.0)

    # Node Set Position
    set_position = remove_curve_attributes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Sample Index
    sample_index = remove_curve_attributes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Index
    index = remove_curve_attributes_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Position
    position = remove_curve_attributes_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Mesh to Curve
    mesh_to_curve = remove_curve_attributes_1.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.show_options = True
    mesh_to_curve.mode = 'EDGES'
    # Selection
    mesh_to_curve.inputs[1].default_value = True

    # Node Repeat Input
    repeat_input = remove_curve_attributes_1.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    repeat_input.show_options = True
    # Node Repeat Output
    repeat_output = remove_curve_attributes_1.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.show_options = True
    repeat_output.active_index = 1
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")
    # Create item "Curve"
    repeat_output.repeat_items.new('GEOMETRY', "Curve")

    # Node Domain Size.001
    domain_size_001 = remove_curve_attributes_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size_001.name = "Domain Size.001"
    domain_size_001.show_options = True
    domain_size_001.component = 'CURVE'

    # Node Separate Geometry
    separate_geometry = remove_curve_attributes_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.show_options = True
    separate_geometry.domain = 'CURVE'

    # Node Compare
    compare = remove_curve_attributes_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'

    # Node Index.001
    index_001 = remove_curve_attributes_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Join Geometry
    join_geometry = remove_curve_attributes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Viewer
    viewer = remove_curve_attributes_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Curve")

    # Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)



    # Set locations
    remove_curve_attributes_1.nodes["Group Output"].location = (1130.0001220703125, 0.0)
    remove_curve_attributes_1.nodes["Group Input"].location = (-1840.0, 0.0)
    remove_curve_attributes_1.nodes["Domain Size"].location = (-419.9998779296875, 10.0)
    remove_curve_attributes_1.nodes["Mesh Line"].location = (0.00012063980102539062, 210.0)
    remove_curve_attributes_1.nodes["Set Position"].location = (300.0, 20.0)
    remove_curve_attributes_1.nodes["Sample Index"].location = (0.00012063980102539062, -90.0)
    remove_curve_attributes_1.nodes["Index"].location = (-179.99989318847656, -250.0)
    remove_curve_attributes_1.nodes["Position"].location = (-179.99989318847656, -190.0)
    remove_curve_attributes_1.nodes["Mesh to Curve"].location = (500.0, 60.0)
    remove_curve_attributes_1.nodes["Repeat Input"].location = (-1440.0, 260.0)
    remove_curve_attributes_1.nodes["Repeat Output"].location = (880.0001220703125, 150.0)
    remove_curve_attributes_1.nodes["Domain Size.001"].location = (-1640.0, -40.0)
    remove_curve_attributes_1.nodes["Separate Geometry"].location = (-640.0, 120.0)
    remove_curve_attributes_1.nodes["Compare"].location = (-839.9999389648438, -60.0)
    remove_curve_attributes_1.nodes["Index.001"].location = (-1100.0, -160.0)
    remove_curve_attributes_1.nodes["Join Geometry"].location = (700.0, 120.0)
    remove_curve_attributes_1.nodes["Viewer"].location = (1046.6666259765625, 230.6666717529297)

    # Set dimensions
    remove_curve_attributes_1.nodes["Group Output"].width  = 140.0
    remove_curve_attributes_1.nodes["Group Output"].height = 100.0

    remove_curve_attributes_1.nodes["Group Input"].width  = 140.0
    remove_curve_attributes_1.nodes["Group Input"].height = 100.0

    remove_curve_attributes_1.nodes["Domain Size"].width  = 140.0
    remove_curve_attributes_1.nodes["Domain Size"].height = 100.0

    remove_curve_attributes_1.nodes["Mesh Line"].width  = 140.0
    remove_curve_attributes_1.nodes["Mesh Line"].height = 100.0

    remove_curve_attributes_1.nodes["Set Position"].width  = 140.0
    remove_curve_attributes_1.nodes["Set Position"].height = 100.0

    remove_curve_attributes_1.nodes["Sample Index"].width  = 140.0
    remove_curve_attributes_1.nodes["Sample Index"].height = 100.0

    remove_curve_attributes_1.nodes["Index"].width  = 140.0
    remove_curve_attributes_1.nodes["Index"].height = 100.0

    remove_curve_attributes_1.nodes["Position"].width  = 140.0
    remove_curve_attributes_1.nodes["Position"].height = 100.0

    remove_curve_attributes_1.nodes["Mesh to Curve"].width  = 140.0
    remove_curve_attributes_1.nodes["Mesh to Curve"].height = 100.0

    remove_curve_attributes_1.nodes["Repeat Input"].width  = 140.0
    remove_curve_attributes_1.nodes["Repeat Input"].height = 100.0

    remove_curve_attributes_1.nodes["Repeat Output"].width  = 140.0
    remove_curve_attributes_1.nodes["Repeat Output"].height = 100.0

    remove_curve_attributes_1.nodes["Domain Size.001"].width  = 140.0
    remove_curve_attributes_1.nodes["Domain Size.001"].height = 100.0

    remove_curve_attributes_1.nodes["Separate Geometry"].width  = 140.0
    remove_curve_attributes_1.nodes["Separate Geometry"].height = 100.0

    remove_curve_attributes_1.nodes["Compare"].width  = 140.0
    remove_curve_attributes_1.nodes["Compare"].height = 100.0

    remove_curve_attributes_1.nodes["Index.001"].width  = 140.0
    remove_curve_attributes_1.nodes["Index.001"].height = 100.0

    remove_curve_attributes_1.nodes["Join Geometry"].width  = 140.0
    remove_curve_attributes_1.nodes["Join Geometry"].height = 100.0

    remove_curve_attributes_1.nodes["Viewer"].width  = 140.0
    remove_curve_attributes_1.nodes["Viewer"].height = 100.0


    # Initialize remove_curve_attributes_1 links

    # set_position.Geometry -> mesh_to_curve.Mesh
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Set Position"].outputs[0],
        remove_curve_attributes_1.nodes["Mesh to Curve"].inputs[0]
    )
    # domain_size.Point Count -> mesh_line.Count
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Domain Size"].outputs[0],
        remove_curve_attributes_1.nodes["Mesh Line"].inputs[0]
    )
    # domain_size_001.Spline Count -> repeat_input.Iterations
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Domain Size.001"].outputs[4],
        remove_curve_attributes_1.nodes["Repeat Input"].inputs[0]
    )
    # position.Position -> sample_index.Value
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Position"].outputs[0],
        remove_curve_attributes_1.nodes["Sample Index"].inputs[1]
    )
    # mesh_line.Mesh -> set_position.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Mesh Line"].outputs[0],
        remove_curve_attributes_1.nodes["Set Position"].inputs[0]
    )
    # separate_geometry.Selection -> domain_size.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Separate Geometry"].outputs[0],
        remove_curve_attributes_1.nodes["Domain Size"].inputs[0]
    )
    # index.Index -> sample_index.Index
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Index"].outputs[0],
        remove_curve_attributes_1.nodes["Sample Index"].inputs[2]
    )
    # sample_index.Value -> set_position.Position
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Sample Index"].outputs[0],
        remove_curve_attributes_1.nodes["Set Position"].inputs[2]
    )
    # repeat_input.Geometry -> separate_geometry.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Repeat Input"].outputs[1],
        remove_curve_attributes_1.nodes["Separate Geometry"].inputs[0]
    )
    # separate_geometry.Selection -> sample_index.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Separate Geometry"].outputs[0],
        remove_curve_attributes_1.nodes["Sample Index"].inputs[0]
    )
    # group_input.Geometry -> repeat_input.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Group Input"].outputs[0],
        remove_curve_attributes_1.nodes["Repeat Input"].inputs[1]
    )
    # group_input.Geometry -> domain_size_001.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Group Input"].outputs[0],
        remove_curve_attributes_1.nodes["Domain Size.001"].inputs[0]
    )
    # repeat_input.Iteration -> compare.B
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Repeat Input"].outputs[0],
        remove_curve_attributes_1.nodes["Compare"].inputs[3]
    )
    # index_001.Index -> compare.A
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Index.001"].outputs[0],
        remove_curve_attributes_1.nodes["Compare"].inputs[2]
    )
    # compare.Result -> separate_geometry.Selection
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Compare"].outputs[0],
        remove_curve_attributes_1.nodes["Separate Geometry"].inputs[1]
    )
    # join_geometry.Geometry -> repeat_output.Curve
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Join Geometry"].outputs[0],
        remove_curve_attributes_1.nodes["Repeat Output"].inputs[1]
    )
    # repeat_input.Curve -> join_geometry.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Repeat Input"].outputs[2],
        remove_curve_attributes_1.nodes["Join Geometry"].inputs[0]
    )
    # repeat_output.Curve -> group_output.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Repeat Output"].outputs[1],
        remove_curve_attributes_1.nodes["Group Output"].inputs[0]
    )
    # repeat_input.Geometry -> repeat_output.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Repeat Input"].outputs[1],
        remove_curve_attributes_1.nodes["Repeat Output"].inputs[0]
    )
    # repeat_output.Curve -> viewer.Curve
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Repeat Output"].outputs[1],
        remove_curve_attributes_1.nodes["Viewer"].inputs[0]
    )
    # mesh_to_curve.Curve -> join_geometry.Geometry
    remove_curve_attributes_1.links.new(
        remove_curve_attributes_1.nodes["Mesh to Curve"].outputs[0],
        remove_curve_attributes_1.nodes["Join Geometry"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True

    return remove_curve_attributes_1


def wire_profile_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Wire Profile.001 node group"""
    wire_profile_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Wire Profile.001")

    wire_profile_001_1.color_tag = 'NONE'
    wire_profile_001_1.description = "Custome Wire Profile"
    wire_profile_001_1.default_group_node_width = 140
    wire_profile_001_1.show_modifier_manage_panel = True

    # wire_profile_001_1 interface

    # Socket Wires
    wires_socket = wire_profile_001_1.interface.new_socket(name="Wires", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    wires_socket.attribute_domain = 'POINT'
    wires_socket.default_input = 'VALUE'
    wires_socket.structure_type = 'AUTO'

    # Socket Curve
    curve_socket = wire_profile_001_1.interface.new_socket(name="Curve", in_out='INPUT', socket_type='NodeSocketGeometry')
    curve_socket.attribute_domain = 'POINT'
    curve_socket.default_input = 'VALUE'
    curve_socket.structure_type = 'AUTO'

    # Socket Radius
    radius_socket = wire_profile_001_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    radius_socket.default_value = 1.0
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    # Socket Sampling
    sampling_socket = wire_profile_001_1.interface.new_socket(name="Sampling", in_out='INPUT', socket_type='NodeSocketInt')
    sampling_socket.default_value = 15
    sampling_socket.min_value = 1
    sampling_socket.max_value = 100000
    sampling_socket.subtype = 'NONE'
    sampling_socket.attribute_domain = 'POINT'
    sampling_socket.default_input = 'VALUE'
    sampling_socket.structure_type = 'AUTO'

    # Socket Fill Caps
    fill_caps_socket = wire_profile_001_1.interface.new_socket(name="Fill Caps", in_out='INPUT', socket_type='NodeSocketBool')
    fill_caps_socket.default_value = False
    fill_caps_socket.attribute_domain = 'POINT'
    fill_caps_socket.default_input = 'VALUE'
    fill_caps_socket.structure_type = 'AUTO'

    # Socket Material
    material_socket = wire_profile_001_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'
    material_socket.optional_label = True

    # Initialize wire_profile_001_1 nodes

    # Node Group Output
    group_output = wire_profile_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = wire_profile_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Curve to Mesh
    curve_to_mesh = wire_profile_001_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.show_options = True

    # Node Set Material
    set_material = wire_profile_001_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Set Spline Type
    set_spline_type = wire_profile_001_1.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type.name = "Set Spline Type"
    set_spline_type.show_options = True
    set_spline_type.spline_type = 'CATMULL_ROM'
    # Selection
    set_spline_type.inputs[1].default_value = True

    # Node Resample Curve
    resample_curve = wire_profile_001_1.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.show_options = True
    resample_curve.keep_last_segment = True
    # Selection
    resample_curve.inputs[1].default_value = True
    # Mode
    resample_curve.inputs[2].default_value = 'Count'
    # Length
    resample_curve.inputs[4].default_value = 0.10000000149011612

    # Node Store Named Attribute.001
    store_named_attribute_001 = wire_profile_001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "electrodes"
    # Value
    store_named_attribute_001.inputs[3].default_value = False

    # Node Store Named Attribute.006
    store_named_attribute_006 = wire_profile_001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_006.name = "Store Named Attribute.006"
    store_named_attribute_006.show_options = True
    store_named_attribute_006.data_type = 'BOOLEAN'
    store_named_attribute_006.domain = 'POINT'
    # Selection
    store_named_attribute_006.inputs[1].default_value = True
    # Name
    store_named_attribute_006.inputs[2].default_value = "is_sensor"
    # Value
    store_named_attribute_006.inputs[3].default_value = False

    # Node Curve Circle
    curve_circle = wire_profile_001_1.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.show_options = True
    curve_circle.mode = 'RADIUS'
    # Resolution
    curve_circle.inputs[0].default_value = 8

    # Node Named Attribute
    named_attribute = wire_profile_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'FLOAT'
    # Name
    named_attribute.inputs[0].default_value = "radius"

    # Node Switch
    switch = wire_profile_001_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'FLOAT'
    # False
    switch.inputs[1].default_value = 1.0

    # Node Reroute
    reroute = wire_profile_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Viewer
    viewer = wire_profile_001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Curve")

    # Node Group
    group = wire_profile_001_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[remove_curve_attributes_1_node_group]]

    # Set locations
    wire_profile_001_1.nodes["Group Output"].location = (1131.875, -10.752584457397461)
    wire_profile_001_1.nodes["Group Input"].location = (-2440.000244140625, -180.0)
    wire_profile_001_1.nodes["Curve to Mesh"].location = (-60.0, -200.0)
    wire_profile_001_1.nodes["Set Material"].location = (20.0, -10.0)
    wire_profile_001_1.nodes["Set Spline Type"].location = (-220.0, 80.0)
    wire_profile_001_1.nodes["Resample Curve"].location = (-400.0, 60.0)
    wire_profile_001_1.nodes["Store Named Attribute.001"].location = (200.000244140625, -10.0)
    wire_profile_001_1.nodes["Store Named Attribute.006"].location = (560.0, 10.0)
    wire_profile_001_1.nodes["Curve Circle"].location = (-560.0, -80.0)
    wire_profile_001_1.nodes["Named Attribute"].location = (-680.0, -320.0)
    wire_profile_001_1.nodes["Switch"].location = (-420.0, -300.0)
    wire_profile_001_1.nodes["Reroute"].location = (-2140.000244140625, -140.0)
    wire_profile_001_1.nodes["Viewer"].location = (-1520.0, 80.0)
    wire_profile_001_1.nodes["Group"].location = (-1880.0, -40.0)

    # Set dimensions
    wire_profile_001_1.nodes["Group Output"].width  = 140.0
    wire_profile_001_1.nodes["Group Output"].height = 100.0

    wire_profile_001_1.nodes["Group Input"].width  = 140.0
    wire_profile_001_1.nodes["Group Input"].height = 100.0

    wire_profile_001_1.nodes["Curve to Mesh"].width  = 140.0
    wire_profile_001_1.nodes["Curve to Mesh"].height = 100.0

    wire_profile_001_1.nodes["Set Material"].width  = 140.0
    wire_profile_001_1.nodes["Set Material"].height = 100.0

    wire_profile_001_1.nodes["Set Spline Type"].width  = 140.0
    wire_profile_001_1.nodes["Set Spline Type"].height = 100.0

    wire_profile_001_1.nodes["Resample Curve"].width  = 140.0
    wire_profile_001_1.nodes["Resample Curve"].height = 100.0

    wire_profile_001_1.nodes["Store Named Attribute.001"].width  = 140.0
    wire_profile_001_1.nodes["Store Named Attribute.001"].height = 100.0

    wire_profile_001_1.nodes["Store Named Attribute.006"].width  = 140.0
    wire_profile_001_1.nodes["Store Named Attribute.006"].height = 100.0

    wire_profile_001_1.nodes["Curve Circle"].width  = 140.0
    wire_profile_001_1.nodes["Curve Circle"].height = 100.0

    wire_profile_001_1.nodes["Named Attribute"].width  = 140.0
    wire_profile_001_1.nodes["Named Attribute"].height = 100.0

    wire_profile_001_1.nodes["Switch"].width  = 140.0
    wire_profile_001_1.nodes["Switch"].height = 100.0

    wire_profile_001_1.nodes["Reroute"].width  = 14.5
    wire_profile_001_1.nodes["Reroute"].height = 100.0

    wire_profile_001_1.nodes["Viewer"].width  = 140.0
    wire_profile_001_1.nodes["Viewer"].height = 100.0

    wire_profile_001_1.nodes["Group"].width  = 240.0
    wire_profile_001_1.nodes["Group"].height = 100.0


    # Initialize wire_profile_001_1 links

    # set_spline_type.Curve -> curve_to_mesh.Curve
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Set Spline Type"].outputs[0],
        wire_profile_001_1.nodes["Curve to Mesh"].inputs[0]
    )
    # curve_to_mesh.Mesh -> set_material.Geometry
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Curve to Mesh"].outputs[0],
        wire_profile_001_1.nodes["Set Material"].inputs[0]
    )
    # set_material.Geometry -> store_named_attribute_001.Geometry
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Set Material"].outputs[0],
        wire_profile_001_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # store_named_attribute_001.Geometry -> store_named_attribute_006.Geometry
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Store Named Attribute.001"].outputs[0],
        wire_profile_001_1.nodes["Store Named Attribute.006"].inputs[0]
    )
    # store_named_attribute_006.Geometry -> group_output.Wires
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Store Named Attribute.006"].outputs[0],
        wire_profile_001_1.nodes["Group Output"].inputs[0]
    )
    # curve_circle.Curve -> curve_to_mesh.Profile Curve
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Curve Circle"].outputs[0],
        wire_profile_001_1.nodes["Curve to Mesh"].inputs[1]
    )
    # group_input.Radius -> curve_circle.Radius
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Group Input"].outputs[1],
        wire_profile_001_1.nodes["Curve Circle"].inputs[4]
    )
    # group_input.Sampling -> resample_curve.Count
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Group Input"].outputs[2],
        wire_profile_001_1.nodes["Resample Curve"].inputs[3]
    )
    # group_input.Fill Caps -> curve_to_mesh.Fill Caps
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Group Input"].outputs[3],
        wire_profile_001_1.nodes["Curve to Mesh"].inputs[3]
    )
    # named_attribute.Exists -> switch.Switch
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Named Attribute"].outputs[1],
        wire_profile_001_1.nodes["Switch"].inputs[0]
    )
    # named_attribute.Attribute -> switch.True
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Named Attribute"].outputs[0],
        wire_profile_001_1.nodes["Switch"].inputs[2]
    )
    # switch.Output -> curve_to_mesh.Scale
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Switch"].outputs[0],
        wire_profile_001_1.nodes["Curve to Mesh"].inputs[2]
    )
    # group_input.Material -> set_material.Material
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Group Input"].outputs[4],
        wire_profile_001_1.nodes["Set Material"].inputs[2]
    )
    # group_input.Curve -> reroute.Input
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Group Input"].outputs[0],
        wire_profile_001_1.nodes["Reroute"].inputs[0]
    )
    # resample_curve.Curve -> set_spline_type.Curve
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Resample Curve"].outputs[0],
        wire_profile_001_1.nodes["Set Spline Type"].inputs[0]
    )
    # reroute.Output -> viewer.Curve
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Reroute"].outputs[0],
        wire_profile_001_1.nodes["Viewer"].inputs[0]
    )
    # reroute.Output -> group.Geometry
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Reroute"].outputs[0],
        wire_profile_001_1.nodes["Group"].inputs[0]
    )
    # group.Geometry -> resample_curve.Curve
    wire_profile_001_1.links.new(
        wire_profile_001_1.nodes["Group"].outputs[0],
        wire_profile_001_1.nodes["Resample Curve"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True

    return wire_profile_001_1


def instantiate_wire_with_crosstalk_att_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Instantiate Wire with Crosstalk Att.001 node group"""
    instantiate_wire_with_crosstalk_att_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Instantiate Wire with Crosstalk Att.001")

    instantiate_wire_with_crosstalk_att_001_1.color_tag = 'NONE'
    instantiate_wire_with_crosstalk_att_001_1.description = ""
    instantiate_wire_with_crosstalk_att_001_1.default_group_node_width = 140
    instantiate_wire_with_crosstalk_att_001_1.show_modifier_manage_panel = True

    # instantiate_wire_with_crosstalk_att_001_1 interface

    # Socket Wires
    wires_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Wires", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    wires_socket.attribute_domain = 'POINT'
    wires_socket.default_input = 'VALUE'
    wires_socket.structure_type = 'AUTO'

    # Socket Grid
    grid_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Grid", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    grid_socket.attribute_domain = 'POINT'
    grid_socket.default_input = 'VALUE'
    grid_socket.structure_type = 'AUTO'

    # Socket Vertex Selection
    vertex_selection_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Vertex Selection", in_out='OUTPUT', socket_type='NodeSocketBool')
    vertex_selection_socket.default_value = False
    vertex_selection_socket.attribute_domain = 'POINT'
    vertex_selection_socket.default_input = 'VALUE'
    vertex_selection_socket.structure_type = 'AUTO'

    # Socket Total Cost
    total_cost_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Total Cost", in_out='OUTPUT', socket_type='NodeSocketFloat')
    total_cost_socket.default_value = 0.0
    total_cost_socket.min_value = -3.4028234663852886e+38
    total_cost_socket.max_value = 3.4028234663852886e+38
    total_cost_socket.subtype = 'NONE'
    total_cost_socket.attribute_domain = 'POINT'
    total_cost_socket.default_input = 'VALUE'
    total_cost_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Socket Start Indice
    start_indice_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Start Indice", in_out='INPUT', socket_type='NodeSocketInt')
    start_indice_socket.default_value = 0
    start_indice_socket.min_value = -2147483648
    start_indice_socket.max_value = 2147483647
    start_indice_socket.subtype = 'NONE'
    start_indice_socket.attribute_domain = 'POINT'
    start_indice_socket.hide_value = True
    start_indice_socket.default_input = 'VALUE'
    start_indice_socket.structure_type = 'AUTO'

    # Socket End Indice
    end_indice_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="End Indice", in_out='INPUT', socket_type='NodeSocketInt')
    end_indice_socket.default_value = 0
    end_indice_socket.min_value = -2147483648
    end_indice_socket.max_value = 2147483647
    end_indice_socket.subtype = 'NONE'
    end_indice_socket.attribute_domain = 'POINT'
    end_indice_socket.default_input = 'VALUE'
    end_indice_socket.structure_type = 'AUTO'

    # Socket Wire Thickness
    wire_thickness_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Wire Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    wire_thickness_socket.default_value = 0.0010000000474974513
    wire_thickness_socket.min_value = 0.0
    wire_thickness_socket.max_value = 3.4028234663852886e+38
    wire_thickness_socket.subtype = 'DISTANCE'
    wire_thickness_socket.attribute_domain = 'POINT'
    wire_thickness_socket.default_input = 'VALUE'
    wire_thickness_socket.structure_type = 'AUTO'

    # Socket Crosstalk Factor
    crosstalk_factor_socket = instantiate_wire_with_crosstalk_att_001_1.interface.new_socket(name="Crosstalk Factor", in_out='INPUT', socket_type='NodeSocketFloat')
    crosstalk_factor_socket.default_value = 0.0
    crosstalk_factor_socket.min_value = 0.0
    crosstalk_factor_socket.max_value = 1.0
    crosstalk_factor_socket.subtype = 'FACTOR'
    crosstalk_factor_socket.attribute_domain = 'POINT'
    crosstalk_factor_socket.default_input = 'VALUE'
    crosstalk_factor_socket.structure_type = 'AUTO'

    # Initialize instantiate_wire_with_crosstalk_att_001_1 nodes

    # Node Group Input
    group_input = instantiate_wire_with_crosstalk_att_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Shortest Edge Paths
    shortest_edge_paths = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeInputShortestEdgePaths")
    shortest_edge_paths.name = "Shortest Edge Paths"
    shortest_edge_paths.show_options = True

    # Node Edge Paths to Curves
    edge_paths_to_curves = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeEdgePathsToCurves")
    edge_paths_to_curves.name = "Edge Paths to Curves"
    edge_paths_to_curves.show_options = True

    # Node Edge Vertices
    edge_vertices = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeInputMeshEdgeVertices")
    edge_vertices.name = "Edge Vertices"
    edge_vertices.show_options = True

    # Node Vector Math
    vector_math = instantiate_wire_with_crosstalk_att_001_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'DISTANCE'

    # Node Group Output
    group_output = instantiate_wire_with_crosstalk_att_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Index
    index = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Compare
    compare = instantiate_wire_with_crosstalk_att_001_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'

    # Node Index.001
    index_001 = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Compare.001
    compare_001 = instantiate_wire_with_crosstalk_att_001_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.show_options = True
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'

    # Node Reroute
    reroute = instantiate_wire_with_crosstalk_att_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Edge Paths to Selection
    edge_paths_to_selection = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeEdgePathsToSelection")
    edge_paths_to_selection.name = "Edge Paths to Selection"
    edge_paths_to_selection.show_options = True

    # Node Frame
    frame = instantiate_wire_with_crosstalk_att_001_1.nodes.new("NodeFrame")
    frame.label = "Crosstalk Heuristic"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.6079999804496765, 0.24301819503307343, 0.3947525918483734)
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Reroute.001
    reroute_001 = instantiate_wire_with_crosstalk_att_001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Reroute.002
    reroute_002 = instantiate_wire_with_crosstalk_att_001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Mix
    mix = instantiate_wire_with_crosstalk_att_001_1.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.show_options = True
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'FLOAT'
    mix.factor_mode = 'UNIFORM'

    # Node Viewer
    viewer = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'EDGE'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")
    viewer.viewer_items.new('FLOAT', "Value")

    # Node Math
    math = instantiate_wire_with_crosstalk_att_001_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'DIVIDE'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 100.0

    # Node Sample Index
    sample_index = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT'
    sample_index.domain = 'EDGE'

    # Node Named Attribute
    named_attribute = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'FLOAT'
    # Name
    named_attribute.inputs[0].default_value = "crosstalk_weight"

    # Node Reroute.003
    reroute_003 = instantiate_wire_with_crosstalk_att_001_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Index.002
    index_002 = instantiate_wire_with_crosstalk_att_001_1.nodes.new("GeometryNodeInputIndex")
    index_002.name = "Index.002"
    index_002.show_options = True

    # Set parents
    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Vertices"].parent = instantiate_wire_with_crosstalk_att_001_1.nodes["Frame"]
    instantiate_wire_with_crosstalk_att_001_1.nodes["Vector Math"].parent = instantiate_wire_with_crosstalk_att_001_1.nodes["Frame"]

    # Set locations
    instantiate_wire_with_crosstalk_att_001_1.nodes["Group Input"].location = (-1820.0, 280.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].location = (-280.0, -20.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Curves"].location = (-86.9710693359375, 152.94639587402344)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Vertices"].location = (30.0, -36.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Vector Math"].location = (210.0, -36.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Group Output"].location = (1020.0, 200.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Index"].location = (-747.4937744140625, 54.251468658447266)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Compare"].location = (-546.8992309570312, 113.68620300292969)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Index.001"].location = (-751.466552734375, -111.96310424804688)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Compare.001"].location = (-550.8720092773438, -52.52836608886719)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute"].location = (-202.9334716796875, 111.42935180664062)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Selection"].location = (-80.0, 280.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Frame"].location = (-1200.0, -744.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.001"].location = (620.0, 340.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.002"].location = (-213.009033203125, 316.1565856933594)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].location = (-400.0, -300.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Viewer"].location = (-220.0, -200.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Math"].location = (-1120.0, -580.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Sample Index"].location = (-1120.0, -120.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Named Attribute"].location = (-1320.0, -220.0)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].location = (-1313.341796875, 221.7642364501953)
    instantiate_wire_with_crosstalk_att_001_1.nodes["Index.002"].location = (-1340.0, -160.0)

    # Set dimensions
    instantiate_wire_with_crosstalk_att_001_1.nodes["Group Input"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Group Input"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Curves"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Curves"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Vertices"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Vertices"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Vector Math"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Vector Math"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Group Output"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Group Output"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Index"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Index"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Compare"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Compare"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Index.001"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Index.001"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Compare.001"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Compare.001"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute"].width  = 10.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Selection"].width  = 150.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Selection"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Frame"].width  = 380.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Frame"].height = 189.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.001"].width  = 10.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.001"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.002"].width  = 10.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.002"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Viewer"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Viewer"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Math"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Math"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Sample Index"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Sample Index"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Named Attribute"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Named Attribute"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].width  = 10.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].height = 100.0

    instantiate_wire_with_crosstalk_att_001_1.nodes["Index.002"].width  = 140.0
    instantiate_wire_with_crosstalk_att_001_1.nodes["Index.002"].height = 100.0


    # Initialize instantiate_wire_with_crosstalk_att_001_1 links

    # reroute.Output -> edge_paths_to_curves.Mesh
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Curves"].inputs[0]
    )
    # edge_vertices.Position 1 -> vector_math.Vector
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Vertices"].outputs[2],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Vector Math"].inputs[0]
    )
    # edge_vertices.Position 2 -> vector_math.Vector
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Vertices"].outputs[3],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Vector Math"].inputs[1]
    )
    # shortest_edge_paths.Next Vertex Index -> edge_paths_to_curves.Next Vertex Index
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Curves"].inputs[2]
    )
    # compare.Result -> edge_paths_to_curves.Start Vertices
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Compare"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Curves"].inputs[1]
    )
    # compare_001.Result -> shortest_edge_paths.End Vertex
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Compare.001"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].inputs[0]
    )
    # group_input.End Indice -> compare_001.B
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Input"].outputs[2],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Compare.001"].inputs[3]
    )
    # group_input.Start Indice -> compare.B
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Input"].outputs[1],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Compare"].inputs[3]
    )
    # index.Index -> compare.A
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Index"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Compare"].inputs[2]
    )
    # index_001.Index -> compare_001.A
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Index.001"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Compare.001"].inputs[2]
    )
    # reroute_003.Output -> reroute.Input
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute"].inputs[0]
    )
    # compare.Result -> edge_paths_to_selection.Start Vertices
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Compare"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Selection"].inputs[0]
    )
    # shortest_edge_paths.Next Vertex Index -> edge_paths_to_selection.Next Vertex Index
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Selection"].inputs[1]
    )
    # edge_paths_to_selection.Selection -> group_output.Vertex Selection
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Selection"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Output"].inputs[2]
    )
    # edge_paths_to_curves.Curves -> group_output.Wires
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Edge Paths to Curves"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Output"].inputs[0]
    )
    # reroute_001.Output -> group_output.Grid
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.001"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Output"].inputs[1]
    )
    # reroute_002.Output -> reroute_001.Input
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.002"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_003.Output -> reroute_002.Input
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.002"].inputs[0]
    )
    # vector_math.Value -> mix.B
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Vector Math"].outputs[1],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].inputs[3]
    )
    # mix.Result -> shortest_edge_paths.Edge Cost
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].inputs[1]
    )
    # shortest_edge_paths.Total Cost -> group_output.Total Cost
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Shortest Edge Paths"].outputs[1],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Output"].inputs[3]
    )
    # mix.Result -> viewer.Value
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Viewer"].inputs[1]
    )
    # reroute_003.Output -> viewer.Geometry
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Crosstalk Factor -> math.Value
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Input"].outputs[4],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Math"].inputs[0]
    )
    # math.Value -> mix.Factor
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Math"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].inputs[0]
    )
    # named_attribute.Attribute -> sample_index.Value
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Named Attribute"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Sample Index"].inputs[1]
    )
    # group_input.Mesh -> reroute_003.Input
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Group Input"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_003.Output -> sample_index.Geometry
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Reroute.003"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Sample Index"].inputs[0]
    )
    # index_002.Index -> sample_index.Index
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Index.002"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Sample Index"].inputs[2]
    )
    # sample_index.Value -> mix.A
    instantiate_wire_with_crosstalk_att_001_1.links.new(
        instantiate_wire_with_crosstalk_att_001_1.nodes["Sample Index"].outputs[0],
        instantiate_wire_with_crosstalk_att_001_1.nodes["Mix"].inputs[2]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return instantiate_wire_with_crosstalk_att_001_1


def weighted_zone_heuristic_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Weighted Zone Heuristic.001 node group"""
    weighted_zone_heuristic_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Weighted Zone Heuristic.001")

    weighted_zone_heuristic_001_1.color_tag = 'NONE'
    weighted_zone_heuristic_001_1.description = ""
    weighted_zone_heuristic_001_1.default_group_node_width = 140
    weighted_zone_heuristic_001_1.show_modifier_manage_panel = True

    # weighted_zone_heuristic_001_1 interface

    # Socket Routing
    routing_socket = weighted_zone_heuristic_001_1.interface.new_socket(name="Routing", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    routing_socket.attribute_domain = 'POINT'
    routing_socket.default_input = 'VALUE'
    routing_socket.structure_type = 'AUTO'

    # Socket Current Crosstalk
    current_crosstalk_socket = weighted_zone_heuristic_001_1.interface.new_socket(name="Current Crosstalk", in_out='OUTPUT', socket_type='NodeSocketFloat')
    current_crosstalk_socket.default_value = 0.0
    current_crosstalk_socket.min_value = -3.4028234663852886e+38
    current_crosstalk_socket.max_value = 3.4028234663852886e+38
    current_crosstalk_socket.subtype = 'NONE'
    current_crosstalk_socket.attribute_domain = 'POINT'
    current_crosstalk_socket.default_input = 'VALUE'
    current_crosstalk_socket.structure_type = 'AUTO'

    # Socket Routing
    routing_socket_1 = weighted_zone_heuristic_001_1.interface.new_socket(name="Routing", in_out='INPUT', socket_type='NodeSocketGeometry')
    routing_socket_1.attribute_domain = 'POINT'
    routing_socket_1.default_input = 'VALUE'
    routing_socket_1.structure_type = 'AUTO'

    # Socket Current Wire
    current_wire_socket = weighted_zone_heuristic_001_1.interface.new_socket(name="Current Wire", in_out='INPUT', socket_type='NodeSocketGeometry')
    current_wire_socket.attribute_domain = 'POINT'
    current_wire_socket.default_input = 'VALUE'
    current_wire_socket.structure_type = 'AUTO'

    # Socket Value Multiplier
    value_multiplier_socket = weighted_zone_heuristic_001_1.interface.new_socket(name="Value Multiplier", in_out='INPUT', socket_type='NodeSocketFloat')
    value_multiplier_socket.default_value = 1.0
    value_multiplier_socket.min_value = -10000.0
    value_multiplier_socket.max_value = 10000.0
    value_multiplier_socket.subtype = 'NONE'
    value_multiplier_socket.attribute_domain = 'POINT'
    value_multiplier_socket.default_input = 'VALUE'
    value_multiplier_socket.structure_type = 'AUTO'

    # Socket Avoid Distance
    avoid_distance_socket = weighted_zone_heuristic_001_1.interface.new_socket(name="Avoid Distance", in_out='INPUT', socket_type='NodeSocketFloat')
    avoid_distance_socket.default_value = 0.019999999552965164
    avoid_distance_socket.min_value = -10000.0
    avoid_distance_socket.max_value = 10000.0
    avoid_distance_socket.subtype = 'NONE'
    avoid_distance_socket.attribute_domain = 'POINT'
    avoid_distance_socket.default_input = 'VALUE'
    avoid_distance_socket.structure_type = 'AUTO'

    # Initialize weighted_zone_heuristic_001_1 nodes

    # Node Group Output
    group_output = weighted_zone_heuristic_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = weighted_zone_heuristic_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Geometry Proximity
    geometry_proximity = weighted_zone_heuristic_001_1.nodes.new("GeometryNodeProximity")
    geometry_proximity.name = "Geometry Proximity"
    geometry_proximity.show_options = True
    geometry_proximity.target_element = 'EDGES'
    # Group ID
    geometry_proximity.inputs[1].default_value = 0
    # Sample Group ID
    geometry_proximity.inputs[3].default_value = 0

    # Node Sample Index
    sample_index = weighted_zone_heuristic_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'EDGE'

    # Node Index
    index = weighted_zone_heuristic_001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Position
    position = weighted_zone_heuristic_001_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Compare
    compare = weighted_zone_heuristic_001_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_THAN'

    # Node Math
    math = weighted_zone_heuristic_001_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Reroute.001
    reroute_001 = weighted_zone_heuristic_001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Reroute.002
    reroute_002 = weighted_zone_heuristic_001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Math.001
    math_001 = weighted_zone_heuristic_001_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    # Node Reroute
    reroute = weighted_zone_heuristic_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Viewer
    viewer = weighted_zone_heuristic_001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'EDGE'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")
    viewer.viewer_items.new('FLOAT', "Value")

    # Set locations
    weighted_zone_heuristic_001_1.nodes["Group Output"].location = (-320.0, 940.0)
    weighted_zone_heuristic_001_1.nodes["Group Input"].location = (-2860.000244140625, 900.0)
    weighted_zone_heuristic_001_1.nodes["Geometry Proximity"].location = (-2200.000244140625, 920.0)
    weighted_zone_heuristic_001_1.nodes["Sample Index"].location = (-2480.000244140625, 800.0)
    weighted_zone_heuristic_001_1.nodes["Index"].location = (-2740.000244140625, 620.0)
    weighted_zone_heuristic_001_1.nodes["Position"].location = (-2740.000244140625, 680.0)
    weighted_zone_heuristic_001_1.nodes["Compare"].location = (-1980.0, 760.0)
    weighted_zone_heuristic_001_1.nodes["Math"].location = (-1660.0, 940.0)
    weighted_zone_heuristic_001_1.nodes["Reroute.001"].location = (-1740.0, 940.0)
    weighted_zone_heuristic_001_1.nodes["Reroute.002"].location = (-2620.000244140625, 920.0)
    weighted_zone_heuristic_001_1.nodes["Math.001"].location = (-1480.0, 840.0)
    weighted_zone_heuristic_001_1.nodes["Reroute"].location = (-1862.11474609375, 1025.4068603515625)
    weighted_zone_heuristic_001_1.nodes["Viewer"].location = (-1300.0, 946.0)

    # Set dimensions
    weighted_zone_heuristic_001_1.nodes["Group Output"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Group Output"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Group Input"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Group Input"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Geometry Proximity"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Geometry Proximity"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Sample Index"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Sample Index"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Index"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Index"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Position"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Position"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Compare"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Compare"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Math"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Math"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Reroute.001"].width  = 20.0
    weighted_zone_heuristic_001_1.nodes["Reroute.001"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Reroute.002"].width  = 20.0
    weighted_zone_heuristic_001_1.nodes["Reroute.002"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Math.001"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Math.001"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Reroute"].width  = 20.0
    weighted_zone_heuristic_001_1.nodes["Reroute"].height = 100.0

    weighted_zone_heuristic_001_1.nodes["Viewer"].width  = 140.0
    weighted_zone_heuristic_001_1.nodes["Viewer"].height = 100.0


    # Initialize weighted_zone_heuristic_001_1 links

    # index.Index -> sample_index.Index
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Index"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Sample Index"].inputs[2]
    )
    # position.Position -> sample_index.Value
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Position"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Sample Index"].inputs[1]
    )
    # sample_index.Value -> geometry_proximity.Sample Position
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Sample Index"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Geometry Proximity"].inputs[2]
    )
    # geometry_proximity.Distance -> compare.A
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Geometry Proximity"].outputs[1],
        weighted_zone_heuristic_001_1.nodes["Compare"].inputs[0]
    )
    # group_input.Routing -> sample_index.Geometry
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Group Input"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Sample Index"].inputs[0]
    )
    # group_input.Current Wire -> geometry_proximity.Geometry
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Group Input"].outputs[1],
        weighted_zone_heuristic_001_1.nodes["Geometry Proximity"].inputs[0]
    )
    # compare.Result -> math.Value
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Compare"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Math"].inputs[0]
    )
    # reroute_001.Output -> math.Value
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Reroute.001"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Math"].inputs[1]
    )
    # reroute_002.Output -> reroute_001.Input
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Reroute.002"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Reroute.001"].inputs[0]
    )
    # group_input.Value Multiplier -> reroute_002.Input
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Group Input"].outputs[2],
        weighted_zone_heuristic_001_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Avoid Distance -> compare.B
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Group Input"].outputs[3],
        weighted_zone_heuristic_001_1.nodes["Compare"].inputs[1]
    )
    # math.Value -> math_001.Value
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Math"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Math.001"].inputs[0]
    )
    # geometry_proximity.Distance -> math_001.Value
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Geometry Proximity"].outputs[1],
        weighted_zone_heuristic_001_1.nodes["Math.001"].inputs[1]
    )
    # group_input.Routing -> reroute.Input
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Group Input"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> group_output.Routing
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Reroute"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Group Output"].inputs[0]
    )
    # math_001.Value -> group_output.Current Crosstalk
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Math.001"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Group Output"].inputs[1]
    )
    # reroute.Output -> viewer.Geometry
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Reroute"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Viewer"].inputs[0]
    )
    # math_001.Value -> viewer.Value
    weighted_zone_heuristic_001_1.links.new(
        weighted_zone_heuristic_001_1.nodes["Math.001"].outputs[0],
        weighted_zone_heuristic_001_1.nodes["Viewer"].inputs[1]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return weighted_zone_heuristic_001_1


def overlap_remover_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Overlap Remover.001 node group"""
    overlap_remover_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Overlap Remover.001")

    overlap_remover_001_1.color_tag = 'NONE'
    overlap_remover_001_1.description = ""
    overlap_remover_001_1.default_group_node_width = 140
    overlap_remover_001_1.show_modifier_manage_panel = True

    # overlap_remover_001_1 interface

    # Socket Result
    result_socket = overlap_remover_001_1.interface.new_socket(name="Result", in_out='OUTPUT', socket_type='NodeSocketBool')
    result_socket.default_value = False
    result_socket.attribute_domain = 'POINT'
    result_socket.default_input = 'VALUE'
    result_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket = overlap_remover_001_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Routing
    routing_socket = overlap_remover_001_1.interface.new_socket(name="Routing", in_out='INPUT', socket_type='NodeSocketGeometry')
    routing_socket.attribute_domain = 'POINT'
    routing_socket.default_input = 'VALUE'
    routing_socket.structure_type = 'AUTO'

    # Socket Wire
    wire_socket = overlap_remover_001_1.interface.new_socket(name="Wire", in_out='INPUT', socket_type='NodeSocketGeometry')
    wire_socket.attribute_domain = 'POINT'
    wire_socket.default_input = 'VALUE'
    wire_socket.structure_type = 'AUTO'

    # Socket Wire Thickness
    wire_thickness_socket = overlap_remover_001_1.interface.new_socket(name="Wire Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    wire_thickness_socket.default_value = 0.5
    wire_thickness_socket.min_value = -10000.0
    wire_thickness_socket.max_value = 10000.0
    wire_thickness_socket.subtype = 'NONE'
    wire_thickness_socket.attribute_domain = 'POINT'
    wire_thickness_socket.default_input = 'VALUE'
    wire_thickness_socket.structure_type = 'AUTO'

    # Socket Level
    level_socket = overlap_remover_001_1.interface.new_socket(name="Level", in_out='INPUT', socket_type='NodeSocketInt')
    level_socket.default_value = 0
    level_socket.min_value = 0
    level_socket.max_value = 6
    level_socket.subtype = 'NONE'
    level_socket.attribute_domain = 'POINT'
    level_socket.default_input = 'VALUE'
    level_socket.structure_type = 'AUTO'

    # Socket Value
    value_socket = overlap_remover_001_1.interface.new_socket(name="Value", in_out='INPUT', socket_type='NodeSocketFloat')
    value_socket.default_value = 2.0
    value_socket.min_value = -10000.0
    value_socket.max_value = 10000.0
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    value_socket.default_input = 'VALUE'
    value_socket.structure_type = 'AUTO'

    # Initialize overlap_remover_001_1 nodes

    # Node Group Output
    group_output = overlap_remover_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = overlap_remover_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Compare.001
    compare_001 = overlap_remover_001_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.show_options = True
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'LESS_THAN'

    # Node Geometry Proximity
    geometry_proximity = overlap_remover_001_1.nodes.new("GeometryNodeProximity")
    geometry_proximity.name = "Geometry Proximity"
    geometry_proximity.show_options = True
    geometry_proximity.target_element = 'EDGES'
    # Group ID
    geometry_proximity.inputs[1].default_value = 0
    # Sample Group ID
    geometry_proximity.inputs[3].default_value = 0

    # Node Sample Index.002
    sample_index_002 = overlap_remover_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'EDGE'

    # Node Position.001
    position_001 = overlap_remover_001_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Index.001
    index_001 = overlap_remover_001_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Curve to Mesh
    curve_to_mesh = overlap_remover_001_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.show_options = True
    # Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    # Node Math.001
    math_001 = overlap_remover_001_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    # Node Subdivide Mesh
    subdivide_mesh = overlap_remover_001_1.nodes.new("GeometryNodeSubdivideMesh")
    subdivide_mesh.name = "Subdivide Mesh"
    subdivide_mesh.show_options = True

    # Node Reroute
    reroute = overlap_remover_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Reroute.001
    reroute_001 = overlap_remover_001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Separate Geometry
    separate_geometry = overlap_remover_001_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.show_options = True
    separate_geometry.domain = 'EDGE'

    # Node Index.003
    index_003 = overlap_remover_001_1.nodes.new("GeometryNodeInputIndex")
    index_003.name = "Index.003"
    index_003.show_options = True

    # Node Reroute.002
    reroute_002 = overlap_remover_001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Viewer.002
    viewer_002 = overlap_remover_001_1.nodes.new("GeometryNodeViewer")
    viewer_002.name = "Viewer.002"
    viewer_002.show_options = True
    viewer_002.active_index = 0
    viewer_002.domain = 'EDGE'
    viewer_002.ui_shortcut = 0
    viewer_002.viewer_items.clear()
    viewer_002.viewer_items.new('GEOMETRY', "Geometry")
    viewer_002.viewer_items.new('FLOAT', "Value")

    # Node Index.004
    index_004 = overlap_remover_001_1.nodes.new("GeometryNodeInputIndex")
    index_004.name = "Index.004"
    index_004.show_options = True

    # Node Store Named Attribute
    store_named_attribute = overlap_remover_001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'INT'
    store_named_attribute.domain = 'EDGE'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "edge_num"

    # Node Index.005
    index_005 = overlap_remover_001_1.nodes.new("GeometryNodeInputIndex")
    index_005.name = "Index.005"
    index_005.show_options = True

    # Node Reroute.003
    reroute_003 = overlap_remover_001_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Sample Index
    sample_index = overlap_remover_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'INT'
    sample_index.domain = 'EDGE'

    # Node Index.002
    index_002 = overlap_remover_001_1.nodes.new("GeometryNodeInputIndex")
    index_002.name = "Index.002"
    index_002.show_options = True

    # Node Named Attribute.001
    named_attribute_001 = overlap_remover_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'INT'
    # Name
    named_attribute_001.inputs[0].default_value = "edge_num"

    # Node Named Attribute
    named_attribute = overlap_remover_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'INT'
    # Name
    named_attribute.inputs[0].default_value = "edge_num"

    # Node Sample Index.001
    sample_index_001 = overlap_remover_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'BOOLEAN'
    sample_index_001.domain = 'EDGE'

    # Node Index.006
    index_006 = overlap_remover_001_1.nodes.new("GeometryNodeInputIndex")
    index_006.name = "Index.006"
    index_006.show_options = True

    # Node Named Attribute.002
    named_attribute_002 = overlap_remover_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.show_options = True
    named_attribute_002.data_type = 'BOOLEAN'
    # Name
    named_attribute_002.inputs[0].default_value = "overlap"

    # Node Repeat Input
    repeat_input = overlap_remover_001_1.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    repeat_input.show_options = True
    # Node Repeat Output
    repeat_output = overlap_remover_001_1.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.show_options = True
    repeat_output.active_index = 0
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")

    # Node Domain Size
    domain_size = overlap_remover_001_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.show_options = True
    domain_size.component = 'MESH'

    # Node Sample Index.003
    sample_index_003 = overlap_remover_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_003.name = "Sample Index.003"
    sample_index_003.show_options = True
    sample_index_003.clamp = False
    sample_index_003.data_type = 'INT'
    sample_index_003.domain = 'EDGE'

    # Node Compare.002
    compare_002 = overlap_remover_001_1.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.show_options = True
    compare_002.data_type = 'INT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'

    # Node Index.007
    index_007 = overlap_remover_001_1.nodes.new("GeometryNodeInputIndex")
    index_007.name = "Index.007"
    index_007.show_options = True

    # Node Store Named Attribute.002
    store_named_attribute_002 = overlap_remover_001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'BOOLEAN'
    store_named_attribute_002.domain = 'EDGE'
    # Name
    store_named_attribute_002.inputs[2].default_value = "overlap"
    # Value
    store_named_attribute_002.inputs[3].default_value = True

    # Node Viewer
    viewer = overlap_remover_001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'EDGE'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")
    viewer.viewer_items.new('FLOAT', "Value")

    # Node Clamp
    clamp = overlap_remover_001_1.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.show_options = True
    clamp.clamp_type = 'MINMAX'
    # Min
    clamp.inputs[1].default_value = 0.0
    # Max
    clamp.inputs[2].default_value = 11.0

    # Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)



    # Set locations
    overlap_remover_001_1.nodes["Group Output"].location = (4000.0, -260.0)
    overlap_remover_001_1.nodes["Group Input"].location = (-1580.0, -20.0)
    overlap_remover_001_1.nodes["Compare.001"].location = (389.99993896484375, 20.0)
    overlap_remover_001_1.nodes["Geometry Proximity"].location = (-10.000000953674316, 80.0)
    overlap_remover_001_1.nodes["Sample Index.002"].location = (-209.99998474121094, 180.0)
    overlap_remover_001_1.nodes["Position.001"].location = (-440.00006103515625, 180.0)
    overlap_remover_001_1.nodes["Index.001"].location = (-440.00006103515625, 100.0)
    overlap_remover_001_1.nodes["Curve to Mesh"].location = (-209.99998474121094, -80.0)
    overlap_remover_001_1.nodes["Math.001"].location = (190.00001525878906, -180.0)
    overlap_remover_001_1.nodes["Subdivide Mesh"].location = (-620.0, 20.0)
    overlap_remover_001_1.nodes["Reroute"].location = (459.9998779296875, 240.0)
    overlap_remover_001_1.nodes["Reroute.001"].location = (-440.00006103515625, 260.0)
    overlap_remover_001_1.nodes["Separate Geometry"].location = (680.0, -40.0)
    overlap_remover_001_1.nodes["Index.003"].location = (1160.0, 240.0)
    overlap_remover_001_1.nodes["Reroute.002"].location = (-700.0, 340.0)
    overlap_remover_001_1.nodes["Viewer.002"].location = (1800.0, 540.0)
    overlap_remover_001_1.nodes["Index.004"].location = (1500.0, 580.0)
    overlap_remover_001_1.nodes["Store Named Attribute"].location = (-1000.0, 160.0)
    overlap_remover_001_1.nodes["Index.005"].location = (-1180.0, 0.0)
    overlap_remover_001_1.nodes["Reroute.003"].location = (1424.726806640625, 323.3970031738281)
    overlap_remover_001_1.nodes["Sample Index"].location = (1160.0, 180.0)
    overlap_remover_001_1.nodes["Index.002"].location = (760.0, 60.0)
    overlap_remover_001_1.nodes["Named Attribute.001"].location = (760.0, 200.0)
    overlap_remover_001_1.nodes["Named Attribute"].location = (1340.0, -500.0)
    overlap_remover_001_1.nodes["Sample Index.001"].location = (3100.0, 160.0)
    overlap_remover_001_1.nodes["Index.006"].location = (2780.0, 140.0)
    overlap_remover_001_1.nodes["Named Attribute.002"].location = (2780.0, 280.0)
    overlap_remover_001_1.nodes["Repeat Input"].location = (1640.0, -300.0)
    overlap_remover_001_1.nodes["Repeat Output"].location = (2660.0, -300.0)
    overlap_remover_001_1.nodes["Domain Size"].location = (1120.0, -260.0)
    overlap_remover_001_1.nodes["Sample Index.003"].location = (1940.0, -500.0)
    overlap_remover_001_1.nodes["Compare.002"].location = (2200.0, -400.0)
    overlap_remover_001_1.nodes["Index.007"].location = (1940.0, -440.0)
    overlap_remover_001_1.nodes["Store Named Attribute.002"].location = (2420.0, -300.0)
    overlap_remover_001_1.nodes["Viewer"].location = (3380.0, -140.0)
    overlap_remover_001_1.nodes["Clamp"].location = (-645.0, 20.0)

    # Set dimensions
    overlap_remover_001_1.nodes["Group Output"].width  = 140.0
    overlap_remover_001_1.nodes["Group Output"].height = 100.0

    overlap_remover_001_1.nodes["Group Input"].width  = 140.0
    overlap_remover_001_1.nodes["Group Input"].height = 100.0

    overlap_remover_001_1.nodes["Compare.001"].width  = 140.0
    overlap_remover_001_1.nodes["Compare.001"].height = 100.0

    overlap_remover_001_1.nodes["Geometry Proximity"].width  = 140.0
    overlap_remover_001_1.nodes["Geometry Proximity"].height = 100.0

    overlap_remover_001_1.nodes["Sample Index.002"].width  = 140.0
    overlap_remover_001_1.nodes["Sample Index.002"].height = 100.0

    overlap_remover_001_1.nodes["Position.001"].width  = 140.0
    overlap_remover_001_1.nodes["Position.001"].height = 100.0

    overlap_remover_001_1.nodes["Index.001"].width  = 140.0
    overlap_remover_001_1.nodes["Index.001"].height = 100.0

    overlap_remover_001_1.nodes["Curve to Mesh"].width  = 140.0
    overlap_remover_001_1.nodes["Curve to Mesh"].height = 100.0

    overlap_remover_001_1.nodes["Math.001"].width  = 140.0
    overlap_remover_001_1.nodes["Math.001"].height = 100.0

    overlap_remover_001_1.nodes["Subdivide Mesh"].width  = 140.0
    overlap_remover_001_1.nodes["Subdivide Mesh"].height = 100.0

    overlap_remover_001_1.nodes["Reroute"].width  = 10.0
    overlap_remover_001_1.nodes["Reroute"].height = 100.0

    overlap_remover_001_1.nodes["Reroute.001"].width  = 10.0
    overlap_remover_001_1.nodes["Reroute.001"].height = 100.0

    overlap_remover_001_1.nodes["Separate Geometry"].width  = 140.0
    overlap_remover_001_1.nodes["Separate Geometry"].height = 100.0

    overlap_remover_001_1.nodes["Index.003"].width  = 140.0
    overlap_remover_001_1.nodes["Index.003"].height = 100.0

    overlap_remover_001_1.nodes["Reroute.002"].width  = 10.0
    overlap_remover_001_1.nodes["Reroute.002"].height = 100.0

    overlap_remover_001_1.nodes["Viewer.002"].width  = 140.0
    overlap_remover_001_1.nodes["Viewer.002"].height = 100.0

    overlap_remover_001_1.nodes["Index.004"].width  = 140.0
    overlap_remover_001_1.nodes["Index.004"].height = 100.0

    overlap_remover_001_1.nodes["Store Named Attribute"].width  = 140.0
    overlap_remover_001_1.nodes["Store Named Attribute"].height = 100.0

    overlap_remover_001_1.nodes["Index.005"].width  = 140.0
    overlap_remover_001_1.nodes["Index.005"].height = 100.0

    overlap_remover_001_1.nodes["Reroute.003"].width  = 10.0
    overlap_remover_001_1.nodes["Reroute.003"].height = 100.0

    overlap_remover_001_1.nodes["Sample Index"].width  = 140.0
    overlap_remover_001_1.nodes["Sample Index"].height = 100.0

    overlap_remover_001_1.nodes["Index.002"].width  = 140.0
    overlap_remover_001_1.nodes["Index.002"].height = 100.0

    overlap_remover_001_1.nodes["Named Attribute.001"].width  = 140.0
    overlap_remover_001_1.nodes["Named Attribute.001"].height = 100.0

    overlap_remover_001_1.nodes["Named Attribute"].width  = 140.0
    overlap_remover_001_1.nodes["Named Attribute"].height = 100.0

    overlap_remover_001_1.nodes["Sample Index.001"].width  = 140.0
    overlap_remover_001_1.nodes["Sample Index.001"].height = 100.0

    overlap_remover_001_1.nodes["Index.006"].width  = 140.0
    overlap_remover_001_1.nodes["Index.006"].height = 100.0

    overlap_remover_001_1.nodes["Named Attribute.002"].width  = 140.0
    overlap_remover_001_1.nodes["Named Attribute.002"].height = 100.0

    overlap_remover_001_1.nodes["Repeat Input"].width  = 140.0
    overlap_remover_001_1.nodes["Repeat Input"].height = 100.0

    overlap_remover_001_1.nodes["Repeat Output"].width  = 140.0
    overlap_remover_001_1.nodes["Repeat Output"].height = 100.0

    overlap_remover_001_1.nodes["Domain Size"].width  = 140.0
    overlap_remover_001_1.nodes["Domain Size"].height = 100.0

    overlap_remover_001_1.nodes["Sample Index.003"].width  = 140.0
    overlap_remover_001_1.nodes["Sample Index.003"].height = 100.0

    overlap_remover_001_1.nodes["Compare.002"].width  = 140.0
    overlap_remover_001_1.nodes["Compare.002"].height = 100.0

    overlap_remover_001_1.nodes["Index.007"].width  = 140.0
    overlap_remover_001_1.nodes["Index.007"].height = 100.0

    overlap_remover_001_1.nodes["Store Named Attribute.002"].width  = 140.0
    overlap_remover_001_1.nodes["Store Named Attribute.002"].height = 100.0

    overlap_remover_001_1.nodes["Viewer"].width  = 140.0
    overlap_remover_001_1.nodes["Viewer"].height = 100.0

    overlap_remover_001_1.nodes["Clamp"].width  = 140.0
    overlap_remover_001_1.nodes["Clamp"].height = 100.0


    # Initialize overlap_remover_001_1 links

    # sample_index_002.Value -> geometry_proximity.Sample Position
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Sample Index.002"].outputs[0],
        overlap_remover_001_1.nodes["Geometry Proximity"].inputs[2]
    )
    # curve_to_mesh.Mesh -> geometry_proximity.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Curve to Mesh"].outputs[0],
        overlap_remover_001_1.nodes["Geometry Proximity"].inputs[0]
    )
    # position_001.Position -> sample_index_002.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Position.001"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.002"].inputs[1]
    )
    # geometry_proximity.Distance -> compare_001.A
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Geometry Proximity"].outputs[1],
        overlap_remover_001_1.nodes["Compare.001"].inputs[0]
    )
    # math_001.Value -> compare_001.B
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Math.001"].outputs[0],
        overlap_remover_001_1.nodes["Compare.001"].inputs[1]
    )
    # index_001.Index -> sample_index_002.Index
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Index.001"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.002"].inputs[2]
    )
    # group_input.Wire -> curve_to_mesh.Curve
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Group Input"].outputs[1],
        overlap_remover_001_1.nodes["Curve to Mesh"].inputs[0]
    )
    # subdivide_mesh.Mesh -> sample_index_002.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Subdivide Mesh"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.002"].inputs[0]
    )
    # group_input.Wire Thickness -> math_001.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Group Input"].outputs[2],
        overlap_remover_001_1.nodes["Math.001"].inputs[0]
    )
    # store_named_attribute.Geometry -> subdivide_mesh.Mesh
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Store Named Attribute"].outputs[0],
        overlap_remover_001_1.nodes["Subdivide Mesh"].inputs[0]
    )
    # reroute_001.Output -> reroute.Input
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Reroute.001"].outputs[0],
        overlap_remover_001_1.nodes["Reroute"].inputs[0]
    )
    # subdivide_mesh.Mesh -> reroute_001.Input
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Subdivide Mesh"].outputs[0],
        overlap_remover_001_1.nodes["Reroute.001"].inputs[0]
    )
    # compare_001.Result -> separate_geometry.Selection
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Compare.001"].outputs[0],
        overlap_remover_001_1.nodes["Separate Geometry"].inputs[1]
    )
    # reroute.Output -> separate_geometry.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Reroute"].outputs[0],
        overlap_remover_001_1.nodes["Separate Geometry"].inputs[0]
    )
    # reroute.Output -> viewer_002.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Reroute"].outputs[0],
        overlap_remover_001_1.nodes["Viewer.002"].inputs[0]
    )
    # index_004.Index -> viewer_002.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Index.004"].outputs[0],
        overlap_remover_001_1.nodes["Viewer.002"].inputs[1]
    )
    # group_input.Routing -> store_named_attribute.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Group Input"].outputs[0],
        overlap_remover_001_1.nodes["Store Named Attribute"].inputs[0]
    )
    # index_005.Index -> store_named_attribute.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Index.005"].outputs[0],
        overlap_remover_001_1.nodes["Store Named Attribute"].inputs[3]
    )
    # store_named_attribute.Geometry -> reroute_002.Input
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Store Named Attribute"].outputs[0],
        overlap_remover_001_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_002.Output -> reroute_003.Input
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Reroute.002"].outputs[0],
        overlap_remover_001_1.nodes["Reroute.003"].inputs[0]
    )
    # separate_geometry.Selection -> sample_index.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Separate Geometry"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index"].inputs[0]
    )
    # index_002.Index -> sample_index.Index
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Index.002"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index"].inputs[2]
    )
    # named_attribute_001.Attribute -> sample_index.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Named Attribute.001"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index"].inputs[1]
    )
    # index_006.Index -> sample_index_001.Index
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Index.006"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.001"].inputs[2]
    )
    # named_attribute_002.Attribute -> sample_index_001.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Named Attribute.002"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.001"].inputs[1]
    )
    # separate_geometry.Selection -> domain_size.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Separate Geometry"].outputs[0],
        overlap_remover_001_1.nodes["Domain Size"].inputs[0]
    )
    # domain_size.Edge Count -> repeat_input.Iterations
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Domain Size"].outputs[1],
        overlap_remover_001_1.nodes["Repeat Input"].inputs[0]
    )
    # reroute_003.Output -> repeat_input.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Reroute.003"].outputs[0],
        overlap_remover_001_1.nodes["Repeat Input"].inputs[1]
    )
    # repeat_input.Iteration -> sample_index_003.Index
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Repeat Input"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.003"].inputs[2]
    )
    # separate_geometry.Selection -> sample_index_003.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Separate Geometry"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.003"].inputs[0]
    )
    # named_attribute.Attribute -> sample_index_003.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Named Attribute"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.003"].inputs[1]
    )
    # index_007.Index -> compare_002.A
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Index.007"].outputs[0],
        overlap_remover_001_1.nodes["Compare.002"].inputs[2]
    )
    # sample_index_003.Value -> compare_002.B
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Sample Index.003"].outputs[0],
        overlap_remover_001_1.nodes["Compare.002"].inputs[3]
    )
    # compare_002.Result -> store_named_attribute_002.Selection
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Compare.002"].outputs[0],
        overlap_remover_001_1.nodes["Store Named Attribute.002"].inputs[1]
    )
    # repeat_input.Geometry -> store_named_attribute_002.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Repeat Input"].outputs[1],
        overlap_remover_001_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # store_named_attribute_002.Geometry -> repeat_output.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Store Named Attribute.002"].outputs[0],
        overlap_remover_001_1.nodes["Repeat Output"].inputs[0]
    )
    # repeat_output.Geometry -> sample_index_001.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Repeat Output"].outputs[0],
        overlap_remover_001_1.nodes["Sample Index.001"].inputs[0]
    )
    # repeat_output.Geometry -> group_output.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Repeat Output"].outputs[0],
        overlap_remover_001_1.nodes["Group Output"].inputs[1]
    )
    # sample_index_001.Value -> group_output.Result
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Sample Index.001"].outputs[0],
        overlap_remover_001_1.nodes["Group Output"].inputs[0]
    )
    # repeat_output.Geometry -> viewer.Geometry
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Repeat Output"].outputs[0],
        overlap_remover_001_1.nodes["Viewer"].inputs[0]
    )
    # sample_index_001.Value -> viewer.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Sample Index.001"].outputs[0],
        overlap_remover_001_1.nodes["Viewer"].inputs[1]
    )
    # group_input.Level -> clamp.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Group Input"].outputs[3],
        overlap_remover_001_1.nodes["Clamp"].inputs[0]
    )
    # group_input.Value -> math_001.Value
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Group Input"].outputs[4],
        overlap_remover_001_1.nodes["Math.001"].inputs[1]
    )
    # clamp.Result -> subdivide_mesh.Level
    overlap_remover_001_1.links.new(
        overlap_remover_001_1.nodes["Clamp"].outputs[0],
        overlap_remover_001_1.nodes["Subdivide Mesh"].inputs[1]
    )
    viewer_002.viewer_items[0].auto_remove = False
    viewer_002.viewer_items[1].auto_remove = False
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return overlap_remover_001_1


def remove_from_set_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Remove From Set node group"""
    remove_from_set_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Remove From Set")

    remove_from_set_1.color_tag = 'NONE'
    remove_from_set_1.description = ""
    remove_from_set_1.default_group_node_width = 140
    remove_from_set_1.show_modifier_manage_panel = True

    # remove_from_set_1 interface

    # Socket Clip Index
    clip_index_socket = remove_from_set_1.interface.new_socket(name="Clip Index", in_out='OUTPUT', socket_type='NodeSocketInt')
    clip_index_socket.default_value = 0
    clip_index_socket.min_value = -2147483648
    clip_index_socket.max_value = 2147483647
    clip_index_socket.subtype = 'NONE'
    clip_index_socket.attribute_domain = 'POINT'
    clip_index_socket.default_input = 'VALUE'
    clip_index_socket.structure_type = 'AUTO'

    # Socket Filtered Unrouted Graph
    filtered_unrouted_graph_socket = remove_from_set_1.interface.new_socket(name="Filtered Unrouted Graph", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    filtered_unrouted_graph_socket.attribute_domain = 'POINT'
    filtered_unrouted_graph_socket.default_input = 'VALUE'
    filtered_unrouted_graph_socket.structure_type = 'AUTO'

    # Socket Electrode Index
    electrode_index_socket = remove_from_set_1.interface.new_socket(name="Electrode Index", in_out='INPUT', socket_type='NodeSocketInt')
    electrode_index_socket.default_value = 0
    electrode_index_socket.min_value = -2147483648
    electrode_index_socket.max_value = 2147483647
    electrode_index_socket.subtype = 'NONE'
    electrode_index_socket.attribute_domain = 'POINT'
    electrode_index_socket.default_input = 'VALUE'
    electrode_index_socket.structure_type = 'AUTO'

    # Socket Unrouted Graph
    unrouted_graph_socket = remove_from_set_1.interface.new_socket(name="Unrouted Graph", in_out='INPUT', socket_type='NodeSocketGeometry')
    unrouted_graph_socket.attribute_domain = 'POINT'
    unrouted_graph_socket.description = "Mesh or point cloud to find the nearest point on"
    unrouted_graph_socket.default_input = 'VALUE'
    unrouted_graph_socket.structure_type = 'AUTO'

    # Socket Clip Position
    clip_position_socket = remove_from_set_1.interface.new_socket(name="Clip Position", in_out='INPUT', socket_type='NodeSocketVector')
    clip_position_socket.default_value = (0.0, 0.0, 0.0)
    clip_position_socket.min_value = -3.4028234663852886e+38
    clip_position_socket.max_value = 3.4028234663852886e+38
    clip_position_socket.subtype = 'NONE'
    clip_position_socket.attribute_domain = 'POINT'
    clip_position_socket.hide_value = True
    clip_position_socket.default_input = 'POSITION'
    clip_position_socket.structure_type = 'AUTO'

    # Initialize remove_from_set_1 nodes

    # Node Group Output
    group_output = remove_from_set_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = remove_from_set_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Store Named Attribute.006
    store_named_attribute_006 = remove_from_set_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_006.name = "Store Named Attribute.006"
    store_named_attribute_006.show_options = True
    store_named_attribute_006.data_type = 'BOOLEAN'
    store_named_attribute_006.domain = 'POINT'
    # Name
    store_named_attribute_006.inputs[2].default_value = "electrodes"
    # Value
    store_named_attribute_006.inputs[3].default_value = False

    # Node Compare.005
    compare_005 = remove_from_set_1.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.show_options = True
    compare_005.data_type = 'INT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'EQUAL'

    # Node Index.006
    index_006 = remove_from_set_1.nodes.new("GeometryNodeInputIndex")
    index_006.name = "Index.006"
    index_006.show_options = True

    # Node Sample Nearest.007
    sample_nearest_007 = remove_from_set_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest_007.name = "Sample Nearest.007"
    sample_nearest_007.show_options = True
    sample_nearest_007.domain = 'POINT'

    # Node Store Named Attribute.008
    store_named_attribute_008 = remove_from_set_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_008.name = "Store Named Attribute.008"
    store_named_attribute_008.show_options = True
    store_named_attribute_008.data_type = 'BOOLEAN'
    store_named_attribute_008.domain = 'POINT'
    # Name
    store_named_attribute_008.inputs[2].default_value = "clips"
    # Value
    store_named_attribute_008.inputs[3].default_value = False

    # Node Compare.006
    compare_006 = remove_from_set_1.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.show_options = True
    compare_006.data_type = 'INT'
    compare_006.mode = 'ELEMENT'
    compare_006.operation = 'EQUAL'

    # Node Reroute.027
    reroute_027 = remove_from_set_1.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    reroute_027.show_options = True
    reroute_027.socket_idname = "NodeSocketBool"
    # Node Reroute
    reroute = remove_from_set_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Sample Index
    sample_index = remove_from_set_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'INT'
    sample_index.domain = 'POINT'

    # Node Named Attribute
    named_attribute = remove_from_set_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'INT'
    # Name
    named_attribute.inputs[0].default_value = "sensor_idx"

    # Node Viewer
    viewer = remove_from_set_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 1
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Unrouted Graph")
    viewer.viewer_items.new('BOOLEAN', "Result")

    # Node Compare.007
    compare_007 = remove_from_set_1.nodes.new("FunctionNodeCompare")
    compare_007.name = "Compare.007"
    compare_007.show_options = True
    compare_007.data_type = 'INT'
    compare_007.mode = 'ELEMENT'
    compare_007.operation = 'EQUAL'

    # Set locations
    remove_from_set_1.nodes["Group Output"].location = (800.0, 20.0)
    remove_from_set_1.nodes["Group Input"].location = (-1000.0, 140.0)
    remove_from_set_1.nodes["Store Named Attribute.006"].location = (60.0, 340.0)
    remove_from_set_1.nodes["Compare.005"].location = (-280.0, 500.0)
    remove_from_set_1.nodes["Index.006"].location = (-520.0, -220.0)
    remove_from_set_1.nodes["Sample Nearest.007"].location = (-520.0, -60.0)
    remove_from_set_1.nodes["Store Named Attribute.008"].location = (420.0, 160.0)
    remove_from_set_1.nodes["Compare.006"].location = (-240.0, -140.0)
    remove_from_set_1.nodes["Reroute.027"].location = (60.0, -240.0)
    remove_from_set_1.nodes["Reroute"].location = (-561.7450561523438, 10.405396461486816)
    remove_from_set_1.nodes["Sample Index"].location = (-480.0, 320.0)
    remove_from_set_1.nodes["Named Attribute"].location = (-1000.0, 280.0)
    remove_from_set_1.nodes["Viewer"].location = (-113.33333587646484, 621.3333129882812)
    remove_from_set_1.nodes["Compare.007"].location = (-240.0, 100.0)

    # Set dimensions
    remove_from_set_1.nodes["Group Output"].width  = 140.0
    remove_from_set_1.nodes["Group Output"].height = 100.0

    remove_from_set_1.nodes["Group Input"].width  = 140.0
    remove_from_set_1.nodes["Group Input"].height = 100.0

    remove_from_set_1.nodes["Store Named Attribute.006"].width  = 140.0
    remove_from_set_1.nodes["Store Named Attribute.006"].height = 100.0

    remove_from_set_1.nodes["Compare.005"].width  = 140.0
    remove_from_set_1.nodes["Compare.005"].height = 100.0

    remove_from_set_1.nodes["Index.006"].width  = 140.0
    remove_from_set_1.nodes["Index.006"].height = 100.0

    remove_from_set_1.nodes["Sample Nearest.007"].width  = 140.0
    remove_from_set_1.nodes["Sample Nearest.007"].height = 100.0

    remove_from_set_1.nodes["Store Named Attribute.008"].width  = 140.0
    remove_from_set_1.nodes["Store Named Attribute.008"].height = 100.0

    remove_from_set_1.nodes["Compare.006"].width  = 140.0
    remove_from_set_1.nodes["Compare.006"].height = 100.0

    remove_from_set_1.nodes["Reroute.027"].width  = 14.5
    remove_from_set_1.nodes["Reroute.027"].height = 100.0

    remove_from_set_1.nodes["Reroute"].width  = 14.5
    remove_from_set_1.nodes["Reroute"].height = 100.0

    remove_from_set_1.nodes["Sample Index"].width  = 140.0
    remove_from_set_1.nodes["Sample Index"].height = 100.0

    remove_from_set_1.nodes["Named Attribute"].width  = 140.0
    remove_from_set_1.nodes["Named Attribute"].height = 100.0

    remove_from_set_1.nodes["Viewer"].width  = 140.0
    remove_from_set_1.nodes["Viewer"].height = 100.0

    remove_from_set_1.nodes["Compare.007"].width  = 140.0
    remove_from_set_1.nodes["Compare.007"].height = 100.0


    # Initialize remove_from_set_1 links

    # reroute_027.Output -> store_named_attribute_008.Selection
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Reroute.027"].outputs[0],
        remove_from_set_1.nodes["Store Named Attribute.008"].inputs[1]
    )
    # store_named_attribute_006.Geometry -> store_named_attribute_008.Geometry
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Store Named Attribute.006"].outputs[0],
        remove_from_set_1.nodes["Store Named Attribute.008"].inputs[0]
    )
    # sample_nearest_007.Index -> compare_006.B
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Sample Nearest.007"].outputs[0],
        remove_from_set_1.nodes["Compare.006"].inputs[3]
    )
    # index_006.Index -> compare_006.A
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Index.006"].outputs[0],
        remove_from_set_1.nodes["Compare.006"].inputs[2]
    )
    # compare_006.Result -> reroute_027.Input
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Compare.006"].outputs[0],
        remove_from_set_1.nodes["Reroute.027"].inputs[0]
    )
    # group_input.Clip Position -> sample_nearest_007.Sample Position
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Group Input"].outputs[2],
        remove_from_set_1.nodes["Sample Nearest.007"].inputs[1]
    )
    # reroute.Output -> sample_nearest_007.Geometry
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Reroute"].outputs[0],
        remove_from_set_1.nodes["Sample Nearest.007"].inputs[0]
    )
    # sample_nearest_007.Index -> group_output.Clip Index
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Sample Nearest.007"].outputs[0],
        remove_from_set_1.nodes["Group Output"].inputs[0]
    )
    # store_named_attribute_008.Geometry -> group_output.Filtered Unrouted Graph
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Store Named Attribute.008"].outputs[0],
        remove_from_set_1.nodes["Group Output"].inputs[1]
    )
    # group_input.Unrouted Graph -> reroute.Input
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Group Input"].outputs[1],
        remove_from_set_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> store_named_attribute_006.Geometry
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Reroute"].outputs[0],
        remove_from_set_1.nodes["Store Named Attribute.006"].inputs[0]
    )
    # group_input.Electrode Index -> sample_index.Index
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Group Input"].outputs[0],
        remove_from_set_1.nodes["Sample Index"].inputs[2]
    )
    # reroute.Output -> sample_index.Geometry
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Reroute"].outputs[0],
        remove_from_set_1.nodes["Sample Index"].inputs[0]
    )
    # named_attribute.Attribute -> sample_index.Value
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Named Attribute"].outputs[0],
        remove_from_set_1.nodes["Sample Index"].inputs[1]
    )
    # group_input.Unrouted Graph -> viewer.Unrouted Graph
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Group Input"].outputs[1],
        remove_from_set_1.nodes["Viewer"].inputs[0]
    )
    # sample_index.Value -> compare_005.B
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Sample Index"].outputs[0],
        remove_from_set_1.nodes["Compare.005"].inputs[3]
    )
    # named_attribute.Attribute -> compare_005.A
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Named Attribute"].outputs[0],
        remove_from_set_1.nodes["Compare.005"].inputs[2]
    )
    # group_input.Electrode Index -> compare_007.B
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Group Input"].outputs[0],
        remove_from_set_1.nodes["Compare.007"].inputs[3]
    )
    # index_006.Index -> compare_007.A
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Index.006"].outputs[0],
        remove_from_set_1.nodes["Compare.007"].inputs[2]
    )
    # compare_005.Result -> viewer.Result
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Compare.005"].outputs[0],
        remove_from_set_1.nodes["Viewer"].inputs[1]
    )
    # compare_005.Result -> store_named_attribute_006.Selection
    remove_from_set_1.links.new(
        remove_from_set_1.nodes["Compare.005"].outputs[0],
        remove_from_set_1.nodes["Store Named Attribute.006"].inputs[1]
    )
    viewer.viewer_items[0].auto_remove = True
    viewer.viewer_items[1].auto_remove = True

    return remove_from_set_1


def sort_by_vector_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Sort By Vector.001 node group"""
    sort_by_vector_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sort By Vector.001")

    sort_by_vector_001_1.color_tag = 'NONE'
    sort_by_vector_001_1.description = ""
    sort_by_vector_001_1.default_group_node_width = 140
    sort_by_vector_001_1.show_modifier_manage_panel = True

    # sort_by_vector_001_1 interface

    # Socket Geometry
    geometry_socket = sort_by_vector_001_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = sort_by_vector_001_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Vector
    vector_socket = sort_by_vector_001_1.interface.new_socket(name="Vector", in_out='INPUT', socket_type='NodeSocketVector')
    vector_socket.default_value = (0.0, 0.0, 0.0)
    vector_socket.min_value = -10000.0
    vector_socket.max_value = 10000.0
    vector_socket.subtype = 'NONE'
    vector_socket.attribute_domain = 'POINT'
    vector_socket.default_input = 'VALUE'
    vector_socket.structure_type = 'AUTO'

    # Initialize sort_by_vector_001_1 nodes

    # Node Group Output
    group_output = sort_by_vector_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = sort_by_vector_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Sort Elements.001
    sort_elements_001 = sort_by_vector_001_1.nodes.new("GeometryNodeSortElements")
    sort_elements_001.name = "Sort Elements.001"
    sort_elements_001.show_options = True
    sort_elements_001.domain = 'POINT'
    # Selection
    sort_elements_001.inputs[1].default_value = True
    # Group ID
    sort_elements_001.inputs[2].default_value = 0

    # Node Vector Math
    vector_math = sort_by_vector_001_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'DOT_PRODUCT'

    # Node Sample Index.001
    sample_index_001 = sort_by_vector_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'

    # Node Position.001
    position_001 = sort_by_vector_001_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Index
    index = sort_by_vector_001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Set locations
    sort_by_vector_001_1.nodes["Group Output"].location = (470.0, 0.0)
    sort_by_vector_001_1.nodes["Group Input"].location = (-480.0, 0.0)
    sort_by_vector_001_1.nodes["Sort Elements.001"].location = (280.0, 140.0)
    sort_by_vector_001_1.nodes["Vector Math"].location = (100.0, 40.0)
    sort_by_vector_001_1.nodes["Sample Index.001"].location = (-80.0, 80.0)
    sort_by_vector_001_1.nodes["Position.001"].location = (-280.0, -140.0)
    sort_by_vector_001_1.nodes["Index"].location = (-280.0, -80.0)

    # Set dimensions
    sort_by_vector_001_1.nodes["Group Output"].width  = 140.0
    sort_by_vector_001_1.nodes["Group Output"].height = 100.0

    sort_by_vector_001_1.nodes["Group Input"].width  = 140.0
    sort_by_vector_001_1.nodes["Group Input"].height = 100.0

    sort_by_vector_001_1.nodes["Sort Elements.001"].width  = 140.0
    sort_by_vector_001_1.nodes["Sort Elements.001"].height = 100.0

    sort_by_vector_001_1.nodes["Vector Math"].width  = 140.0
    sort_by_vector_001_1.nodes["Vector Math"].height = 100.0

    sort_by_vector_001_1.nodes["Sample Index.001"].width  = 140.0
    sort_by_vector_001_1.nodes["Sample Index.001"].height = 100.0

    sort_by_vector_001_1.nodes["Position.001"].width  = 140.0
    sort_by_vector_001_1.nodes["Position.001"].height = 100.0

    sort_by_vector_001_1.nodes["Index"].width  = 140.0
    sort_by_vector_001_1.nodes["Index"].height = 100.0


    # Initialize sort_by_vector_001_1 links

    # index.Index -> sample_index_001.Index
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Index"].outputs[0],
        sort_by_vector_001_1.nodes["Sample Index.001"].inputs[2]
    )
    # vector_math.Value -> sort_elements_001.Sort Weight
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Vector Math"].outputs[1],
        sort_by_vector_001_1.nodes["Sort Elements.001"].inputs[3]
    )
    # position_001.Position -> sample_index_001.Value
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Position.001"].outputs[0],
        sort_by_vector_001_1.nodes["Sample Index.001"].inputs[1]
    )
    # sample_index_001.Value -> vector_math.Vector
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Sample Index.001"].outputs[0],
        sort_by_vector_001_1.nodes["Vector Math"].inputs[0]
    )
    # group_input.Geometry -> sort_elements_001.Geometry
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Group Input"].outputs[0],
        sort_by_vector_001_1.nodes["Sort Elements.001"].inputs[0]
    )
    # group_input.Geometry -> sample_index_001.Geometry
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Group Input"].outputs[0],
        sort_by_vector_001_1.nodes["Sample Index.001"].inputs[0]
    )
    # group_input.Vector -> vector_math.Vector
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Group Input"].outputs[1],
        sort_by_vector_001_1.nodes["Vector Math"].inputs[1]
    )
    # sort_elements_001.Geometry -> group_output.Geometry
    sort_by_vector_001_1.links.new(
        sort_by_vector_001_1.nodes["Sort Elements.001"].outputs[0],
        sort_by_vector_001_1.nodes["Group Output"].inputs[0]
    )

    return sort_by_vector_001_1


def sort_by_distance_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Sort by Distance.001 node group"""
    sort_by_distance_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sort by Distance.001")

    sort_by_distance_001_1.color_tag = 'NONE'
    sort_by_distance_001_1.description = ""
    sort_by_distance_001_1.default_group_node_width = 140
    sort_by_distance_001_1.show_modifier_manage_panel = True

    # sort_by_distance_001_1 interface

    # Socket Electrodes Sorted
    electrodes_sorted_socket = sort_by_distance_001_1.interface.new_socket(name="Electrodes Sorted", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    electrodes_sorted_socket.attribute_domain = 'POINT'
    electrodes_sorted_socket.default_input = 'VALUE'
    electrodes_sorted_socket.structure_type = 'AUTO'

    # Socket Clips Sorted
    clips_sorted_socket = sort_by_distance_001_1.interface.new_socket(name="Clips Sorted", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    clips_sorted_socket.attribute_domain = 'POINT'
    clips_sorted_socket.default_input = 'VALUE'
    clips_sorted_socket.structure_type = 'AUTO'

    # Socket Set 1
    set_1_socket = sort_by_distance_001_1.interface.new_socket(name="Set 1", in_out='INPUT', socket_type='NodeSocketGeometry')
    set_1_socket.attribute_domain = 'POINT'
    set_1_socket.default_input = 'VALUE'
    set_1_socket.structure_type = 'AUTO'

    # Socket Set 2
    set_2_socket = sort_by_distance_001_1.interface.new_socket(name="Set 2", in_out='INPUT', socket_type='NodeSocketGeometry')
    set_2_socket.attribute_domain = 'POINT'
    set_2_socket.default_input = 'VALUE'
    set_2_socket.structure_type = 'AUTO'

    # Initialize sort_by_distance_001_1 nodes

    # Node Group Output
    group_output = sort_by_distance_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = sort_by_distance_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Sample Nearest
    sample_nearest = sort_by_distance_001_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Index
    index = sort_by_distance_001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Sample Index
    sample_index = sort_by_distance_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Position
    position = sort_by_distance_001_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Store Named Attribute
    store_named_attribute = sort_by_distance_001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'INT'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "nearest_clip"

    # Node Vector Math
    vector_math = sort_by_distance_001_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'DISTANCE'

    # Node Named Attribute
    named_attribute = sort_by_distance_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'FLOAT'
    # Name
    named_attribute.inputs[0].default_value = ""

    # Node Sample Index.001
    sample_index_001 = sort_by_distance_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'

    # Node Position.001
    position_001 = sort_by_distance_001_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Viewer
    viewer = sort_by_distance_001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")
    viewer.viewer_items.new('FLOAT', "Value")

    # Node Store Named Attribute.001
    store_named_attribute_001 = sort_by_distance_001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'FLOAT'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "nearest_dist"

    # Node Sort Elements
    sort_elements = sort_by_distance_001_1.nodes.new("GeometryNodeSortElements")
    sort_elements.name = "Sort Elements"
    sort_elements.show_options = True
    sort_elements.domain = 'POINT'
    # Selection
    sort_elements.inputs[1].default_value = True
    # Group ID
    sort_elements.inputs[2].default_value = 0

    # Node Reroute
    reroute = sort_by_distance_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketInt"
    # Node Sample Index.002
    sample_index_002 = sort_by_distance_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'

    # Node Sample Nearest.001
    sample_nearest_001 = sort_by_distance_001_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest_001.name = "Sample Nearest.001"
    sample_nearest_001.show_options = True
    sample_nearest_001.domain = 'POINT'

    # Node Reroute.001
    reroute_001 = sort_by_distance_001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Position.002
    position_002 = sort_by_distance_001_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Index.001
    index_001 = sort_by_distance_001_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Sample Index.003
    sample_index_003 = sort_by_distance_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_003.name = "Sample Index.003"
    sample_index_003.show_options = True
    sample_index_003.clamp = False
    sample_index_003.data_type = 'FLOAT_VECTOR'
    sample_index_003.domain = 'POINT'

    # Node Position.003
    position_003 = sort_by_distance_001_1.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    position_003.show_options = True

    # Node Vector Math.001
    vector_math_001 = sort_by_distance_001_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'DISTANCE'

    # Node Sort Elements.001
    sort_elements_001 = sort_by_distance_001_1.nodes.new("GeometryNodeSortElements")
    sort_elements_001.name = "Sort Elements.001"
    sort_elements_001.show_options = True
    sort_elements_001.domain = 'POINT'
    # Selection
    sort_elements_001.inputs[1].default_value = True
    # Group ID
    sort_elements_001.inputs[2].default_value = 0

    # Node Reroute.002
    reroute_002 = sort_by_distance_001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Viewer.001
    viewer_001 = sort_by_distance_001_1.nodes.new("GeometryNodeViewer")
    viewer_001.name = "Viewer.001"
    viewer_001.show_options = True
    viewer_001.active_index = 0
    viewer_001.domain = 'AUTO'
    viewer_001.ui_shortcut = 0
    viewer_001.viewer_items.clear()
    viewer_001.viewer_items.new('GEOMETRY', "Geometry")
    viewer_001.viewer_items.new('FLOAT', "Value")

    # Node Viewer.002
    viewer_002 = sort_by_distance_001_1.nodes.new("GeometryNodeViewer")
    viewer_002.name = "Viewer.002"
    viewer_002.show_options = True
    viewer_002.active_index = 0
    viewer_002.domain = 'AUTO'
    viewer_002.ui_shortcut = 0
    viewer_002.viewer_items.clear()
    viewer_002.viewer_items.new('GEOMETRY', "Geometry")
    viewer_002.viewer_items.new('FLOAT', "Value")

    # Node Index.002
    index_002 = sort_by_distance_001_1.nodes.new("GeometryNodeInputIndex")
    index_002.name = "Index.002"
    index_002.show_options = True

    # Node Index.003
    index_003 = sort_by_distance_001_1.nodes.new("GeometryNodeInputIndex")
    index_003.name = "Index.003"
    index_003.show_options = True

    # Node Index.004
    index_004 = sort_by_distance_001_1.nodes.new("GeometryNodeInputIndex")
    index_004.name = "Index.004"
    index_004.show_options = True

    # Set locations
    sort_by_distance_001_1.nodes["Group Output"].location = (2360.0, 60.0)
    sort_by_distance_001_1.nodes["Group Input"].location = (-1140.0, -40.0)
    sort_by_distance_001_1.nodes["Sample Nearest"].location = (-680.0, 80.0)
    sort_by_distance_001_1.nodes["Index"].location = (-1140.0, 80.0)
    sort_by_distance_001_1.nodes["Sample Index"].location = (-920.0, 140.0)
    sort_by_distance_001_1.nodes["Position"].location = (-1140.0, 20.0)
    sort_by_distance_001_1.nodes["Store Named Attribute"].location = (60.0, 20.0)
    sort_by_distance_001_1.nodes["Vector Math"].location = (60.0, 160.0)
    sort_by_distance_001_1.nodes["Named Attribute"].location = (-460.0, -480.0531005859375)
    sort_by_distance_001_1.nodes["Sample Index.001"].location = (-220.0, -200.0)
    sort_by_distance_001_1.nodes["Position.001"].location = (-460.0, -360.0)
    sort_by_distance_001_1.nodes["Viewer"].location = (2180.0, 460.0)
    sort_by_distance_001_1.nodes["Store Named Attribute.001"].location = (320.0, 20.0)
    sort_by_distance_001_1.nodes["Sort Elements"].location = (840.0, 200.0)
    sort_by_distance_001_1.nodes["Reroute"].location = (23.3858642578125, -152.50021362304688)
    sort_by_distance_001_1.nodes["Sample Index.002"].location = (860.0, -240.0)
    sort_by_distance_001_1.nodes["Sample Nearest.001"].location = (1100.0, -60.0)
    sort_by_distance_001_1.nodes["Reroute.001"].location = (665.51025390625, -205.74012756347656)
    sort_by_distance_001_1.nodes["Position.002"].location = (620.0, -400.0)
    sort_by_distance_001_1.nodes["Index.001"].location = (620.0, -460.0)
    sort_by_distance_001_1.nodes["Sample Index.003"].location = (1340.0, 120.0)
    sort_by_distance_001_1.nodes["Position.003"].location = (1100.0, 0.0)
    sort_by_distance_001_1.nodes["Vector Math.001"].location = (1620.0, 60.0)
    sort_by_distance_001_1.nodes["Sort Elements.001"].location = (1840.0, -40.0)
    sort_by_distance_001_1.nodes["Reroute.002"].location = (1320.0, -200.0)
    sort_by_distance_001_1.nodes["Viewer.001"].location = (1080.0, 380.0)
    sort_by_distance_001_1.nodes["Viewer.002"].location = (1460.0, -260.0)
    sort_by_distance_001_1.nodes["Index.002"].location = (1160.0, -320.0)
    sort_by_distance_001_1.nodes["Index.003"].location = (1860.0, 380.0)
    sort_by_distance_001_1.nodes["Index.004"].location = (840.0, 320.0)

    # Set dimensions
    sort_by_distance_001_1.nodes["Group Output"].width  = 140.0
    sort_by_distance_001_1.nodes["Group Output"].height = 100.0

    sort_by_distance_001_1.nodes["Group Input"].width  = 140.0
    sort_by_distance_001_1.nodes["Group Input"].height = 100.0

    sort_by_distance_001_1.nodes["Sample Nearest"].width  = 140.0
    sort_by_distance_001_1.nodes["Sample Nearest"].height = 100.0

    sort_by_distance_001_1.nodes["Index"].width  = 140.0
    sort_by_distance_001_1.nodes["Index"].height = 100.0

    sort_by_distance_001_1.nodes["Sample Index"].width  = 140.0
    sort_by_distance_001_1.nodes["Sample Index"].height = 100.0

    sort_by_distance_001_1.nodes["Position"].width  = 140.0
    sort_by_distance_001_1.nodes["Position"].height = 100.0

    sort_by_distance_001_1.nodes["Store Named Attribute"].width  = 140.0
    sort_by_distance_001_1.nodes["Store Named Attribute"].height = 100.0

    sort_by_distance_001_1.nodes["Vector Math"].width  = 140.0
    sort_by_distance_001_1.nodes["Vector Math"].height = 100.0

    sort_by_distance_001_1.nodes["Named Attribute"].width  = 140.0
    sort_by_distance_001_1.nodes["Named Attribute"].height = 100.0

    sort_by_distance_001_1.nodes["Sample Index.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Sample Index.001"].height = 100.0

    sort_by_distance_001_1.nodes["Position.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Position.001"].height = 100.0

    sort_by_distance_001_1.nodes["Viewer"].width  = 140.0
    sort_by_distance_001_1.nodes["Viewer"].height = 100.0

    sort_by_distance_001_1.nodes["Store Named Attribute.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Store Named Attribute.001"].height = 100.0

    sort_by_distance_001_1.nodes["Sort Elements"].width  = 140.0
    sort_by_distance_001_1.nodes["Sort Elements"].height = 100.0

    sort_by_distance_001_1.nodes["Reroute"].width  = 14.5
    sort_by_distance_001_1.nodes["Reroute"].height = 100.0

    sort_by_distance_001_1.nodes["Sample Index.002"].width  = 140.0
    sort_by_distance_001_1.nodes["Sample Index.002"].height = 100.0

    sort_by_distance_001_1.nodes["Sample Nearest.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Sample Nearest.001"].height = 100.0

    sort_by_distance_001_1.nodes["Reroute.001"].width  = 14.5
    sort_by_distance_001_1.nodes["Reroute.001"].height = 100.0

    sort_by_distance_001_1.nodes["Position.002"].width  = 140.0
    sort_by_distance_001_1.nodes["Position.002"].height = 100.0

    sort_by_distance_001_1.nodes["Index.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Index.001"].height = 100.0

    sort_by_distance_001_1.nodes["Sample Index.003"].width  = 140.0
    sort_by_distance_001_1.nodes["Sample Index.003"].height = 100.0

    sort_by_distance_001_1.nodes["Position.003"].width  = 140.0
    sort_by_distance_001_1.nodes["Position.003"].height = 100.0

    sort_by_distance_001_1.nodes["Vector Math.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Vector Math.001"].height = 100.0

    sort_by_distance_001_1.nodes["Sort Elements.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Sort Elements.001"].height = 100.0

    sort_by_distance_001_1.nodes["Reroute.002"].width  = 14.5
    sort_by_distance_001_1.nodes["Reroute.002"].height = 100.0

    sort_by_distance_001_1.nodes["Viewer.001"].width  = 140.0
    sort_by_distance_001_1.nodes["Viewer.001"].height = 100.0

    sort_by_distance_001_1.nodes["Viewer.002"].width  = 140.0
    sort_by_distance_001_1.nodes["Viewer.002"].height = 100.0

    sort_by_distance_001_1.nodes["Index.002"].width  = 140.0
    sort_by_distance_001_1.nodes["Index.002"].height = 100.0

    sort_by_distance_001_1.nodes["Index.003"].width  = 140.0
    sort_by_distance_001_1.nodes["Index.003"].height = 100.0

    sort_by_distance_001_1.nodes["Index.004"].width  = 140.0
    sort_by_distance_001_1.nodes["Index.004"].height = 100.0


    # Initialize sort_by_distance_001_1 links

    # group_input.Set 1 -> sample_index.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Group Input"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index"].inputs[0]
    )
    # index.Index -> sample_index.Index
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Index"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index"].inputs[2]
    )
    # position.Position -> sample_index.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Position"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index"].inputs[1]
    )
    # sample_index.Value -> sample_nearest.Sample Position
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Index"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Nearest"].inputs[1]
    )
    # group_input.Set 2 -> sample_nearest.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Group Input"].outputs[1],
        sort_by_distance_001_1.nodes["Sample Nearest"].inputs[0]
    )
    # group_input.Set 1 -> store_named_attribute.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Group Input"].outputs[0],
        sort_by_distance_001_1.nodes["Store Named Attribute"].inputs[0]
    )
    # reroute.Output -> store_named_attribute.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Reroute"].outputs[0],
        sort_by_distance_001_1.nodes["Store Named Attribute"].inputs[3]
    )
    # sample_index.Value -> vector_math.Vector
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Index"].outputs[0],
        sort_by_distance_001_1.nodes["Vector Math"].inputs[0]
    )
    # sample_nearest.Index -> sample_index_001.Index
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Nearest"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.001"].inputs[2]
    )
    # position_001.Position -> sample_index_001.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Position.001"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.001"].inputs[1]
    )
    # sample_index_001.Value -> vector_math.Vector
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Index.001"].outputs[0],
        sort_by_distance_001_1.nodes["Vector Math"].inputs[1]
    )
    # sort_elements_001.Geometry -> viewer.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sort Elements.001"].outputs[0],
        sort_by_distance_001_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Set 2 -> sample_index_001.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Group Input"].outputs[1],
        sort_by_distance_001_1.nodes["Sample Index.001"].inputs[0]
    )
    # store_named_attribute.Geometry -> store_named_attribute_001.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Store Named Attribute"].outputs[0],
        sort_by_distance_001_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # vector_math.Value -> store_named_attribute_001.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Vector Math"].outputs[1],
        sort_by_distance_001_1.nodes["Store Named Attribute.001"].inputs[3]
    )
    # store_named_attribute_001.Geometry -> sort_elements.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Store Named Attribute.001"].outputs[0],
        sort_by_distance_001_1.nodes["Sort Elements"].inputs[0]
    )
    # sample_nearest.Index -> reroute.Input
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Nearest"].outputs[0],
        sort_by_distance_001_1.nodes["Reroute"].inputs[0]
    )
    # vector_math.Value -> sort_elements.Sort Weight
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Vector Math"].outputs[1],
        sort_by_distance_001_1.nodes["Sort Elements"].inputs[3]
    )
    # reroute_001.Output -> sample_index_002.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Reroute.001"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.002"].inputs[0]
    )
    # group_input.Set 2 -> reroute_001.Input
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Group Input"].outputs[1],
        sort_by_distance_001_1.nodes["Reroute.001"].inputs[0]
    )
    # position_002.Position -> sample_index_002.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Position.002"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.002"].inputs[1]
    )
    # index_001.Index -> sample_index_002.Index
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Index.001"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.002"].inputs[2]
    )
    # sort_elements.Geometry -> sample_nearest_001.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sort Elements"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Nearest.001"].inputs[0]
    )
    # sample_index_002.Value -> sample_nearest_001.Sample Position
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Index.002"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Nearest.001"].inputs[1]
    )
    # position_003.Position -> sample_index_003.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Position.003"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.003"].inputs[1]
    )
    # sample_nearest_001.Index -> sample_index_003.Index
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Nearest.001"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.003"].inputs[2]
    )
    # sort_elements.Geometry -> sample_index_003.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sort Elements"].outputs[0],
        sort_by_distance_001_1.nodes["Sample Index.003"].inputs[0]
    )
    # sample_index_003.Value -> vector_math_001.Vector
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Index.003"].outputs[0],
        sort_by_distance_001_1.nodes["Vector Math.001"].inputs[0]
    )
    # sample_index_002.Value -> vector_math_001.Vector
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sample Index.002"].outputs[0],
        sort_by_distance_001_1.nodes["Vector Math.001"].inputs[1]
    )
    # reroute_002.Output -> sort_elements_001.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Reroute.002"].outputs[0],
        sort_by_distance_001_1.nodes["Sort Elements.001"].inputs[0]
    )
    # reroute_001.Output -> reroute_002.Input
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Reroute.001"].outputs[0],
        sort_by_distance_001_1.nodes["Reroute.002"].inputs[0]
    )
    # vector_math_001.Value -> sort_elements_001.Sort Weight
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Vector Math.001"].outputs[1],
        sort_by_distance_001_1.nodes["Sort Elements.001"].inputs[3]
    )
    # sort_elements_001.Geometry -> group_output.Clips Sorted
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sort Elements.001"].outputs[0],
        sort_by_distance_001_1.nodes["Group Output"].inputs[1]
    )
    # sort_elements.Geometry -> group_output.Electrodes Sorted
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sort Elements"].outputs[0],
        sort_by_distance_001_1.nodes["Group Output"].inputs[0]
    )
    # sort_elements.Geometry -> viewer_001.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Sort Elements"].outputs[0],
        sort_by_distance_001_1.nodes["Viewer.001"].inputs[0]
    )
    # reroute_002.Output -> viewer_002.Geometry
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Reroute.002"].outputs[0],
        sort_by_distance_001_1.nodes["Viewer.002"].inputs[0]
    )
    # index_002.Index -> viewer_002.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Index.002"].outputs[0],
        sort_by_distance_001_1.nodes["Viewer.002"].inputs[1]
    )
    # index_003.Index -> viewer.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Index.003"].outputs[0],
        sort_by_distance_001_1.nodes["Viewer"].inputs[1]
    )
    # index_004.Index -> viewer_001.Value
    sort_by_distance_001_1.links.new(
        sort_by_distance_001_1.nodes["Index.004"].outputs[0],
        sort_by_distance_001_1.nodes["Viewer.001"].inputs[1]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False
    viewer_001.viewer_items[0].auto_remove = False
    viewer_001.viewer_items[1].auto_remove = False
    viewer_002.viewer_items[0].auto_remove = False
    viewer_002.viewer_items[1].auto_remove = False

    return sort_by_distance_001_1


def select_clip_and_electrode_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Select Clip and Electrode node group"""
    select_clip_and_electrode_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Select Clip and Electrode")

    select_clip_and_electrode_1.color_tag = 'NONE'
    select_clip_and_electrode_1.description = ""
    select_clip_and_electrode_1.default_group_node_width = 140
    select_clip_and_electrode_1.show_modifier_manage_panel = True

    # select_clip_and_electrode_1 interface

    # Socket Electrode Index
    electrode_index_socket = select_clip_and_electrode_1.interface.new_socket(name="Electrode Index", in_out='OUTPUT', socket_type='NodeSocketInt')
    electrode_index_socket.default_value = 0
    electrode_index_socket.min_value = -2147483648
    electrode_index_socket.max_value = 2147483647
    electrode_index_socket.subtype = 'NONE'
    electrode_index_socket.attribute_domain = 'POINT'
    electrode_index_socket.default_input = 'VALUE'
    electrode_index_socket.structure_type = 'AUTO'

    # Socket Clip Position
    clip_position_socket = select_clip_and_electrode_1.interface.new_socket(name="Clip Position", in_out='OUTPUT', socket_type='NodeSocketVector')
    clip_position_socket.default_value = (0.0, 0.0, 0.0)
    clip_position_socket.min_value = -3.4028234663852886e+38
    clip_position_socket.max_value = 3.4028234663852886e+38
    clip_position_socket.subtype = 'NONE'
    clip_position_socket.attribute_domain = 'POINT'
    clip_position_socket.default_input = 'VALUE'
    clip_position_socket.structure_type = 'AUTO'

    # Socket Unrouted Graph
    unrouted_graph_socket = select_clip_and_electrode_1.interface.new_socket(name="Unrouted Graph", in_out='INPUT', socket_type='NodeSocketGeometry')
    unrouted_graph_socket.attribute_domain = 'POINT'
    unrouted_graph_socket.default_input = 'VALUE'
    unrouted_graph_socket.structure_type = 'AUTO'

    # Socket Sort by Vector
    sort_by_vector_socket = select_clip_and_electrode_1.interface.new_socket(name="Sort by Vector", in_out='INPUT', socket_type='NodeSocketBool')
    sort_by_vector_socket.default_value = False
    sort_by_vector_socket.attribute_domain = 'POINT'
    sort_by_vector_socket.default_input = 'VALUE'
    sort_by_vector_socket.structure_type = 'AUTO'

    # Socket Electrode Sorting Vector
    electrode_sorting_vector_socket = select_clip_and_electrode_1.interface.new_socket(name="Electrode Sorting Vector", in_out='INPUT', socket_type='NodeSocketVector')
    electrode_sorting_vector_socket.default_value = (0.0, 0.0, 0.0)
    electrode_sorting_vector_socket.min_value = -10000.0
    electrode_sorting_vector_socket.max_value = 10000.0
    electrode_sorting_vector_socket.subtype = 'NONE'
    electrode_sorting_vector_socket.attribute_domain = 'POINT'
    electrode_sorting_vector_socket.default_input = 'VALUE'
    electrode_sorting_vector_socket.structure_type = 'AUTO'

    # Socket Clip Sorting Vector
    clip_sorting_vector_socket = select_clip_and_electrode_1.interface.new_socket(name="Clip Sorting Vector", in_out='INPUT', socket_type='NodeSocketVector')
    clip_sorting_vector_socket.default_value = (0.0, 0.0, 0.0)
    clip_sorting_vector_socket.min_value = -10000.0
    clip_sorting_vector_socket.max_value = 10000.0
    clip_sorting_vector_socket.subtype = 'NONE'
    clip_sorting_vector_socket.attribute_domain = 'POINT'
    clip_sorting_vector_socket.default_input = 'VALUE'
    clip_sorting_vector_socket.structure_type = 'AUTO'

    # Initialize select_clip_and_electrode_1 nodes

    # Node Group Output
    group_output = select_clip_and_electrode_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = select_clip_and_electrode_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Separate Geometry.004
    separate_geometry_004 = select_clip_and_electrode_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_004.name = "Separate Geometry.004"
    separate_geometry_004.show_options = True
    separate_geometry_004.domain = 'POINT'

    # Node Named Attribute.005
    named_attribute_005 = select_clip_and_electrode_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_005.name = "Named Attribute.005"
    named_attribute_005.show_options = True
    named_attribute_005.data_type = 'BOOLEAN'
    # Name
    named_attribute_005.inputs[0].default_value = "electrodes"

    # Node Sample Nearest.006
    sample_nearest_006 = select_clip_and_electrode_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest_006.name = "Sample Nearest.006"
    sample_nearest_006.show_options = True
    sample_nearest_006.domain = 'POINT'

    # Node Reroute.020
    reroute_020 = select_clip_and_electrode_1.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.show_options = True
    reroute_020.socket_idname = "NodeSocketGeometry"
    # Node Separate Geometry.005
    separate_geometry_005 = select_clip_and_electrode_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_005.name = "Separate Geometry.005"
    separate_geometry_005.show_options = True
    separate_geometry_005.domain = 'POINT'

    # Node Named Attribute.007
    named_attribute_007 = select_clip_and_electrode_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_007.name = "Named Attribute.007"
    named_attribute_007.show_options = True
    named_attribute_007.data_type = 'BOOLEAN'
    # Name
    named_attribute_007.inputs[0].default_value = "clips"

    # Node Sample Index.006
    sample_index_006 = select_clip_and_electrode_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_006.name = "Sample Index.006"
    sample_index_006.show_options = True
    sample_index_006.clamp = False
    sample_index_006.data_type = 'FLOAT_VECTOR'
    sample_index_006.domain = 'POINT'
    # Index
    sample_index_006.inputs[2].default_value = 0

    # Node Position.006
    position_006 = select_clip_and_electrode_1.nodes.new("GeometryNodeInputPosition")
    position_006.name = "Position.006"
    position_006.show_options = True

    # Node Reroute.023
    reroute_023 = select_clip_and_electrode_1.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.show_options = True
    reroute_023.socket_idname = "NodeSocketGeometry"
    # Node Reroute.025
    reroute_025 = select_clip_and_electrode_1.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.show_options = True
    reroute_025.socket_idname = "NodeSocketGeometry"
    # Node Sample Index.002
    sample_index_002 = select_clip_and_electrode_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'
    # Index
    sample_index_002.inputs[2].default_value = 0

    # Node Position.001
    position_001 = select_clip_and_electrode_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Group.005
    group_005 = select_clip_and_electrode_1.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.show_options = True
    group_005.node_tree = bpy.data.node_groups[node_tree_names[sort_by_vector_001_1_node_group]]

    # Node Group.006
    group_006 = select_clip_and_electrode_1.nodes.new("GeometryNodeGroup")
    group_006.name = "Group.006"
    group_006.show_options = True
    group_006.node_tree = bpy.data.node_groups[node_tree_names[sort_by_distance_001_1_node_group]]

    # Node Switch.002
    switch_002 = select_clip_and_electrode_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.show_options = True
    switch_002.input_type = 'GEOMETRY'

    # Node Reroute.033
    reroute_033 = select_clip_and_electrode_1.nodes.new("NodeReroute")
    reroute_033.name = "Reroute.033"
    reroute_033.show_options = True
    reroute_033.socket_idname = "NodeSocketBool"
    # Node Switch.003
    switch_003 = select_clip_and_electrode_1.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.show_options = True
    switch_003.input_type = 'GEOMETRY'

    # Node Group.007
    group_007 = select_clip_and_electrode_1.nodes.new("GeometryNodeGroup")
    group_007.name = "Group.007"
    group_007.show_options = True
    group_007.node_tree = bpy.data.node_groups[node_tree_names[sort_by_vector_001_1_node_group]]

    # Node Viewer
    viewer = select_clip_and_electrode_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 1
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Unrouted Graph")
    viewer.viewer_items.new('FLOAT', "Attribute")

    # Node Named Attribute
    named_attribute = select_clip_and_electrode_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'INT'
    # Name
    named_attribute.inputs[0].default_value = "sensor_idx"

    # Set locations
    select_clip_and_electrode_1.nodes["Group Output"].location = (980.0, 20.0)
    select_clip_and_electrode_1.nodes["Group Input"].location = (-790.0, 0.0)
    select_clip_and_electrode_1.nodes["Separate Geometry.004"].location = (-410.0, 290.0)
    select_clip_and_electrode_1.nodes["Named Attribute.005"].location = (-840.0, 260.0)
    select_clip_and_electrode_1.nodes["Sample Nearest.006"].location = (580.0, 320.0)
    select_clip_and_electrode_1.nodes["Reroute.020"].location = (-50.0, 330.0)
    select_clip_and_electrode_1.nodes["Separate Geometry.005"].location = (-330.0, -130.0)
    select_clip_and_electrode_1.nodes["Named Attribute.007"].location = (-880.0, -240.0)
    select_clip_and_electrode_1.nodes["Sample Index.006"].location = (290.0, -270.0)
    select_clip_and_electrode_1.nodes["Position.006"].location = (90.0, -470.0)
    select_clip_and_electrode_1.nodes["Reroute.023"].location = (-510.0, -110.0)
    select_clip_and_electrode_1.nodes["Reroute.025"].location = (-510.0, 330.0)
    select_clip_and_electrode_1.nodes["Sample Index.002"].location = (290.0, 310.0)
    select_clip_and_electrode_1.nodes["Position.001"].location = (130.0, 70.0)
    select_clip_and_electrode_1.nodes["Group.005"].location = (-130.0, 290.0)
    select_clip_and_electrode_1.nodes["Group.006"].location = (-130.0, 130.0)
    select_clip_and_electrode_1.nodes["Switch.002"].location = (110.0, 230.0)
    select_clip_and_electrode_1.nodes["Reroute.033"].location = (70.0, 370.0)
    select_clip_and_electrode_1.nodes["Switch.003"].location = (130.0, -230.0)
    select_clip_and_electrode_1.nodes["Group.007"].location = (-130.0, -250.0)
    select_clip_and_electrode_1.nodes["Viewer"].location = (-623.3333129882812, 106.66666412353516)
    select_clip_and_electrode_1.nodes["Named Attribute"].location = (-1020.0, 100.0)

    # Set dimensions
    select_clip_and_electrode_1.nodes["Group Output"].width  = 140.0
    select_clip_and_electrode_1.nodes["Group Output"].height = 100.0

    select_clip_and_electrode_1.nodes["Group Input"].width  = 140.0
    select_clip_and_electrode_1.nodes["Group Input"].height = 100.0

    select_clip_and_electrode_1.nodes["Separate Geometry.004"].width  = 140.0
    select_clip_and_electrode_1.nodes["Separate Geometry.004"].height = 100.0

    select_clip_and_electrode_1.nodes["Named Attribute.005"].width  = 140.0
    select_clip_and_electrode_1.nodes["Named Attribute.005"].height = 100.0

    select_clip_and_electrode_1.nodes["Sample Nearest.006"].width  = 140.0
    select_clip_and_electrode_1.nodes["Sample Nearest.006"].height = 100.0

    select_clip_and_electrode_1.nodes["Reroute.020"].width  = 14.5
    select_clip_and_electrode_1.nodes["Reroute.020"].height = 100.0

    select_clip_and_electrode_1.nodes["Separate Geometry.005"].width  = 140.0
    select_clip_and_electrode_1.nodes["Separate Geometry.005"].height = 100.0

    select_clip_and_electrode_1.nodes["Named Attribute.007"].width  = 140.0
    select_clip_and_electrode_1.nodes["Named Attribute.007"].height = 100.0

    select_clip_and_electrode_1.nodes["Sample Index.006"].width  = 140.0
    select_clip_and_electrode_1.nodes["Sample Index.006"].height = 100.0

    select_clip_and_electrode_1.nodes["Position.006"].width  = 140.0
    select_clip_and_electrode_1.nodes["Position.006"].height = 100.0

    select_clip_and_electrode_1.nodes["Reroute.023"].width  = 14.5
    select_clip_and_electrode_1.nodes["Reroute.023"].height = 100.0

    select_clip_and_electrode_1.nodes["Reroute.025"].width  = 14.5
    select_clip_and_electrode_1.nodes["Reroute.025"].height = 100.0

    select_clip_and_electrode_1.nodes["Sample Index.002"].width  = 140.0
    select_clip_and_electrode_1.nodes["Sample Index.002"].height = 100.0

    select_clip_and_electrode_1.nodes["Position.001"].width  = 140.0
    select_clip_and_electrode_1.nodes["Position.001"].height = 100.0

    select_clip_and_electrode_1.nodes["Group.005"].width  = 200.0
    select_clip_and_electrode_1.nodes["Group.005"].height = 100.0

    select_clip_and_electrode_1.nodes["Group.006"].width  = 200.0
    select_clip_and_electrode_1.nodes["Group.006"].height = 100.0

    select_clip_and_electrode_1.nodes["Switch.002"].width  = 140.0
    select_clip_and_electrode_1.nodes["Switch.002"].height = 100.0

    select_clip_and_electrode_1.nodes["Reroute.033"].width  = 14.5
    select_clip_and_electrode_1.nodes["Reroute.033"].height = 100.0

    select_clip_and_electrode_1.nodes["Switch.003"].width  = 140.0
    select_clip_and_electrode_1.nodes["Switch.003"].height = 100.0

    select_clip_and_electrode_1.nodes["Group.007"].width  = 200.0
    select_clip_and_electrode_1.nodes["Group.007"].height = 100.0

    select_clip_and_electrode_1.nodes["Viewer"].width  = 140.0
    select_clip_and_electrode_1.nodes["Viewer"].height = 100.0

    select_clip_and_electrode_1.nodes["Named Attribute"].width  = 140.0
    select_clip_and_electrode_1.nodes["Named Attribute"].height = 100.0


    # Initialize select_clip_and_electrode_1 links

    # reroute_033.Output -> switch_002.Switch
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Reroute.033"].outputs[0],
        select_clip_and_electrode_1.nodes["Switch.002"].inputs[0]
    )
    # named_attribute_005.Attribute -> separate_geometry_004.Selection
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Named Attribute.005"].outputs[0],
        select_clip_and_electrode_1.nodes["Separate Geometry.004"].inputs[1]
    )
    # group_007.Geometry -> switch_003.True
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group.007"].outputs[0],
        select_clip_and_electrode_1.nodes["Switch.003"].inputs[2]
    )
    # switch_003.Output -> sample_index_006.Geometry
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Switch.003"].outputs[0],
        select_clip_and_electrode_1.nodes["Sample Index.006"].inputs[0]
    )
    # reroute_023.Output -> separate_geometry_005.Geometry
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Reroute.023"].outputs[0],
        select_clip_and_electrode_1.nodes["Separate Geometry.005"].inputs[0]
    )
    # reroute_025.Output -> reroute_020.Input
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Reroute.025"].outputs[0],
        select_clip_and_electrode_1.nodes["Reroute.020"].inputs[0]
    )
    # group_006.Clips Sorted -> switch_003.False
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group.006"].outputs[1],
        select_clip_and_electrode_1.nodes["Switch.003"].inputs[1]
    )
    # position_001.Position -> sample_index_002.Value
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Position.001"].outputs[0],
        select_clip_and_electrode_1.nodes["Sample Index.002"].inputs[1]
    )
    # switch_002.Output -> sample_index_002.Geometry
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Switch.002"].outputs[0],
        select_clip_and_electrode_1.nodes["Sample Index.002"].inputs[0]
    )
    # reroute_020.Output -> sample_nearest_006.Geometry
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Reroute.020"].outputs[0],
        select_clip_and_electrode_1.nodes["Sample Nearest.006"].inputs[0]
    )
    # reroute_033.Output -> switch_003.Switch
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Reroute.033"].outputs[0],
        select_clip_and_electrode_1.nodes["Switch.003"].inputs[0]
    )
    # separate_geometry_004.Selection -> group_005.Geometry
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Separate Geometry.004"].outputs[0],
        select_clip_and_electrode_1.nodes["Group.005"].inputs[0]
    )
    # separate_geometry_005.Selection -> group_007.Geometry
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Separate Geometry.005"].outputs[0],
        select_clip_and_electrode_1.nodes["Group.007"].inputs[0]
    )
    # separate_geometry_005.Selection -> group_006.Set 2
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Separate Geometry.005"].outputs[0],
        select_clip_and_electrode_1.nodes["Group.006"].inputs[1]
    )
    # reroute_025.Output -> separate_geometry_004.Geometry
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Reroute.025"].outputs[0],
        select_clip_and_electrode_1.nodes["Separate Geometry.004"].inputs[0]
    )
    # separate_geometry_004.Selection -> group_006.Set 1
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Separate Geometry.004"].outputs[0],
        select_clip_and_electrode_1.nodes["Group.006"].inputs[0]
    )
    # position_006.Position -> sample_index_006.Value
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Position.006"].outputs[0],
        select_clip_and_electrode_1.nodes["Sample Index.006"].inputs[1]
    )
    # group_005.Geometry -> switch_002.True
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group.005"].outputs[0],
        select_clip_and_electrode_1.nodes["Switch.002"].inputs[2]
    )
    # named_attribute_007.Attribute -> separate_geometry_005.Selection
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Named Attribute.007"].outputs[0],
        select_clip_and_electrode_1.nodes["Separate Geometry.005"].inputs[1]
    )
    # group_006.Electrodes Sorted -> switch_002.False
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group.006"].outputs[0],
        select_clip_and_electrode_1.nodes["Switch.002"].inputs[1]
    )
    # group_input.Clip Sorting Vector -> group_007.Vector
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group Input"].outputs[3],
        select_clip_and_electrode_1.nodes["Group.007"].inputs[1]
    )
    # group_input.Unrouted Graph -> reroute_023.Input
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group Input"].outputs[0],
        select_clip_and_electrode_1.nodes["Reroute.023"].inputs[0]
    )
    # group_input.Unrouted Graph -> reroute_025.Input
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group Input"].outputs[0],
        select_clip_and_electrode_1.nodes["Reroute.025"].inputs[0]
    )
    # group_input.Electrode Sorting Vector -> group_005.Vector
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group Input"].outputs[2],
        select_clip_and_electrode_1.nodes["Group.005"].inputs[1]
    )
    # group_input.Sort by Vector -> reroute_033.Input
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group Input"].outputs[1],
        select_clip_and_electrode_1.nodes["Reroute.033"].inputs[0]
    )
    # sample_nearest_006.Index -> group_output.Electrode Index
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Sample Nearest.006"].outputs[0],
        select_clip_and_electrode_1.nodes["Group Output"].inputs[0]
    )
    # sample_index_006.Value -> group_output.Clip Position
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Sample Index.006"].outputs[0],
        select_clip_and_electrode_1.nodes["Group Output"].inputs[1]
    )
    # sample_index_002.Value -> sample_nearest_006.Sample Position
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Sample Index.002"].outputs[0],
        select_clip_and_electrode_1.nodes["Sample Nearest.006"].inputs[1]
    )
    # group_input.Unrouted Graph -> viewer.Unrouted Graph
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Group Input"].outputs[0],
        select_clip_and_electrode_1.nodes["Viewer"].inputs[0]
    )
    # named_attribute.Attribute -> viewer.Attribute
    select_clip_and_electrode_1.links.new(
        select_clip_and_electrode_1.nodes["Named Attribute"].outputs[0],
        select_clip_and_electrode_1.nodes["Viewer"].inputs[1]
    )
    viewer.viewer_items[0].auto_remove = True
    viewer.viewer_items[1].auto_remove = True

    return select_clip_and_electrode_1


def non_overlapping_wires__order_by_vector__distance__001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Non-overlapping Wires (Order By Vector, Distance).001 node group"""
    non_overlapping_wires__order_by_vector__distance__001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Non-overlapping Wires (Order By Vector, Distance).001")

    non_overlapping_wires__order_by_vector__distance__001_1.color_tag = 'NONE'
    non_overlapping_wires__order_by_vector__distance__001_1.description = ""
    non_overlapping_wires__order_by_vector__distance__001_1.default_group_node_width = 140
    non_overlapping_wires__order_by_vector__distance__001_1.show_modifier_manage_panel = True

    # non_overlapping_wires__order_by_vector__distance__001_1 interface

    # Socket Wire Curves
    wire_curves_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Wire Curves", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    wire_curves_socket.attribute_domain = 'POINT'
    wire_curves_socket.default_input = 'VALUE'
    wire_curves_socket.structure_type = 'AUTO'

    # Socket Routing
    routing_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Routing", in_out='INPUT', socket_type='NodeSocketGeometry')
    routing_socket.attribute_domain = 'POINT'
    routing_socket.default_input = 'VALUE'
    routing_socket.structure_type = 'AUTO'

    # Socket Wire Thickness
    wire_thickness_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Wire Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    wire_thickness_socket.default_value = 0.0010000000474974513
    wire_thickness_socket.min_value = 0.0
    wire_thickness_socket.max_value = 3.4028234663852886e+38
    wire_thickness_socket.subtype = 'DISTANCE'
    wire_thickness_socket.attribute_domain = 'POINT'
    wire_thickness_socket.default_input = 'VALUE'
    wire_thickness_socket.structure_type = 'AUTO'

    # Socket Crosstalk Power
    crosstalk_power_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Crosstalk Power", in_out='INPUT', socket_type='NodeSocketFloat')
    crosstalk_power_socket.default_value = 0.5
    crosstalk_power_socket.min_value = 0.0
    crosstalk_power_socket.max_value = 10000.0
    crosstalk_power_socket.subtype = 'NONE'
    crosstalk_power_socket.attribute_domain = 'POINT'
    crosstalk_power_socket.default_input = 'VALUE'
    crosstalk_power_socket.structure_type = 'AUTO'

    # Socket Crosstalk Factor
    crosstalk_factor_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Crosstalk Factor", in_out='INPUT', socket_type='NodeSocketFloat')
    crosstalk_factor_socket.default_value = 0.0
    crosstalk_factor_socket.min_value = 0.0
    crosstalk_factor_socket.max_value = 1.0
    crosstalk_factor_socket.subtype = 'FACTOR'
    crosstalk_factor_socket.attribute_domain = 'POINT'
    crosstalk_factor_socket.default_input = 'VALUE'
    crosstalk_factor_socket.structure_type = 'AUTO'

    # Socket Alignment Vector
    alignment_vector_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Alignment Vector", in_out='INPUT', socket_type='NodeSocketVector')
    alignment_vector_socket.default_value = (0.0, 0.0, 0.0)
    alignment_vector_socket.min_value = -10000.0
    alignment_vector_socket.max_value = 10000.0
    alignment_vector_socket.subtype = 'NONE'
    alignment_vector_socket.attribute_domain = 'POINT'
    alignment_vector_socket.default_input = 'VALUE'
    alignment_vector_socket.structure_type = 'AUTO'

    # Socket Avoid Distance
    avoid_distance_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Avoid Distance", in_out='INPUT', socket_type='NodeSocketFloat')
    avoid_distance_socket.default_value = 0.019999999552965164
    avoid_distance_socket.min_value = -10000.0
    avoid_distance_socket.max_value = 10000.0
    avoid_distance_socket.subtype = 'NONE'
    avoid_distance_socket.attribute_domain = 'POINT'
    avoid_distance_socket.default_input = 'VALUE'
    avoid_distance_socket.structure_type = 'AUTO'

    # Socket Use Alignment Vector Sorting
    use_alignment_vector_sorting_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Use Alignment Vector Sorting", in_out='INPUT', socket_type='NodeSocketBool')
    use_alignment_vector_sorting_socket.default_value = False
    use_alignment_vector_sorting_socket.attribute_domain = 'POINT'
    use_alignment_vector_sorting_socket.description = "Will find the closest electrode if false"
    use_alignment_vector_sorting_socket.default_input = 'VALUE'
    use_alignment_vector_sorting_socket.structure_type = 'AUTO'

    # Socket Overlap Accuracy
    overlap_accuracy_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Overlap Accuracy", in_out='INPUT', socket_type='NodeSocketInt')
    overlap_accuracy_socket.default_value = 0
    overlap_accuracy_socket.min_value = 0
    overlap_accuracy_socket.max_value = 10000
    overlap_accuracy_socket.subtype = 'NONE'
    overlap_accuracy_socket.attribute_domain = 'POINT'
    overlap_accuracy_socket.default_input = 'VALUE'
    overlap_accuracy_socket.structure_type = 'AUTO'

    # Socket Route Removal Multiplier
    route_removal_multiplier_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Route Removal Multiplier", in_out='INPUT', socket_type='NodeSocketFloat')
    route_removal_multiplier_socket.default_value = 2.0
    route_removal_multiplier_socket.min_value = 0.0
    route_removal_multiplier_socket.max_value = 10000.0
    route_removal_multiplier_socket.subtype = 'NONE'
    route_removal_multiplier_socket.attribute_domain = 'POINT'
    route_removal_multiplier_socket.default_input = 'VALUE'
    route_removal_multiplier_socket.structure_type = 'AUTO'

    # Socket Vector
    vector_socket = non_overlapping_wires__order_by_vector__distance__001_1.interface.new_socket(name="Vector", in_out='INPUT', socket_type='NodeSocketVector')
    vector_socket.default_value = (0.0, 0.0, 0.0)
    vector_socket.min_value = -10000.0
    vector_socket.max_value = 10000.0
    vector_socket.subtype = 'NONE'
    vector_socket.attribute_domain = 'POINT'
    vector_socket.default_input = 'VALUE'
    vector_socket.structure_type = 'AUTO'

    # Initialize non_overlapping_wires__order_by_vector__distance__001_1 nodes

    # Node Group Output
    group_output = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.hide = True
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Repeat Input
    repeat_input = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    repeat_input.show_options = True
    # Node Repeat Output
    repeat_output = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.show_options = True
    repeat_output.active_index = 2
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")
    # Create item "Input"
    repeat_output.repeat_items.new('GEOMETRY', "Input")
    # Create item "Input.001"
    repeat_output.repeat_items.new('GEOMETRY', "Input.001")

    # Node Group.008
    group_008 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeGroup")
    group_008.name = "Group.008"
    group_008.show_options = True
    group_008.node_tree = bpy.data.node_groups[node_tree_names[instantiate_wire_with_crosstalk_att_001_1_node_group]]

    # Node Store Named Attribute.007
    store_named_attribute_007 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_007.name = "Store Named Attribute.007"
    store_named_attribute_007.show_options = True
    store_named_attribute_007.data_type = 'BOOLEAN'
    store_named_attribute_007.domain = 'POINT'
    # Name
    store_named_attribute_007.inputs[2].default_value = "unrouted"
    # Value
    store_named_attribute_007.inputs[3].default_value = False

    # Node Named Attribute.006
    named_attribute_006 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_006.name = "Named Attribute.006"
    named_attribute_006.show_options = True
    named_attribute_006.data_type = 'BOOLEAN'
    # Name
    named_attribute_006.inputs[0].default_value = "unrouted"

    # Node Remove from set.001
    remove_from_set_001 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeFrame")
    remove_from_set_001.label = "Remove from set"
    remove_from_set_001.name = "Remove from set.001"
    remove_from_set_001.show_options = True
    remove_from_set_001.label_size = 20
    remove_from_set_001.shrink = True

    # Node Join Geometry.001
    join_geometry_001 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Separate Geometry.006
    separate_geometry_006 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_006.name = "Separate Geometry.006"
    separate_geometry_006.show_options = True
    separate_geometry_006.domain = 'POINT'

    # Node Reroute.031
    reroute_031 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_031.name = "Reroute.031"
    reroute_031.show_options = True
    reroute_031.socket_idname = "NodeSocketGeometry"
    # Node Reroute.032
    reroute_032 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_032.name = "Reroute.032"
    reroute_032.show_options = True
    reroute_032.socket_idname = "NodeSocketGeometry"
    # Node Group.004
    group_004 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.show_options = True
    group_004.node_tree = bpy.data.node_groups[node_tree_names[weighted_zone_heuristic_001_1_node_group]]

    # Node Store Named Attribute.002
    store_named_attribute_002 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'FLOAT'
    store_named_attribute_002.domain = 'EDGE'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "crosstalk_weight"

    # Node Reroute.034
    reroute_034 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_034.name = "Reroute.034"
    reroute_034.show_options = True
    reroute_034.socket_idname = "NodeSocketGeometry"
    # Node Reroute.035
    reroute_035 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_035.name = "Reroute.035"
    reroute_035.show_options = True
    reroute_035.socket_idname = "NodeSocketGeometry"
    # Node Reroute.037
    reroute_037 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_037.name = "Reroute.037"
    reroute_037.show_options = True
    reroute_037.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.038
    reroute_038 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_038.name = "Reroute.038"
    reroute_038.show_options = True
    reroute_038.socket_idname = "NodeSocketFloatFactor"
    # Node Group.009
    group_009 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeGroup")
    group_009.name = "Group.009"
    group_009.show_options = True
    group_009.node_tree = bpy.data.node_groups[node_tree_names[overlap_remover_001_1_node_group]]

    # Node Reroute.039
    reroute_039 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_039.name = "Reroute.039"
    reroute_039.show_options = True
    reroute_039.socket_idname = "NodeSocketGeometry"
    # Node Boolean Math.001
    boolean_math_001 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.show_options = True
    boolean_math_001.operation = 'OR'
    # Boolean
    boolean_math_001.inputs[0].default_value = False

    # Node Separate Geometry.007
    separate_geometry_007 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_007.name = "Separate Geometry.007"
    separate_geometry_007.show_options = True
    separate_geometry_007.domain = 'EDGE'

    # Node Curve to Mesh.001
    curve_to_mesh_001 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    curve_to_mesh_001.show_options = True
    # Scale
    curve_to_mesh_001.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh_001.inputs[3].default_value = False

    # Node Group Input.001
    group_input_001 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Store Named Attribute.009
    store_named_attribute_009 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_009.name = "Store Named Attribute.009"
    store_named_attribute_009.show_options = True
    store_named_attribute_009.data_type = 'BOOLEAN'
    store_named_attribute_009.domain = 'POINT'
    # Selection
    store_named_attribute_009.inputs[1].default_value = True
    # Name
    store_named_attribute_009.inputs[2].default_value = "unrouted"
    # Value
    store_named_attribute_009.inputs[3].default_value = True

    # Node Separate Geometry.008
    separate_geometry_008 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_008.name = "Separate Geometry.008"
    separate_geometry_008.show_options = True
    separate_geometry_008.domain = 'POINT'

    # Node Named Attribute.008
    named_attribute_008 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_008.name = "Named Attribute.008"
    named_attribute_008.show_options = True
    named_attribute_008.data_type = 'BOOLEAN'
    # Name
    named_attribute_008.inputs[0].default_value = "electrodes"

    # Node Group
    group = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[remove_from_set_1_node_group]]

    # Node Group.001
    group_001 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.show_options = True
    group_001.node_tree = bpy.data.node_groups[node_tree_names[select_clip_and_electrode_1_node_group]]

    # Node Reroute.002
    reroute_002 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketInt"
    # Node Reroute.003
    reroute_003 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Reroute
    reroute = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.004
    reroute_004 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketInt"
    # Node Reroute.005
    reroute_005 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketVector"
    # Node Reroute.006
    reroute_006 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketVector"
    # Node Reroute.007
    reroute_007 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketFloat"
    # Node Reroute.008
    reroute_008 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketBool"
    # Node Reroute.009
    reroute_009 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloatFactor"
    # Node Reroute.010
    reroute_010 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketInt"
    # Node Reroute.011
    reroute_011 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketVector"
    # Node Reroute.012
    reroute_012 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketVector"
    # Node Reroute.013
    reroute_013 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketBool"
    # Node Reroute.014
    reroute_014 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    reroute_014.socket_idname = "NodeSocketFloat"
    # Node Reroute.015
    reroute_015 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.016
    reroute_016 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    reroute_016.socket_idname = "NodeSocketFloatFactor"
    # Node Reroute.017
    reroute_017 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.show_options = True
    reroute_017.socket_idname = "NodeSocketInt"
    # Node Reroute.001
    reroute_001 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Reroute.018
    reroute_018 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    reroute_018.socket_idname = "NodeSocketGeometry"
    # Node Reroute.019
    reroute_019 = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    reroute_019.socket_idname = "NodeSocketGeometry"
    # Node Named Attribute
    named_attribute = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'INT'
    # Name
    named_attribute.inputs[0].default_value = "sensor_idx"

    # Node Attribute Statistic
    attribute_statistic = non_overlapping_wires__order_by_vector__distance__001_1.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.show_options = True
    attribute_statistic.data_type = 'FLOAT'
    attribute_statistic.domain = 'POINT'
    # Selection
    attribute_statistic.inputs[1].default_value = True

    # Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)



    # Set parents
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].parent = non_overlapping_wires__order_by_vector__distance__001_1.nodes["Remove from set.001"]

    # Set locations
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Output"].location = (1900.0, -2160.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].location = (-2460.0, -2120.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Output"].location = (1700.0, -2120.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].location = (40.0, -1880.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.007"].location = (1100.0, -2140.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.006"].location = (-2380.0, -2380.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Remove from set.001"].location = (-389.0, -2084.199951171875)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Join Geometry.001"].location = (1320.0, -1980.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.006"].location = (-2100.0, -2100.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.031"].location = (280.0, -1780.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.032"].location = (-2140.0, -2300.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].location = (-1800.0, -2180.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.002"].location = (-1460.0, -1840.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.034"].location = (-1880.0, -2140.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.035"].location = (-1200.0, -1920.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.037"].location = (-120.0, -2360.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.038"].location = (-120.0, -2380.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].location = (500.0, -2140.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.039"].location = (100.0, -2500.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Boolean Math.001"].location = (840.0, -2040.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.007"].location = (1320.0, -2280.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Curve to Mesh.001"].location = (1320.0, -2100.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].location = (-4020.0, -2300.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.009"].location = (-3700.0, -2120.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.008"].location = (-3400.0, -1820.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.008"].location = (-3700.0, -1900.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].location = (29.0, -35.800048828125)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].location = (-1040.0, -2040.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.002"].location = (-380.0, -2020.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.003"].location = (-480.0, -1920.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute"].location = (-1600.0, -2940.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.004"].location = (-1600.0, -3020.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.005"].location = (-1600.0, -2880.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.006"].location = (-1600.0, -2860.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.007"].location = (-1600.0, -3040.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.008"].location = (-1600.0, -2840.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.009"].location = (-1600.0, -2960.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.010"].location = (-3580.0, -2960.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.011"].location = (-3580.0, -2820.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.012"].location = (-3580.0, -2800.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.013"].location = (-3580.0, -2780.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.014"].location = (-3580.0, -2980.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.015"].location = (-3580.0, -2880.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.016"].location = (-3580.0, -2900.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.017"].location = (-100.0, -2020.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.001"].location = (900.0, -2000.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.018"].location = (980.0, -2500.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.019"].location = (-1960.0, -1780.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute"].location = (-3400.0, -1640.0)
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Attribute Statistic"].location = (-2900.0, -1700.0)

    # Set dimensions
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Output"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Output"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Output"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Output"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].width  = 240.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.007"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.007"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.006"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.006"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Remove from set.001"].width  = 318.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Remove from set.001"].height = 217.466796875

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Join Geometry.001"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Join Geometry.001"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.006"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.006"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.031"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.031"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.032"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.032"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].width  = 260.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.002"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.002"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.034"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.034"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.035"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.035"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.037"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.037"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.038"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.038"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].width  = 220.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.039"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.039"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Boolean Math.001"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Boolean Math.001"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.007"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.007"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Curve to Mesh.001"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Curve to Mesh.001"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.009"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.009"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.008"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.008"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.008"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.008"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].width  = 260.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].width  = 260.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.002"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.002"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.003"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.003"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.004"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.004"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.005"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.005"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.006"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.006"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.007"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.007"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.008"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.008"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.009"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.009"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.010"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.010"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.011"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.011"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.012"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.012"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.013"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.013"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.014"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.014"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.015"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.015"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.016"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.016"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.017"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.017"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.001"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.001"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.018"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.018"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.019"].width  = 14.5
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.019"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute"].height = 100.0

    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Attribute Statistic"].width  = 140.0
    non_overlapping_wires__order_by_vector__distance__001_1.nodes["Attribute Statistic"].height = 100.0


    # Initialize non_overlapping_wires__order_by_vector__distance__001_1 links

    # reroute_017.Output -> group_008.Start Indice
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.017"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].inputs[1]
    )
    # group.Clip Index -> group_008.End Indice
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].inputs[2]
    )
    # reroute_018.Output -> store_named_attribute_007.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.018"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.007"].inputs[0]
    )
    # reroute_037.Output -> group_008.Wire Thickness
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.037"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].inputs[3]
    )
    # reroute_001.Output -> join_geometry_001.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Join Geometry.001"].inputs[0]
    )
    # named_attribute_006.Attribute -> separate_geometry_006.Selection
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.006"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.006"].inputs[1]
    )
    # reroute_038.Output -> group_008.Crosstalk Factor
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.038"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].inputs[4]
    )
    # reroute_032.Output -> group_004.Current Wire
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.032"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].inputs[1]
    )
    # reroute_034.Output -> store_named_attribute_002.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.034"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # store_named_attribute_002.Geometry -> reroute_035.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.002"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.035"].inputs[0]
    )
    # group_008.Wires -> group_009.Wire
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].inputs[1]
    )
    # reroute_037.Output -> group_009.Wire Thickness
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.037"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].inputs[2]
    )
    # group_008.Vertex Selection -> boolean_math_001.Boolean
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].outputs[2],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Boolean Math.001"].inputs[1]
    )
    # boolean_math_001.Boolean -> store_named_attribute_007.Selection
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Boolean Math.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.007"].inputs[1]
    )
    # store_named_attribute_007.Geometry -> separate_geometry_007.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.007"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.007"].inputs[0]
    )
    # group_009.Result -> separate_geometry_007.Selection
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.007"].inputs[1]
    )
    # reroute_001.Output -> curve_to_mesh_001.Curve
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Curve to Mesh.001"].inputs[0]
    )
    # repeat_input.Geometry -> separate_geometry_006.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.006"].inputs[0]
    )
    # repeat_input.Input.001 -> reroute_032.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].outputs[3],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.032"].inputs[0]
    )
    # reroute_004.Output -> group_009.Level
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.004"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].inputs[3]
    )
    # group_input_001.Crosstalk Power -> group_004.Value Multiplier
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[2],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].inputs[2]
    )
    # group_input_001.Avoid Distance -> group_004.Avoid Distance
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[5],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].inputs[3]
    )
    # reroute.Output -> reroute_037.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.037"].inputs[0]
    )
    # reroute_009.Output -> reroute_038.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.009"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.038"].inputs[0]
    )
    # separate_geometry_007.Inverted -> repeat_output.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.007"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Output"].inputs[0]
    )
    # curve_to_mesh_001.Mesh -> repeat_output.Input.001
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Curve to Mesh.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Output"].inputs[2]
    )
    # join_geometry_001.Geometry -> repeat_output.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Join Geometry.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Output"].inputs[1]
    )
    # repeat_output.Input -> group_output.Wire Curves
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Output"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Output"].inputs[0]
    )
    # group_input_001.Routing -> store_named_attribute_009.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.009"].inputs[0]
    )
    # store_named_attribute_009.Geometry -> repeat_input.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.009"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].inputs[1]
    )
    # store_named_attribute_009.Geometry -> separate_geometry_008.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.009"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.008"].inputs[0]
    )
    # named_attribute_008.Attribute -> separate_geometry_008.Selection
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute.008"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.008"].inputs[1]
    )
    # reroute_007.Output -> group_009.Value
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.007"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].inputs[4]
    )
    # group_004.Current Crosstalk -> store_named_attribute_002.Value
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Store Named Attribute.002"].inputs[3]
    )
    # group_001.Clip Position -> group.Clip Position
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].inputs[2]
    )
    # reroute_005.Output -> group_001.Clip Sorting Vector
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.005"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].inputs[3]
    )
    # reroute_006.Output -> group_001.Electrode Sorting Vector
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.006"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].inputs[2]
    )
    # reroute_008.Output -> group_001.Sort by Vector
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.008"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].inputs[1]
    )
    # group_001.Electrode Index -> group.Electrode Index
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].inputs[0]
    )
    # group_001.Electrode Index -> reroute_002.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_035.Output -> group_001.Unrouted Graph
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.035"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.001"].inputs[0]
    )
    # reroute_003.Output -> group.Unrouted Graph
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.003"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].inputs[1]
    )
    # reroute_003.Output -> group_008.Mesh
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.003"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].inputs[0]
    )
    # reroute_035.Output -> reroute_003.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.035"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_015.Output -> reroute.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.015"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute"].inputs[0]
    )
    # reroute_010.Output -> reroute_004.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.010"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_011.Output -> reroute_005.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.011"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_012.Output -> reroute_006.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.012"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_014.Output -> reroute_007.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.014"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_013.Output -> reroute_008.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.013"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.008"].inputs[0]
    )
    # reroute_016.Output -> reroute_009.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.016"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.009"].inputs[0]
    )
    # group_input_001.Overlap Accuracy -> reroute_010.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[7],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.010"].inputs[0]
    )
    # group_input_001.Vector -> reroute_011.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[9],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.011"].inputs[0]
    )
    # group_input_001.Alignment Vector -> reroute_012.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[4],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.012"].inputs[0]
    )
    # group_input_001.Use Alignment Vector Sorting -> reroute_013.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[6],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.013"].inputs[0]
    )
    # group_input_001.Route Removal Multiplier -> reroute_014.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[8],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.014"].inputs[0]
    )
    # group_input_001.Wire Thickness -> reroute_015.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.015"].inputs[0]
    )
    # group_input_001.Crosstalk Factor -> reroute_016.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group Input.001"].outputs[3],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.016"].inputs[0]
    )
    # reroute_002.Output -> reroute_017.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.002"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.017"].inputs[0]
    )
    # group.Filtered Unrouted Graph -> group_009.Routing
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.009"].inputs[0]
    )
    # group.Filtered Unrouted Graph -> reroute_039.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group"].outputs[1],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.039"].inputs[0]
    )
    # group_008.Wires -> reroute_001.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.008"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_039.Output -> reroute_018.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.039"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.018"].inputs[0]
    )
    # reroute_019.Output -> reroute_031.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.019"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.031"].inputs[0]
    )
    # repeat_input.Input -> reroute_019.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].outputs[2],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.019"].inputs[0]
    )
    # reroute_034.Output -> group_004.Routing
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.034"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Group.004"].inputs[0]
    )
    # separate_geometry_006.Selection -> reroute_034.Input
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.006"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.034"].inputs[0]
    )
    # separate_geometry_008.Selection -> attribute_statistic.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Separate Geometry.008"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Attribute Statistic"].inputs[0]
    )
    # named_attribute.Attribute -> attribute_statistic.Attribute
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Named Attribute"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Attribute Statistic"].inputs[2]
    )
    # attribute_statistic.Max -> repeat_input.Iterations
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Attribute Statistic"].outputs[4],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Repeat Input"].inputs[0]
    )
    # reroute_031.Output -> join_geometry_001.Geometry
    non_overlapping_wires__order_by_vector__distance__001_1.links.new(
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Reroute.031"].outputs[0],
        non_overlapping_wires__order_by_vector__distance__001_1.nodes["Join Geometry.001"].inputs[0]
    )

    return non_overlapping_wires__order_by_vector__distance__001_1


def connect_vertices_in_distance_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Connect vertices in distance.001 node group"""
    connect_vertices_in_distance_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Connect vertices in distance.001")

    connect_vertices_in_distance_001_1.color_tag = 'NONE'
    connect_vertices_in_distance_001_1.description = "Connects all vertices in mesh together"
    connect_vertices_in_distance_001_1.default_group_node_width = 140
    connect_vertices_in_distance_001_1.show_modifier_manage_panel = True

    # connect_vertices_in_distance_001_1 interface

    # Socket Geometry
    geometry_socket = connect_vertices_in_distance_001_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Connection Factor
    connection_factor_socket = connect_vertices_in_distance_001_1.interface.new_socket(name="Connection Factor", in_out='INPUT', socket_type='NodeSocketFloat')
    connection_factor_socket.default_value = 0.029999999329447746
    connection_factor_socket.min_value = -10000.0
    connection_factor_socket.max_value = 10000.0
    connection_factor_socket.subtype = 'NONE'
    connection_factor_socket.attribute_domain = 'POINT'
    connection_factor_socket.default_input = 'VALUE'
    connection_factor_socket.structure_type = 'AUTO'

    # Socket Input
    input_socket = connect_vertices_in_distance_001_1.interface.new_socket(name="Input", in_out='INPUT', socket_type='NodeSocketGeometry')
    input_socket.attribute_domain = 'POINT'
    input_socket.default_input = 'VALUE'
    input_socket.structure_type = 'AUTO'

    # Socket Connecting Geometry
    connecting_geometry_socket = connect_vertices_in_distance_001_1.interface.new_socket(name="Connecting Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    connecting_geometry_socket.attribute_domain = 'POINT'
    connecting_geometry_socket.default_input = 'VALUE'
    connecting_geometry_socket.structure_type = 'AUTO'

    # Initialize connect_vertices_in_distance_001_1 nodes

    # Node Group Output
    group_output = connect_vertices_in_distance_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = connect_vertices_in_distance_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node For Each Geometry Element Input
    for_each_geometry_element_input = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeForeachGeometryElementInput")
    for_each_geometry_element_input.name = "For Each Geometry Element Input"
    for_each_geometry_element_input.show_options = True
    # Node For Each Geometry Element Output
    for_each_geometry_element_output = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeForeachGeometryElementOutput")
    for_each_geometry_element_output.name = "For Each Geometry Element Output"
    for_each_geometry_element_output.show_options = True
    for_each_geometry_element_output.active_generation_index = 0
    for_each_geometry_element_output.active_input_index = 0
    for_each_geometry_element_output.active_main_index = 0
    for_each_geometry_element_output.domain = 'POINT'
    for_each_geometry_element_output.generation_items.clear()
    for_each_geometry_element_output.generation_items.new('GEOMETRY', "Geometry")
    for_each_geometry_element_output.generation_items[0].domain = 'POINT'
    for_each_geometry_element_output.input_items.clear()
    for_each_geometry_element_output.input_items.new('VECTOR', "Position")
    for_each_geometry_element_output.inspection_index = 0
    for_each_geometry_element_output.main_items.clear()

    # Node Curve Line
    curve_line = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.show_options = True
    curve_line.mode = 'POINTS'

    # Node Position
    position = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Join Geometry
    join_geometry = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Curve to Mesh
    curve_to_mesh = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.show_options = True
    # Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    # Node For Each Geometry Element Input.001
    for_each_geometry_element_input_001 = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeForeachGeometryElementInput")
    for_each_geometry_element_input_001.name = "For Each Geometry Element Input.001"
    for_each_geometry_element_input_001.show_options = True
    # Node For Each Geometry Element Output.001
    for_each_geometry_element_output_001 = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeForeachGeometryElementOutput")
    for_each_geometry_element_output_001.name = "For Each Geometry Element Output.001"
    for_each_geometry_element_output_001.show_options = True
    for_each_geometry_element_output_001.active_generation_index = 0
    for_each_geometry_element_output_001.active_input_index = 0
    for_each_geometry_element_output_001.active_main_index = 0
    for_each_geometry_element_output_001.domain = 'POINT'
    for_each_geometry_element_output_001.generation_items.clear()
    for_each_geometry_element_output_001.generation_items.new('GEOMETRY', "Geometry")
    for_each_geometry_element_output_001.generation_items[0].domain = 'POINT'
    for_each_geometry_element_output_001.input_items.clear()
    for_each_geometry_element_output_001.inspection_index = 0
    for_each_geometry_element_output_001.main_items.clear()

    # Node Sample Index
    sample_index = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'
    # Index
    sample_index.inputs[2].default_value = 0

    # Node Position.001
    position_001 = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Vector Math
    vector_math = connect_vertices_in_distance_001_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'DISTANCE'

    # Node Sample Index.001
    sample_index_001 = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'

    # Node Index
    index = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Compare
    compare = connect_vertices_in_distance_001_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_EQUAL'

    # Node Reroute
    reroute = connect_vertices_in_distance_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Reroute.001
    reroute_001 = connect_vertices_in_distance_001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Viewer
    viewer = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeViewer")
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

    # Node Sample Nearest
    sample_nearest = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Sample Index.002
    sample_index_002 = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'

    # Node Reroute.002
    reroute_002 = connect_vertices_in_distance_001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketVector"
    # Node Vector Math.001
    vector_math_001 = connect_vertices_in_distance_001_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'DISTANCE'

    # Node Position.002
    position_002 = connect_vertices_in_distance_001_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Reroute.003
    reroute_003 = connect_vertices_in_distance_001_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketVector"
    # Node Math
    math = connect_vertices_in_distance_001_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'ADD'
    math.use_clamp = False

    # Process zone input For Each Geometry Element Input
    for_each_geometry_element_input.pair_with_output(for_each_geometry_element_output)
    # Selection
    for_each_geometry_element_input.inputs[1].default_value = True


    # Process zone input For Each Geometry Element Input.001
    for_each_geometry_element_input_001.pair_with_output(for_each_geometry_element_output_001)



    # Set locations
    connect_vertices_in_distance_001_1.nodes["Group Output"].location = (1590.0, 0.0)
    connect_vertices_in_distance_001_1.nodes["Group Input"].location = (-1900.0, 200.0)
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].location = (-1280.0, 440.0)
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output"].location = (1020.0, 93.54461669921875)
    connect_vertices_in_distance_001_1.nodes["Curve Line"].location = (620.0, 133.54461669921875)
    connect_vertices_in_distance_001_1.nodes["Position"].location = (-1480.0, 220.0)
    connect_vertices_in_distance_001_1.nodes["Join Geometry"].location = (1400.0, 133.54461669921875)
    connect_vertices_in_distance_001_1.nodes["Curve to Mesh"].location = (1200.0, 33.54461669921875)
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input.001"].location = (175.41795349121094, -18.4775390625)
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output.001"].location = (832.697265625, -23.927581787109375)
    connect_vertices_in_distance_001_1.nodes["Sample Index"].location = (448.64013671875, -35.27886962890625)
    connect_vertices_in_distance_001_1.nodes["Position.001"].location = (-170.42822265625, -202.89080810546875)
    connect_vertices_in_distance_001_1.nodes["Vector Math"].location = (-520.0, -180.0)
    connect_vertices_in_distance_001_1.nodes["Sample Index.001"].location = (-740.0, -120.0)
    connect_vertices_in_distance_001_1.nodes["Index"].location = (-960.0, -260.0)
    connect_vertices_in_distance_001_1.nodes["Compare"].location = (1.3113021850585938e-05, -240.0)
    connect_vertices_in_distance_001_1.nodes["Reroute"].location = (-1080.0, -340.0)
    connect_vertices_in_distance_001_1.nodes["Reroute.001"].location = (-862.2825927734375, 55.633018493652344)
    connect_vertices_in_distance_001_1.nodes["Viewer"].location = (1200.0, 200.0)
    connect_vertices_in_distance_001_1.nodes["Sample Nearest"].location = (-740.0, 60.0)
    connect_vertices_in_distance_001_1.nodes["Sample Index.002"].location = (-560.0, 260.0)
    connect_vertices_in_distance_001_1.nodes["Reroute.002"].location = (180.0, 280.0)
    connect_vertices_in_distance_001_1.nodes["Vector Math.001"].location = (-360.0, 220.0)
    connect_vertices_in_distance_001_1.nodes["Position.002"].location = (-740.0, 180.0)
    connect_vertices_in_distance_001_1.nodes["Reroute.003"].location = (-403.5496520996094, 285.29620361328125)
    connect_vertices_in_distance_001_1.nodes["Math"].location = (-160.0, -380.0)

    # Set dimensions
    connect_vertices_in_distance_001_1.nodes["Group Output"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Group Output"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Group Input"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Group Input"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Curve Line"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Curve Line"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Position"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Position"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Join Geometry"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Join Geometry"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Curve to Mesh"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Curve to Mesh"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input.001"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input.001"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output.001"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output.001"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Sample Index"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Sample Index"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Position.001"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Position.001"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Vector Math"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Vector Math"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Sample Index.001"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Sample Index.001"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Index"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Index"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Compare"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Compare"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Reroute"].width  = 10.0
    connect_vertices_in_distance_001_1.nodes["Reroute"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Reroute.001"].width  = 10.0
    connect_vertices_in_distance_001_1.nodes["Reroute.001"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Viewer"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Viewer"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Sample Nearest"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Sample Nearest"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Sample Index.002"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Sample Index.002"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Reroute.002"].width  = 10.0
    connect_vertices_in_distance_001_1.nodes["Reroute.002"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Vector Math.001"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Vector Math.001"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Position.002"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Position.002"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Reroute.003"].width  = 10.0
    connect_vertices_in_distance_001_1.nodes["Reroute.003"].height = 100.0

    connect_vertices_in_distance_001_1.nodes["Math"].width  = 140.0
    connect_vertices_in_distance_001_1.nodes["Math"].height = 100.0


    # Initialize connect_vertices_in_distance_001_1 links

    # for_each_geometry_element_input_001.Element -> sample_index.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input.001"].outputs[1],
        connect_vertices_in_distance_001_1.nodes["Sample Index"].inputs[0]
    )
    # position_001.Position -> sample_index.Value
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Position.001"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Index"].inputs[1]
    )
    # curve_line.Curve -> for_each_geometry_element_output_001.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Curve Line"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output.001"].inputs[1]
    )
    # compare.Result -> for_each_geometry_element_input_001.Selection
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Compare"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input.001"].inputs[1]
    )
    # for_each_geometry_element_output_001.Geometry -> for_each_geometry_element_output.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output.001"].outputs[2],
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output"].inputs[1]
    )
    # vector_math.Value -> compare.A
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Vector Math"].outputs[1],
        connect_vertices_in_distance_001_1.nodes["Compare"].inputs[0]
    )
    # reroute_002.Output -> curve_line.Start
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute.002"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Curve Line"].inputs[0]
    )
    # sample_index_001.Value -> vector_math.Vector
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Sample Index.001"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Vector Math"].inputs[1]
    )
    # for_each_geometry_element_output.Geometry -> curve_to_mesh.Curve
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output"].outputs[2],
        connect_vertices_in_distance_001_1.nodes["Curve to Mesh"].inputs[0]
    )
    # index.Index -> sample_index_001.Index
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Index"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Index.001"].inputs[2]
    )
    # position.Position -> sample_index_001.Value
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Position"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Index.001"].inputs[1]
    )
    # curve_to_mesh.Mesh -> join_geometry.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Curve to Mesh"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Join Geometry"].inputs[0]
    )
    # for_each_geometry_element_input.Position -> vector_math.Vector
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].outputs[2],
        connect_vertices_in_distance_001_1.nodes["Vector Math"].inputs[0]
    )
    # position.Position -> for_each_geometry_element_input.Position
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Position"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].inputs[2]
    )
    # sample_index.Value -> curve_line.End
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Sample Index"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Curve Line"].inputs[1]
    )
    # join_geometry.Geometry -> group_output.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Join Geometry"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Connection Factor -> reroute.Input
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Group Input"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Reroute"].inputs[0]
    )
    # reroute_001.Output -> for_each_geometry_element_input_001.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute.001"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input.001"].inputs[0]
    )
    # group_input.Input -> for_each_geometry_element_input.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Group Input"].outputs[1],
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].inputs[0]
    )
    # group_input.Connecting Geometry -> reroute_001.Input
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Group Input"].outputs[2],
        connect_vertices_in_distance_001_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_001.Output -> sample_index_001.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute.001"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Index.001"].inputs[0]
    )
    # for_each_geometry_element_output.Geometry -> viewer.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Viewer"].inputs[0]
    )
    # reroute_001.Output -> sample_nearest.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute.001"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Nearest"].inputs[0]
    )
    # for_each_geometry_element_input.Position -> sample_nearest.Sample Position
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].outputs[2],
        connect_vertices_in_distance_001_1.nodes["Sample Nearest"].inputs[1]
    )
    # reroute_003.Output -> reroute_002.Input
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute.003"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Reroute.002"].inputs[0]
    )
    # position_002.Position -> sample_index_002.Value
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Position.002"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Index.002"].inputs[1]
    )
    # sample_nearest.Index -> sample_index_002.Index
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Sample Nearest"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Index.002"].inputs[2]
    )
    # reroute_001.Output -> sample_index_002.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute.001"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Sample Index.002"].inputs[0]
    )
    # sample_index_002.Value -> vector_math_001.Vector
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Sample Index.002"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Vector Math.001"].inputs[1]
    )
    # for_each_geometry_element_input.Position -> reroute_003.Input
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Input"].outputs[2],
        connect_vertices_in_distance_001_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_003.Output -> vector_math_001.Vector
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute.003"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Vector Math.001"].inputs[0]
    )
    # math.Value -> compare.B
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Math"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Compare"].inputs[1]
    )
    # vector_math_001.Value -> math.Value
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Vector Math.001"].outputs[1],
        connect_vertices_in_distance_001_1.nodes["Math"].inputs[0]
    )
    # reroute.Output -> math.Value
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["Reroute"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Math"].inputs[1]
    )
    # for_each_geometry_element_output.Geometry -> join_geometry.Geometry
    connect_vertices_in_distance_001_1.links.new(
        connect_vertices_in_distance_001_1.nodes["For Each Geometry Element Output"].outputs[0],
        connect_vertices_in_distance_001_1.nodes["Join Geometry"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return connect_vertices_in_distance_001_1


def wiring_layers__consolidated__001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Wiring Layers (Consolidated).001 node group"""
    wiring_layers__consolidated__001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Wiring Layers (Consolidated).001")

    wiring_layers__consolidated__001_1.color_tag = 'NONE'
    wiring_layers__consolidated__001_1.description = ""
    wiring_layers__consolidated__001_1.default_group_node_width = 140
    wiring_layers__consolidated__001_1.show_modifier_manage_panel = True

    # wiring_layers__consolidated__001_1 interface

    # Socket Routing Layers
    routing_layers_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Routing Layers", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    routing_layers_socket.attribute_domain = 'POINT'
    routing_layers_socket.default_input = 'VALUE'
    routing_layers_socket.structure_type = 'AUTO'

    # Socket Routing Cutout
    routing_cutout_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Routing Cutout", in_out='INPUT', socket_type='NodeSocketGeometry')
    routing_cutout_socket.attribute_domain = 'POINT'
    routing_cutout_socket.default_input = 'VALUE'
    routing_cutout_socket.structure_type = 'AUTO'

    # Socket Endpoints Set 1
    endpoints_set_1_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Endpoints Set 1", in_out='INPUT', socket_type='NodeSocketGeometry')
    endpoints_set_1_socket.attribute_domain = 'POINT'
    endpoints_set_1_socket.description = "Must be a set of individual vertices!"
    endpoints_set_1_socket.default_input = 'VALUE'
    endpoints_set_1_socket.structure_type = 'AUTO'

    # Socket Endpoints Set 2
    endpoints_set_2_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Endpoints Set 2", in_out='INPUT', socket_type='NodeSocketGeometry')
    endpoints_set_2_socket.attribute_domain = 'POINT'
    endpoints_set_2_socket.default_input = 'VALUE'
    endpoints_set_2_socket.structure_type = 'AUTO'

    # Socket Layers
    layers_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Layers", in_out='INPUT', socket_type='NodeSocketInt')
    layers_socket.default_value = 4
    layers_socket.min_value = 0
    layers_socket.max_value = 2147483647
    layers_socket.subtype = 'NONE'
    layers_socket.attribute_domain = 'POINT'
    layers_socket.default_input = 'VALUE'
    layers_socket.structure_type = 'AUTO'

    # Socket Base Offset
    base_offset_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Base Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    base_offset_socket.default_value = 1.0
    base_offset_socket.min_value = -3.4028234663852886e+38
    base_offset_socket.max_value = 3.4028234663852886e+38
    base_offset_socket.subtype = 'NONE'
    base_offset_socket.attribute_domain = 'POINT'
    base_offset_socket.default_input = 'VALUE'
    base_offset_socket.structure_type = 'AUTO'

    # Socket Thickness
    thickness_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    thickness_socket.default_value = 0.1000000536441803
    thickness_socket.min_value = -3.4028234663852886e+38
    thickness_socket.max_value = 3.4028234663852886e+38
    thickness_socket.subtype = 'NONE'
    thickness_socket.attribute_domain = 'POINT'
    thickness_socket.default_input = 'VALUE'
    thickness_socket.structure_type = 'AUTO'

    # Socket Connector Endpoint Margin
    connector_endpoint_margin_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Connector Endpoint Margin", in_out='INPUT', socket_type='NodeSocketFloat')
    connector_endpoint_margin_socket.default_value = 0.0
    connector_endpoint_margin_socket.min_value = -10000.0
    connector_endpoint_margin_socket.max_value = 10000.0
    connector_endpoint_margin_socket.subtype = 'NONE'
    connector_endpoint_margin_socket.attribute_domain = 'POINT'
    connector_endpoint_margin_socket.default_input = 'VALUE'
    connector_endpoint_margin_socket.structure_type = 'AUTO'

    # Socket Routing Self Margin
    routing_self_margin_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Routing Self Margin", in_out='INPUT', socket_type='NodeSocketFloat')
    routing_self_margin_socket.default_value = 0.0
    routing_self_margin_socket.min_value = -10000.0
    routing_self_margin_socket.max_value = 10000.0
    routing_self_margin_socket.subtype = 'NONE'
    routing_self_margin_socket.attribute_domain = 'POINT'
    routing_self_margin_socket.default_input = 'VALUE'
    routing_self_margin_socket.structure_type = 'AUTO'

    # Socket Sensor Endpoint Margin
    sensor_endpoint_margin_socket = wiring_layers__consolidated__001_1.interface.new_socket(name="Sensor Endpoint Margin", in_out='INPUT', socket_type='NodeSocketFloat')
    sensor_endpoint_margin_socket.default_value = 0.0
    sensor_endpoint_margin_socket.min_value = -10000.0
    sensor_endpoint_margin_socket.max_value = 10000.0
    sensor_endpoint_margin_socket.subtype = 'NONE'
    sensor_endpoint_margin_socket.attribute_domain = 'POINT'
    sensor_endpoint_margin_socket.default_input = 'VALUE'
    sensor_endpoint_margin_socket.structure_type = 'AUTO'

    # Initialize wiring_layers__consolidated__001_1 nodes

    # Node Routing Layers
    routing_layers = wiring_layers__consolidated__001_1.nodes.new("NodeGroupOutput")
    routing_layers.name = "Routing Layers"
    routing_layers.show_options = True
    routing_layers.is_active_output = True

    # Node Group Input
    group_input = wiring_layers__consolidated__001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Extrude Mesh.001
    extrude_mesh_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_001.name = "Extrude Mesh.001"
    extrude_mesh_001.show_options = True
    extrude_mesh_001.mode = 'FACES'
    # Selection
    extrude_mesh_001.inputs[1].default_value = True
    # Offset
    extrude_mesh_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh_001.inputs[4].default_value = False

    # Node Extrude Mesh.002
    extrude_mesh_002 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.show_options = True
    extrude_mesh_002.mode = 'FACES'
    # Selection
    extrude_mesh_002.inputs[1].default_value = True
    # Offset
    extrude_mesh_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh_002.inputs[4].default_value = False

    # Node Merge by Distance
    merge_by_distance = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.show_options = True
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance.inputs[3].default_value = 0.0010000000474974513

    # Node Delete Geometry
    delete_geometry = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.show_options = True
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ONLY_FACE'

    # Node Delete Geometry.001
    delete_geometry_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.show_options = True
    delete_geometry_001.domain = 'FACE'
    delete_geometry_001.mode = 'ONLY_FACE'

    # Node Reroute
    reroute = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Delete Geometry.003
    delete_geometry_003 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_003.name = "Delete Geometry.003"
    delete_geometry_003.show_options = True
    delete_geometry_003.domain = 'FACE'
    delete_geometry_003.mode = 'ONLY_FACE'
    # Selection
    delete_geometry_003.inputs[1].default_value = True

    # Node Merge by Distance.001
    merge_by_distance_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.show_options = True
    # Selection
    merge_by_distance_001.inputs[1].default_value = True
    # Mode
    merge_by_distance_001.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance_001.inputs[3].default_value = 0.0010000000474974513

    # Node Frame
    frame = wiring_layers__consolidated__001_1.nodes.new("NodeFrame")
    frame.label = "Instnatiate 3 layers"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.4694683253765106, 0.3309366703033447, 0.6079999804496765)
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Reroute.001
    reroute_001 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Delete Geometry.004
    delete_geometry_004 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_004.name = "Delete Geometry.004"
    delete_geometry_004.show_options = True
    delete_geometry_004.domain = 'FACE'
    delete_geometry_004.mode = 'ALL'

    # Node Triangulate
    triangulate = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeTriangulate")
    triangulate.name = "Triangulate"
    triangulate.show_options = True
    # Selection
    triangulate.inputs[1].default_value = True
    # Quad Method
    triangulate.inputs[2].default_value = 'Shortest Diagonal'
    # N-gon Method
    triangulate.inputs[3].default_value = 'Beauty'

    # Node Group
    group = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[connect_vertices_in_distance_001_1_node_group]]

    # Node Reroute.018
    reroute_018 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    reroute_018.socket_idname = "NodeSocketGeometry"
    # Node Group.001
    group_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.show_options = True
    group_001.node_tree = bpy.data.node_groups[node_tree_names[connect_vertices_in_distance_001_1_node_group]]

    # Node Reroute.019
    reroute_019 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    reroute_019.socket_idname = "NodeSocketFloat"
    # Node Join Geometry
    join_geometry = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Repeat Input
    repeat_input = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    repeat_input.show_options = True
    # Node Repeat Output
    repeat_output = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.show_options = True
    repeat_output.active_index = 0
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")

    # Node Join Geometry.003
    join_geometry_003 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"
    join_geometry_003.show_options = True

    # Node Reroute.003
    reroute_003 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloat"
    # Node Math.001
    math_001 = wiring_layers__consolidated__001_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'SUBTRACT'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 1.0

    # Node Frame.001
    frame_001 = wiring_layers__consolidated__001_1.nodes.new("NodeFrame")
    frame_001.label = "Combine Layers Together"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.20418763160705566, 0.5564008355140686, 0.6079999804496765)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Reroute.002
    reroute_002 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Group.002
    group_002 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.show_options = True
    group_002.node_tree = bpy.data.node_groups[node_tree_names[connect_vertices_in_distance_001_1_node_group]]

    # Node Store Named Attribute.001
    store_named_attribute_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "electrodes"
    # Value
    store_named_attribute_001.inputs[3].default_value = True

    # Node Frame.002
    frame_002 = wiring_layers__consolidated__001_1.nodes.new("NodeFrame")
    frame_002.label = "Connect Wires to Electrodes"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.29208049178123474, 0.5932955145835876, 0.6079999804496765)
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Reroute.004
    reroute_004 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketGeometry"
    # Node Reroute.005
    reroute_005 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketGeometry"
    # Node Store Named Attribute.002
    store_named_attribute_002 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'BOOLEAN'
    store_named_attribute_002.domain = 'POINT'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "clips"
    # Value
    store_named_attribute_002.inputs[3].default_value = True

    # Node Frame.003
    frame_003 = wiring_layers__consolidated__001_1.nodes.new("NodeFrame")
    frame_003.label = "Connect Wires to Clips"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.10491319745779037, 0.36224204301834106, 0.6079999804496765)
    frame_003.show_options = True
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Join Geometry.001
    join_geometry_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Merge by Distance.002
    merge_by_distance_002 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_002.name = "Merge by Distance.002"
    merge_by_distance_002.show_options = True
    # Selection
    merge_by_distance_002.inputs[1].default_value = True
    # Mode
    merge_by_distance_002.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance_002.inputs[3].default_value = 0.0010000000474974513

    # Node Store Named Attribute
    store_named_attribute = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'INT'
    store_named_attribute.domain = 'POINT'
    # Name
    store_named_attribute.inputs[2].default_value = "sensor_idx"

    # Node Named Attribute
    named_attribute = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'BOOLEAN'
    # Name
    named_attribute.inputs[0].default_value = "electrodes"

    # Node Sample Nearest
    sample_nearest = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Separate Geometry
    separate_geometry = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.show_options = True
    separate_geometry.domain = 'POINT'

    # Node Sample Index
    sample_index = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Index
    index = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Position
    position = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Viewer
    viewer = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 1
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")
    viewer.viewer_items.new('INT', "Attribute")

    # Node Frame.004
    frame_004 = wiring_layers__consolidated__001_1.nodes.new("NodeFrame")
    frame_004.label = "Fix Electrode Mismatch"
    frame_004.name = "Frame.004"
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Named Attribute.001
    named_attribute_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'INT'
    # Name
    named_attribute_001.inputs[0].default_value = "sensor_idx"

    # Node Sample Index.001
    sample_index_001 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'INT'
    sample_index_001.domain = 'POINT'

    # Node Named Attribute.002
    named_attribute_002 = wiring_layers__consolidated__001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.show_options = True
    named_attribute_002.data_type = 'INT'
    # Name
    named_attribute_002.inputs[0].default_value = "sensor_idx"

    # Node Reroute.006
    reroute_006 = wiring_layers__consolidated__001_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketGeometry"
    # Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)



    # Set parents
    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Merge by Distance"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Delete Geometry"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Reroute"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.003"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Merge by Distance.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.004"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Group"].parent = wiring_layers__consolidated__001_1.nodes["Frame.003"]
    wiring_layers__consolidated__001_1.nodes["Reroute.018"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Group.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Join Geometry"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Repeat Input"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Repeat Output"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Join Geometry.003"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Reroute.003"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Math.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame"]
    wiring_layers__consolidated__001_1.nodes["Group.002"].parent = wiring_layers__consolidated__001_1.nodes["Frame.002"]
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame.002"]
    wiring_layers__consolidated__001_1.nodes["Frame.002"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Reroute.004"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Reroute.005"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.002"].parent = wiring_layers__consolidated__001_1.nodes["Frame.003"]
    wiring_layers__consolidated__001_1.nodes["Frame.003"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Named Attribute"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Sample Nearest"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Separate Geometry"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Sample Index"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Index"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Position"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Named Attribute.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame.001"]
    wiring_layers__consolidated__001_1.nodes["Sample Index.001"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Named Attribute.002"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]
    wiring_layers__consolidated__001_1.nodes["Reroute.006"].parent = wiring_layers__consolidated__001_1.nodes["Frame.004"]

    # Set locations
    wiring_layers__consolidated__001_1.nodes["Routing Layers"].location = (5580.0, 60.0)
    wiring_layers__consolidated__001_1.nodes["Group Input"].location = (-900.0, 100.0)
    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].location = (28.77099609375, -55.52604293823242)
    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].location = (886.0, -284.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Merge by Distance"].location = (1646.0, -184.8000030517578)
    wiring_layers__consolidated__001_1.nodes["Delete Geometry"].location = (227.471923828125, -81.84916687011719)
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.001"].location = (1066.0, -264.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Reroute"].location = (278.85028076171875, -385.8141784667969)
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.003"].location = (1826.0, -264.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Merge by Distance.001"].location = (973.833251953125, -615.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Frame"].location = (89.0, -40.20000076293945)
    wiring_layers__consolidated__001_1.nodes["Reroute.001"].location = (2080.0, -20.0)
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.004"].location = (406.9999694824219, -153.6768798828125)
    wiring_layers__consolidated__001_1.nodes["Triangulate"].location = (-40.0, -100.0)
    wiring_layers__consolidated__001_1.nodes["Group"].location = (29.0, -55.80000305175781)
    wiring_layers__consolidated__001_1.nodes["Reroute.018"].location = (33.833251953125, -855.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Group.001"].location = (113.833251953125, -735.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Reroute.019"].location = (2080.0, 0.0)
    wiring_layers__consolidated__001_1.nodes["Join Geometry"].location = (793.833251953125, -675.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Repeat Input"].location = (666.0, -144.8000030517578)
    wiring_layers__consolidated__001_1.nodes["Repeat Output"].location = (1406.0, -224.8000030517578)
    wiring_layers__consolidated__001_1.nodes["Join Geometry.003"].location = (1246.0, -164.8000030517578)
    wiring_layers__consolidated__001_1.nodes["Reroute.003"].location = (506.0, -444.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Math.001"].location = (106.0, -424.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Frame.001"].location = (2686.166748046875, 675.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Reroute.002"].location = (2080.0, 40.0)
    wiring_layers__consolidated__001_1.nodes["Group.002"].location = (29.0, -275.8000183105469)
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.001"].location = (69.0, -55.800018310546875)
    wiring_layers__consolidated__001_1.nodes["Frame.002"].location = (444.833251953125, -179.99996948242188)
    wiring_layers__consolidated__001_1.nodes["Reroute.004"].location = (313.833251953125, -555.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Reroute.005"].location = (313.833251953125, -1035.800048828125)
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.002"].location = (89.0, -275.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Frame.003"].location = (464.833251953125, -860.0)
    wiring_layers__consolidated__001_1.nodes["Join Geometry.001"].location = (3940.0, 80.0)
    wiring_layers__consolidated__001_1.nodes["Merge by Distance.002"].location = (4160.0, 20.0)
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].location = (1189.0, -75.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Named Attribute"].location = (29.0, -515.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Sample Nearest"].location = (729.0, -55.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Separate Geometry"].location = (209.0, -395.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Sample Index"].location = (449.0, -115.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Index"].location = (129.0, -255.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Position"].location = (249.0, -195.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Viewer"].location = (5300.0, 900.4758911132812)
    wiring_layers__consolidated__001_1.nodes["Frame.004"].location = (3951.0, 835.7999877929688)
    wiring_layers__consolidated__001_1.nodes["Named Attribute.001"].location = (533.833251953125, -35.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Sample Index.001"].location = (1009.0, -375.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Named Attribute.002"].location = (809.0, -475.79998779296875)
    wiring_layers__consolidated__001_1.nodes["Reroute.006"].location = (689.46533203125, -138.723876953125)

    # Set dimensions
    wiring_layers__consolidated__001_1.nodes["Routing Layers"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Routing Layers"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Group Input"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Group Input"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Merge by Distance"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Merge by Distance"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Delete Geometry"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Delete Geometry"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Delete Geometry.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Reroute"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Delete Geometry.003"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.003"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Merge by Distance.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Merge by Distance.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Frame"].width  = 1995.333251953125
    wiring_layers__consolidated__001_1.nodes["Frame"].height = 595.4666748046875

    wiring_layers__consolidated__001_1.nodes["Reroute.001"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Delete Geometry.004"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Delete Geometry.004"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Triangulate"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Triangulate"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Group"].width  = 260.0
    wiring_layers__consolidated__001_1.nodes["Group"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Reroute.018"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.018"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Group.001"].width  = 280.0
    wiring_layers__consolidated__001_1.nodes["Group.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Reroute.019"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.019"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Join Geometry"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Join Geometry"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Repeat Input"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Repeat Input"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Repeat Output"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Repeat Output"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Join Geometry.003"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Join Geometry.003"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Reroute.003"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.003"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Math.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Math.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Frame.001"].width  = 1142.833251953125
    wiring_layers__consolidated__001_1.nodes["Frame.001"].height = 1349.800048828125

    wiring_layers__consolidated__001_1.nodes["Reroute.002"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.002"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Group.002"].width  = 220.0
    wiring_layers__consolidated__001_1.nodes["Group.002"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Frame.002"].width  = 278.0
    wiring_layers__consolidated__001_1.nodes["Frame.002"].height = 440.8000183105469

    wiring_layers__consolidated__001_1.nodes["Reroute.004"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.004"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Reroute.005"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.005"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.002"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute.002"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Frame.003"].width  = 318.0
    wiring_layers__consolidated__001_1.nodes["Frame.003"].height = 460.79998779296875

    wiring_layers__consolidated__001_1.nodes["Join Geometry.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Join Geometry.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Merge by Distance.002"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Merge by Distance.002"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Named Attribute"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Named Attribute"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Sample Nearest"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Sample Nearest"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Separate Geometry"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Separate Geometry"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Sample Index"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Sample Index"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Index"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Index"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Position"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Position"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Viewer"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Viewer"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Frame.004"].width  = 1358.0
    wiring_layers__consolidated__001_1.nodes["Frame.004"].height = 661.4666748046875

    wiring_layers__consolidated__001_1.nodes["Named Attribute.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Named Attribute.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Sample Index.001"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Sample Index.001"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Named Attribute.002"].width  = 140.0
    wiring_layers__consolidated__001_1.nodes["Named Attribute.002"].height = 100.0

    wiring_layers__consolidated__001_1.nodes["Reroute.006"].width  = 14.5
    wiring_layers__consolidated__001_1.nodes["Reroute.006"].height = 100.0


    # Initialize wiring_layers__consolidated__001_1 links

    # reroute.Output -> extrude_mesh_002.Offset Scale
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].inputs[3]
    )
    # triangulate.Mesh -> extrude_mesh_001.Mesh
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Triangulate"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].inputs[0]
    )
    # group_input.Base Offset -> extrude_mesh_001.Offset Scale
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[4],
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].inputs[3]
    )
    # extrude_mesh_001.Mesh -> delete_geometry.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Delete Geometry"].inputs[0]
    )
    # extrude_mesh_001.Side -> delete_geometry.Selection
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].outputs[2],
        wiring_layers__consolidated__001_1.nodes["Delete Geometry"].inputs[1]
    )
    # extrude_mesh_002.Mesh -> delete_geometry_001.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.001"].inputs[0]
    )
    # extrude_mesh_002.Side -> delete_geometry_001.Selection
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].outputs[2],
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.001"].inputs[1]
    )
    # group_input.Thickness -> reroute.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[5],
        wiring_layers__consolidated__001_1.nodes["Reroute"].inputs[0]
    )
    # merge_by_distance.Geometry -> delete_geometry_003.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Merge by Distance"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.003"].inputs[0]
    )
    # group_input.Routing Self Margin -> reroute_001.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[7],
        wiring_layers__consolidated__001_1.nodes["Reroute.001"].inputs[0]
    )
    # delete_geometry.Geometry -> delete_geometry_004.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Delete Geometry"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.004"].inputs[0]
    )
    # extrude_mesh_001.Side -> delete_geometry_004.Selection
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.001"].outputs[2],
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.004"].inputs[1]
    )
    # group_input.Routing Cutout -> triangulate.Mesh
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Triangulate"].inputs[0]
    )
    # group_001.Geometry -> group.Connecting Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group"].inputs[2]
    )
    # delete_geometry_003.Geometry -> reroute_018.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.003"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Reroute.018"].inputs[0]
    )
    # reroute_018.Output -> group_001.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.018"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group.001"].inputs[1]
    )
    # reroute_018.Output -> group_001.Connecting Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.018"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group.001"].inputs[2]
    )
    # group_input.Connector Endpoint Margin -> reroute_019.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[6],
        wiring_layers__consolidated__001_1.nodes["Reroute.019"].inputs[0]
    )
    # reroute_001.Output -> group_001.Connection Factor
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group.001"].inputs[0]
    )
    # reroute_019.Output -> group.Connection Factor
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.019"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group"].inputs[0]
    )
    # group_001.Geometry -> join_geometry.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Join Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> merge_by_distance_001.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Join Geometry"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Merge by Distance.001"].inputs[0]
    )
    # delete_geometry_004.Geometry -> repeat_input.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.004"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Repeat Input"].inputs[1]
    )
    # repeat_input.Geometry -> extrude_mesh_002.Mesh
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Repeat Input"].outputs[1],
        wiring_layers__consolidated__001_1.nodes["Extrude Mesh.002"].inputs[0]
    )
    # delete_geometry_001.Geometry -> join_geometry_003.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Delete Geometry.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Join Geometry.003"].inputs[0]
    )
    # join_geometry_003.Geometry -> repeat_output.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Join Geometry.003"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Repeat Output"].inputs[0]
    )
    # repeat_output.Geometry -> merge_by_distance.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Repeat Output"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Merge by Distance"].inputs[0]
    )
    # reroute_003.Output -> repeat_input.Iterations
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.003"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Repeat Input"].inputs[0]
    )
    # math_001.Value -> reroute_003.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Math.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Reroute.003"].inputs[0]
    )
    # group_input.Layers -> math_001.Value
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[3],
        wiring_layers__consolidated__001_1.nodes["Math.001"].inputs[0]
    )
    # reroute_005.Output -> group.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.005"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group"].inputs[1]
    )
    # group_input.Endpoints Set 1 -> reroute_002.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[1],
        wiring_layers__consolidated__001_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_004.Output -> group_002.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.004"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group.002"].inputs[1]
    )
    # group_input.Endpoints Set 2 -> reroute_004.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[2],
        wiring_layers__consolidated__001_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_004.Output -> store_named_attribute_001.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.004"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # group_001.Geometry -> group_002.Connecting Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Group.002"].inputs[2]
    )
    # reroute_002.Output -> reroute_005.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.002"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_005.Output -> store_named_attribute_002.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.005"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # merge_by_distance_001.Geometry -> join_geometry_001.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Merge by Distance.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Join Geometry.001"].inputs[0]
    )
    # join_geometry_001.Geometry -> merge_by_distance_002.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Join Geometry.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Merge by Distance.002"].inputs[0]
    )
    # group_input.Sensor Endpoint Margin -> group_002.Connection Factor
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group Input"].outputs[8],
        wiring_layers__consolidated__001_1.nodes["Group.002"].inputs[0]
    )
    # named_attribute.Attribute -> store_named_attribute.Selection
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Named Attribute"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].inputs[1]
    )
    # merge_by_distance_002.Geometry -> separate_geometry.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Merge by Distance.002"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Separate Geometry"].inputs[0]
    )
    # merge_by_distance_002.Geometry -> store_named_attribute.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Merge by Distance.002"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].inputs[0]
    )
    # store_named_attribute.Geometry -> routing_layers.Routing Layers
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Routing Layers"].inputs[0]
    )
    # named_attribute.Attribute -> separate_geometry.Selection
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Named Attribute"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Separate Geometry"].inputs[1]
    )
    # index.Index -> sample_index.Index
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Index"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Index"].inputs[2]
    )
    # position.Position -> sample_index.Value
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Position"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Index"].inputs[1]
    )
    # sample_index.Value -> sample_nearest.Sample Position
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Sample Index"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Nearest"].inputs[1]
    )
    # store_named_attribute.Geometry -> viewer.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Viewer"].inputs[0]
    )
    # named_attribute_001.Attribute -> viewer.Attribute
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Named Attribute.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Viewer"].inputs[1]
    )
    # separate_geometry.Selection -> sample_index.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Separate Geometry"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Index"].inputs[0]
    )
    # reroute_006.Output -> sample_nearest.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.006"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Nearest"].inputs[0]
    )
    # sample_nearest.Index -> sample_index_001.Index
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Sample Nearest"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Index.001"].inputs[2]
    )
    # named_attribute_002.Attribute -> sample_index_001.Value
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Named Attribute.002"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Index.001"].inputs[1]
    )
    # store_named_attribute_001.Geometry -> reroute_006.Input
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_006.Output -> sample_index_001.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Reroute.006"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Sample Index.001"].inputs[0]
    )
    # sample_index_001.Value -> store_named_attribute.Value
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Sample Index.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute"].inputs[3]
    )
    # group.Geometry -> join_geometry.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Join Geometry"].inputs[0]
    )
    # repeat_input.Geometry -> join_geometry_003.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Repeat Input"].outputs[1],
        wiring_layers__consolidated__001_1.nodes["Join Geometry.003"].inputs[0]
    )
    # store_named_attribute_002.Geometry -> join_geometry_001.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute.002"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Join Geometry.001"].inputs[0]
    )
    # group_002.Geometry -> join_geometry.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Group.002"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Join Geometry"].inputs[0]
    )
    # store_named_attribute_001.Geometry -> join_geometry_001.Geometry
    wiring_layers__consolidated__001_1.links.new(
        wiring_layers__consolidated__001_1.nodes["Store Named Attribute.001"].outputs[0],
        wiring_layers__consolidated__001_1.nodes["Join Geometry.001"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True
    viewer.viewer_items[1].auto_remove = True

    return wiring_layers__consolidated__001_1


def generate_wires_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Generate Wires.001 node group"""
    generate_wires_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Generate Wires.001")

    generate_wires_001_1.color_tag = 'NONE'
    generate_wires_001_1.description = ""
    generate_wires_001_1.default_group_node_width = 140
    generate_wires_001_1.show_modifier_manage_panel = True

    # generate_wires_001_1 interface

    # Socket Wires
    wires_socket = generate_wires_001_1.interface.new_socket(name="Wires", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    wires_socket.attribute_domain = 'POINT'
    wires_socket.default_input = 'VALUE'
    wires_socket.structure_type = 'AUTO'

    # Socket Wire Curves
    wire_curves_socket = generate_wires_001_1.interface.new_socket(name="Wire Curves", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    wire_curves_socket.attribute_domain = 'POINT'
    wire_curves_socket.default_input = 'VALUE'
    wire_curves_socket.structure_type = 'AUTO'

    # Socket Routing Layers
    routing_layers_socket = generate_wires_001_1.interface.new_socket(name="Routing Layers", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    routing_layers_socket.attribute_domain = 'POINT'
    routing_layers_socket.default_input = 'VALUE'
    routing_layers_socket.structure_type = 'AUTO'

    # Socket Material
    material_socket = generate_wires_001_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'
    material_socket.optional_label = True

    # Panel Routing
    routing_panel = generate_wires_001_1.interface.new_panel("Routing")
    # Socket Routing Cutout
    routing_cutout_socket = generate_wires_001_1.interface.new_socket(name="Routing Cutout", in_out='INPUT', socket_type='NodeSocketGeometry', parent = routing_panel)
    routing_cutout_socket.attribute_domain = 'POINT'
    routing_cutout_socket.default_input = 'VALUE'
    routing_cutout_socket.structure_type = 'AUTO'

    # Socket Clip Points
    clip_points_socket = generate_wires_001_1.interface.new_socket(name="Clip Points", in_out='INPUT', socket_type='NodeSocketGeometry', parent = routing_panel)
    clip_points_socket.attribute_domain = 'POINT'
    clip_points_socket.default_input = 'VALUE'
    clip_points_socket.structure_type = 'AUTO'

    # Socket Electrode Points
    electrode_points_socket = generate_wires_001_1.interface.new_socket(name="Electrode Points", in_out='INPUT', socket_type='NodeSocketGeometry', parent = routing_panel)
    electrode_points_socket.attribute_domain = 'POINT'
    electrode_points_socket.default_input = 'VALUE'
    electrode_points_socket.structure_type = 'AUTO'

    # Socket Layers
    layers_socket = generate_wires_001_1.interface.new_socket(name="Layers", in_out='INPUT', socket_type='NodeSocketInt', parent = routing_panel)
    layers_socket.default_value = 4
    layers_socket.min_value = 0
    layers_socket.max_value = 2147483647
    layers_socket.subtype = 'NONE'
    layers_socket.attribute_domain = 'POINT'
    layers_socket.default_input = 'VALUE'
    layers_socket.structure_type = 'AUTO'

    # Socket Base Offset
    base_offset_socket = generate_wires_001_1.interface.new_socket(name="Base Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_panel)
    base_offset_socket.default_value = 1.0
    base_offset_socket.min_value = -3.4028234663852886e+38
    base_offset_socket.max_value = 3.4028234663852886e+38
    base_offset_socket.subtype = 'NONE'
    base_offset_socket.attribute_domain = 'POINT'
    base_offset_socket.default_input = 'VALUE'
    base_offset_socket.structure_type = 'AUTO'

    # Socket Thickness
    thickness_socket = generate_wires_001_1.interface.new_socket(name="Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_panel)
    thickness_socket.default_value = 0.1000000536441803
    thickness_socket.min_value = -3.4028234663852886e+38
    thickness_socket.max_value = 3.4028234663852886e+38
    thickness_socket.subtype = 'NONE'
    thickness_socket.attribute_domain = 'POINT'
    thickness_socket.default_input = 'VALUE'
    thickness_socket.structure_type = 'AUTO'

    # Socket Sensor Endpoint Margin
    sensor_endpoint_margin_socket = generate_wires_001_1.interface.new_socket(name="Sensor Endpoint Margin", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_panel)
    sensor_endpoint_margin_socket.default_value = 0.019999999552965164
    sensor_endpoint_margin_socket.min_value = -10000.0
    sensor_endpoint_margin_socket.max_value = 10000.0
    sensor_endpoint_margin_socket.subtype = 'NONE'
    sensor_endpoint_margin_socket.attribute_domain = 'POINT'
    sensor_endpoint_margin_socket.default_input = 'VALUE'
    sensor_endpoint_margin_socket.structure_type = 'AUTO'

    # Socket Connector Endpoint Margin
    connector_endpoint_margin_socket = generate_wires_001_1.interface.new_socket(name="Connector Endpoint Margin", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_panel)
    connector_endpoint_margin_socket.default_value = 0.004999999888241291
    connector_endpoint_margin_socket.min_value = -10000.0
    connector_endpoint_margin_socket.max_value = 10000.0
    connector_endpoint_margin_socket.subtype = 'NONE'
    connector_endpoint_margin_socket.attribute_domain = 'POINT'
    connector_endpoint_margin_socket.default_input = 'VALUE'
    connector_endpoint_margin_socket.structure_type = 'AUTO'

    # Socket Routing Self Margin
    routing_self_margin_socket = generate_wires_001_1.interface.new_socket(name="Routing Self Margin", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_panel)
    routing_self_margin_socket.default_value = 0.029999999329447746
    routing_self_margin_socket.min_value = -10000.0
    routing_self_margin_socket.max_value = 10000.0
    routing_self_margin_socket.subtype = 'NONE'
    routing_self_margin_socket.attribute_domain = 'POINT'
    routing_self_margin_socket.default_input = 'VALUE'
    routing_self_margin_socket.structure_type = 'AUTO'


    # Panel Wire Generation
    wire_generation_panel = generate_wires_001_1.interface.new_panel("Wire Generation")
    # Socket Use Alignment Vector Sorting
    use_alignment_vector_sorting_socket = generate_wires_001_1.interface.new_socket(name="Use Alignment Vector Sorting", in_out='INPUT', socket_type='NodeSocketBool', parent = wire_generation_panel)
    use_alignment_vector_sorting_socket.default_value = False
    use_alignment_vector_sorting_socket.attribute_domain = 'POINT'
    use_alignment_vector_sorting_socket.description = "Will find the closest electrode if false"
    use_alignment_vector_sorting_socket.default_input = 'VALUE'
    use_alignment_vector_sorting_socket.structure_type = 'AUTO'

    # Socket Radius
    radius_socket = generate_wires_001_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = wire_generation_panel)
    radius_socket.default_value = 1.0
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    # Socket Crosstalk Power
    crosstalk_power_socket = generate_wires_001_1.interface.new_socket(name="Crosstalk Power", in_out='INPUT', socket_type='NodeSocketFloat', parent = wire_generation_panel)
    crosstalk_power_socket.default_value = 0.5
    crosstalk_power_socket.min_value = 0.0
    crosstalk_power_socket.max_value = 10000.0
    crosstalk_power_socket.subtype = 'NONE'
    crosstalk_power_socket.attribute_domain = 'POINT'
    crosstalk_power_socket.default_input = 'VALUE'
    crosstalk_power_socket.structure_type = 'AUTO'

    # Socket Crosstalk Factor
    crosstalk_factor_socket = generate_wires_001_1.interface.new_socket(name="Crosstalk Factor", in_out='INPUT', socket_type='NodeSocketFloat', parent = wire_generation_panel)
    crosstalk_factor_socket.default_value = 0.0
    crosstalk_factor_socket.min_value = 0.0
    crosstalk_factor_socket.max_value = 1.0
    crosstalk_factor_socket.subtype = 'FACTOR'
    crosstalk_factor_socket.attribute_domain = 'POINT'
    crosstalk_factor_socket.default_input = 'VALUE'
    crosstalk_factor_socket.structure_type = 'AUTO'

    # Socket Electrode Sorting Vector
    electrode_sorting_vector_socket = generate_wires_001_1.interface.new_socket(name="Electrode Sorting Vector", in_out='INPUT', socket_type='NodeSocketVector', parent = wire_generation_panel)
    electrode_sorting_vector_socket.default_value = (0.0, 0.0, 0.0)
    electrode_sorting_vector_socket.min_value = -10000.0
    electrode_sorting_vector_socket.max_value = 10000.0
    electrode_sorting_vector_socket.subtype = 'NONE'
    electrode_sorting_vector_socket.attribute_domain = 'POINT'
    electrode_sorting_vector_socket.default_input = 'VALUE'
    electrode_sorting_vector_socket.structure_type = 'AUTO'

    # Socket Clip Sorting Vector
    clip_sorting_vector_socket = generate_wires_001_1.interface.new_socket(name="Clip Sorting Vector", in_out='INPUT', socket_type='NodeSocketVector', parent = wire_generation_panel)
    clip_sorting_vector_socket.default_value = (0.0, 0.0, 0.0)
    clip_sorting_vector_socket.min_value = -10000.0
    clip_sorting_vector_socket.max_value = 10000.0
    clip_sorting_vector_socket.subtype = 'NONE'
    clip_sorting_vector_socket.attribute_domain = 'POINT'
    clip_sorting_vector_socket.default_input = 'VALUE'
    clip_sorting_vector_socket.structure_type = 'AUTO'

    # Socket Avoid Distance
    avoid_distance_socket = generate_wires_001_1.interface.new_socket(name="Avoid Distance", in_out='INPUT', socket_type='NodeSocketFloat', parent = wire_generation_panel)
    avoid_distance_socket.default_value = 0.019999999552965164
    avoid_distance_socket.min_value = -10000.0
    avoid_distance_socket.max_value = 10000.0
    avoid_distance_socket.subtype = 'NONE'
    avoid_distance_socket.attribute_domain = 'POINT'
    avoid_distance_socket.default_input = 'VALUE'
    avoid_distance_socket.structure_type = 'AUTO'

    # Socket Route Removal Multiplier
    route_removal_multiplier_socket = generate_wires_001_1.interface.new_socket(name="Route Removal Multiplier", in_out='INPUT', socket_type='NodeSocketFloat', parent = wire_generation_panel)
    route_removal_multiplier_socket.default_value = 2.0
    route_removal_multiplier_socket.min_value = -10000.0
    route_removal_multiplier_socket.max_value = 10000.0
    route_removal_multiplier_socket.subtype = 'NONE'
    route_removal_multiplier_socket.attribute_domain = 'POINT'
    route_removal_multiplier_socket.default_input = 'VALUE'
    route_removal_multiplier_socket.structure_type = 'AUTO'

    # Socket Overlap Accuracy
    overlap_accuracy_socket = generate_wires_001_1.interface.new_socket(name="Overlap Accuracy", in_out='INPUT', socket_type='NodeSocketInt', parent = wire_generation_panel)
    overlap_accuracy_socket.default_value = 4
    overlap_accuracy_socket.min_value = 0
    overlap_accuracy_socket.max_value = 10000
    overlap_accuracy_socket.subtype = 'NONE'
    overlap_accuracy_socket.attribute_domain = 'POINT'
    overlap_accuracy_socket.default_input = 'VALUE'
    overlap_accuracy_socket.structure_type = 'AUTO'

    # Socket Sampling
    sampling_socket = generate_wires_001_1.interface.new_socket(name="Sampling", in_out='INPUT', socket_type='NodeSocketInt', parent = wire_generation_panel)
    sampling_socket.default_value = 15
    sampling_socket.min_value = 1
    sampling_socket.max_value = 100000
    sampling_socket.subtype = 'NONE'
    sampling_socket.attribute_domain = 'POINT'
    sampling_socket.default_input = 'VALUE'
    sampling_socket.structure_type = 'AUTO'


    # Initialize generate_wires_001_1 nodes

    # Node Group Output
    group_output = generate_wires_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = generate_wires_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group.008
    group_008 = generate_wires_001_1.nodes.new("GeometryNodeGroup")
    group_008.name = "Group.008"
    group_008.show_options = True
    group_008.node_tree = bpy.data.node_groups[node_tree_names[wire_profile_001_1_node_group]]
    # Socket_4
    group_008.inputs[3].default_value = True

    # Node Group.010
    group_010 = generate_wires_001_1.nodes.new("GeometryNodeGroup")
    group_010.name = "Group.010"
    group_010.show_options = True
    group_010.node_tree = bpy.data.node_groups[node_tree_names[non_overlapping_wires__order_by_vector__distance__001_1_node_group]]

    # Node Group.004
    group_004 = generate_wires_001_1.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.show_options = True
    group_004.node_tree = bpy.data.node_groups[node_tree_names[wiring_layers__consolidated__001_1_node_group]]

    # Node Reroute
    reroute = generate_wires_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloatDistance"
    # Node Viewer
    viewer = generate_wires_001_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'POINT'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Electrode Points")
    viewer.viewer_items.new('FLOAT', "Value")

    # Node For Each Geometry Element Input
    for_each_geometry_element_input = generate_wires_001_1.nodes.new("GeometryNodeForeachGeometryElementInput")
    for_each_geometry_element_input.name = "For Each Geometry Element Input"
    for_each_geometry_element_input.show_options = True
    # Node For Each Geometry Element Output
    for_each_geometry_element_output = generate_wires_001_1.nodes.new("GeometryNodeForeachGeometryElementOutput")
    for_each_geometry_element_output.name = "For Each Geometry Element Output"
    for_each_geometry_element_output.show_options = True
    for_each_geometry_element_output.active_generation_index = 0
    for_each_geometry_element_output.active_input_index = 0
    for_each_geometry_element_output.active_main_index = 0
    for_each_geometry_element_output.domain = 'CURVE'
    for_each_geometry_element_output.generation_items.clear()
    for_each_geometry_element_output.generation_items.new('GEOMETRY', "Geometry")
    for_each_geometry_element_output.generation_items[0].domain = 'POINT'
    for_each_geometry_element_output.input_items.clear()
    for_each_geometry_element_output.inspection_index = 0
    for_each_geometry_element_output.main_items.clear()

    # Node Store Named Attribute
    store_named_attribute = generate_wires_001_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT'
    store_named_attribute.domain = 'CURVE'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "length"

    # Node Curve Length
    curve_length = generate_wires_001_1.nodes.new("GeometryNodeCurveLength")
    curve_length.name = "Curve Length"
    curve_length.show_options = True

    # Node Index
    index = generate_wires_001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Evaluate on Domain
    evaluate_on_domain = generate_wires_001_1.nodes.new("GeometryNodeFieldOnDomain")
    evaluate_on_domain.name = "Evaluate on Domain"
    evaluate_on_domain.show_options = True
    evaluate_on_domain.data_type = 'BOOLEAN'
    evaluate_on_domain.domain = 'POINT'
    # Value
    evaluate_on_domain.inputs[0].default_value = False

    # Node Named Attribute
    named_attribute = generate_wires_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'INT'
    # Name
    named_attribute.inputs[0].default_value = "sensor_idx"

    # Process zone input For Each Geometry Element Input
    for_each_geometry_element_input.pair_with_output(for_each_geometry_element_output)
    # Selection
    for_each_geometry_element_input.inputs[1].default_value = True



    # Set locations
    generate_wires_001_1.nodes["Group Output"].location = (1420.0, 260.0)
    generate_wires_001_1.nodes["Group Input"].location = (-2020.0, 260.0)
    generate_wires_001_1.nodes["Group.008"].location = (-120.0, 860.0)
    generate_wires_001_1.nodes["Group.010"].location = (-500.0, 660.0)
    generate_wires_001_1.nodes["Group.004"].location = (-800.0, 300.0)
    generate_wires_001_1.nodes["Reroute"].location = (-729.9616088867188, 619.4212036132812)
    generate_wires_001_1.nodes["Viewer"].location = (-1720.0, 440.0)
    generate_wires_001_1.nodes["For Each Geometry Element Input"].location = (908.5181274414062, 786.0928344726562)
    generate_wires_001_1.nodes["For Each Geometry Element Output"].location = (1764.8670654296875, 772.8311767578125)
    generate_wires_001_1.nodes["Store Named Attribute"].location = (1355.165771484375, 802.2455444335938)
    generate_wires_001_1.nodes["Curve Length"].location = (1145.4307861328125, 577.9026489257812)
    generate_wires_001_1.nodes["Index"].location = (2076.90478515625, 674.1001586914062)
    generate_wires_001_1.nodes["Evaluate on Domain"].location = (60.0, 780.0)
    generate_wires_001_1.nodes["Named Attribute"].location = (-2020.0, 420.0)

    # Set dimensions
    generate_wires_001_1.nodes["Group Output"].width  = 140.0
    generate_wires_001_1.nodes["Group Output"].height = 100.0

    generate_wires_001_1.nodes["Group Input"].width  = 140.0
    generate_wires_001_1.nodes["Group Input"].height = 100.0

    generate_wires_001_1.nodes["Group.008"].width  = 140.0
    generate_wires_001_1.nodes["Group.008"].height = 100.0

    generate_wires_001_1.nodes["Group.010"].width  = 320.0
    generate_wires_001_1.nodes["Group.010"].height = 100.0

    generate_wires_001_1.nodes["Group.004"].width  = 212.0716552734375
    generate_wires_001_1.nodes["Group.004"].height = 100.0

    generate_wires_001_1.nodes["Reroute"].width  = 14.5
    generate_wires_001_1.nodes["Reroute"].height = 100.0

    generate_wires_001_1.nodes["Viewer"].width  = 140.0
    generate_wires_001_1.nodes["Viewer"].height = 100.0

    generate_wires_001_1.nodes["For Each Geometry Element Input"].width  = 140.0
    generate_wires_001_1.nodes["For Each Geometry Element Input"].height = 100.0

    generate_wires_001_1.nodes["For Each Geometry Element Output"].width  = 140.0
    generate_wires_001_1.nodes["For Each Geometry Element Output"].height = 100.0

    generate_wires_001_1.nodes["Store Named Attribute"].width  = 140.0
    generate_wires_001_1.nodes["Store Named Attribute"].height = 100.0

    generate_wires_001_1.nodes["Curve Length"].width  = 140.0
    generate_wires_001_1.nodes["Curve Length"].height = 100.0

    generate_wires_001_1.nodes["Index"].width  = 140.0
    generate_wires_001_1.nodes["Index"].height = 100.0

    generate_wires_001_1.nodes["Evaluate on Domain"].width  = 140.0
    generate_wires_001_1.nodes["Evaluate on Domain"].height = 100.0

    generate_wires_001_1.nodes["Named Attribute"].width  = 140.0
    generate_wires_001_1.nodes["Named Attribute"].height = 100.0


    # Initialize generate_wires_001_1 links

    # group_004.Routing Layers -> group_010.Routing
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group.004"].outputs[0],
        generate_wires_001_1.nodes["Group.010"].inputs[0]
    )
    # group_010.Wire Curves -> group_008.Curve
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group.010"].outputs[0],
        generate_wires_001_1.nodes["Group.008"].inputs[0]
    )
    # group_input.Sampling -> group_008.Sampling
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[19],
        generate_wires_001_1.nodes["Group.008"].inputs[2]
    )
    # group_input.Crosstalk Factor -> group_010.Crosstalk Factor
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[13],
        generate_wires_001_1.nodes["Group.010"].inputs[3]
    )
    # group_input.Overlap Accuracy -> group_010.Overlap Accuracy
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[18],
        generate_wires_001_1.nodes["Group.010"].inputs[7]
    )
    # group_input.Thickness -> group_004.Thickness
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[6],
        generate_wires_001_1.nodes["Group.004"].inputs[5]
    )
    # group_input.Crosstalk Power -> group_010.Crosstalk Power
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[12],
        generate_wires_001_1.nodes["Group.010"].inputs[2]
    )
    # group_input.Electrode Sorting Vector -> group_010.Alignment Vector
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[14],
        generate_wires_001_1.nodes["Group.010"].inputs[4]
    )
    # group_input.Use Alignment Vector Sorting -> group_010.Use Alignment Vector Sorting
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[10],
        generate_wires_001_1.nodes["Group.010"].inputs[6]
    )
    # reroute.Output -> group_008.Radius
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Reroute"].outputs[0],
        generate_wires_001_1.nodes["Group.008"].inputs[1]
    )
    # group_input.Base Offset -> group_004.Base Offset
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[5],
        generate_wires_001_1.nodes["Group.004"].inputs[4]
    )
    # group_input.Routing Cutout -> group_004.Routing Cutout
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[1],
        generate_wires_001_1.nodes["Group.004"].inputs[0]
    )
    # group_input.Avoid Distance -> group_010.Avoid Distance
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[16],
        generate_wires_001_1.nodes["Group.010"].inputs[5]
    )
    # group_input.Layers -> group_004.Layers
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[4],
        generate_wires_001_1.nodes["Group.004"].inputs[3]
    )
    # group_input.Electrode Points -> group_004.Endpoints Set 2
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[3],
        generate_wires_001_1.nodes["Group.004"].inputs[2]
    )
    # group_004.Routing Layers -> group_output.Routing Layers
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group.004"].outputs[0],
        generate_wires_001_1.nodes["Group Output"].inputs[2]
    )
    # group_input.Radius -> reroute.Input
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[11],
        generate_wires_001_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> group_010.Wire Thickness
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Reroute"].outputs[0],
        generate_wires_001_1.nodes["Group.010"].inputs[1]
    )
    # group_input.Route Removal Multiplier -> group_010.Route Removal Multiplier
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[17],
        generate_wires_001_1.nodes["Group.010"].inputs[8]
    )
    # group_010.Wire Curves -> for_each_geometry_element_input.Geometry
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group.010"].outputs[0],
        generate_wires_001_1.nodes["For Each Geometry Element Input"].inputs[0]
    )
    # for_each_geometry_element_input.Element -> curve_length.Curve
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["For Each Geometry Element Input"].outputs[1],
        generate_wires_001_1.nodes["Curve Length"].inputs[0]
    )
    # curve_length.Length -> store_named_attribute.Value
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Curve Length"].outputs[0],
        generate_wires_001_1.nodes["Store Named Attribute"].inputs[3]
    )
    # for_each_geometry_element_input.Element -> store_named_attribute.Geometry
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["For Each Geometry Element Input"].outputs[1],
        generate_wires_001_1.nodes["Store Named Attribute"].inputs[0]
    )
    # store_named_attribute.Geometry -> for_each_geometry_element_output.Geometry
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Store Named Attribute"].outputs[0],
        generate_wires_001_1.nodes["For Each Geometry Element Output"].inputs[1]
    )
    # group_input.Clip Points -> group_004.Endpoints Set 1
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[2],
        generate_wires_001_1.nodes["Group.004"].inputs[1]
    )
    # group_input.Material -> group_008.Material
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[0],
        generate_wires_001_1.nodes["Group.008"].inputs[4]
    )
    # group_input.Sensor Endpoint Margin -> group_004.Sensor Endpoint Margin
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[7],
        generate_wires_001_1.nodes["Group.004"].inputs[8]
    )
    # group_input.Routing Self Margin -> group_004.Routing Self Margin
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[9],
        generate_wires_001_1.nodes["Group.004"].inputs[7]
    )
    # group_input.Connector Endpoint Margin -> group_004.Connector Endpoint Margin
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[8],
        generate_wires_001_1.nodes["Group.004"].inputs[6]
    )
    # group_input.Electrode Points -> viewer.Electrode Points
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[3],
        generate_wires_001_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Clip Sorting Vector -> group_010.Vector
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group Input"].outputs[15],
        generate_wires_001_1.nodes["Group.010"].inputs[9]
    )
    # named_attribute.Attribute -> viewer.Value
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Named Attribute"].outputs[0],
        generate_wires_001_1.nodes["Viewer"].inputs[1]
    )
    # group_008.Wires -> group_output.Wires
    generate_wires_001_1.links.new(
        generate_wires_001_1.nodes["Group.008"].outputs[0],
        generate_wires_001_1.nodes["Group Output"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True
    viewer.viewer_items[1].auto_remove = False

    return generate_wires_001_1


def generate_clips_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Generate Clips.001 node group"""
    generate_clips_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Generate Clips.001")

    generate_clips_001_1.color_tag = 'NONE'
    generate_clips_001_1.description = ""
    generate_clips_001_1.default_group_node_width = 140
    generate_clips_001_1.show_modifier_manage_panel = True

    # generate_clips_001_1 interface

    # Socket Clips
    clips_socket = generate_clips_001_1.interface.new_socket(name="Clips", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    clips_socket.attribute_domain = 'POINT'
    clips_socket.default_input = 'VALUE'
    clips_socket.structure_type = 'AUTO'

    # Socket Clip Points
    clip_points_socket = generate_clips_001_1.interface.new_socket(name="Clip Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    clip_points_socket.attribute_domain = 'POINT'
    clip_points_socket.default_input = 'VALUE'
    clip_points_socket.structure_type = 'AUTO'

    # Socket Clip Reference
    clip_reference_socket = generate_clips_001_1.interface.new_socket(name="Clip Reference", in_out='INPUT', socket_type='NodeSocketObject')
    clip_reference_socket.attribute_domain = 'POINT'
    clip_reference_socket.default_input = 'VALUE'
    clip_reference_socket.structure_type = 'AUTO'

    # Socket Boundary Cutout
    boundary_cutout_socket = generate_clips_001_1.interface.new_socket(name="Boundary Cutout", in_out='INPUT', socket_type='NodeSocketGeometry')
    boundary_cutout_socket.attribute_domain = 'POINT'
    boundary_cutout_socket.default_input = 'VALUE'
    boundary_cutout_socket.structure_type = 'AUTO'

    # Socket Seperation
    seperation_socket = generate_clips_001_1.interface.new_socket(name="Seperation", in_out='INPUT', socket_type='NodeSocketFloat')
    seperation_socket.default_value = 0.10000002384185791
    seperation_socket.min_value = -10000.0
    seperation_socket.max_value = 10000.0
    seperation_socket.subtype = 'NONE'
    seperation_socket.attribute_domain = 'POINT'
    seperation_socket.default_input = 'VALUE'
    seperation_socket.structure_type = 'AUTO'

    # Socket Count
    count_socket = generate_clips_001_1.interface.new_socket(name="Count", in_out='INPUT', socket_type='NodeSocketInt')
    count_socket.default_value = 10
    count_socket.min_value = 2
    count_socket.max_value = 100000
    count_socket.subtype = 'NONE'
    count_socket.attribute_domain = 'POINT'
    count_socket.default_input = 'VALUE'
    count_socket.structure_type = 'AUTO'

    # Socket Depth
    depth_socket = generate_clips_001_1.interface.new_socket(name="Depth", in_out='INPUT', socket_type='NodeSocketFloat')
    depth_socket.default_value = 0.0
    depth_socket.min_value = -3.4028234663852886e+38
    depth_socket.max_value = 3.4028234663852886e+38
    depth_socket.subtype = 'DISTANCE'
    depth_socket.attribute_domain = 'POINT'
    depth_socket.default_input = 'VALUE'
    depth_socket.structure_type = 'AUTO'

    # Socket Radius
    radius_socket = generate_clips_001_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    radius_socket.default_value = 0.0010000000474974513
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    # Socket Rotation
    rotation_socket = generate_clips_001_1.interface.new_socket(name="Rotation", in_out='INPUT', socket_type='NodeSocketFloat')
    rotation_socket.default_value = 0.0
    rotation_socket.min_value = -3.4028234663852886e+38
    rotation_socket.max_value = 3.4028234663852886e+38
    rotation_socket.subtype = 'NONE'
    rotation_socket.attribute_domain = 'POINT'
    rotation_socket.default_input = 'VALUE'
    rotation_socket.structure_type = 'AUTO'

    # Socket Translattion
    translattion_socket = generate_clips_001_1.interface.new_socket(name="Translattion", in_out='INPUT', socket_type='NodeSocketVector')
    translattion_socket.default_value = (0.0, 0.0, 0.0)
    translattion_socket.min_value = -3.4028234663852886e+38
    translattion_socket.max_value = 3.4028234663852886e+38
    translattion_socket.subtype = 'TRANSLATION'
    translattion_socket.attribute_domain = 'POINT'
    translattion_socket.default_input = 'VALUE'
    translattion_socket.structure_type = 'AUTO'

    # Initialize generate_clips_001_1 nodes

    # Node Group Output
    group_output = generate_clips_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = generate_clips_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Sample Nearest
    sample_nearest = generate_clips_001_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Object Info
    object_info = generate_clips_001_1.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.show_options = True
    object_info.transform_space = 'RELATIVE'
    # As Instance
    object_info.inputs[1].default_value = False

    # Node Reroute.002
    reroute_002 = generate_clips_001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketObject"
    # Node Extrude Mesh
    extrude_mesh = generate_clips_001_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.show_options = True
    extrude_mesh.mode = 'FACES'
    # Selection
    extrude_mesh.inputs[1].default_value = True
    # Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset Scale
    extrude_mesh.inputs[3].default_value = 0.0
    # Individual
    extrude_mesh.inputs[4].default_value = False

    # Node Delete Geometry.005
    delete_geometry_005 = generate_clips_001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_005.name = "Delete Geometry.005"
    delete_geometry_005.show_options = True
    delete_geometry_005.domain = 'POINT'
    delete_geometry_005.mode = 'ALL'

    # Node Merge by Distance.002
    merge_by_distance_002 = generate_clips_001_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_002.name = "Merge by Distance.002"
    merge_by_distance_002.show_options = True
    # Selection
    merge_by_distance_002.inputs[1].default_value = True
    # Mode
    merge_by_distance_002.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance_002.inputs[3].default_value = 0.0010000000474974513

    # Node Sample Index.002
    sample_index_002 = generate_clips_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'

    # Node Position.002
    position_002 = generate_clips_001_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Edge Vertices
    edge_vertices = generate_clips_001_1.nodes.new("GeometryNodeInputMeshEdgeVertices")
    edge_vertices.name = "Edge Vertices"
    edge_vertices.show_options = True

    # Node Vector Math.001
    vector_math_001 = generate_clips_001_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'DISTANCE'

    # Node Compare.001
    compare_001 = generate_clips_001_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.show_options = True
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'GREATER_THAN'

    # Node Delete Geometry.006
    delete_geometry_006 = generate_clips_001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_006.name = "Delete Geometry.006"
    delete_geometry_006.show_options = True
    delete_geometry_006.domain = 'POINT'
    delete_geometry_006.mode = 'ALL'

    # Node Mesh to Curve
    mesh_to_curve = generate_clips_001_1.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.show_options = True
    mesh_to_curve.mode = 'EDGES'
    # Selection
    mesh_to_curve.inputs[1].default_value = True

    # Node Curve to Points
    curve_to_points = generate_clips_001_1.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points.name = "Curve to Points"
    curve_to_points.show_options = True
    curve_to_points.mode = 'COUNT'

    # Node Points to Vertices
    points_to_vertices = generate_clips_001_1.nodes.new("GeometryNodePointsToVertices")
    points_to_vertices.name = "Points to Vertices"
    points_to_vertices.show_options = True
    # Selection
    points_to_vertices.inputs[1].default_value = True

    # Node Frame.001
    frame_001 = generate_clips_001_1.nodes.new("NodeFrame")
    frame_001.label = "Create points for the clips"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.6079999804496765, 0.5649587512016296, 0.37342357635498047)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Instance on Points
    instance_on_points = generate_clips_001_1.nodes.new("GeometryNodeInstanceOnPoints")
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

    # Node Translate Instances
    translate_instances = generate_clips_001_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances.name = "Translate Instances"
    translate_instances.show_options = True
    # Selection
    translate_instances.inputs[1].default_value = True
    # Local Space
    translate_instances.inputs[3].default_value = True

    # Node Cylinder
    cylinder = generate_clips_001_1.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.show_options = True
    cylinder.fill_type = 'NGON'
    # Vertices
    cylinder.inputs[0].default_value = 32
    # Side Segments
    cylinder.inputs[1].default_value = 1
    # Fill Segments
    cylinder.inputs[2].default_value = 1

    # Node Rotate Rotation
    rotate_rotation = generate_clips_001_1.nodes.new("FunctionNodeRotateRotation")
    rotate_rotation.name = "Rotate Rotation"
    rotate_rotation.show_options = True
    rotate_rotation.rotation_space = 'LOCAL'

    # Node Combine XYZ
    combine_xyz = generate_clips_001_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # Node Math
    math = generate_clips_001_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'RADIANS'
    math.use_clamp = False
    # Value
    math.inputs[0].default_value = 90.0

    # Node Reroute.012
    reroute_012 = generate_clips_001_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketFloat"
    # Node Instances to Points
    instances_to_points = generate_clips_001_1.nodes.new("GeometryNodeInstancesToPoints")
    instances_to_points.name = "Instances to Points"
    instances_to_points.show_options = True
    # Selection
    instances_to_points.inputs[1].default_value = True
    # Position
    instances_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    instances_to_points.inputs[3].default_value = 0.05000000074505806

    # Node Reroute.013
    reroute_013 = generate_clips_001_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketGeometry"
    # Node Reroute.014
    reroute_014 = generate_clips_001_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    reroute_014.socket_idname = "NodeSocketGeometry"
    # Node Reroute.015
    reroute_015 = generate_clips_001_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketVectorTranslation"
    # Node Reroute.016
    reroute_016 = generate_clips_001_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    reroute_016.socket_idname = "NodeSocketVectorTranslation"
    # Node Translate Instances.001
    translate_instances_001 = generate_clips_001_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances_001.name = "Translate Instances.001"
    translate_instances_001.show_options = True
    # Selection
    translate_instances_001.inputs[1].default_value = True
    # Local Space
    translate_instances_001.inputs[3].default_value = True

    # Node Reroute.021
    reroute_021 = generate_clips_001_1.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.show_options = True
    reroute_021.socket_idname = "NodeSocketFloatDistance"
    # Node Math.002
    math_002 = generate_clips_001_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False
    # Value_001
    math_002.inputs[1].default_value = 2.5

    # Node Combine XYZ.001
    combine_xyz_001 = generate_clips_001_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.show_options = True
    # X
    combine_xyz_001.inputs[0].default_value = 0.0
    # Y
    combine_xyz_001.inputs[1].default_value = 0.0

    # Node Set Material
    set_material = generate_clips_001_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True
    if "Skin_Bound_Mat.001" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["Skin_Bound_Mat.001"]

    # Node Reroute
    reroute = generate_clips_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloatDistance"
    # Node Viewer
    viewer = generate_clips_001_1.nodes.new("GeometryNodeViewer")
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
    generate_clips_001_1.nodes["Sample Nearest"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Object Info"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute.002"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Extrude Mesh"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Delete Geometry.005"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Merge by Distance.002"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Sample Index.002"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Position.002"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Edge Vertices"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Vector Math.001"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Compare.001"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Delete Geometry.006"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Mesh to Curve"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Curve to Points"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Points to Vertices"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Instance on Points"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Translate Instances"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Cylinder"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Rotate Rotation"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Combine XYZ"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Math"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute.012"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Instances to Points"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute.013"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute.014"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute.015"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute.016"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute.021"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Math.002"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Combine XYZ.001"].parent = generate_clips_001_1.nodes["Frame.001"]
    generate_clips_001_1.nodes["Reroute"].parent = generate_clips_001_1.nodes["Frame.001"]

    # Set locations
    generate_clips_001_1.nodes["Group Output"].location = (4640.0, 900.0)
    generate_clips_001_1.nodes["Group Input"].location = (-340.0, 980.0)
    generate_clips_001_1.nodes["Sample Nearest"].location = (802.7615356445312, -618.8970947265625)
    generate_clips_001_1.nodes["Object Info"].location = (407.85028076171875, -654.1273193359375)
    generate_clips_001_1.nodes["Reroute.002"].location = (33.83332824707031, -835.800048828125)
    generate_clips_001_1.nodes["Extrude Mesh"].location = (243.4729766845703, -1005.1202392578125)
    generate_clips_001_1.nodes["Delete Geometry.005"].location = (411.58062744140625, -932.2386474609375)
    generate_clips_001_1.nodes["Merge by Distance.002"].location = (591.8323364257812, -950.6632080078125)
    generate_clips_001_1.nodes["Sample Index.002"].location = (1014.45556640625, -903.9041748046875)
    generate_clips_001_1.nodes["Position.002"].location = (810.0130004882812, -1036.2493896484375)
    generate_clips_001_1.nodes["Edge Vertices"].location = (1011.1171875, -761.3734130859375)
    generate_clips_001_1.nodes["Vector Math.001"].location = (1202.1029052734375, -810.7750244140625)
    generate_clips_001_1.nodes["Compare.001"].location = (1390.5592041015625, -798.4405517578125)
    generate_clips_001_1.nodes["Delete Geometry.006"].location = (1657.4332275390625, -868.1124267578125)
    generate_clips_001_1.nodes["Mesh to Curve"].location = (1833.8323974609375, -869.3856201171875)
    generate_clips_001_1.nodes["Curve to Points"].location = (2053.832275390625, -869.3856201171875)
    generate_clips_001_1.nodes["Points to Vertices"].location = (2413.83251953125, -1169.3856201171875)
    generate_clips_001_1.nodes["Frame.001"].location = (-218.8333282470703, 2155.800048828125)
    generate_clips_001_1.nodes["Instance on Points"].location = (3533.832275390625, -439.3856201171875)
    generate_clips_001_1.nodes["Translate Instances"].location = (3793.832275390625, -479.3856201171875)
    generate_clips_001_1.nodes["Cylinder"].location = (3333.833251953125, -215.800048828125)
    generate_clips_001_1.nodes["Rotate Rotation"].location = (3213.832275390625, -619.3856201171875)
    generate_clips_001_1.nodes["Combine XYZ"].location = (2773.832275390625, -939.3856201171875)
    generate_clips_001_1.nodes["Math"].location = (2573.832275390625, -899.3856201171875)
    generate_clips_001_1.nodes["Reroute.012"].location = (2613.832275390625, -1279.3856201171875)
    generate_clips_001_1.nodes["Instances to Points"].location = (2233.833251953125, -1115.800048828125)
    generate_clips_001_1.nodes["Reroute.013"].location = (4033.833251953125, -1055.800048828125)
    generate_clips_001_1.nodes["Reroute.014"].location = (2133.833251953125, -1095.800048828125)
    generate_clips_001_1.nodes["Reroute.015"].location = (3733.833251953125, -1155.800048828125)
    generate_clips_001_1.nodes["Reroute.016"].location = (2613.833251953125, -1315.800048828125)
    generate_clips_001_1.nodes["Translate Instances.001"].location = (3960.0, 1080.0)
    generate_clips_001_1.nodes["Reroute.021"].location = (3053.833251953125, -515.800048828125)
    generate_clips_001_1.nodes["Math.002"].location = (3198.833251953125, -35.800048828125)
    generate_clips_001_1.nodes["Combine XYZ.001"].location = (3798.833251953125, -295.800048828125)
    generate_clips_001_1.nodes["Set Material"].location = (4200.0, 1080.0)
    generate_clips_001_1.nodes["Reroute"].location = (3050.406494140625, -473.1048583984375)
    generate_clips_001_1.nodes["Viewer"].location = (2015.0, 1392.0)

    # Set dimensions
    generate_clips_001_1.nodes["Group Output"].width  = 140.0
    generate_clips_001_1.nodes["Group Output"].height = 100.0

    generate_clips_001_1.nodes["Group Input"].width  = 140.0
    generate_clips_001_1.nodes["Group Input"].height = 100.0

    generate_clips_001_1.nodes["Sample Nearest"].width  = 140.0
    generate_clips_001_1.nodes["Sample Nearest"].height = 100.0

    generate_clips_001_1.nodes["Object Info"].width  = 140.0
    generate_clips_001_1.nodes["Object Info"].height = 100.0

    generate_clips_001_1.nodes["Reroute.002"].width  = 14.5
    generate_clips_001_1.nodes["Reroute.002"].height = 100.0

    generate_clips_001_1.nodes["Extrude Mesh"].width  = 140.0
    generate_clips_001_1.nodes["Extrude Mesh"].height = 100.0

    generate_clips_001_1.nodes["Delete Geometry.005"].width  = 140.0
    generate_clips_001_1.nodes["Delete Geometry.005"].height = 100.0

    generate_clips_001_1.nodes["Merge by Distance.002"].width  = 140.0
    generate_clips_001_1.nodes["Merge by Distance.002"].height = 100.0

    generate_clips_001_1.nodes["Sample Index.002"].width  = 140.0
    generate_clips_001_1.nodes["Sample Index.002"].height = 100.0

    generate_clips_001_1.nodes["Position.002"].width  = 140.0
    generate_clips_001_1.nodes["Position.002"].height = 100.0

    generate_clips_001_1.nodes["Edge Vertices"].width  = 140.0
    generate_clips_001_1.nodes["Edge Vertices"].height = 100.0

    generate_clips_001_1.nodes["Vector Math.001"].width  = 140.0
    generate_clips_001_1.nodes["Vector Math.001"].height = 100.0

    generate_clips_001_1.nodes["Compare.001"].width  = 140.0
    generate_clips_001_1.nodes["Compare.001"].height = 100.0

    generate_clips_001_1.nodes["Delete Geometry.006"].width  = 140.0
    generate_clips_001_1.nodes["Delete Geometry.006"].height = 100.0

    generate_clips_001_1.nodes["Mesh to Curve"].width  = 140.0
    generate_clips_001_1.nodes["Mesh to Curve"].height = 100.0

    generate_clips_001_1.nodes["Curve to Points"].width  = 140.0
    generate_clips_001_1.nodes["Curve to Points"].height = 100.0

    generate_clips_001_1.nodes["Points to Vertices"].width  = 140.0
    generate_clips_001_1.nodes["Points to Vertices"].height = 100.0

    generate_clips_001_1.nodes["Frame.001"].width  = 4067.66650390625
    generate_clips_001_1.nodes["Frame.001"].height = 1349.63330078125

    generate_clips_001_1.nodes["Instance on Points"].width  = 140.0
    generate_clips_001_1.nodes["Instance on Points"].height = 100.0

    generate_clips_001_1.nodes["Translate Instances"].width  = 140.0
    generate_clips_001_1.nodes["Translate Instances"].height = 100.0

    generate_clips_001_1.nodes["Cylinder"].width  = 140.0
    generate_clips_001_1.nodes["Cylinder"].height = 100.0

    generate_clips_001_1.nodes["Rotate Rotation"].width  = 140.0
    generate_clips_001_1.nodes["Rotate Rotation"].height = 100.0

    generate_clips_001_1.nodes["Combine XYZ"].width  = 140.0
    generate_clips_001_1.nodes["Combine XYZ"].height = 100.0

    generate_clips_001_1.nodes["Math"].width  = 140.0
    generate_clips_001_1.nodes["Math"].height = 100.0

    generate_clips_001_1.nodes["Reroute.012"].width  = 14.5
    generate_clips_001_1.nodes["Reroute.012"].height = 100.0

    generate_clips_001_1.nodes["Instances to Points"].width  = 140.0
    generate_clips_001_1.nodes["Instances to Points"].height = 100.0

    generate_clips_001_1.nodes["Reroute.013"].width  = 14.5
    generate_clips_001_1.nodes["Reroute.013"].height = 100.0

    generate_clips_001_1.nodes["Reroute.014"].width  = 14.5
    generate_clips_001_1.nodes["Reroute.014"].height = 100.0

    generate_clips_001_1.nodes["Reroute.015"].width  = 14.5
    generate_clips_001_1.nodes["Reroute.015"].height = 100.0

    generate_clips_001_1.nodes["Reroute.016"].width  = 14.5
    generate_clips_001_1.nodes["Reroute.016"].height = 100.0

    generate_clips_001_1.nodes["Translate Instances.001"].width  = 140.0
    generate_clips_001_1.nodes["Translate Instances.001"].height = 100.0

    generate_clips_001_1.nodes["Reroute.021"].width  = 14.5
    generate_clips_001_1.nodes["Reroute.021"].height = 100.0

    generate_clips_001_1.nodes["Math.002"].width  = 140.0
    generate_clips_001_1.nodes["Math.002"].height = 100.0

    generate_clips_001_1.nodes["Combine XYZ.001"].width  = 140.0
    generate_clips_001_1.nodes["Combine XYZ.001"].height = 100.0

    generate_clips_001_1.nodes["Set Material"].width  = 140.0
    generate_clips_001_1.nodes["Set Material"].height = 100.0

    generate_clips_001_1.nodes["Reroute"].width  = 14.5
    generate_clips_001_1.nodes["Reroute"].height = 100.0

    generate_clips_001_1.nodes["Viewer"].width  = 140.0
    generate_clips_001_1.nodes["Viewer"].height = 100.0


    # Initialize generate_clips_001_1 links

    # reroute_014.Output -> instances_to_points.Instances
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.014"].outputs[0],
        generate_clips_001_1.nodes["Instances to Points"].inputs[0]
    )
    # edge_vertices.Position 1 -> vector_math_001.Vector
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Edge Vertices"].outputs[2],
        generate_clips_001_1.nodes["Vector Math.001"].inputs[0]
    )
    # translate_instances.Instances -> reroute_013.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Translate Instances"].outputs[0],
        generate_clips_001_1.nodes["Reroute.013"].inputs[0]
    )
    # sample_index_002.Value -> vector_math_001.Vector
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Sample Index.002"].outputs[0],
        generate_clips_001_1.nodes["Vector Math.001"].inputs[1]
    )
    # reroute_013.Output -> reroute_014.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.013"].outputs[0],
        generate_clips_001_1.nodes["Reroute.014"].inputs[0]
    )
    # vector_math_001.Value -> compare_001.A
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Vector Math.001"].outputs[1],
        generate_clips_001_1.nodes["Compare.001"].inputs[0]
    )
    # merge_by_distance_002.Geometry -> delete_geometry_006.Geometry
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Merge by Distance.002"].outputs[0],
        generate_clips_001_1.nodes["Delete Geometry.006"].inputs[0]
    )
    # reroute_015.Output -> translate_instances.Translation
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.015"].outputs[0],
        generate_clips_001_1.nodes["Translate Instances"].inputs[2]
    )
    # compare_001.Result -> delete_geometry_006.Selection
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Compare.001"].outputs[0],
        generate_clips_001_1.nodes["Delete Geometry.006"].inputs[1]
    )
    # translate_instances.Instances -> translate_instances_001.Instances
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Translate Instances"].outputs[0],
        generate_clips_001_1.nodes["Translate Instances.001"].inputs[0]
    )
    # reroute_016.Output -> reroute_015.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.016"].outputs[0],
        generate_clips_001_1.nodes["Reroute.015"].inputs[0]
    )
    # merge_by_distance_002.Geometry -> sample_index_002.Geometry
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Merge by Distance.002"].outputs[0],
        generate_clips_001_1.nodes["Sample Index.002"].inputs[0]
    )
    # delete_geometry_006.Geometry -> mesh_to_curve.Mesh
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Delete Geometry.006"].outputs[0],
        generate_clips_001_1.nodes["Mesh to Curve"].inputs[0]
    )
    # instance_on_points.Instances -> translate_instances.Instances
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Instance on Points"].outputs[0],
        generate_clips_001_1.nodes["Translate Instances"].inputs[0]
    )
    # object_info.Location -> sample_nearest.Sample Position
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Object Info"].outputs[1],
        generate_clips_001_1.nodes["Sample Nearest"].inputs[1]
    )
    # mesh_to_curve.Curve -> curve_to_points.Curve
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Mesh to Curve"].outputs[0],
        generate_clips_001_1.nodes["Curve to Points"].inputs[0]
    )
    # cylinder.Mesh -> instance_on_points.Instance
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Cylinder"].outputs[0],
        generate_clips_001_1.nodes["Instance on Points"].inputs[2]
    )
    # rotate_rotation.Rotation -> instance_on_points.Rotation
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Rotate Rotation"].outputs[0],
        generate_clips_001_1.nodes["Instance on Points"].inputs[5]
    )
    # instances_to_points.Points -> points_to_vertices.Points
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Instances to Points"].outputs[0],
        generate_clips_001_1.nodes["Points to Vertices"].inputs[0]
    )
    # extrude_mesh.Mesh -> delete_geometry_005.Geometry
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Extrude Mesh"].outputs[0],
        generate_clips_001_1.nodes["Delete Geometry.005"].inputs[0]
    )
    # curve_to_points.Points -> instance_on_points.Points
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Curve to Points"].outputs[0],
        generate_clips_001_1.nodes["Instance on Points"].inputs[0]
    )
    # extrude_mesh.Top -> delete_geometry_005.Selection
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Extrude Mesh"].outputs[1],
        generate_clips_001_1.nodes["Delete Geometry.005"].inputs[1]
    )
    # curve_to_points.Rotation -> rotate_rotation.Rotation
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Curve to Points"].outputs[3],
        generate_clips_001_1.nodes["Rotate Rotation"].inputs[0]
    )
    # reroute_021.Output -> math_002.Value
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.021"].outputs[0],
        generate_clips_001_1.nodes["Math.002"].inputs[0]
    )
    # delete_geometry_005.Geometry -> merge_by_distance_002.Geometry
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Delete Geometry.005"].outputs[0],
        generate_clips_001_1.nodes["Merge by Distance.002"].inputs[0]
    )
    # math_002.Value -> combine_xyz_001.Z
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Math.002"].outputs[0],
        generate_clips_001_1.nodes["Combine XYZ.001"].inputs[2]
    )
    # reroute_002.Output -> object_info.Object
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.002"].outputs[0],
        generate_clips_001_1.nodes["Object Info"].inputs[0]
    )
    # combine_xyz.Vector -> rotate_rotation.Rotate By
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Combine XYZ"].outputs[0],
        generate_clips_001_1.nodes["Rotate Rotation"].inputs[1]
    )
    # combine_xyz_001.Vector -> translate_instances_001.Translation
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Combine XYZ.001"].outputs[0],
        generate_clips_001_1.nodes["Translate Instances.001"].inputs[2]
    )
    # translate_instances_001.Instances -> set_material.Geometry
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Translate Instances.001"].outputs[0],
        generate_clips_001_1.nodes["Set Material"].inputs[0]
    )
    # math.Value -> combine_xyz.X
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Math"].outputs[0],
        generate_clips_001_1.nodes["Combine XYZ"].inputs[0]
    )
    # merge_by_distance_002.Geometry -> sample_nearest.Geometry
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Merge by Distance.002"].outputs[0],
        generate_clips_001_1.nodes["Sample Nearest"].inputs[0]
    )
    # reroute_021.Output -> cylinder.Depth
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.021"].outputs[0],
        generate_clips_001_1.nodes["Cylinder"].inputs[4]
    )
    # sample_nearest.Index -> sample_index_002.Index
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Sample Nearest"].outputs[0],
        generate_clips_001_1.nodes["Sample Index.002"].inputs[2]
    )
    # position_002.Position -> sample_index_002.Value
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Position.002"].outputs[0],
        generate_clips_001_1.nodes["Sample Index.002"].inputs[1]
    )
    # reroute_012.Output -> combine_xyz.Z
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute.012"].outputs[0],
        generate_clips_001_1.nodes["Combine XYZ"].inputs[2]
    )
    # group_input.Translattion -> reroute_016.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[7],
        generate_clips_001_1.nodes["Reroute.016"].inputs[0]
    )
    # group_input.Count -> curve_to_points.Count
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[3],
        generate_clips_001_1.nodes["Curve to Points"].inputs[1]
    )
    # group_input.Clip Reference -> reroute_002.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[0],
        generate_clips_001_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Depth -> reroute_021.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[4],
        generate_clips_001_1.nodes["Reroute.021"].inputs[0]
    )
    # reroute.Output -> cylinder.Radius
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Reroute"].outputs[0],
        generate_clips_001_1.nodes["Cylinder"].inputs[3]
    )
    # group_input.Seperation -> compare_001.B
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[2],
        generate_clips_001_1.nodes["Compare.001"].inputs[1]
    )
    # group_input.Rotation -> reroute_012.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[6],
        generate_clips_001_1.nodes["Reroute.012"].inputs[0]
    )
    # group_input.Boundary Cutout -> extrude_mesh.Mesh
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[1],
        generate_clips_001_1.nodes["Extrude Mesh"].inputs[0]
    )
    # group_input.Radius -> reroute.Input
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Group Input"].outputs[5],
        generate_clips_001_1.nodes["Reroute"].inputs[0]
    )
    # set_material.Geometry -> group_output.Clips
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Set Material"].outputs[0],
        generate_clips_001_1.nodes["Group Output"].inputs[0]
    )
    # points_to_vertices.Mesh -> group_output.Clip Points
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Points to Vertices"].outputs[0],
        generate_clips_001_1.nodes["Group Output"].inputs[1]
    )
    # curve_to_points.Points -> viewer.Geometry
    generate_clips_001_1.links.new(
        generate_clips_001_1.nodes["Curve to Points"].outputs[0],
        generate_clips_001_1.nodes["Viewer"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return generate_clips_001_1


def smooth_mesh_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Smooth Mesh.001 node group"""
    smooth_mesh_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Smooth Mesh.001")

    smooth_mesh_001_1.color_tag = 'NONE'
    smooth_mesh_001_1.description = ""
    smooth_mesh_001_1.default_group_node_width = 140
    smooth_mesh_001_1.show_modifier_manage_panel = True

    # smooth_mesh_001_1 interface

    # Socket Curve
    curve_socket = smooth_mesh_001_1.interface.new_socket(name="Curve", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    curve_socket.attribute_domain = 'POINT'
    curve_socket.default_input = 'VALUE'
    curve_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket = smooth_mesh_001_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Initialize smooth_mesh_001_1 nodes

    # Node Position
    position = smooth_mesh_001_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Set Position
    set_position = smooth_mesh_001_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Mix
    mix = smooth_mesh_001_1.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.show_options = True
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    # Factor_Float
    mix.inputs[0].default_value = 1.0

    # Node Capture Attribute
    capture_attribute = smooth_mesh_001_1.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.show_options = True
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Value")
    capture_attribute.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute.domain = 'EDGE'

    # Node Capture Attribute.001
    capture_attribute_001 = smooth_mesh_001_1.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.name = "Capture Attribute.001"
    capture_attribute_001.show_options = True
    capture_attribute_001.active_index = 0
    capture_attribute_001.capture_items.clear()
    capture_attribute_001.capture_items.new('FLOAT', "Value")
    capture_attribute_001.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_001.domain = 'POINT'

    # Node Group Output
    group_output = smooth_mesh_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = smooth_mesh_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Viewer
    viewer = smooth_mesh_001_1.nodes.new("GeometryNodeViewer")
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

    # Node Separate Color
    separate_color = smooth_mesh_001_1.nodes.new("FunctionNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.show_options = True
    separate_color.mode = 'RGB'

    # Node Separate Color.001
    separate_color_001 = smooth_mesh_001_1.nodes.new("FunctionNodeSeparateColor")
    separate_color_001.name = "Separate Color.001"
    separate_color_001.show_options = True
    separate_color_001.mode = 'RGB'

    # Node Combine Color
    combine_color = smooth_mesh_001_1.nodes.new("FunctionNodeCombineColor")
    combine_color.name = "Combine Color"
    combine_color.show_options = True
    combine_color.mode = 'RGB'

    # Set locations
    smooth_mesh_001_1.nodes["Position"].location = (-92.76598358154297, 97.1854476928711)
    smooth_mesh_001_1.nodes["Set Position"].location = (1038.5457763671875, 271.39013671875)
    smooth_mesh_001_1.nodes["Mix"].location = (715.2521362304688, 184.14190673828125)
    smooth_mesh_001_1.nodes["Capture Attribute"].location = (199.31112670898438, 289.65960693359375)
    smooth_mesh_001_1.nodes["Capture Attribute.001"].location = (449.3230285644531, 289.40081787109375)
    smooth_mesh_001_1.nodes["Group Output"].location = (1320.9512939453125, 285.59918212890625)
    smooth_mesh_001_1.nodes["Group Input"].location = (-350.2554931640625, 193.12229919433594)
    smooth_mesh_001_1.nodes["Viewer"].location = (1244.740478515625, 419.02447509765625)
    smooth_mesh_001_1.nodes["Separate Color"].location = (705.2521362304688, 184.14190673828125)
    smooth_mesh_001_1.nodes["Separate Color.001"].location = (705.2521362304688, 184.14190673828125)
    smooth_mesh_001_1.nodes["Combine Color"].location = (705.2521362304688, 184.14190673828125)

    # Set dimensions
    smooth_mesh_001_1.nodes["Position"].width  = 140.0
    smooth_mesh_001_1.nodes["Position"].height = 100.0

    smooth_mesh_001_1.nodes["Set Position"].width  = 140.0
    smooth_mesh_001_1.nodes["Set Position"].height = 100.0

    smooth_mesh_001_1.nodes["Mix"].width  = 140.0
    smooth_mesh_001_1.nodes["Mix"].height = 100.0

    smooth_mesh_001_1.nodes["Capture Attribute"].width  = 140.0
    smooth_mesh_001_1.nodes["Capture Attribute"].height = 100.0

    smooth_mesh_001_1.nodes["Capture Attribute.001"].width  = 140.0
    smooth_mesh_001_1.nodes["Capture Attribute.001"].height = 100.0

    smooth_mesh_001_1.nodes["Group Output"].width  = 140.0
    smooth_mesh_001_1.nodes["Group Output"].height = 100.0

    smooth_mesh_001_1.nodes["Group Input"].width  = 140.0
    smooth_mesh_001_1.nodes["Group Input"].height = 100.0

    smooth_mesh_001_1.nodes["Viewer"].width  = 140.0
    smooth_mesh_001_1.nodes["Viewer"].height = 100.0

    smooth_mesh_001_1.nodes["Separate Color"].width  = 140.0
    smooth_mesh_001_1.nodes["Separate Color"].height = 100.0

    smooth_mesh_001_1.nodes["Separate Color.001"].width  = 140.0
    smooth_mesh_001_1.nodes["Separate Color.001"].height = 100.0

    smooth_mesh_001_1.nodes["Combine Color"].width  = 140.0
    smooth_mesh_001_1.nodes["Combine Color"].height = 100.0


    # Initialize smooth_mesh_001_1 links

    # position.Position -> capture_attribute.Value
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Position"].outputs[0],
        smooth_mesh_001_1.nodes["Capture Attribute"].inputs[1]
    )
    # capture_attribute.Geometry -> capture_attribute_001.Geometry
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Capture Attribute"].outputs[0],
        smooth_mesh_001_1.nodes["Capture Attribute.001"].inputs[0]
    )
    # capture_attribute.Value -> capture_attribute_001.Value
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Capture Attribute"].outputs[1],
        smooth_mesh_001_1.nodes["Capture Attribute.001"].inputs[1]
    )
    # position.Position -> mix.A
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Position"].outputs[0],
        smooth_mesh_001_1.nodes["Mix"].inputs[6]
    )
    # capture_attribute_001.Value -> mix.B
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Capture Attribute.001"].outputs[1],
        smooth_mesh_001_1.nodes["Mix"].inputs[7]
    )
    # capture_attribute_001.Geometry -> set_position.Geometry
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Capture Attribute.001"].outputs[0],
        smooth_mesh_001_1.nodes["Set Position"].inputs[0]
    )
    # group_input.Mesh -> capture_attribute.Geometry
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Group Input"].outputs[0],
        smooth_mesh_001_1.nodes["Capture Attribute"].inputs[0]
    )
    # set_position.Geometry -> group_output.Curve
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Set Position"].outputs[0],
        smooth_mesh_001_1.nodes["Group Output"].inputs[0]
    )
    # set_position.Geometry -> viewer.Geometry
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Set Position"].outputs[0],
        smooth_mesh_001_1.nodes["Viewer"].inputs[0]
    )
    # position.Position -> separate_color.Color
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Position"].outputs[0],
        smooth_mesh_001_1.nodes["Separate Color"].inputs[0]
    )
    # mix.Result -> separate_color_001.Color
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Mix"].outputs[2],
        smooth_mesh_001_1.nodes["Separate Color.001"].inputs[0]
    )
    # separate_color_001.Red -> combine_color.Red
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Separate Color.001"].outputs[0],
        smooth_mesh_001_1.nodes["Combine Color"].inputs[0]
    )
    # separate_color_001.Green -> combine_color.Green
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Separate Color.001"].outputs[1],
        smooth_mesh_001_1.nodes["Combine Color"].inputs[1]
    )
    # separate_color_001.Blue -> combine_color.Blue
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Separate Color.001"].outputs[2],
        smooth_mesh_001_1.nodes["Combine Color"].inputs[2]
    )
    # separate_color.Alpha -> combine_color.Alpha
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Separate Color"].outputs[3],
        smooth_mesh_001_1.nodes["Combine Color"].inputs[3]
    )
    # combine_color.Color -> set_position.Position
    smooth_mesh_001_1.links.new(
        smooth_mesh_001_1.nodes["Combine Color"].outputs[0],
        smooth_mesh_001_1.nodes["Set Position"].inputs[2]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return smooth_mesh_001_1


def skin_cutout_2_001_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Skin Cutout 2.001 node group"""
    skin_cutout_2_001_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Skin Cutout 2.001")

    skin_cutout_2_001_1.color_tag = 'NONE'
    skin_cutout_2_001_1.description = ""
    skin_cutout_2_001_1.default_group_node_width = 140
    skin_cutout_2_001_1.show_modifier_manage_panel = True

    # skin_cutout_2_001_1 interface

    # Socket Geometry
    geometry_socket = skin_cutout_2_001_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket = skin_cutout_2_001_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Socket Smoothing
    smoothing_socket = skin_cutout_2_001_1.interface.new_socket(name="Smoothing", in_out='INPUT', socket_type='NodeSocketBool')
    smoothing_socket.default_value = False
    smoothing_socket.attribute_domain = 'POINT'
    smoothing_socket.default_input = 'VALUE'
    smoothing_socket.structure_type = 'AUTO'

    # Socket Paint Name
    paint_name_socket = skin_cutout_2_001_1.interface.new_socket(name="Paint Name", in_out='INPUT', socket_type='NodeSocketString')
    paint_name_socket.default_value = ""
    paint_name_socket.subtype = 'NONE'
    paint_name_socket.attribute_domain = 'POINT'
    paint_name_socket.default_input = 'VALUE'
    paint_name_socket.structure_type = 'AUTO'

    # Socket Cutout Tolerance
    cutout_tolerance_socket = skin_cutout_2_001_1.interface.new_socket(name="Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat')
    cutout_tolerance_socket.default_value = 0.0
    cutout_tolerance_socket.min_value = -3.4028234663852886e+38
    cutout_tolerance_socket.max_value = 3.4028234663852886e+38
    cutout_tolerance_socket.subtype = 'NONE'
    cutout_tolerance_socket.attribute_domain = 'POINT'
    cutout_tolerance_socket.default_input = 'VALUE'
    cutout_tolerance_socket.structure_type = 'AUTO'

    # Socket Smooth Sampling
    smooth_sampling_socket = skin_cutout_2_001_1.interface.new_socket(name="Smooth Sampling", in_out='INPUT', socket_type='NodeSocketInt')
    smooth_sampling_socket.default_value = 10
    smooth_sampling_socket.min_value = 1
    smooth_sampling_socket.max_value = 100000
    smooth_sampling_socket.subtype = 'NONE'
    smooth_sampling_socket.attribute_domain = 'POINT'
    smooth_sampling_socket.default_input = 'VALUE'
    smooth_sampling_socket.structure_type = 'AUTO'

    # Initialize skin_cutout_2_001_1 nodes

    # Node Group Output
    group_output = skin_cutout_2_001_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = skin_cutout_2_001_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Skin Flat Cutout
    skin_flat_cutout = skin_cutout_2_001_1.nodes.new("NodeFrame")
    skin_flat_cutout.label = "Skin Flat Cutout"
    skin_flat_cutout.name = "Skin Flat Cutout"
    skin_flat_cutout.use_custom_color = True
    skin_flat_cutout.color = (0.1496679037809372, 0.272470623254776, 0.3146030902862549)
    skin_flat_cutout.show_options = True
    skin_flat_cutout.label_size = 30
    skin_flat_cutout.shrink = True

    # Node Index
    index = skin_cutout_2_001_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Named Attribute.001
    named_attribute_001 = skin_cutout_2_001_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'FLOAT'

    # Node Math.002
    math_002 = skin_cutout_2_001_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.hide = True
    math_002.show_options = True
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False
    # Value_001
    math_002.inputs[1].default_value = 100.0

    # Node Sample Index
    sample_index = skin_cutout_2_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT'
    sample_index.domain = 'POINT'

    # Node Delete Geometry
    delete_geometry = skin_cutout_2_001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.show_options = True
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    # Node Compare
    compare = skin_cutout_2_001_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.hide = True
    compare.show_options = True
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_EQUAL'

    # Node Math
    math = skin_cutout_2_001_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.hide = True
    math.show_options = True
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    # Value
    math.inputs[0].default_value = 1.0

    # Node Reroute.001
    reroute_001 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Viewer
    viewer = skin_cutout_2_001_1.nodes.new("GeometryNodeViewer")
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

    # Node Frame.005
    frame_005 = skin_cutout_2_001_1.nodes.new("NodeFrame")
    frame_005.label = "Smooth Cutout"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.20436476171016693, 0.5617048144340515, 0.6079999804496765)
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Group.001
    group_001 = skin_cutout_2_001_1.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.show_options = True
    group_001.node_tree = bpy.data.node_groups[node_tree_names[smooth_mesh_001_1_node_group]]

    # Node Group.002
    group_002 = skin_cutout_2_001_1.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.show_options = True
    group_002.node_tree = bpy.data.node_groups[node_tree_names[smooth_mesh_001_1_node_group]]

    # Node Merge by Distance.002
    merge_by_distance_002 = skin_cutout_2_001_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_002.name = "Merge by Distance.002"
    merge_by_distance_002.show_options = True
    # Selection
    merge_by_distance_002.inputs[1].default_value = True
    # Mode
    merge_by_distance_002.inputs[2].default_value = 'All'

    # Node Reroute
    reroute = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Reroute.002
    reroute_002 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Mesh to Curve
    mesh_to_curve = skin_cutout_2_001_1.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.show_options = True
    mesh_to_curve.mode = 'EDGES'
    # Selection
    mesh_to_curve.inputs[1].default_value = True

    # Node Delete Geometry.001
    delete_geometry_001 = skin_cutout_2_001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.show_options = True
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'

    # Node Extrude Mesh
    extrude_mesh = skin_cutout_2_001_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.show_options = True
    extrude_mesh.mode = 'FACES'
    # Selection
    extrude_mesh.inputs[1].default_value = True
    # Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset Scale
    extrude_mesh.inputs[3].default_value = 0.0
    # Individual
    extrude_mesh.inputs[4].default_value = False

    # Node Resample Curve
    resample_curve = skin_cutout_2_001_1.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.show_options = True
    resample_curve.keep_last_segment = True
    # Selection
    resample_curve.inputs[1].default_value = True
    # Mode
    resample_curve.inputs[2].default_value = 'Count'
    # Length
    resample_curve.inputs[4].default_value = 0.10000000149011612

    # Node Reroute.003
    reroute_003 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketInt"
    # Node Reroute.004
    reroute_004 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketInt"
    # Node Set Spline Type
    set_spline_type = skin_cutout_2_001_1.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type.name = "Set Spline Type"
    set_spline_type.show_options = True
    set_spline_type.spline_type = 'CATMULL_ROM'
    # Selection
    set_spline_type.inputs[1].default_value = True

    # Node Sample Nearest
    sample_nearest = skin_cutout_2_001_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Position.001
    position_001 = skin_cutout_2_001_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Set Position.001
    set_position_001 = skin_cutout_2_001_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.show_options = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Sample Index.001
    sample_index_001 = skin_cutout_2_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'

    # Node Position.002
    position_002 = skin_cutout_2_001_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Sample Index.002
    sample_index_002 = skin_cutout_2_001_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'

    # Node Index.003
    index_003 = skin_cutout_2_001_1.nodes.new("GeometryNodeInputIndex")
    index_003.name = "Index.003"
    index_003.show_options = True

    # Node Merge by Distance.001
    merge_by_distance_001 = skin_cutout_2_001_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.show_options = True
    # Mode
    merge_by_distance_001.inputs[2].default_value = 'All'

    # Node Align Mesh with Spline
    align_mesh_with_spline = skin_cutout_2_001_1.nodes.new("NodeFrame")
    align_mesh_with_spline.label = "Align Mesh with Spline"
    align_mesh_with_spline.name = "Align Mesh with Spline"
    align_mesh_with_spline.show_options = True
    align_mesh_with_spline.label_size = 20
    align_mesh_with_spline.shrink = True

    # Node Curve to Mesh
    curve_to_mesh = skin_cutout_2_001_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.show_options = True
    # Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    # Node Reroute.005
    reroute_005 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketGeometry"
    # Node Reroute.006
    reroute_006 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketGeometry"
    # Node Reroute.007
    reroute_007 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketBool"
    # Node Value
    value = skin_cutout_2_001_1.nodes.new("ShaderNodeValue")
    value.name = "Value"
    value.show_options = True

    value.outputs[0].default_value = 0.0010000000474974513
    # Node Reroute.008
    reroute_008 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketFloat"
    # Node Edge Neighbors
    edge_neighbors = skin_cutout_2_001_1.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
    edge_neighbors.name = "Edge Neighbors"
    edge_neighbors.show_options = True

    # Node Compare.001
    compare_001 = skin_cutout_2_001_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.show_options = True
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    # B_INT
    compare_001.inputs[3].default_value = 0

    # Node Delete Geometry.002
    delete_geometry_002 = skin_cutout_2_001_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.show_options = True
    delete_geometry_002.domain = 'POINT'
    delete_geometry_002.mode = 'ALL'

    # Node Switch
    switch = skin_cutout_2_001_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'GEOMETRY'

    # Node Reroute.009
    reroute_009 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketBool"
    # Node Reroute.010
    reroute_010 = skin_cutout_2_001_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketBool"
    # Set parents
    skin_cutout_2_001_1.nodes["Index"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Named Attribute.001"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Math.002"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Sample Index"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Delete Geometry"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Compare"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Math"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Reroute.001"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Group.001"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Group.002"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Merge by Distance.002"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Reroute"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Reroute.002"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Mesh to Curve"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Delete Geometry.001"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Extrude Mesh"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Resample Curve"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Set Spline Type"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Sample Nearest"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Position.001"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Set Position.001"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Sample Index.001"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Position.002"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Sample Index.002"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Index.003"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Merge by Distance.001"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Curve to Mesh"].parent = skin_cutout_2_001_1.nodes["Frame.005"]
    skin_cutout_2_001_1.nodes["Reroute.005"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Reroute.006"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Reroute.007"].parent = skin_cutout_2_001_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_001_1.nodes["Edge Neighbors"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Compare.001"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_001_1.nodes["Delete Geometry.002"].parent = skin_cutout_2_001_1.nodes["Skin Flat Cutout"]

    # Set locations
    skin_cutout_2_001_1.nodes["Group Output"].location = (3700.0, 400.0)
    skin_cutout_2_001_1.nodes["Group Input"].location = (-1351.0828857421875, 407.08544921875)
    skin_cutout_2_001_1.nodes["Skin Flat Cutout"].location = (-1077.0, 804.0)
    skin_cutout_2_001_1.nodes["Index"].location = (405.34869384765625, -858.9393310546875)
    skin_cutout_2_001_1.nodes["Named Attribute.001"].location = (239.07568359375, -703.385986328125)
    skin_cutout_2_001_1.nodes["Math.002"].location = (29.9884033203125, -541.060302734375)
    skin_cutout_2_001_1.nodes["Sample Index"].location = (638.3048095703125, -584.5645751953125)
    skin_cutout_2_001_1.nodes["Delete Geometry"].location = (1091.0009765625, -196.79534912109375)
    skin_cutout_2_001_1.nodes["Compare"].location = (867.5344848632812, -536.4532470703125)
    skin_cutout_2_001_1.nodes["Math"].location = (198.04608154296875, -542.2776489257812)
    skin_cutout_2_001_1.nodes["Reroute.001"].location = (420.58990478515625, -369.8586730957031)
    skin_cutout_2_001_1.nodes["Viewer"].location = (2080.9931640625, 315.12640380859375)
    skin_cutout_2_001_1.nodes["Frame.005"].location = (720.8032836914062, 382.0)
    skin_cutout_2_001_1.nodes["Group.001"].location = (241.3150634765625, -46.418548583984375)
    skin_cutout_2_001_1.nodes["Group.002"].location = (415.98101806640625, -35.68646240234375)
    skin_cutout_2_001_1.nodes["Merge by Distance.002"].location = (59.70556640625, -205.22015380859375)
    skin_cutout_2_001_1.nodes["Reroute"].location = (592.2180786132812, -152.989990234375)
    skin_cutout_2_001_1.nodes["Reroute.002"].location = (35.0, -155.92022705078125)
    skin_cutout_2_001_1.nodes["Mesh to Curve"].location = (640.2412719726562, -351.8543701171875)
    skin_cutout_2_001_1.nodes["Delete Geometry.001"].location = (444.70733642578125, -282.67486572265625)
    skin_cutout_2_001_1.nodes["Extrude Mesh"].location = (257.9547119140625, -287.199951171875)
    skin_cutout_2_001_1.nodes["Resample Curve"].location = (820.2713012695312, -322.87530517578125)
    skin_cutout_2_001_1.nodes["Reroute.003"].location = (1412.6131591796875, -231.26043701171875)
    skin_cutout_2_001_1.nodes["Reroute.004"].location = (-1080.3211669921875, -169.61830139160156)
    skin_cutout_2_001_1.nodes["Set Spline Type"].location = (1000.2717895507812, -314.5982666015625)
    skin_cutout_2_001_1.nodes["Sample Nearest"].location = (384.082763671875, -424.27685546875)
    skin_cutout_2_001_1.nodes["Position.001"].location = (29.819580078125, -532.0337524414062)
    skin_cutout_2_001_1.nodes["Set Position.001"].location = (785.648681640625, -183.0235137939453)
    skin_cutout_2_001_1.nodes["Sample Index.001"].location = (589.653076171875, -315.15240478515625)
    skin_cutout_2_001_1.nodes["Position.002"].location = (376.870849609375, -573.1759033203125)
    skin_cutout_2_001_1.nodes["Sample Index.002"].location = (212.033935546875, -497.62042236328125)
    skin_cutout_2_001_1.nodes["Index.003"].location = (38.988037109375, -688.8377075195312)
    skin_cutout_2_001_1.nodes["Merge by Distance.001"].location = (988.182373046875, -35.52864074707031)
    skin_cutout_2_001_1.nodes["Align Mesh with Spline"].location = (2089.0, 211.0)
    skin_cutout_2_001_1.nodes["Curve to Mesh"].location = (1163.035400390625, -298.85455322265625)
    skin_cutout_2_001_1.nodes["Reroute.005"].location = (110.689697265625, -274.87054443359375)
    skin_cutout_2_001_1.nodes["Reroute.006"].location = (39.08837890625, -106.16355895996094)
    skin_cutout_2_001_1.nodes["Reroute.007"].location = (701.663330078125, -121.35810852050781)
    skin_cutout_2_001_1.nodes["Value"].location = (329.65716552734375, -530.4838256835938)
    skin_cutout_2_001_1.nodes["Reroute.008"].location = (2985.95849609375, -620.7373657226562)
    skin_cutout_2_001_1.nodes["Edge Neighbors"].location = (1098.998046875, -73.8663330078125)
    skin_cutout_2_001_1.nodes["Compare.001"].location = (1302.21484375, -51.263671875)
    skin_cutout_2_001_1.nodes["Delete Geometry.002"].location = (1474.80029296875, -158.545654296875)
    skin_cutout_2_001_1.nodes["Switch"].location = (3300.0, 420.0)
    skin_cutout_2_001_1.nodes["Reroute.009"].location = (3220.0, 1020.0)
    skin_cutout_2_001_1.nodes["Reroute.010"].location = (-1060.0, 1000.0)

    # Set dimensions
    skin_cutout_2_001_1.nodes["Group Output"].width  = 140.0
    skin_cutout_2_001_1.nodes["Group Output"].height = 100.0

    skin_cutout_2_001_1.nodes["Group Input"].width  = 140.0
    skin_cutout_2_001_1.nodes["Group Input"].height = 100.0

    skin_cutout_2_001_1.nodes["Skin Flat Cutout"].width  = 1645.0
    skin_cutout_2_001_1.nodes["Skin Flat Cutout"].height = 939.0

    skin_cutout_2_001_1.nodes["Index"].width  = 140.0
    skin_cutout_2_001_1.nodes["Index"].height = 100.0

    skin_cutout_2_001_1.nodes["Named Attribute.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Named Attribute.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Math.002"].width  = 140.0
    skin_cutout_2_001_1.nodes["Math.002"].height = 100.0

    skin_cutout_2_001_1.nodes["Sample Index"].width  = 140.0
    skin_cutout_2_001_1.nodes["Sample Index"].height = 100.0

    skin_cutout_2_001_1.nodes["Delete Geometry"].width  = 140.0
    skin_cutout_2_001_1.nodes["Delete Geometry"].height = 100.0

    skin_cutout_2_001_1.nodes["Compare"].width  = 140.0
    skin_cutout_2_001_1.nodes["Compare"].height = 100.0

    skin_cutout_2_001_1.nodes["Math"].width  = 140.0
    skin_cutout_2_001_1.nodes["Math"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.001"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Viewer"].width  = 140.0
    skin_cutout_2_001_1.nodes["Viewer"].height = 100.0

    skin_cutout_2_001_1.nodes["Frame.005"].width  = 1333.19677734375
    skin_cutout_2_001_1.nodes["Frame.005"].height = 548.0

    skin_cutout_2_001_1.nodes["Group.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Group.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Group.002"].width  = 140.0
    skin_cutout_2_001_1.nodes["Group.002"].height = 100.0

    skin_cutout_2_001_1.nodes["Merge by Distance.002"].width  = 140.0
    skin_cutout_2_001_1.nodes["Merge by Distance.002"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.002"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.002"].height = 100.0

    skin_cutout_2_001_1.nodes["Mesh to Curve"].width  = 140.0
    skin_cutout_2_001_1.nodes["Mesh to Curve"].height = 100.0

    skin_cutout_2_001_1.nodes["Delete Geometry.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Delete Geometry.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Extrude Mesh"].width  = 140.0
    skin_cutout_2_001_1.nodes["Extrude Mesh"].height = 100.0

    skin_cutout_2_001_1.nodes["Resample Curve"].width  = 140.0
    skin_cutout_2_001_1.nodes["Resample Curve"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.003"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.003"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.004"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.004"].height = 100.0

    skin_cutout_2_001_1.nodes["Set Spline Type"].width  = 140.0
    skin_cutout_2_001_1.nodes["Set Spline Type"].height = 100.0

    skin_cutout_2_001_1.nodes["Sample Nearest"].width  = 140.0
    skin_cutout_2_001_1.nodes["Sample Nearest"].height = 100.0

    skin_cutout_2_001_1.nodes["Position.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Position.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Set Position.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Set Position.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Sample Index.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Sample Index.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Position.002"].width  = 140.0
    skin_cutout_2_001_1.nodes["Position.002"].height = 100.0

    skin_cutout_2_001_1.nodes["Sample Index.002"].width  = 140.0
    skin_cutout_2_001_1.nodes["Sample Index.002"].height = 100.0

    skin_cutout_2_001_1.nodes["Index.003"].width  = 140.0
    skin_cutout_2_001_1.nodes["Index.003"].height = 100.0

    skin_cutout_2_001_1.nodes["Merge by Distance.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Merge by Distance.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Align Mesh with Spline"].width  = 1158.0
    skin_cutout_2_001_1.nodes["Align Mesh with Spline"].height = 769.0

    skin_cutout_2_001_1.nodes["Curve to Mesh"].width  = 140.0
    skin_cutout_2_001_1.nodes["Curve to Mesh"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.005"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.005"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.006"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.006"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.007"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.007"].height = 100.0

    skin_cutout_2_001_1.nodes["Value"].width  = 123.92022705078125
    skin_cutout_2_001_1.nodes["Value"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.008"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.008"].height = 100.0

    skin_cutout_2_001_1.nodes["Edge Neighbors"].width  = 140.0
    skin_cutout_2_001_1.nodes["Edge Neighbors"].height = 100.0

    skin_cutout_2_001_1.nodes["Compare.001"].width  = 140.0
    skin_cutout_2_001_1.nodes["Compare.001"].height = 100.0

    skin_cutout_2_001_1.nodes["Delete Geometry.002"].width  = 140.0
    skin_cutout_2_001_1.nodes["Delete Geometry.002"].height = 100.0

    skin_cutout_2_001_1.nodes["Switch"].width  = 140.0
    skin_cutout_2_001_1.nodes["Switch"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.009"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.009"].height = 100.0

    skin_cutout_2_001_1.nodes["Reroute.010"].width  = 10.0
    skin_cutout_2_001_1.nodes["Reroute.010"].height = 100.0


    # Initialize skin_cutout_2_001_1 links

    # math.Value -> compare.B
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Math"].outputs[0],
        skin_cutout_2_001_1.nodes["Compare"].inputs[1]
    )
    # compare.Result -> delete_geometry.Selection
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Compare"].outputs[0],
        skin_cutout_2_001_1.nodes["Delete Geometry"].inputs[1]
    )
    # index.Index -> sample_index.Index
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Index"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index"].inputs[2]
    )
    # sample_index.Value -> compare.A
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Sample Index"].outputs[0],
        skin_cutout_2_001_1.nodes["Compare"].inputs[0]
    )
    # math_002.Value -> math.Value
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Math.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Math"].inputs[1]
    )
    # named_attribute_001.Attribute -> sample_index.Value
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Named Attribute.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index"].inputs[1]
    )
    # reroute_001.Output -> sample_index.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index"].inputs[0]
    )
    # reroute_001.Output -> delete_geometry.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Delete Geometry"].inputs[0]
    )
    # group_input.Mesh -> reroute_001.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Group Input"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute.001"].inputs[0]
    )
    # group_input.Paint Name -> named_attribute_001.Name
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Group Input"].outputs[2],
        skin_cutout_2_001_1.nodes["Named Attribute.001"].inputs[0]
    )
    # group_input.Cutout Tolerance -> math_002.Value
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Group Input"].outputs[3],
        skin_cutout_2_001_1.nodes["Math.002"].inputs[0]
    )
    # group_001.Curve -> group_002.Mesh
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Group.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Group.002"].inputs[0]
    )
    # reroute_002.Output -> merge_by_distance_002.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Merge by Distance.002"].inputs[0]
    )
    # group_002.Curve -> reroute.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Group.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute"].inputs[0]
    )
    # merge_by_distance_002.Geometry -> extrude_mesh.Mesh
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Merge by Distance.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Extrude Mesh"].inputs[0]
    )
    # extrude_mesh.Mesh -> delete_geometry_001.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Extrude Mesh"].outputs[0],
        skin_cutout_2_001_1.nodes["Delete Geometry.001"].inputs[0]
    )
    # extrude_mesh.Top -> delete_geometry_001.Selection
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Extrude Mesh"].outputs[1],
        skin_cutout_2_001_1.nodes["Delete Geometry.001"].inputs[1]
    )
    # delete_geometry_001.Geometry -> mesh_to_curve.Mesh
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Delete Geometry.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Mesh to Curve"].inputs[0]
    )
    # mesh_to_curve.Curve -> resample_curve.Curve
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Mesh to Curve"].outputs[0],
        skin_cutout_2_001_1.nodes["Resample Curve"].inputs[0]
    )
    # reroute_003.Output -> resample_curve.Count
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.003"].outputs[0],
        skin_cutout_2_001_1.nodes["Resample Curve"].inputs[3]
    )
    # reroute_004.Output -> reroute_003.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.004"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute.003"].inputs[0]
    )
    # group_input.Smooth Sampling -> reroute_004.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Group Input"].outputs[4],
        skin_cutout_2_001_1.nodes["Reroute.004"].inputs[0]
    )
    # resample_curve.Curve -> set_spline_type.Curve
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Resample Curve"].outputs[0],
        skin_cutout_2_001_1.nodes["Set Spline Type"].inputs[0]
    )
    # set_position_001.Geometry -> merge_by_distance_001.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Set Position.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Merge by Distance.001"].inputs[0]
    )
    # index_003.Index -> sample_index_002.Index
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Index.003"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index.002"].inputs[2]
    )
    # sample_index_002.Value -> sample_nearest.Sample Position
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Sample Index.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Nearest"].inputs[1]
    )
    # position_001.Position -> sample_index_002.Value
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Position.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index.002"].inputs[1]
    )
    # sample_index_001.Value -> set_position_001.Position
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Sample Index.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Set Position.001"].inputs[2]
    )
    # position_002.Position -> sample_index_001.Value
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Position.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index.001"].inputs[1]
    )
    # sample_nearest.Index -> sample_index_001.Index
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Sample Nearest"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index.001"].inputs[2]
    )
    # set_spline_type.Curve -> curve_to_mesh.Curve
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Set Spline Type"].outputs[0],
        skin_cutout_2_001_1.nodes["Curve to Mesh"].inputs[0]
    )
    # reroute_005.Output -> sample_nearest.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.005"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Nearest"].inputs[0]
    )
    # curve_to_mesh.Mesh -> reroute_005.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Curve to Mesh"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_005.Output -> sample_index_001.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.005"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index.001"].inputs[0]
    )
    # reroute_006.Output -> set_position_001.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.006"].outputs[0],
        skin_cutout_2_001_1.nodes["Set Position.001"].inputs[0]
    )
    # extrude_mesh.Mesh -> reroute_006.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Extrude Mesh"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_007.Output -> set_position_001.Selection
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.007"].outputs[0],
        skin_cutout_2_001_1.nodes["Set Position.001"].inputs[1]
    )
    # extrude_mesh.Side -> reroute_007.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Extrude Mesh"].outputs[2],
        skin_cutout_2_001_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_007.Output -> merge_by_distance_001.Selection
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.007"].outputs[0],
        skin_cutout_2_001_1.nodes["Merge by Distance.001"].inputs[1]
    )
    # value.Value -> merge_by_distance_002.Distance
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Value"].outputs[0],
        skin_cutout_2_001_1.nodes["Merge by Distance.002"].inputs[3]
    )
    # reroute_008.Output -> merge_by_distance_001.Distance
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.008"].outputs[0],
        skin_cutout_2_001_1.nodes["Merge by Distance.001"].inputs[3]
    )
    # value.Value -> reroute_008.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Value"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute.008"].inputs[0]
    )
    # reroute_006.Output -> sample_index_002.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.006"].outputs[0],
        skin_cutout_2_001_1.nodes["Sample Index.002"].inputs[0]
    )
    # reroute.Output -> viewer.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute"].outputs[0],
        skin_cutout_2_001_1.nodes["Viewer"].inputs[0]
    )
    # edge_neighbors.Face Count -> compare_001.A
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Edge Neighbors"].outputs[0],
        skin_cutout_2_001_1.nodes["Compare.001"].inputs[2]
    )
    # delete_geometry.Geometry -> delete_geometry_002.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Delete Geometry"].outputs[0],
        skin_cutout_2_001_1.nodes["Delete Geometry.002"].inputs[0]
    )
    # compare_001.Result -> delete_geometry_002.Selection
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Compare.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Delete Geometry.002"].inputs[1]
    )
    # reroute.Output -> reroute_002.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute.002"].inputs[0]
    )
    # delete_geometry_002.Geometry -> group_001.Mesh
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Delete Geometry.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Group.001"].inputs[0]
    )
    # merge_by_distance_001.Geometry -> switch.True
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Merge by Distance.001"].outputs[0],
        skin_cutout_2_001_1.nodes["Switch"].inputs[2]
    )
    # reroute_009.Output -> switch.Switch
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.009"].outputs[0],
        skin_cutout_2_001_1.nodes["Switch"].inputs[0]
    )
    # reroute_010.Output -> reroute_009.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Reroute.010"].outputs[0],
        skin_cutout_2_001_1.nodes["Reroute.009"].inputs[0]
    )
    # group_input.Smoothing -> reroute_010.Input
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Group Input"].outputs[1],
        skin_cutout_2_001_1.nodes["Reroute.010"].inputs[0]
    )
    # delete_geometry_002.Geometry -> switch.False
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Delete Geometry.002"].outputs[0],
        skin_cutout_2_001_1.nodes["Switch"].inputs[1]
    )
    # switch.Output -> group_output.Geometry
    skin_cutout_2_001_1.links.new(
        skin_cutout_2_001_1.nodes["Switch"].outputs[0],
        skin_cutout_2_001_1.nodes["Group Output"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = False
    viewer.viewer_items[1].auto_remove = False

    return skin_cutout_2_001_1


def remove_boundary_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Remove Boundary node group"""
    remove_boundary_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Remove Boundary")

    remove_boundary_1.color_tag = 'NONE'
    remove_boundary_1.description = ""
    remove_boundary_1.default_group_node_width = 140
    remove_boundary_1.show_modifier_manage_panel = True

    # remove_boundary_1 interface

    # Socket Mesh
    mesh_socket = remove_boundary_1.interface.new_socket(name="Mesh", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket_1 = remove_boundary_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket_1.attribute_domain = 'POINT'
    mesh_socket_1.default_input = 'VALUE'
    mesh_socket_1.structure_type = 'AUTO'

    # Initialize remove_boundary_1 nodes

    # Node Group Input
    group_input = remove_boundary_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = remove_boundary_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Extrude Mesh
    extrude_mesh = remove_boundary_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.show_options = True
    extrude_mesh.mode = 'FACES'
    # Selection
    extrude_mesh.inputs[1].default_value = True
    # Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset Scale
    extrude_mesh.inputs[3].default_value = 0.0
    # Individual
    extrude_mesh.inputs[4].default_value = False

    # Node Delete Geometry
    delete_geometry = remove_boundary_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.show_options = True
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    # Set locations
    remove_boundary_1.nodes["Group Input"].location = (-740.0, 0.0)
    remove_boundary_1.nodes["Group Output"].location = (300.0, 0.0)
    remove_boundary_1.nodes["Extrude Mesh"].location = (-180.0, 200.0)
    remove_boundary_1.nodes["Delete Geometry"].location = (80.0, 80.0)

    # Set dimensions
    remove_boundary_1.nodes["Group Input"].width  = 140.0
    remove_boundary_1.nodes["Group Input"].height = 100.0

    remove_boundary_1.nodes["Group Output"].width  = 140.0
    remove_boundary_1.nodes["Group Output"].height = 100.0

    remove_boundary_1.nodes["Extrude Mesh"].width  = 140.0
    remove_boundary_1.nodes["Extrude Mesh"].height = 100.0

    remove_boundary_1.nodes["Delete Geometry"].width  = 140.0
    remove_boundary_1.nodes["Delete Geometry"].height = 100.0


    # Initialize remove_boundary_1 links

    # delete_geometry.Geometry -> group_output.Mesh
    remove_boundary_1.links.new(
        remove_boundary_1.nodes["Delete Geometry"].outputs[0],
        remove_boundary_1.nodes["Group Output"].inputs[0]
    )
    # extrude_mesh.Mesh -> delete_geometry.Geometry
    remove_boundary_1.links.new(
        remove_boundary_1.nodes["Extrude Mesh"].outputs[0],
        remove_boundary_1.nodes["Delete Geometry"].inputs[0]
    )
    # extrude_mesh.Side -> delete_geometry.Selection
    remove_boundary_1.links.new(
        remove_boundary_1.nodes["Extrude Mesh"].outputs[2],
        remove_boundary_1.nodes["Delete Geometry"].inputs[1]
    )
    # group_input.Mesh -> extrude_mesh.Mesh
    remove_boundary_1.links.new(
        remove_boundary_1.nodes["Group Input"].outputs[0],
        remove_boundary_1.nodes["Extrude Mesh"].inputs[0]
    )

    return remove_boundary_1


def filter_points_by_index_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Filter Points By Index node group"""
    filter_points_by_index_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Filter Points By Index")

    filter_points_by_index_1.color_tag = 'GEOMETRY'
    filter_points_by_index_1.description = ""
    filter_points_by_index_1.default_group_node_width = 140
    filter_points_by_index_1.show_modifier_manage_panel = True

    # filter_points_by_index_1 interface

    # Socket Points
    points_socket = filter_points_by_index_1.interface.new_socket(name="Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.description = "The parts of the geometry in the selection"
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket = filter_points_by_index_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.description = "Geometry to split into two parts"
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Point Count
    point_count_socket = filter_points_by_index_1.interface.new_socket(name="Point Count", in_out='INPUT', socket_type='NodeSocketInt')
    point_count_socket.default_value = 10
    point_count_socket.min_value = -2147483648
    point_count_socket.max_value = 2147483647
    point_count_socket.subtype = 'NONE'
    point_count_socket.attribute_domain = 'POINT'
    point_count_socket.hide_value = True
    point_count_socket.description = "The parts of the geometry that go into the first output"
    point_count_socket.default_input = 'VALUE'
    point_count_socket.structure_type = 'AUTO'

    # Initialize filter_points_by_index_1 nodes

    # Node Group Input
    group_input = filter_points_by_index_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = filter_points_by_index_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Separate Geometry.006
    separate_geometry_006 = filter_points_by_index_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_006.name = "Separate Geometry.006"
    separate_geometry_006.show_options = True
    separate_geometry_006.domain = 'POINT'

    # Node Math
    math = filter_points_by_index_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'LESS_THAN'
    math.use_clamp = False

    # Node Named Attribute
    named_attribute = filter_points_by_index_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'INT'
    # Name
    named_attribute.inputs[0].default_value = "sensor_idx"

    # Set locations
    filter_points_by_index_1.nodes["Group Input"].location = (-660.0, 0.0)
    filter_points_by_index_1.nodes["Group Output"].location = (300.0, 0.0)
    filter_points_by_index_1.nodes["Separate Geometry.006"].location = (-70.0, 0.0)
    filter_points_by_index_1.nodes["Math"].location = (-400.0, -100.0)
    filter_points_by_index_1.nodes["Named Attribute"].location = (-640.0, -180.0)

    # Set dimensions
    filter_points_by_index_1.nodes["Group Input"].width  = 140.0
    filter_points_by_index_1.nodes["Group Input"].height = 100.0

    filter_points_by_index_1.nodes["Group Output"].width  = 140.0
    filter_points_by_index_1.nodes["Group Output"].height = 100.0

    filter_points_by_index_1.nodes["Separate Geometry.006"].width  = 140.0
    filter_points_by_index_1.nodes["Separate Geometry.006"].height = 100.0

    filter_points_by_index_1.nodes["Math"].width  = 140.0
    filter_points_by_index_1.nodes["Math"].height = 100.0

    filter_points_by_index_1.nodes["Named Attribute"].width  = 140.0
    filter_points_by_index_1.nodes["Named Attribute"].height = 100.0


    # Initialize filter_points_by_index_1 links

    # group_input.Point Count -> math.Value
    filter_points_by_index_1.links.new(
        filter_points_by_index_1.nodes["Group Input"].outputs[1],
        filter_points_by_index_1.nodes["Math"].inputs[1]
    )
    # math.Value -> separate_geometry_006.Selection
    filter_points_by_index_1.links.new(
        filter_points_by_index_1.nodes["Math"].outputs[0],
        filter_points_by_index_1.nodes["Separate Geometry.006"].inputs[1]
    )
    # group_input.Geometry -> separate_geometry_006.Geometry
    filter_points_by_index_1.links.new(
        filter_points_by_index_1.nodes["Group Input"].outputs[0],
        filter_points_by_index_1.nodes["Separate Geometry.006"].inputs[0]
    )
    # separate_geometry_006.Selection -> group_output.Points
    filter_points_by_index_1.links.new(
        filter_points_by_index_1.nodes["Separate Geometry.006"].outputs[0],
        filter_points_by_index_1.nodes["Group Output"].inputs[0]
    )
    # named_attribute.Attribute -> math.Value
    filter_points_by_index_1.links.new(
        filter_points_by_index_1.nodes["Named Attribute"].outputs[0],
        filter_points_by_index_1.nodes["Math"].inputs[0]
    )

    return filter_points_by_index_1


def wiring_layer_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Wiring Layer node group"""
    wiring_layer_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Wiring Layer")

    wiring_layer_1.color_tag = 'NONE'
    wiring_layer_1.description = ""
    wiring_layer_1.default_group_node_width = 140
    wiring_layer_1.is_modifier = True
    wiring_layer_1.show_modifier_manage_panel = True

    # wiring_layer_1 interface

    # Socket Geometry
    geometry_socket = wiring_layer_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Wires
    wires_socket = wiring_layer_1.interface.new_socket(name="Wires", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    wires_socket.attribute_domain = 'POINT'
    wires_socket.default_input = 'VALUE'
    wires_socket.structure_type = 'AUTO'

    # Socket Connection Port Holes
    connection_port_holes_socket = wiring_layer_1.interface.new_socket(name="Connection Port Holes", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    connection_port_holes_socket.attribute_domain = 'POINT'
    connection_port_holes_socket.default_input = 'VALUE'
    connection_port_holes_socket.structure_type = 'AUTO'

    # Socket Routing Layer
    routing_layer_socket = wiring_layer_1.interface.new_socket(name="Routing Layer", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    routing_layer_socket.attribute_domain = 'POINT'
    routing_layer_socket.default_input = 'VALUE'
    routing_layer_socket.structure_type = 'AUTO'

    # Socket Clips
    clips_socket = wiring_layer_1.interface.new_socket(name="Clips", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    clips_socket.attribute_domain = 'POINT'
    clips_socket.default_input = 'VALUE'
    clips_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = wiring_layer_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Isolate
    isolate_socket = wiring_layer_1.interface.new_socket(name="Isolate", in_out='INPUT', socket_type='NodeSocketBool')
    isolate_socket.default_value = False
    isolate_socket.attribute_domain = 'POINT'
    isolate_socket.default_input = 'VALUE'
    isolate_socket.structure_type = 'AUTO'

    # Socket Menu
    menu_socket = wiring_layer_1.interface.new_socket(name="Menu", in_out='INPUT', socket_type='NodeSocketMenu')
    menu_socket.attribute_domain = 'POINT'
    menu_socket.default_input = 'VALUE'
    menu_socket.structure_type = 'AUTO'
    menu_socket.optional_label = True

    # Panel Clip Options
    clip_options_panel = wiring_layer_1.interface.new_panel("Clip Options")
    # Socket Clip Points
    clip_points_socket = wiring_layer_1.interface.new_socket(name="Clip Points", in_out='INPUT', socket_type='NodeSocketMenu', parent = clip_options_panel)
    clip_points_socket.attribute_domain = 'POINT'
    clip_points_socket.default_input = 'VALUE'
    clip_points_socket.structure_type = 'AUTO'
    clip_points_socket.optional_label = True

    # Socket Starting Points Paint
    starting_points_paint_socket = wiring_layer_1.interface.new_socket(name="Starting Points Paint", in_out='INPUT', socket_type='NodeSocketString', parent = clip_options_panel)
    starting_points_paint_socket.default_value = "wiring_endpoint"
    starting_points_paint_socket.subtype = 'NONE'
    starting_points_paint_socket.attribute_domain = 'POINT'
    starting_points_paint_socket.default_input = 'VALUE'
    starting_points_paint_socket.structure_type = 'AUTO'
    starting_points_paint_socket.optional_label = True

    # Socket Electrode Points Paint
    electrode_points_paint_socket = wiring_layer_1.interface.new_socket(name="Electrode Points Paint", in_out='INPUT', socket_type='NodeSocketString', parent = clip_options_panel)
    electrode_points_paint_socket.default_value = "electrode"
    electrode_points_paint_socket.subtype = 'NONE'
    electrode_points_paint_socket.attribute_domain = 'POINT'
    electrode_points_paint_socket.default_input = 'VALUE'
    electrode_points_paint_socket.structure_type = 'AUTO'
    electrode_points_paint_socket.optional_label = True

    # Socket Point Count
    point_count_socket = wiring_layer_1.interface.new_socket(name="Point Count", in_out='INPUT', socket_type='NodeSocketInt', parent = clip_options_panel)
    point_count_socket.default_value = 0
    point_count_socket.min_value = -2147483648
    point_count_socket.max_value = 2147483647
    point_count_socket.subtype = 'NONE'
    point_count_socket.attribute_domain = 'POINT'
    point_count_socket.hide_value = True
    point_count_socket.description = "The parts of the geometry that go into the first output"
    point_count_socket.default_input = 'VALUE'
    point_count_socket.structure_type = 'AUTO'

    # Socket Clip Reference
    clip_reference_socket = wiring_layer_1.interface.new_socket(name="Clip Reference", in_out='INPUT', socket_type='NodeSocketObject', parent = clip_options_panel)
    clip_reference_socket.attribute_domain = 'POINT'
    clip_reference_socket.default_input = 'VALUE'
    clip_reference_socket.structure_type = 'AUTO'

    # Socket Holes
    holes_socket = wiring_layer_1.interface.new_socket(name="Holes", in_out='INPUT', socket_type='NodeSocketObject', parent = clip_options_panel)
    holes_socket.attribute_domain = 'POINT'
    holes_socket.default_input = 'VALUE'
    holes_socket.structure_type = 'AUTO'
    holes_socket.optional_label = True

    # Socket Seperation
    seperation_socket = wiring_layer_1.interface.new_socket(name="Seperation", in_out='INPUT', socket_type='NodeSocketFloat', parent = clip_options_panel)
    seperation_socket.default_value = 0.10000002384185791
    seperation_socket.min_value = -10000.0
    seperation_socket.max_value = 10000.0
    seperation_socket.subtype = 'NONE'
    seperation_socket.attribute_domain = 'POINT'
    seperation_socket.default_input = 'VALUE'
    seperation_socket.structure_type = 'AUTO'

    # Socket Depth
    depth_socket = wiring_layer_1.interface.new_socket(name="Depth", in_out='INPUT', socket_type='NodeSocketFloat', parent = clip_options_panel)
    depth_socket.default_value = 0.05000000074505806
    depth_socket.min_value = 0.0
    depth_socket.max_value = 3.4028234663852886e+38
    depth_socket.subtype = 'DISTANCE'
    depth_socket.attribute_domain = 'POINT'
    depth_socket.default_input = 'VALUE'
    depth_socket.structure_type = 'AUTO'

    # Socket Radius
    radius_socket = wiring_layer_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = clip_options_panel)
    radius_socket.default_value = 0.009999999776482582
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    # Socket Rotation
    rotation_socket = wiring_layer_1.interface.new_socket(name="Rotation", in_out='INPUT', socket_type='NodeSocketFloat', parent = clip_options_panel)
    rotation_socket.default_value = 0.0
    rotation_socket.min_value = -3.4028234663852886e+38
    rotation_socket.max_value = 3.4028234663852886e+38
    rotation_socket.subtype = 'ANGLE'
    rotation_socket.attribute_domain = 'POINT'
    rotation_socket.default_input = 'VALUE'
    rotation_socket.structure_type = 'AUTO'

    # Socket Translation
    translation_socket = wiring_layer_1.interface.new_socket(name="Translation", in_out='INPUT', socket_type='NodeSocketVector', parent = clip_options_panel)
    translation_socket.default_value = (0.0, 0.0, 0.0)
    translation_socket.min_value = -3.4028234663852886e+38
    translation_socket.max_value = 3.4028234663852886e+38
    translation_socket.subtype = 'TRANSLATION'
    translation_socket.attribute_domain = 'POINT'
    translation_socket.default_input = 'VALUE'
    translation_socket.structure_type = 'AUTO'


    # Panel Routing Layer
    routing_layer_panel = wiring_layer_1.interface.new_panel("Routing Layer")
    # Socket Show Routing Layer
    show_routing_layer_socket = wiring_layer_1.interface.new_socket(name="Show Routing Layer", in_out='INPUT', socket_type='NodeSocketBool', parent = routing_layer_panel)
    show_routing_layer_socket.default_value = True
    show_routing_layer_socket.attribute_domain = 'POINT'
    show_routing_layer_socket.default_input = 'VALUE'
    show_routing_layer_socket.structure_type = 'AUTO'

    # Socket Layers
    layers_socket = wiring_layer_1.interface.new_socket(name="Layers", in_out='INPUT', socket_type='NodeSocketInt', parent = routing_layer_panel)
    layers_socket.default_value = 2
    layers_socket.min_value = 0
    layers_socket.max_value = 2147483647
    layers_socket.subtype = 'NONE'
    layers_socket.attribute_domain = 'POINT'
    layers_socket.default_input = 'VALUE'
    layers_socket.structure_type = 'AUTO'

    # Socket Bottom Layer Offset
    bottom_layer_offset_socket = wiring_layer_1.interface.new_socket(name="Bottom Layer Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_layer_panel)
    bottom_layer_offset_socket.default_value = 0.0
    bottom_layer_offset_socket.min_value = -200.0
    bottom_layer_offset_socket.max_value = 200.0
    bottom_layer_offset_socket.subtype = 'PERCENTAGE'
    bottom_layer_offset_socket.attribute_domain = 'POINT'
    bottom_layer_offset_socket.default_input = 'VALUE'
    bottom_layer_offset_socket.structure_type = 'AUTO'

    # Socket Layer Separation
    layer_separation_socket = wiring_layer_1.interface.new_socket(name="Layer Separation", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_layer_panel)
    layer_separation_socket.default_value = 0.009999999776482582
    layer_separation_socket.min_value = -3.4028234663852886e+38
    layer_separation_socket.max_value = 3.4028234663852886e+38
    layer_separation_socket.subtype = 'NONE'
    layer_separation_socket.attribute_domain = 'POINT'
    layer_separation_socket.default_input = 'VALUE'
    layer_separation_socket.structure_type = 'AUTO'

    # Socket Sensor Endpoint Margin
    sensor_endpoint_margin_socket = wiring_layer_1.interface.new_socket(name="Sensor Endpoint Margin", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_layer_panel)
    sensor_endpoint_margin_socket.default_value = 0.019999999552965164
    sensor_endpoint_margin_socket.min_value = -10000.0
    sensor_endpoint_margin_socket.max_value = 10000.0
    sensor_endpoint_margin_socket.subtype = 'NONE'
    sensor_endpoint_margin_socket.attribute_domain = 'POINT'
    sensor_endpoint_margin_socket.default_input = 'VALUE'
    sensor_endpoint_margin_socket.structure_type = 'AUTO'

    # Socket Connector Endpoint Margin
    connector_endpoint_margin_socket = wiring_layer_1.interface.new_socket(name="Connector Endpoint Margin", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_layer_panel)
    connector_endpoint_margin_socket.default_value = 0.004999999888241291
    connector_endpoint_margin_socket.min_value = -10000.0
    connector_endpoint_margin_socket.max_value = 10000.0
    connector_endpoint_margin_socket.subtype = 'NONE'
    connector_endpoint_margin_socket.attribute_domain = 'POINT'
    connector_endpoint_margin_socket.default_input = 'VALUE'
    connector_endpoint_margin_socket.structure_type = 'AUTO'

    # Socket Routing Self Margin
    routing_self_margin_socket = wiring_layer_1.interface.new_socket(name="Routing Self Margin", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_layer_panel)
    routing_self_margin_socket.default_value = 0.0
    routing_self_margin_socket.min_value = -10000.0
    routing_self_margin_socket.max_value = 10000.0
    routing_self_margin_socket.subtype = 'NONE'
    routing_self_margin_socket.attribute_domain = 'POINT'
    routing_self_margin_socket.default_input = 'VALUE'
    routing_self_margin_socket.structure_type = 'AUTO'


    # Panel Wire Generation
    wire_generation_panel = wiring_layer_1.interface.new_panel("Wire Generation")
    # Socket Radius
    radius_socket_1 = wiring_layer_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = wire_generation_panel)
    radius_socket_1.default_value = 0.0010000000474974513
    radius_socket_1.min_value = 0.0
    radius_socket_1.max_value = 3.4028234663852886e+38
    radius_socket_1.subtype = 'DISTANCE'
    radius_socket_1.attribute_domain = 'POINT'
    radius_socket_1.default_input = 'VALUE'
    radius_socket_1.structure_type = 'AUTO'

    # Socket Wire Sampling
    wire_sampling_socket = wiring_layer_1.interface.new_socket(name="Wire Sampling", in_out='INPUT', socket_type='NodeSocketInt', parent = wire_generation_panel)
    wire_sampling_socket.default_value = 15
    wire_sampling_socket.min_value = 1
    wire_sampling_socket.max_value = 100000
    wire_sampling_socket.subtype = 'NONE'
    wire_sampling_socket.attribute_domain = 'POINT'
    wire_sampling_socket.default_input = 'VALUE'
    wire_sampling_socket.structure_type = 'AUTO'

    # Socket Material
    material_socket = wiring_layer_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = wire_generation_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'
    material_socket.optional_label = True

    # Panel Crosstalk Heuristics
    crosstalk_heuristics_panel = wiring_layer_1.interface.new_panel("Crosstalk Heuristics")
    # Socket Crosstalk Power
    crosstalk_power_socket = wiring_layer_1.interface.new_socket(name="Crosstalk Power", in_out='INPUT', socket_type='NodeSocketFloat', parent = crosstalk_heuristics_panel)
    crosstalk_power_socket.default_value = 1.0
    crosstalk_power_socket.min_value = 0.0
    crosstalk_power_socket.max_value = 10000.0
    crosstalk_power_socket.subtype = 'NONE'
    crosstalk_power_socket.attribute_domain = 'POINT'
    crosstalk_power_socket.default_input = 'VALUE'
    crosstalk_power_socket.structure_type = 'AUTO'

    # Socket Crosstalk Factor
    crosstalk_factor_socket = wiring_layer_1.interface.new_socket(name="Crosstalk Factor", in_out='INPUT', socket_type='NodeSocketFloat', parent = crosstalk_heuristics_panel)
    crosstalk_factor_socket.default_value = 50.0
    crosstalk_factor_socket.min_value = 0.0
    crosstalk_factor_socket.max_value = 100.0
    crosstalk_factor_socket.subtype = 'PERCENTAGE'
    crosstalk_factor_socket.attribute_domain = 'POINT'
    crosstalk_factor_socket.default_input = 'VALUE'
    crosstalk_factor_socket.structure_type = 'AUTO'

    # Socket Avoid Distance
    avoid_distance_socket = wiring_layer_1.interface.new_socket(name="Avoid Distance", in_out='INPUT', socket_type='NodeSocketFloat', parent = crosstalk_heuristics_panel)
    avoid_distance_socket.default_value = 0.019999999552965164
    avoid_distance_socket.min_value = 0.0
    avoid_distance_socket.max_value = 10000.0
    avoid_distance_socket.subtype = 'NONE'
    avoid_distance_socket.attribute_domain = 'POINT'
    avoid_distance_socket.default_input = 'VALUE'
    avoid_distance_socket.structure_type = 'AUTO'

    # Socket Route Removal Multiplier
    route_removal_multiplier_socket = wiring_layer_1.interface.new_socket(name="Route Removal Multiplier", in_out='INPUT', socket_type='NodeSocketFloat', parent = crosstalk_heuristics_panel)
    route_removal_multiplier_socket.default_value = 2.0
    route_removal_multiplier_socket.min_value = 0.0
    route_removal_multiplier_socket.max_value = 10000.0
    route_removal_multiplier_socket.subtype = 'NONE'
    route_removal_multiplier_socket.attribute_domain = 'POINT'
    route_removal_multiplier_socket.default_input = 'VALUE'
    route_removal_multiplier_socket.structure_type = 'AUTO'

    # Socket Overlap Accuracy
    overlap_accuracy_socket = wiring_layer_1.interface.new_socket(name="Overlap Accuracy", in_out='INPUT', socket_type='NodeSocketInt', parent = crosstalk_heuristics_panel)
    overlap_accuracy_socket.default_value = 1
    overlap_accuracy_socket.min_value = 0
    overlap_accuracy_socket.max_value = 10000
    overlap_accuracy_socket.subtype = 'NONE'
    overlap_accuracy_socket.attribute_domain = 'POINT'
    overlap_accuracy_socket.default_input = 'VALUE'
    overlap_accuracy_socket.structure_type = 'AUTO'


    wiring_layer_1.interface.move_to_parent(crosstalk_heuristics_panel, wire_generation_panel, 32)
    # Panel Sort by Vector
    sort_by_vector_panel = wiring_layer_1.interface.new_panel("Sort by Vector", default_closed=True)
    # Socket Sort by Vector
    sort_by_vector_socket = wiring_layer_1.interface.new_socket(name="Sort by Vector", in_out='INPUT', socket_type='NodeSocketBool', parent = sort_by_vector_panel)
    sort_by_vector_socket.default_value = False
    sort_by_vector_socket.attribute_domain = 'POINT'
    sort_by_vector_socket.default_input = 'VALUE'
    sort_by_vector_socket.is_panel_toggle = True
    sort_by_vector_socket.structure_type = 'AUTO'

    # Socket Sorting View
    sorting_view_socket = wiring_layer_1.interface.new_socket(name="Sorting View", in_out='INPUT', socket_type='NodeSocketMenu', parent = sort_by_vector_panel)
    sorting_view_socket.attribute_domain = 'POINT'
    sorting_view_socket.default_input = 'VALUE'
    sorting_view_socket.structure_type = 'AUTO'
    sorting_view_socket.optional_label = True

    # Socket Electrode Sorting Vector
    electrode_sorting_vector_socket = wiring_layer_1.interface.new_socket(name="Electrode Sorting Vector", in_out='INPUT', socket_type='NodeSocketVector', parent = sort_by_vector_panel)
    electrode_sorting_vector_socket.default_value = (0.0, 0.0, 0.0)
    electrode_sorting_vector_socket.min_value = -10000.0
    electrode_sorting_vector_socket.max_value = 10000.0
    electrode_sorting_vector_socket.subtype = 'NONE'
    electrode_sorting_vector_socket.attribute_domain = 'POINT'
    electrode_sorting_vector_socket.default_input = 'VALUE'
    electrode_sorting_vector_socket.structure_type = 'AUTO'

    # Socket Clip Sorting Vector
    clip_sorting_vector_socket = wiring_layer_1.interface.new_socket(name="Clip Sorting Vector", in_out='INPUT', socket_type='NodeSocketVector', parent = sort_by_vector_panel)
    clip_sorting_vector_socket.default_value = (0.0, 0.0, 0.0)
    clip_sorting_vector_socket.min_value = -10000.0
    clip_sorting_vector_socket.max_value = 10000.0
    clip_sorting_vector_socket.subtype = 'NONE'
    clip_sorting_vector_socket.attribute_domain = 'POINT'
    clip_sorting_vector_socket.default_input = 'VALUE'
    clip_sorting_vector_socket.structure_type = 'AUTO'


    wiring_layer_1.interface.move_to_parent(sort_by_vector_panel, wire_generation_panel, 38)

    # Panel Routing Coverage
    routing_coverage_panel = wiring_layer_1.interface.new_panel("Routing Coverage")
    # Socket Smoothing
    smoothing_socket = wiring_layer_1.interface.new_socket(name="Smoothing", in_out='INPUT', socket_type='NodeSocketBool', parent = routing_coverage_panel)
    smoothing_socket.default_value = True
    smoothing_socket.attribute_domain = 'POINT'
    smoothing_socket.default_input = 'VALUE'
    smoothing_socket.structure_type = 'AUTO'

    # Socket Cutout Tolerance
    cutout_tolerance_socket = wiring_layer_1.interface.new_socket(name="Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat', parent = routing_coverage_panel)
    cutout_tolerance_socket.default_value = 100.0
    cutout_tolerance_socket.min_value = 0.0
    cutout_tolerance_socket.max_value = 100.0
    cutout_tolerance_socket.subtype = 'PERCENTAGE'
    cutout_tolerance_socket.attribute_domain = 'POINT'
    cutout_tolerance_socket.default_input = 'VALUE'
    cutout_tolerance_socket.structure_type = 'AUTO'

    # Socket Smooth Sampling
    smooth_sampling_socket = wiring_layer_1.interface.new_socket(name="Smooth Sampling", in_out='INPUT', socket_type='NodeSocketInt', parent = routing_coverage_panel)
    smooth_sampling_socket.default_value = 50
    smooth_sampling_socket.min_value = 1
    smooth_sampling_socket.max_value = 100000
    smooth_sampling_socket.subtype = 'NONE'
    smooth_sampling_socket.attribute_domain = 'POINT'
    smooth_sampling_socket.default_input = 'VALUE'
    smooth_sampling_socket.structure_type = 'AUTO'


    # Panel Options
    options_panel = wiring_layer_1.interface.new_panel("Options")
    # Socket Electrodes Name
    electrodes_name_socket = wiring_layer_1.interface.new_socket(name="Electrodes Name", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    electrodes_name_socket.default_value = "wiring_endpoint"
    electrodes_name_socket.subtype = 'NONE'
    electrodes_name_socket.attribute_domain = 'POINT'
    electrodes_name_socket.default_input = 'VALUE'
    electrodes_name_socket.structure_type = 'AUTO'

    # Socket Routing Domain Paint Name
    routing_domain_paint_name_socket = wiring_layer_1.interface.new_socket(name="Routing Domain Paint Name", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    routing_domain_paint_name_socket.default_value = "dermis_bottom"
    routing_domain_paint_name_socket.subtype = 'NONE'
    routing_domain_paint_name_socket.attribute_domain = 'POINT'
    routing_domain_paint_name_socket.description = "Dermis"
    routing_domain_paint_name_socket.default_input = 'VALUE'
    routing_domain_paint_name_socket.structure_type = 'AUTO'


    # Initialize wiring_layer_1 nodes

    # Node Group Input
    group_input = wiring_layer_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = wiring_layer_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group.018
    group_018 = wiring_layer_1.nodes.new("GeometryNodeGroup")
    group_018.name = "Group.018"
    group_018.show_options = True
    group_018.node_tree = bpy.data.node_groups[node_tree_names[generate_wires_001_1_node_group]]

    # Node Group.011
    group_011 = wiring_layer_1.nodes.new("GeometryNodeGroup")
    group_011.name = "Group.011"
    group_011.show_options = True
    group_011.node_tree = bpy.data.node_groups[node_tree_names[generate_clips_001_1_node_group]]

    # Node Separate Geometry
    separate_geometry = wiring_layer_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.show_options = True
    separate_geometry.domain = 'POINT'

    # Node Named Attribute
    named_attribute = wiring_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'BOOLEAN'

    # Node Separate Geometry.001
    separate_geometry_001 = wiring_layer_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_001.name = "Separate Geometry.001"
    separate_geometry_001.show_options = True
    separate_geometry_001.domain = 'POINT'

    # Node Reroute
    reroute = wiring_layer_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Named Attribute.001
    named_attribute_001 = wiring_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'BOOLEAN'

    # Node Switch
    switch = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'GEOMETRY'

    # Node Join Geometry
    join_geometry = wiring_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Domain Size
    domain_size = wiring_layer_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.hide = True
    domain_size.show_options = True
    domain_size.component = 'MESH'

    # Node Skin Cutout 2
    skin_cutout_2 = wiring_layer_1.nodes.new("GeometryNodeGroup")
    skin_cutout_2.name = "Skin Cutout 2"
    skin_cutout_2.show_options = True
    skin_cutout_2.node_tree = bpy.data.node_groups[node_tree_names[skin_cutout_2_001_1_node_group]]
    # Socket_3
    skin_cutout_2.inputs[2].default_value = ""

    # Node Separate Geometry.002
    separate_geometry_002 = wiring_layer_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_002.name = "Separate Geometry.002"
    separate_geometry_002.show_options = True
    separate_geometry_002.domain = 'POINT'

    # Node Named Attribute.002
    named_attribute_002 = wiring_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.show_options = True
    named_attribute_002.data_type = 'BOOLEAN'
    # Name
    named_attribute_002.inputs[0].default_value = "original_mesh"

    # Node Switch.001
    switch_001 = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'GEOMETRY'
    # Switch
    switch_001.inputs[0].default_value = False

    # Node Reroute.001
    reroute_001 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Reroute.003
    reroute_003 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketVector"
    # Node Reroute.005
    reroute_005 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketInt"
    # Node Reroute.006
    reroute_006 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.007
    reroute_007 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketInt"
    # Node Reroute.008
    reroute_008 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketInt"
    # Node Reroute.009
    reroute_009 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloat"
    # Node Reroute.010
    reroute_010 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketFloat"
    # Node Reroute.011
    reroute_011 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.012
    reroute_012 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketFloat"
    # Node Reroute.013
    reroute_013 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketFloat"
    # Node Reroute.015
    reroute_015 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketBool"
    # Node Reroute.016
    reroute_016 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    reroute_016.socket_idname = "NodeSocketFloat"
    # Node Reroute.018
    reroute_018 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    reroute_018.socket_idname = "NodeSocketVector"
    # Node Reroute.021
    reroute_021 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.show_options = True
    reroute_021.socket_idname = "NodeSocketInt"
    # Node Reroute.022
    reroute_022 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    reroute_022.show_options = True
    reroute_022.socket_idname = "NodeSocketFloat"
    # Node Reroute.023
    reroute_023 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.show_options = True
    reroute_023.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.024
    reroute_024 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.show_options = True
    reroute_024.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.025
    reroute_025 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.show_options = True
    reroute_025.socket_idname = "NodeSocketFloat"
    # Node Reroute.026
    reroute_026 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.show_options = True
    reroute_026.socket_idname = "NodeSocketFloat"
    # Node Reroute.027
    reroute_027 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    reroute_027.show_options = True
    reroute_027.socket_idname = "NodeSocketInt"
    # Node Reroute.028
    reroute_028 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    reroute_028.show_options = True
    reroute_028.socket_idname = "NodeSocketBool"
    # Node Reroute.029
    reroute_029 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_029.name = "Reroute.029"
    reroute_029.show_options = True
    reroute_029.socket_idname = "NodeSocketFloat"
    # Node Reroute.030
    reroute_030 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_030.name = "Reroute.030"
    reroute_030.show_options = True
    reroute_030.socket_idname = "NodeSocketInt"
    # Node Reroute.031
    reroute_031 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_031.name = "Reroute.031"
    reroute_031.show_options = True
    reroute_031.socket_idname = "NodeSocketFloatDistance"
    # Node Switch.002
    switch_002 = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.show_options = True
    switch_002.input_type = 'GEOMETRY'

    # Node Reroute.033
    reroute_033 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_033.name = "Reroute.033"
    reroute_033.show_options = True
    reroute_033.socket_idname = "NodeSocketGeometry"
    # Node Switch.004
    switch_004 = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.show_options = True
    switch_004.input_type = 'GEOMETRY'

    # Node Reroute.034
    reroute_034 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_034.name = "Reroute.034"
    reroute_034.show_options = True
    reroute_034.socket_idname = "NodeSocketBool"
    # Node Reroute.035
    reroute_035 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_035.name = "Reroute.035"
    reroute_035.show_options = True
    reroute_035.socket_idname = "NodeSocketBool"
    # Node Sample Index
    sample_index = wiring_layer_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT'
    sample_index.domain = 'POINT'
    # Index
    sample_index.inputs[2].default_value = 0

    # Node Named Attribute.003
    named_attribute_003 = wiring_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.show_options = True
    named_attribute_003.data_type = 'FLOAT'
    # Name
    named_attribute_003.inputs[0].default_value = "thickness"

    # Node Math
    math = wiring_layer_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Math.001
    math_001 = wiring_layer_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.hide = True
    math_001.show_options = True
    math_001.operation = 'DIVIDE'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 100.0

    # Node Reroute.036
    reroute_036 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_036.name = "Reroute.036"
    reroute_036.show_options = True
    reroute_036.socket_idname = "NodeSocketFloatPercentage"
    # Node Flip Faces.001
    flip_faces_001 = wiring_layer_1.nodes.new("GeometryNodeGroup")
    flip_faces_001.name = "Flip Faces.001"
    flip_faces_001.show_options = True
    flip_faces_001.node_tree = bpy.data.node_groups[node_tree_names[remove_boundary_1_node_group]]

    # Node Flip Faces
    flip_faces = wiring_layer_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    flip_faces.show_options = True
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Separate Geometry.003
    separate_geometry_003 = wiring_layer_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_003.name = "Separate Geometry.003"
    separate_geometry_003.show_options = True
    separate_geometry_003.domain = 'POINT'

    # Node Named Attribute.004
    named_attribute_004 = wiring_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_004.name = "Named Attribute.004"
    named_attribute_004.show_options = True
    named_attribute_004.data_type = 'BOOLEAN'
    # Name
    named_attribute_004.inputs[0].default_value = "wiring_endpoint"

    # Node Reroute.037
    reroute_037 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_037.name = "Reroute.037"
    reroute_037.show_options = True
    reroute_037.socket_idname = "NodeSocketObject"
    # Node Object Info
    object_info = wiring_layer_1.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.show_options = True
    object_info.transform_space = 'RELATIVE'
    # As Instance
    object_info.inputs[1].default_value = False

    # Node Menu Switch.002
    menu_switch_002 = wiring_layer_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch_002.name = "Menu Switch.002"
    menu_switch_002.show_options = True
    menu_switch_002.active_index = 1
    menu_switch_002.data_type = 'BOOLEAN'
    menu_switch_002.enum_items.clear()
    menu_switch_002.enum_items.new("Default")
    menu_switch_002.enum_items[0].description = ""
    menu_switch_002.enum_items.new("Advanced")
    menu_switch_002.enum_items[1].description = ""
    # Item_0
    menu_switch_002.inputs[1].default_value = True
    # Item_1
    menu_switch_002.inputs[2].default_value = False

    # Node Switch.005
    switch_005 = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch_005.name = "Switch.005"
    switch_005.show_options = True
    switch_005.input_type = 'STRING'
    # True
    switch_005.inputs[2].default_value = "dermis_bottom"

    # Node Switch.006
    switch_006 = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch_006.name = "Switch.006"
    switch_006.show_options = True
    switch_006.input_type = 'STRING'
    # True
    switch_006.inputs[2].default_value = "wiring_endpoint"

    # Node Reroute.004
    reroute_004 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketBool"
    # Node Menu Switch.001
    menu_switch_001 = wiring_layer_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch_001.name = "Menu Switch.001"
    menu_switch_001.show_options = True
    menu_switch_001.active_index = 2
    menu_switch_001.data_type = 'GEOMETRY'
    menu_switch_001.enum_items.clear()
    menu_switch_001.enum_items.new("Generate Clips")
    menu_switch_001.enum_items[0].description = ""
    menu_switch_001.enum_items.new("Custom Clips")
    menu_switch_001.enum_items[1].description = ""
    menu_switch_001.enum_items.new("Just Endpoints")
    menu_switch_001.enum_items[2].description = ""

    # Node Separate Geometry.004
    separate_geometry_004 = wiring_layer_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_004.name = "Separate Geometry.004"
    separate_geometry_004.show_options = True
    separate_geometry_004.domain = 'POINT'

    # Node Named Attribute.005
    named_attribute_005 = wiring_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_005.name = "Named Attribute.005"
    named_attribute_005.show_options = True
    named_attribute_005.data_type = 'BOOLEAN'

    # Node Separate Geometry.005
    separate_geometry_005 = wiring_layer_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_005.name = "Separate Geometry.005"
    separate_geometry_005.show_options = True
    separate_geometry_005.domain = 'POINT'

    # Node Named Attribute.006
    named_attribute_006 = wiring_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_006.name = "Named Attribute.006"
    named_attribute_006.show_options = True
    named_attribute_006.data_type = 'BOOLEAN'

    # Node Switch.003
    switch_003 = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.show_options = True
    switch_003.input_type = 'GEOMETRY'

    # Node Separate Geometry.006
    separate_geometry_006 = wiring_layer_1.nodes.new("GeometryNodeGroup")
    separate_geometry_006.name = "Separate Geometry.006"
    separate_geometry_006.show_options = True
    separate_geometry_006.node_tree = bpy.data.node_groups[node_tree_names[filter_points_by_index_1_node_group]]

    # Node Separate Geometry.007
    separate_geometry_007 = wiring_layer_1.nodes.new("GeometryNodeGroup")
    separate_geometry_007.name = "Separate Geometry.007"
    separate_geometry_007.show_options = True
    separate_geometry_007.node_tree = bpy.data.node_groups[node_tree_names[filter_points_by_index_1_node_group]]

    # Node Reroute.014
    reroute_014 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    reroute_014.socket_idname = "NodeSocketInt"
    # Node Viewer
    viewer = wiring_layer_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")

    # Node Reroute.017
    reroute_017 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.show_options = True
    reroute_017.socket_idname = "NodeSocketVector"
    # Node Reroute.019
    reroute_019 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    reroute_019.socket_idname = "NodeSocketVector"
    # Node Menu Switch.003
    menu_switch_003 = wiring_layer_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch_003.name = "Menu Switch.003"
    menu_switch_003.show_options = True
    menu_switch_003.active_index = 0
    menu_switch_003.data_type = 'GEOMETRY'
    menu_switch_003.enum_items.clear()
    menu_switch_003.enum_items.new("Default")
    menu_switch_003.enum_items[0].description = ""
    menu_switch_003.enum_items.new("Isolate Electrodes")
    menu_switch_003.enum_items[1].description = ""
    menu_switch_003.enum_items.new("Isolate Clips")
    menu_switch_003.enum_items[2].description = ""

    # Node Reroute.020
    reroute_020 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.show_options = True
    reroute_020.socket_idname = "NodeSocketMenu"
    # Node Reroute.032
    reroute_032 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_032.name = "Reroute.032"
    reroute_032.show_options = True
    reroute_032.socket_idname = "NodeSocketMenu"
    # Node Instance on Points
    instance_on_points = wiring_layer_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Boolean Math
    boolean_math = wiring_layer_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.hide = True
    boolean_math.show_options = True
    boolean_math.operation = 'OR'

    # Node Switch.007
    switch_007 = wiring_layer_1.nodes.new("GeometryNodeSwitch")
    switch_007.name = "Switch.007"
    switch_007.show_options = True
    switch_007.input_type = 'GEOMETRY'

    # Node Reroute.038
    reroute_038 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_038.name = "Reroute.038"
    reroute_038.show_options = True
    reroute_038.socket_idname = "NodeSocketGeometry"
    # Node UV Sphere
    uv_sphere = wiring_layer_1.nodes.new("GeometryNodeMeshUVSphere")
    uv_sphere.name = "UV Sphere"
    uv_sphere.show_options = True
    # Segments
    uv_sphere.inputs[0].default_value = 32
    # Rings
    uv_sphere.inputs[1].default_value = 16
    # Radius
    uv_sphere.inputs[2].default_value = 0.0020000000949949026

    # Node Viewer.001
    viewer_001 = wiring_layer_1.nodes.new("GeometryNodeViewer")
    viewer_001.name = "Viewer.001"
    viewer_001.show_options = True
    viewer_001.active_index = 0
    viewer_001.domain = 'INSTANCE'
    viewer_001.ui_shortcut = 0
    viewer_001.viewer_items.clear()

    # Node Index
    index = wiring_layer_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Object Info.001
    object_info_001 = wiring_layer_1.nodes.new("GeometryNodeObjectInfo")
    object_info_001.name = "Object Info.001"
    object_info_001.show_options = True
    object_info_001.transform_space = 'RELATIVE'
    # As Instance
    object_info_001.inputs[1].default_value = False

    # Node Mesh Boolean
    mesh_boolean = wiring_layer_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.show_options = True
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'FLOAT'

    # Node Join Geometry.001
    join_geometry_001 = wiring_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Reroute.002
    reroute_002 = wiring_layer_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Set locations
    wiring_layer_1.nodes["Group Input"].location = (-3540.0, -60.0)
    wiring_layer_1.nodes["Group Output"].location = (2260.0, -260.0)
    wiring_layer_1.nodes["Group.018"].location = (100.0, 100.0)
    wiring_layer_1.nodes["Group.011"].location = (-1300.0, 320.0)
    wiring_layer_1.nodes["Separate Geometry"].location = (-2420.0, 480.0)
    wiring_layer_1.nodes["Named Attribute"].location = (-2740.0, 480.0)
    wiring_layer_1.nodes["Separate Geometry.001"].location = (-2420.0, 320.0)
    wiring_layer_1.nodes["Reroute"].location = (-2500.0, 300.0)
    wiring_layer_1.nodes["Named Attribute.001"].location = (-2740.0, 340.0)
    wiring_layer_1.nodes["Switch"].location = (920.0, 80.0)
    wiring_layer_1.nodes["Join Geometry"].location = (1220.0, -240.0)
    wiring_layer_1.nodes["Domain Size"].location = (-1880.0, 120.0)
    wiring_layer_1.nodes["Skin Cutout 2"].location = (-1680.0, -260.0)
    wiring_layer_1.nodes["Separate Geometry.002"].location = (-2420.0, 640.0)
    wiring_layer_1.nodes["Named Attribute.002"].location = (-2740.0, 620.0)
    wiring_layer_1.nodes["Switch.001"].location = (-1120.0, -140.0)
    wiring_layer_1.nodes["Reroute.001"].location = (-1480.0, 240.0)
    wiring_layer_1.nodes["Reroute.003"].location = (-760.0, -900.0)
    wiring_layer_1.nodes["Reroute.005"].location = (-760.0, -1000.0)
    wiring_layer_1.nodes["Reroute.006"].location = (-760.0, -880.0)
    wiring_layer_1.nodes["Reroute.007"].location = (-740.0, -680.0)
    wiring_layer_1.nodes["Reroute.008"].location = (-760.0, -980.0)
    wiring_layer_1.nodes["Reroute.009"].location = (-760.0, -860.0)
    wiring_layer_1.nodes["Reroute.010"].location = (-760.0, -960.0)
    wiring_layer_1.nodes["Reroute.011"].location = (-760.0, -840.0)
    wiring_layer_1.nodes["Reroute.012"].location = (-740.0, -720.0)
    wiring_layer_1.nodes["Reroute.013"].location = (-740.0, -700.0)
    wiring_layer_1.nodes["Reroute.015"].location = (-760.0, -820.0)
    wiring_layer_1.nodes["Reroute.016"].location = (-760.0, -920.0)
    wiring_layer_1.nodes["Reroute.018"].location = (-1960.0, -900.0)
    wiring_layer_1.nodes["Reroute.021"].location = (-1960.0, -1000.0)
    wiring_layer_1.nodes["Reroute.022"].location = (-1960.0, -860.0)
    wiring_layer_1.nodes["Reroute.023"].location = (-1960.0, -700.0)
    wiring_layer_1.nodes["Reroute.024"].location = (-1960.0, -880.0)
    wiring_layer_1.nodes["Reroute.025"].location = (-1960.0, -720.0)
    wiring_layer_1.nodes["Reroute.026"].location = (-1960.0, -960.0)
    wiring_layer_1.nodes["Reroute.027"].location = (-1960.0, -980.0)
    wiring_layer_1.nodes["Reroute.028"].location = (-1960.0, -820.0)
    wiring_layer_1.nodes["Reroute.029"].location = (-1960.0, -920.0)
    wiring_layer_1.nodes["Reroute.030"].location = (-1960.0, -680.0)
    wiring_layer_1.nodes["Reroute.031"].location = (-1960.0, -840.0)
    wiring_layer_1.nodes["Switch.002"].location = (-400.0, 560.0)
    wiring_layer_1.nodes["Reroute.033"].location = (520.0, 160.0)
    wiring_layer_1.nodes["Switch.004"].location = (540.0, -520.0)
    wiring_layer_1.nodes["Reroute.034"].location = (-760.0, -1020.0)
    wiring_layer_1.nodes["Reroute.035"].location = (-1960.0, -1020.0)
    wiring_layer_1.nodes["Sample Index"].location = (-1660.0, 762.7564697265625)
    wiring_layer_1.nodes["Named Attribute.003"].location = (-1840.0, 700.479736328125)
    wiring_layer_1.nodes["Math"].location = (-1380.0, -320.0)
    wiring_layer_1.nodes["Math.001"].location = (-1600.0, -700.0)
    wiring_layer_1.nodes["Reroute.036"].location = (-1633.71142578125, -700.0)
    wiring_layer_1.nodes["Flip Faces.001"].location = (-1380.0, -40.0)
    wiring_layer_1.nodes["Flip Faces"].location = (-1720.0, 260.0)
    wiring_layer_1.nodes["Separate Geometry.003"].location = (-1000.0, 740.0)
    wiring_layer_1.nodes["Named Attribute.004"].location = (-1360.0, 840.0)
    wiring_layer_1.nodes["Reroute.037"].location = (-1420.0, 200.0)
    wiring_layer_1.nodes["Object Info"].location = (-1340.0, 660.0)
    wiring_layer_1.nodes["Menu Switch.002"].location = (-3320.0, 580.0)
    wiring_layer_1.nodes["Switch.005"].location = (-3020.0, 520.0)
    wiring_layer_1.nodes["Switch.006"].location = (-3020.0, 360.0)
    wiring_layer_1.nodes["Reroute.004"].location = (-3060.0, 460.0)
    wiring_layer_1.nodes["Menu Switch.001"].location = (-780.0, 200.0)
    wiring_layer_1.nodes["Separate Geometry.004"].location = (-2420.0, 160.0)
    wiring_layer_1.nodes["Named Attribute.005"].location = (-2740.0, 180.0)
    wiring_layer_1.nodes["Separate Geometry.005"].location = (-2420.0, 0.0)
    wiring_layer_1.nodes["Named Attribute.006"].location = (-2740.0, 20.0)
    wiring_layer_1.nodes["Switch.003"].location = (-540.0, 100.0)
    wiring_layer_1.nodes["Separate Geometry.006"].location = (-1900.0, 0.0)
    wiring_layer_1.nodes["Separate Geometry.007"].location = (-2239.99951171875, 180.0)
    wiring_layer_1.nodes["Reroute.014"].location = (-2071.697998046875, -108.05559539794922)
    wiring_layer_1.nodes["Viewer"].location = (880.0, 440.0)
    wiring_layer_1.nodes["Reroute.017"].location = (-760.0, -940.0)
    wiring_layer_1.nodes["Reroute.019"].location = (-1960.0, -940.0)
    wiring_layer_1.nodes["Menu Switch.003"].location = (1460.0, -260.0)
    wiring_layer_1.nodes["Reroute.020"].location = (-740.0, -1060.0)
    wiring_layer_1.nodes["Reroute.032"].location = (-1960.0, -1060.0)
    wiring_layer_1.nodes["Instance on Points"].location = (1900.0, -380.0)
    wiring_layer_1.nodes["Boolean Math"].location = (1620.0, -380.0)
    wiring_layer_1.nodes["Switch.007"].location = (2080.0, -60.0)
    wiring_layer_1.nodes["Reroute.038"].location = (1834.9569091796875, -307.01312255859375)
    wiring_layer_1.nodes["UV Sphere"].location = (1460.0, -480.0)
    wiring_layer_1.nodes["Viewer.001"].location = (960.0, -440.0)
    wiring_layer_1.nodes["Index"].location = (2080.0, -440.0)
    wiring_layer_1.nodes["Object Info.001"].location = (460.0, 460.0)
    wiring_layer_1.nodes["Mesh Boolean"].location = (700.0, 280.0)
    wiring_layer_1.nodes["Join Geometry.001"].location = (1260.0, -60.0)
    wiring_layer_1.nodes["Reroute.002"].location = (1015.11328125, -188.9800262451172)

    # Set dimensions
    wiring_layer_1.nodes["Group Input"].width  = 140.0
    wiring_layer_1.nodes["Group Input"].height = 100.0

    wiring_layer_1.nodes["Group Output"].width  = 140.0
    wiring_layer_1.nodes["Group Output"].height = 100.0

    wiring_layer_1.nodes["Group.018"].width  = 380.0
    wiring_layer_1.nodes["Group.018"].height = 100.0

    wiring_layer_1.nodes["Group.011"].width  = 400.0
    wiring_layer_1.nodes["Group.011"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry"].width  = 140.0
    wiring_layer_1.nodes["Separate Geometry"].height = 100.0

    wiring_layer_1.nodes["Named Attribute"].width  = 140.0
    wiring_layer_1.nodes["Named Attribute"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry.001"].width  = 140.0
    wiring_layer_1.nodes["Separate Geometry.001"].height = 100.0

    wiring_layer_1.nodes["Reroute"].width  = 14.5
    wiring_layer_1.nodes["Reroute"].height = 100.0

    wiring_layer_1.nodes["Named Attribute.001"].width  = 140.0
    wiring_layer_1.nodes["Named Attribute.001"].height = 100.0

    wiring_layer_1.nodes["Switch"].width  = 140.0
    wiring_layer_1.nodes["Switch"].height = 100.0

    wiring_layer_1.nodes["Join Geometry"].width  = 140.0
    wiring_layer_1.nodes["Join Geometry"].height = 100.0

    wiring_layer_1.nodes["Domain Size"].width  = 140.0
    wiring_layer_1.nodes["Domain Size"].height = 100.0

    wiring_layer_1.nodes["Skin Cutout 2"].width  = 140.0
    wiring_layer_1.nodes["Skin Cutout 2"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry.002"].width  = 140.0
    wiring_layer_1.nodes["Separate Geometry.002"].height = 100.0

    wiring_layer_1.nodes["Named Attribute.002"].width  = 140.0
    wiring_layer_1.nodes["Named Attribute.002"].height = 100.0

    wiring_layer_1.nodes["Switch.001"].width  = 140.0
    wiring_layer_1.nodes["Switch.001"].height = 100.0

    wiring_layer_1.nodes["Reroute.001"].width  = 14.5
    wiring_layer_1.nodes["Reroute.001"].height = 100.0

    wiring_layer_1.nodes["Reroute.003"].width  = 14.5
    wiring_layer_1.nodes["Reroute.003"].height = 100.0

    wiring_layer_1.nodes["Reroute.005"].width  = 14.5
    wiring_layer_1.nodes["Reroute.005"].height = 100.0

    wiring_layer_1.nodes["Reroute.006"].width  = 14.5
    wiring_layer_1.nodes["Reroute.006"].height = 100.0

    wiring_layer_1.nodes["Reroute.007"].width  = 14.5
    wiring_layer_1.nodes["Reroute.007"].height = 100.0

    wiring_layer_1.nodes["Reroute.008"].width  = 14.5
    wiring_layer_1.nodes["Reroute.008"].height = 100.0

    wiring_layer_1.nodes["Reroute.009"].width  = 14.5
    wiring_layer_1.nodes["Reroute.009"].height = 100.0

    wiring_layer_1.nodes["Reroute.010"].width  = 14.5
    wiring_layer_1.nodes["Reroute.010"].height = 100.0

    wiring_layer_1.nodes["Reroute.011"].width  = 14.5
    wiring_layer_1.nodes["Reroute.011"].height = 100.0

    wiring_layer_1.nodes["Reroute.012"].width  = 14.5
    wiring_layer_1.nodes["Reroute.012"].height = 100.0

    wiring_layer_1.nodes["Reroute.013"].width  = 14.5
    wiring_layer_1.nodes["Reroute.013"].height = 100.0

    wiring_layer_1.nodes["Reroute.015"].width  = 14.5
    wiring_layer_1.nodes["Reroute.015"].height = 100.0

    wiring_layer_1.nodes["Reroute.016"].width  = 14.5
    wiring_layer_1.nodes["Reroute.016"].height = 100.0

    wiring_layer_1.nodes["Reroute.018"].width  = 14.5
    wiring_layer_1.nodes["Reroute.018"].height = 100.0

    wiring_layer_1.nodes["Reroute.021"].width  = 14.5
    wiring_layer_1.nodes["Reroute.021"].height = 100.0

    wiring_layer_1.nodes["Reroute.022"].width  = 14.5
    wiring_layer_1.nodes["Reroute.022"].height = 100.0

    wiring_layer_1.nodes["Reroute.023"].width  = 14.5
    wiring_layer_1.nodes["Reroute.023"].height = 100.0

    wiring_layer_1.nodes["Reroute.024"].width  = 14.5
    wiring_layer_1.nodes["Reroute.024"].height = 100.0

    wiring_layer_1.nodes["Reroute.025"].width  = 14.5
    wiring_layer_1.nodes["Reroute.025"].height = 100.0

    wiring_layer_1.nodes["Reroute.026"].width  = 14.5
    wiring_layer_1.nodes["Reroute.026"].height = 100.0

    wiring_layer_1.nodes["Reroute.027"].width  = 14.5
    wiring_layer_1.nodes["Reroute.027"].height = 100.0

    wiring_layer_1.nodes["Reroute.028"].width  = 14.5
    wiring_layer_1.nodes["Reroute.028"].height = 100.0

    wiring_layer_1.nodes["Reroute.029"].width  = 14.5
    wiring_layer_1.nodes["Reroute.029"].height = 100.0

    wiring_layer_1.nodes["Reroute.030"].width  = 14.5
    wiring_layer_1.nodes["Reroute.030"].height = 100.0

    wiring_layer_1.nodes["Reroute.031"].width  = 14.5
    wiring_layer_1.nodes["Reroute.031"].height = 100.0

    wiring_layer_1.nodes["Switch.002"].width  = 140.0
    wiring_layer_1.nodes["Switch.002"].height = 100.0

    wiring_layer_1.nodes["Reroute.033"].width  = 14.5
    wiring_layer_1.nodes["Reroute.033"].height = 100.0

    wiring_layer_1.nodes["Switch.004"].width  = 140.0
    wiring_layer_1.nodes["Switch.004"].height = 100.0

    wiring_layer_1.nodes["Reroute.034"].width  = 14.5
    wiring_layer_1.nodes["Reroute.034"].height = 100.0

    wiring_layer_1.nodes["Reroute.035"].width  = 14.5
    wiring_layer_1.nodes["Reroute.035"].height = 100.0

    wiring_layer_1.nodes["Sample Index"].width  = 140.0
    wiring_layer_1.nodes["Sample Index"].height = 100.0

    wiring_layer_1.nodes["Named Attribute.003"].width  = 140.0
    wiring_layer_1.nodes["Named Attribute.003"].height = 100.0

    wiring_layer_1.nodes["Math"].width  = 140.0
    wiring_layer_1.nodes["Math"].height = 100.0

    wiring_layer_1.nodes["Math.001"].width  = 140.0
    wiring_layer_1.nodes["Math.001"].height = 100.0

    wiring_layer_1.nodes["Reroute.036"].width  = 14.5
    wiring_layer_1.nodes["Reroute.036"].height = 100.0

    wiring_layer_1.nodes["Flip Faces.001"].width  = 220.0
    wiring_layer_1.nodes["Flip Faces.001"].height = 100.0

    wiring_layer_1.nodes["Flip Faces"].width  = 140.0
    wiring_layer_1.nodes["Flip Faces"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry.003"].width  = 140.0
    wiring_layer_1.nodes["Separate Geometry.003"].height = 100.0

    wiring_layer_1.nodes["Named Attribute.004"].width  = 140.0
    wiring_layer_1.nodes["Named Attribute.004"].height = 100.0

    wiring_layer_1.nodes["Reroute.037"].width  = 14.5
    wiring_layer_1.nodes["Reroute.037"].height = 100.0

    wiring_layer_1.nodes["Object Info"].width  = 140.0
    wiring_layer_1.nodes["Object Info"].height = 100.0

    wiring_layer_1.nodes["Menu Switch.002"].width  = 140.0
    wiring_layer_1.nodes["Menu Switch.002"].height = 100.0

    wiring_layer_1.nodes["Switch.005"].width  = 200.0
    wiring_layer_1.nodes["Switch.005"].height = 100.0

    wiring_layer_1.nodes["Switch.006"].width  = 200.0
    wiring_layer_1.nodes["Switch.006"].height = 100.0

    wiring_layer_1.nodes["Reroute.004"].width  = 14.5
    wiring_layer_1.nodes["Reroute.004"].height = 100.0

    wiring_layer_1.nodes["Menu Switch.001"].width  = 140.0
    wiring_layer_1.nodes["Menu Switch.001"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry.004"].width  = 140.0
    wiring_layer_1.nodes["Separate Geometry.004"].height = 100.0

    wiring_layer_1.nodes["Named Attribute.005"].width  = 140.0
    wiring_layer_1.nodes["Named Attribute.005"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry.005"].width  = 140.0
    wiring_layer_1.nodes["Separate Geometry.005"].height = 100.0

    wiring_layer_1.nodes["Named Attribute.006"].width  = 140.0
    wiring_layer_1.nodes["Named Attribute.006"].height = 100.0

    wiring_layer_1.nodes["Switch.003"].width  = 140.0
    wiring_layer_1.nodes["Switch.003"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry.006"].width  = 240.0
    wiring_layer_1.nodes["Separate Geometry.006"].height = 100.0

    wiring_layer_1.nodes["Separate Geometry.007"].width  = 140.0
    wiring_layer_1.nodes["Separate Geometry.007"].height = 100.0

    wiring_layer_1.nodes["Reroute.014"].width  = 14.5
    wiring_layer_1.nodes["Reroute.014"].height = 100.0

    wiring_layer_1.nodes["Viewer"].width  = 140.0
    wiring_layer_1.nodes["Viewer"].height = 100.0

    wiring_layer_1.nodes["Reroute.017"].width  = 14.5
    wiring_layer_1.nodes["Reroute.017"].height = 100.0

    wiring_layer_1.nodes["Reroute.019"].width  = 14.5
    wiring_layer_1.nodes["Reroute.019"].height = 100.0

    wiring_layer_1.nodes["Menu Switch.003"].width  = 140.0
    wiring_layer_1.nodes["Menu Switch.003"].height = 100.0

    wiring_layer_1.nodes["Reroute.020"].width  = 14.5
    wiring_layer_1.nodes["Reroute.020"].height = 100.0

    wiring_layer_1.nodes["Reroute.032"].width  = 14.5
    wiring_layer_1.nodes["Reroute.032"].height = 100.0

    wiring_layer_1.nodes["Instance on Points"].width  = 140.0
    wiring_layer_1.nodes["Instance on Points"].height = 100.0

    wiring_layer_1.nodes["Boolean Math"].width  = 140.0
    wiring_layer_1.nodes["Boolean Math"].height = 100.0

    wiring_layer_1.nodes["Switch.007"].width  = 140.0
    wiring_layer_1.nodes["Switch.007"].height = 100.0

    wiring_layer_1.nodes["Reroute.038"].width  = 14.5
    wiring_layer_1.nodes["Reroute.038"].height = 100.0

    wiring_layer_1.nodes["UV Sphere"].width  = 140.0
    wiring_layer_1.nodes["UV Sphere"].height = 100.0

    wiring_layer_1.nodes["Viewer.001"].width  = 140.0
    wiring_layer_1.nodes["Viewer.001"].height = 100.0

    wiring_layer_1.nodes["Index"].width  = 140.0
    wiring_layer_1.nodes["Index"].height = 100.0

    wiring_layer_1.nodes["Object Info.001"].width  = 140.0
    wiring_layer_1.nodes["Object Info.001"].height = 100.0

    wiring_layer_1.nodes["Mesh Boolean"].width  = 140.0
    wiring_layer_1.nodes["Mesh Boolean"].height = 100.0

    wiring_layer_1.nodes["Join Geometry.001"].width  = 140.0
    wiring_layer_1.nodes["Join Geometry.001"].height = 100.0

    wiring_layer_1.nodes["Reroute.002"].width  = 14.5
    wiring_layer_1.nodes["Reroute.002"].height = 100.0


    # Initialize wiring_layer_1 links

    # named_attribute.Attribute -> separate_geometry.Selection
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Named Attribute"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry"].inputs[1]
    )
    # reroute.Output -> separate_geometry.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry"].inputs[0]
    )
    # reroute_037.Output -> group_011.Clip Reference
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.037"].outputs[0],
        wiring_layer_1.nodes["Group.011"].inputs[0]
    )
    # group_input.Geometry -> reroute.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[0],
        wiring_layer_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> separate_geometry_001.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.001"].inputs[0]
    )
    # named_attribute_001.Attribute -> separate_geometry_001.Selection
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Named Attribute.001"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.001"].inputs[1]
    )
    # group_input.Seperation -> group_011.Seperation
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[9],
        wiring_layer_1.nodes["Group.011"].inputs[2]
    )
    # group_input.Isolate -> switch.Switch
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[1],
        wiring_layer_1.nodes["Switch"].inputs[0]
    )
    # switch_007.Output -> group_output.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.007"].outputs[0],
        wiring_layer_1.nodes["Group Output"].inputs[0]
    )
    # domain_size.Point Count -> group_011.Count
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Domain Size"].outputs[0],
        wiring_layer_1.nodes["Group.011"].inputs[3]
    )
    # separate_geometry_001.Selection -> domain_size.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.001"].outputs[0],
        wiring_layer_1.nodes["Domain Size"].inputs[0]
    )
    # group_input.Depth -> group_011.Depth
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[10],
        wiring_layer_1.nodes["Group.011"].inputs[4]
    )
    # group_input.Radius -> group_011.Radius
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[11],
        wiring_layer_1.nodes["Group.011"].inputs[5]
    )
    # group_input.Rotation -> group_011.Rotation
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[12],
        wiring_layer_1.nodes["Group.011"].inputs[6]
    )
    # group_input.Translation -> group_011.Translattion
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[13],
        wiring_layer_1.nodes["Group.011"].inputs[7]
    )
    # reroute.Output -> separate_geometry_002.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.002"].inputs[0]
    )
    # named_attribute_002.Attribute -> separate_geometry_002.Selection
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Named Attribute.002"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.002"].inputs[1]
    )
    # separate_geometry_002.Selection -> skin_cutout_2.Mesh
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.002"].outputs[0],
        wiring_layer_1.nodes["Skin Cutout 2"].inputs[0]
    )
    # group_input.Smoothing -> skin_cutout_2.Smoothing
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[33],
        wiring_layer_1.nodes["Skin Cutout 2"].inputs[1]
    )
    # group_input.Cutout Tolerance -> skin_cutout_2.Cutout Tolerance
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[34],
        wiring_layer_1.nodes["Skin Cutout 2"].inputs[3]
    )
    # group_input.Smooth Sampling -> skin_cutout_2.Smooth Sampling
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[35],
        wiring_layer_1.nodes["Skin Cutout 2"].inputs[4]
    )
    # skin_cutout_2.Geometry -> switch_001.True
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Skin Cutout 2"].outputs[0],
        wiring_layer_1.nodes["Switch.001"].inputs[2]
    )
    # switch_001.Output -> group_018.Routing Cutout
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.001"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[1]
    )
    # reroute_001.Output -> group_011.Boundary Cutout
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.001"].outputs[0],
        wiring_layer_1.nodes["Group.011"].inputs[1]
    )
    # reroute_007.Output -> group_018.Layers
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.007"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[4]
    )
    # reroute_013.Output -> group_018.Base Offset
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.013"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[5]
    )
    # reroute_012.Output -> group_018.Thickness
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.012"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[6]
    )
    # reroute_015.Output -> group_018.Use Alignment Vector Sorting
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.015"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[10]
    )
    # reroute_011.Output -> group_018.Radius
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.011"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[11]
    )
    # reroute_009.Output -> group_018.Crosstalk Power
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.009"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[12]
    )
    # reroute_006.Output -> group_018.Crosstalk Factor
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.006"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[13]
    )
    # reroute_003.Output -> group_018.Electrode Sorting Vector
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.003"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[14]
    )
    # reroute_016.Output -> group_018.Avoid Distance
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.016"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[16]
    )
    # reroute_010.Output -> group_018.Route Removal Multiplier
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.010"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[17]
    )
    # reroute_008.Output -> group_018.Overlap Accuracy
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.008"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[18]
    )
    # reroute_005.Output -> group_018.Sampling
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.005"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[19]
    )
    # reroute_018.Output -> reroute_003.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.018"].outputs[0],
        wiring_layer_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_021.Output -> reroute_005.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.021"].outputs[0],
        wiring_layer_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_024.Output -> reroute_006.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.024"].outputs[0],
        wiring_layer_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_030.Output -> reroute_007.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.030"].outputs[0],
        wiring_layer_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_027.Output -> reroute_008.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.027"].outputs[0],
        wiring_layer_1.nodes["Reroute.008"].inputs[0]
    )
    # reroute_022.Output -> reroute_009.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.022"].outputs[0],
        wiring_layer_1.nodes["Reroute.009"].inputs[0]
    )
    # reroute_026.Output -> reroute_010.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.026"].outputs[0],
        wiring_layer_1.nodes["Reroute.010"].inputs[0]
    )
    # reroute_031.Output -> reroute_011.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.031"].outputs[0],
        wiring_layer_1.nodes["Reroute.011"].inputs[0]
    )
    # reroute_025.Output -> reroute_012.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.025"].outputs[0],
        wiring_layer_1.nodes["Reroute.012"].inputs[0]
    )
    # reroute_028.Output -> reroute_015.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.028"].outputs[0],
        wiring_layer_1.nodes["Reroute.015"].inputs[0]
    )
    # reroute_029.Output -> reroute_016.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.029"].outputs[0],
        wiring_layer_1.nodes["Reroute.016"].inputs[0]
    )
    # group_input.Electrode Sorting Vector -> reroute_018.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[31],
        wiring_layer_1.nodes["Reroute.018"].inputs[0]
    )
    # group_input.Wire Sampling -> reroute_021.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[22],
        wiring_layer_1.nodes["Reroute.021"].inputs[0]
    )
    # group_input.Crosstalk Power -> reroute_022.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[24],
        wiring_layer_1.nodes["Reroute.022"].inputs[0]
    )
    # group_input.Bottom Layer Offset -> reroute_023.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[16],
        wiring_layer_1.nodes["Reroute.023"].inputs[0]
    )
    # group_input.Crosstalk Factor -> reroute_024.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[25],
        wiring_layer_1.nodes["Reroute.024"].inputs[0]
    )
    # group_input.Layer Separation -> reroute_025.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[17],
        wiring_layer_1.nodes["Reroute.025"].inputs[0]
    )
    # group_input.Route Removal Multiplier -> reroute_026.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[27],
        wiring_layer_1.nodes["Reroute.026"].inputs[0]
    )
    # group_input.Overlap Accuracy -> reroute_027.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[28],
        wiring_layer_1.nodes["Reroute.027"].inputs[0]
    )
    # group_input.Avoid Distance -> reroute_029.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[26],
        wiring_layer_1.nodes["Reroute.029"].inputs[0]
    )
    # group_input.Layers -> reroute_030.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[15],
        wiring_layer_1.nodes["Reroute.030"].inputs[0]
    )
    # group_input.Radius -> reroute_031.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[21],
        wiring_layer_1.nodes["Reroute.031"].inputs[0]
    )
    # group_input.Sort by Vector -> reroute_028.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[29],
        wiring_layer_1.nodes["Reroute.028"].inputs[0]
    )
    # group_011.Clips -> switch_002.True
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group.011"].outputs[0],
        wiring_layer_1.nodes["Switch.002"].inputs[2]
    )
    # switch_002.Output -> reroute_033.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.002"].outputs[0],
        wiring_layer_1.nodes["Reroute.033"].inputs[0]
    )
    # group_018.Routing Layers -> switch_004.True
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group.018"].outputs[2],
        wiring_layer_1.nodes["Switch.004"].inputs[2]
    )
    # reroute_034.Output -> switch_004.Switch
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.034"].outputs[0],
        wiring_layer_1.nodes["Switch.004"].inputs[0]
    )
    # reroute_035.Output -> reroute_034.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.035"].outputs[0],
        wiring_layer_1.nodes["Reroute.034"].inputs[0]
    )
    # group_input.Show Routing Layer -> reroute_035.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[14],
        wiring_layer_1.nodes["Reroute.035"].inputs[0]
    )
    # separate_geometry.Selection -> sample_index.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry"].outputs[0],
        wiring_layer_1.nodes["Sample Index"].inputs[0]
    )
    # named_attribute_003.Attribute -> sample_index.Value
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Named Attribute.003"].outputs[0],
        wiring_layer_1.nodes["Sample Index"].inputs[1]
    )
    # sample_index.Value -> math.Value
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Sample Index"].outputs[0],
        wiring_layer_1.nodes["Math"].inputs[0]
    )
    # reroute_023.Output -> reroute_036.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.023"].outputs[0],
        wiring_layer_1.nodes["Reroute.036"].inputs[0]
    )
    # reroute_036.Output -> math_001.Value
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.036"].outputs[0],
        wiring_layer_1.nodes["Math.001"].inputs[0]
    )
    # math_001.Value -> math.Value
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Math.001"].outputs[0],
        wiring_layer_1.nodes["Math"].inputs[1]
    )
    # math.Value -> reroute_013.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Math"].outputs[0],
        wiring_layer_1.nodes["Reroute.013"].inputs[0]
    )
    # flip_faces_001.Mesh -> switch_001.False
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Flip Faces.001"].outputs[0],
        wiring_layer_1.nodes["Switch.001"].inputs[1]
    )
    # reroute_001.Output -> flip_faces_001.Mesh
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.001"].outputs[0],
        wiring_layer_1.nodes["Flip Faces.001"].inputs[0]
    )
    # separate_geometry.Selection -> flip_faces.Mesh
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry"].outputs[0],
        wiring_layer_1.nodes["Flip Faces"].inputs[0]
    )
    # flip_faces.Mesh -> reroute_001.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Flip Faces"].outputs[0],
        wiring_layer_1.nodes["Reroute.001"].inputs[0]
    )
    # named_attribute_004.Attribute -> separate_geometry_003.Selection
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Named Attribute.004"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.003"].inputs[1]
    )
    # group_input.Clip Reference -> reroute_037.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[7],
        wiring_layer_1.nodes["Reroute.037"].inputs[0]
    )
    # reroute_037.Output -> object_info.Object
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.037"].outputs[0],
        wiring_layer_1.nodes["Object Info"].inputs[0]
    )
    # object_info.Geometry -> separate_geometry_003.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Object Info"].outputs[4],
        wiring_layer_1.nodes["Separate Geometry.003"].inputs[0]
    )
    # group_input.Material -> group_018.Material
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[23],
        wiring_layer_1.nodes["Group.018"].inputs[0]
    )
    # group_input.Routing Self Margin -> group_018.Routing Self Margin
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[20],
        wiring_layer_1.nodes["Group.018"].inputs[9]
    )
    # group_input.Connector Endpoint Margin -> group_018.Connector Endpoint Margin
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[19],
        wiring_layer_1.nodes["Group.018"].inputs[8]
    )
    # group_input.Sensor Endpoint Margin -> group_018.Sensor Endpoint Margin
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[18],
        wiring_layer_1.nodes["Group.018"].inputs[7]
    )
    # group_input.Menu -> menu_switch_002.Menu
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[2],
        wiring_layer_1.nodes["Menu Switch.002"].inputs[0]
    )
    # group_input.Routing Domain Paint Name -> switch_005.False
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[37],
        wiring_layer_1.nodes["Switch.005"].inputs[1]
    )
    # reroute_004.Output -> switch_005.Switch
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.004"].outputs[0],
        wiring_layer_1.nodes["Switch.005"].inputs[0]
    )
    # switch_005.Output -> named_attribute.Name
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.005"].outputs[0],
        wiring_layer_1.nodes["Named Attribute"].inputs[0]
    )
    # menu_switch_002.Output -> reroute_004.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Menu Switch.002"].outputs[0],
        wiring_layer_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_004.Output -> switch_006.Switch
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.004"].outputs[0],
        wiring_layer_1.nodes["Switch.006"].inputs[0]
    )
    # group_input.Electrodes Name -> switch_006.False
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[36],
        wiring_layer_1.nodes["Switch.006"].inputs[1]
    )
    # switch_006.Output -> named_attribute_001.Name
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.006"].outputs[0],
        wiring_layer_1.nodes["Named Attribute.001"].inputs[0]
    )
    # group_input.Clip Points -> menu_switch_001.Menu
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[3],
        wiring_layer_1.nodes["Menu Switch.001"].inputs[0]
    )
    # group_011.Clip Points -> menu_switch_001.Generate Clips
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group.011"].outputs[1],
        wiring_layer_1.nodes["Menu Switch.001"].inputs[1]
    )
    # separate_geometry_003.Selection -> menu_switch_001.Custom Clips
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.003"].outputs[0],
        wiring_layer_1.nodes["Menu Switch.001"].inputs[2]
    )
    # menu_switch_001.Generate Clips -> switch_002.Switch
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Menu Switch.001"].outputs[1],
        wiring_layer_1.nodes["Switch.002"].inputs[0]
    )
    # menu_switch_001.Output -> group_018.Clip Points
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Menu Switch.001"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[2]
    )
    # named_attribute_005.Attribute -> separate_geometry_004.Selection
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Named Attribute.005"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.004"].inputs[1]
    )
    # reroute.Output -> separate_geometry_004.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.004"].inputs[0]
    )
    # group_input.Starting Points Paint -> named_attribute_005.Name
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[4],
        wiring_layer_1.nodes["Named Attribute.005"].inputs[0]
    )
    # separate_geometry_007.Points -> menu_switch_001.Just Endpoints
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.007"].outputs[0],
        wiring_layer_1.nodes["Menu Switch.001"].inputs[3]
    )
    # named_attribute_006.Attribute -> separate_geometry_005.Selection
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Named Attribute.006"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.005"].inputs[1]
    )
    # reroute.Output -> separate_geometry_005.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.005"].inputs[0]
    )
    # group_input.Electrode Points Paint -> named_attribute_006.Name
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[5],
        wiring_layer_1.nodes["Named Attribute.006"].inputs[0]
    )
    # menu_switch_001.Just Endpoints -> switch_003.Switch
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Menu Switch.001"].outputs[3],
        wiring_layer_1.nodes["Switch.003"].inputs[0]
    )
    # separate_geometry_001.Selection -> switch_003.False
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.001"].outputs[0],
        wiring_layer_1.nodes["Switch.003"].inputs[1]
    )
    # switch_003.Output -> group_018.Electrode Points
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.003"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[3]
    )
    # separate_geometry_005.Selection -> separate_geometry_006.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.005"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.006"].inputs[0]
    )
    # reroute_014.Output -> separate_geometry_006.Point Count
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.014"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.006"].inputs[1]
    )
    # separate_geometry_006.Points -> switch_003.True
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.006"].outputs[0],
        wiring_layer_1.nodes["Switch.003"].inputs[2]
    )
    # separate_geometry_004.Selection -> separate_geometry_007.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.004"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.007"].inputs[0]
    )
    # group_input.Point Count -> reroute_014.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[6],
        wiring_layer_1.nodes["Reroute.014"].inputs[0]
    )
    # reroute_014.Output -> separate_geometry_007.Point Count
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.014"].outputs[0],
        wiring_layer_1.nodes["Separate Geometry.007"].inputs[1]
    )
    # object_info_001.Geometry -> viewer.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Object Info.001"].outputs[4],
        wiring_layer_1.nodes["Viewer"].inputs[0]
    )
    # reroute_017.Output -> group_018.Clip Sorting Vector
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.017"].outputs[0],
        wiring_layer_1.nodes["Group.018"].inputs[15]
    )
    # reroute_019.Output -> reroute_017.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.019"].outputs[0],
        wiring_layer_1.nodes["Reroute.017"].inputs[0]
    )
    # group_input.Clip Sorting Vector -> reroute_019.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[32],
        wiring_layer_1.nodes["Reroute.019"].inputs[0]
    )
    # join_geometry.Geometry -> menu_switch_003.Default
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Join Geometry"].outputs[0],
        wiring_layer_1.nodes["Menu Switch.003"].inputs[1]
    )
    # reroute_020.Output -> menu_switch_003.Menu
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.020"].outputs[0],
        wiring_layer_1.nodes["Menu Switch.003"].inputs[0]
    )
    # reroute_032.Output -> reroute_020.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.032"].outputs[0],
        wiring_layer_1.nodes["Reroute.020"].inputs[0]
    )
    # group_input.Sorting View -> reroute_032.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[30],
        wiring_layer_1.nodes["Reroute.032"].inputs[0]
    )
    # separate_geometry_006.Points -> menu_switch_003.Isolate Electrodes
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.006"].outputs[0],
        wiring_layer_1.nodes["Menu Switch.003"].inputs[2]
    )
    # separate_geometry_007.Points -> menu_switch_003.Isolate Clips
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Separate Geometry.007"].outputs[0],
        wiring_layer_1.nodes["Menu Switch.003"].inputs[3]
    )
    # menu_switch_003.Isolate Electrodes -> boolean_math.Boolean
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Menu Switch.003"].outputs[2],
        wiring_layer_1.nodes["Boolean Math"].inputs[0]
    )
    # menu_switch_003.Isolate Clips -> boolean_math.Boolean
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Menu Switch.003"].outputs[3],
        wiring_layer_1.nodes["Boolean Math"].inputs[1]
    )
    # boolean_math.Boolean -> instance_on_points.Selection
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Boolean Math"].outputs[0],
        wiring_layer_1.nodes["Instance on Points"].inputs[1]
    )
    # reroute_038.Output -> switch_007.False
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.038"].outputs[0],
        wiring_layer_1.nodes["Switch.007"].inputs[1]
    )
    # boolean_math.Boolean -> switch_007.Switch
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Boolean Math"].outputs[0],
        wiring_layer_1.nodes["Switch.007"].inputs[0]
    )
    # instance_on_points.Instances -> switch_007.True
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Instance on Points"].outputs[0],
        wiring_layer_1.nodes["Switch.007"].inputs[2]
    )
    # menu_switch_003.Output -> reroute_038.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Menu Switch.003"].outputs[0],
        wiring_layer_1.nodes["Reroute.038"].inputs[0]
    )
    # reroute_038.Output -> instance_on_points.Points
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.038"].outputs[0],
        wiring_layer_1.nodes["Instance on Points"].inputs[0]
    )
    # uv_sphere.Mesh -> instance_on_points.Instance
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["UV Sphere"].outputs[0],
        wiring_layer_1.nodes["Instance on Points"].inputs[2]
    )
    # switch.Output -> join_geometry.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch"].outputs[0],
        wiring_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # object_info_001.Geometry -> mesh_boolean.Mesh 2
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Object Info.001"].outputs[4],
        wiring_layer_1.nodes["Mesh Boolean"].inputs[1]
    )
    # mesh_boolean.Mesh -> switch.False
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Mesh Boolean"].outputs[0],
        wiring_layer_1.nodes["Switch"].inputs[1]
    )
    # join_geometry_001.Geometry -> group_output.Wires
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Join Geometry.001"].outputs[0],
        wiring_layer_1.nodes["Group Output"].inputs[1]
    )
    # object_info_001.Geometry -> group_output.Connection Port Holes
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Object Info.001"].outputs[4],
        wiring_layer_1.nodes["Group Output"].inputs[2]
    )
    # switch_004.Output -> group_output.Routing Layer
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.004"].outputs[0],
        wiring_layer_1.nodes["Group Output"].inputs[3]
    )
    # group_018.Wire Curves -> join_geometry_001.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group.018"].outputs[1],
        wiring_layer_1.nodes["Join Geometry.001"].inputs[0]
    )
    # reroute_033.Output -> reroute_002.Input
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.033"].outputs[0],
        wiring_layer_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_002.Output -> group_output.Clips
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.002"].outputs[0],
        wiring_layer_1.nodes["Group Output"].inputs[4]
    )
    # switch_004.Output -> join_geometry.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Switch.004"].outputs[0],
        wiring_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Geometry -> mesh_boolean.Mesh 1
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[0],
        wiring_layer_1.nodes["Mesh Boolean"].inputs[0]
    )
    # group_input.Holes -> object_info_001.Object
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group Input"].outputs[8],
        wiring_layer_1.nodes["Object Info.001"].inputs[0]
    )
    # group_018.Wires -> join_geometry_001.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group.018"].outputs[0],
        wiring_layer_1.nodes["Join Geometry.001"].inputs[0]
    )
    # group_018.Wires -> join_geometry.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Group.018"].outputs[0],
        wiring_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # reroute_002.Output -> join_geometry.Geometry
    wiring_layer_1.links.new(
        wiring_layer_1.nodes["Reroute.002"].outputs[0],
        wiring_layer_1.nodes["Join Geometry"].inputs[0]
    )
    menu_socket.default_value = 'Default'
    clip_points_socket.default_value = 'Generate Clips'
    sorting_view_socket.default_value = 'Default'
    viewer.viewer_items[0].auto_remove = True

    return wiring_layer_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    remove_curve_attributes = remove_curve_attributes_1_node_group(node_tree_names)
    node_tree_names[remove_curve_attributes_1_node_group] = remove_curve_attributes.name

    wire_profile_001 = wire_profile_001_1_node_group(node_tree_names)
    node_tree_names[wire_profile_001_1_node_group] = wire_profile_001.name

    instantiate_wire_with_crosstalk_att_001 = instantiate_wire_with_crosstalk_att_001_1_node_group(node_tree_names)
    node_tree_names[instantiate_wire_with_crosstalk_att_001_1_node_group] = instantiate_wire_with_crosstalk_att_001.name

    weighted_zone_heuristic_001 = weighted_zone_heuristic_001_1_node_group(node_tree_names)
    node_tree_names[weighted_zone_heuristic_001_1_node_group] = weighted_zone_heuristic_001.name

    overlap_remover_001 = overlap_remover_001_1_node_group(node_tree_names)
    node_tree_names[overlap_remover_001_1_node_group] = overlap_remover_001.name

    remove_from_set = remove_from_set_1_node_group(node_tree_names)
    node_tree_names[remove_from_set_1_node_group] = remove_from_set.name

    sort_by_vector_001 = sort_by_vector_001_1_node_group(node_tree_names)
    node_tree_names[sort_by_vector_001_1_node_group] = sort_by_vector_001.name

    sort_by_distance_001 = sort_by_distance_001_1_node_group(node_tree_names)
    node_tree_names[sort_by_distance_001_1_node_group] = sort_by_distance_001.name

    select_clip_and_electrode = select_clip_and_electrode_1_node_group(node_tree_names)
    node_tree_names[select_clip_and_electrode_1_node_group] = select_clip_and_electrode.name

    non_overlapping_wires__order_by_vector__distance__001 = non_overlapping_wires__order_by_vector__distance__001_1_node_group(node_tree_names)
    node_tree_names[non_overlapping_wires__order_by_vector__distance__001_1_node_group] = non_overlapping_wires__order_by_vector__distance__001.name

    connect_vertices_in_distance_001 = connect_vertices_in_distance_001_1_node_group(node_tree_names)
    node_tree_names[connect_vertices_in_distance_001_1_node_group] = connect_vertices_in_distance_001.name

    wiring_layers__consolidated__001 = wiring_layers__consolidated__001_1_node_group(node_tree_names)
    node_tree_names[wiring_layers__consolidated__001_1_node_group] = wiring_layers__consolidated__001.name

    generate_wires_001 = generate_wires_001_1_node_group(node_tree_names)
    node_tree_names[generate_wires_001_1_node_group] = generate_wires_001.name

    generate_clips_001 = generate_clips_001_1_node_group(node_tree_names)
    node_tree_names[generate_clips_001_1_node_group] = generate_clips_001.name

    smooth_mesh_001 = smooth_mesh_001_1_node_group(node_tree_names)
    node_tree_names[smooth_mesh_001_1_node_group] = smooth_mesh_001.name

    skin_cutout_2_001 = skin_cutout_2_001_1_node_group(node_tree_names)
    node_tree_names[skin_cutout_2_001_1_node_group] = skin_cutout_2_001.name

    remove_boundary = remove_boundary_1_node_group(node_tree_names)
    node_tree_names[remove_boundary_1_node_group] = remove_boundary.name

    filter_points_by_index = filter_points_by_index_1_node_group(node_tree_names)
    node_tree_names[filter_points_by_index_1_node_group] = filter_points_by_index.name

    wiring_layer = wiring_layer_1_node_group(node_tree_names)
    node_tree_names[wiring_layer_1_node_group] = wiring_layer.name

