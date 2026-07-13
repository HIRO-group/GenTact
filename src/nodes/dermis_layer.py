import bpy
import mathutils
import os
import typing


def smooth_mesh_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Smooth Mesh node group"""
    smooth_mesh_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Smooth Mesh")

    smooth_mesh_1.color_tag = 'NONE'
    smooth_mesh_1.description = ""
    smooth_mesh_1.default_group_node_width = 140
    smooth_mesh_1.show_modifier_manage_panel = True

    # smooth_mesh_1 interface

    # Socket Smoothed Surface Cutout
    smoothed_surface_cutout_socket = smooth_mesh_1.interface.new_socket(name="Smoothed Surface Cutout", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    smoothed_surface_cutout_socket.attribute_domain = 'POINT'
    smoothed_surface_cutout_socket.default_input = 'VALUE'
    smoothed_surface_cutout_socket.structure_type = 'AUTO'

    # Socket Surface Cutout
    surface_cutout_socket = smooth_mesh_1.interface.new_socket(name="Surface Cutout", in_out='INPUT', socket_type='NodeSocketGeometry')
    surface_cutout_socket.attribute_domain = 'POINT'
    surface_cutout_socket.default_input = 'VALUE'
    surface_cutout_socket.structure_type = 'AUTO'

    # Initialize smooth_mesh_1 nodes

    # Node Position
    position = smooth_mesh_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Set Position
    set_position = smooth_mesh_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Mix
    mix = smooth_mesh_1.nodes.new("ShaderNodeMix")
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
    capture_attribute = smooth_mesh_1.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.show_options = True
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Value")
    capture_attribute.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute.domain = 'EDGE'

    # Node Capture Attribute.001
    capture_attribute_001 = smooth_mesh_1.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.name = "Capture Attribute.001"
    capture_attribute_001.show_options = True
    capture_attribute_001.active_index = 0
    capture_attribute_001.capture_items.clear()
    capture_attribute_001.capture_items.new('FLOAT', "Value")
    capture_attribute_001.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_001.domain = 'POINT'

    # Node Group Output
    group_output = smooth_mesh_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = smooth_mesh_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Separate Color
    separate_color = smooth_mesh_1.nodes.new("FunctionNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.show_options = True
    separate_color.mode = 'RGB'

    # Node Separate Color.001
    separate_color_001 = smooth_mesh_1.nodes.new("FunctionNodeSeparateColor")
    separate_color_001.name = "Separate Color.001"
    separate_color_001.show_options = True
    separate_color_001.mode = 'RGB'

    # Node Combine Color
    combine_color = smooth_mesh_1.nodes.new("FunctionNodeCombineColor")
    combine_color.name = "Combine Color"
    combine_color.show_options = True
    combine_color.mode = 'RGB'

    # Set locations
    smooth_mesh_1.nodes["Position"].location = (-92.76598358154297, 97.1854476928711)
    smooth_mesh_1.nodes["Set Position"].location = (1419.9998779296875, 280.0)
    smooth_mesh_1.nodes["Mix"].location = (880.0, 199.99998474121094)
    smooth_mesh_1.nodes["Capture Attribute"].location = (199.31112670898438, 289.65960693359375)
    smooth_mesh_1.nodes["Capture Attribute.001"].location = (449.3230285644531, 289.40081787109375)
    smooth_mesh_1.nodes["Group Output"].location = (1599.9998779296875, 280.0)
    smooth_mesh_1.nodes["Group Input"].location = (-350.2554931640625, 193.12229919433594)
    smooth_mesh_1.nodes["Separate Color"].location = (1080.0, 20.0)
    smooth_mesh_1.nodes["Separate Color.001"].location = (1080.0, 199.99998474121094)
    smooth_mesh_1.nodes["Combine Color"].location = (1260.0, 199.99998474121094)

    # Set dimensions
    smooth_mesh_1.nodes["Position"].width  = 140.0
    smooth_mesh_1.nodes["Position"].height = 100.0

    smooth_mesh_1.nodes["Set Position"].width  = 140.0
    smooth_mesh_1.nodes["Set Position"].height = 100.0

    smooth_mesh_1.nodes["Mix"].width  = 140.0
    smooth_mesh_1.nodes["Mix"].height = 100.0

    smooth_mesh_1.nodes["Capture Attribute"].width  = 140.0
    smooth_mesh_1.nodes["Capture Attribute"].height = 100.0

    smooth_mesh_1.nodes["Capture Attribute.001"].width  = 140.0
    smooth_mesh_1.nodes["Capture Attribute.001"].height = 100.0

    smooth_mesh_1.nodes["Group Output"].width  = 140.0
    smooth_mesh_1.nodes["Group Output"].height = 100.0

    smooth_mesh_1.nodes["Group Input"].width  = 140.0
    smooth_mesh_1.nodes["Group Input"].height = 100.0

    smooth_mesh_1.nodes["Separate Color"].width  = 140.0
    smooth_mesh_1.nodes["Separate Color"].height = 100.0

    smooth_mesh_1.nodes["Separate Color.001"].width  = 140.0
    smooth_mesh_1.nodes["Separate Color.001"].height = 100.0

    smooth_mesh_1.nodes["Combine Color"].width  = 140.0
    smooth_mesh_1.nodes["Combine Color"].height = 100.0


    # Initialize smooth_mesh_1 links

    # position.Position -> capture_attribute.Value
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Position"].outputs[0],
        smooth_mesh_1.nodes["Capture Attribute"].inputs[1]
    )
    # capture_attribute.Geometry -> capture_attribute_001.Geometry
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Capture Attribute"].outputs[0],
        smooth_mesh_1.nodes["Capture Attribute.001"].inputs[0]
    )
    # capture_attribute.Value -> capture_attribute_001.Value
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Capture Attribute"].outputs[1],
        smooth_mesh_1.nodes["Capture Attribute.001"].inputs[1]
    )
    # position.Position -> mix.A
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Position"].outputs[0],
        smooth_mesh_1.nodes["Mix"].inputs[6]
    )
    # capture_attribute_001.Value -> mix.B
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Capture Attribute.001"].outputs[1],
        smooth_mesh_1.nodes["Mix"].inputs[7]
    )
    # capture_attribute_001.Geometry -> set_position.Geometry
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Capture Attribute.001"].outputs[0],
        smooth_mesh_1.nodes["Set Position"].inputs[0]
    )
    # group_input.Surface Cutout -> capture_attribute.Geometry
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Group Input"].outputs[0],
        smooth_mesh_1.nodes["Capture Attribute"].inputs[0]
    )
    # set_position.Geometry -> group_output.Smoothed Surface Cutout
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Set Position"].outputs[0],
        smooth_mesh_1.nodes["Group Output"].inputs[0]
    )
    # position.Position -> separate_color.Color
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Position"].outputs[0],
        smooth_mesh_1.nodes["Separate Color"].inputs[0]
    )
    # mix.Result -> separate_color_001.Color
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Mix"].outputs[2],
        smooth_mesh_1.nodes["Separate Color.001"].inputs[0]
    )
    # separate_color_001.Red -> combine_color.Red
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Separate Color.001"].outputs[0],
        smooth_mesh_1.nodes["Combine Color"].inputs[0]
    )
    # separate_color_001.Green -> combine_color.Green
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Separate Color.001"].outputs[1],
        smooth_mesh_1.nodes["Combine Color"].inputs[1]
    )
    # separate_color_001.Blue -> combine_color.Blue
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Separate Color.001"].outputs[2],
        smooth_mesh_1.nodes["Combine Color"].inputs[2]
    )
    # separate_color.Alpha -> combine_color.Alpha
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Separate Color"].outputs[3],
        smooth_mesh_1.nodes["Combine Color"].inputs[3]
    )
    # combine_color.Color -> set_position.Position
    smooth_mesh_1.links.new(
        smooth_mesh_1.nodes["Combine Color"].outputs[0],
        smooth_mesh_1.nodes["Set Position"].inputs[2]
    )

    return smooth_mesh_1


def skin_cutout_2_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Skin Cutout 2 node group"""
    skin_cutout_2_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Skin Cutout 2")

    skin_cutout_2_1.color_tag = 'NONE'
    skin_cutout_2_1.description = ""
    skin_cutout_2_1.default_group_node_width = 140
    skin_cutout_2_1.show_modifier_manage_panel = True

    # skin_cutout_2_1 interface

    # Socket Geometry
    geometry_socket = skin_cutout_2_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket = skin_cutout_2_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Socket Smoothing
    smoothing_socket = skin_cutout_2_1.interface.new_socket(name="Smoothing", in_out='INPUT', socket_type='NodeSocketBool')
    smoothing_socket.default_value = False
    smoothing_socket.attribute_domain = 'POINT'
    smoothing_socket.default_input = 'VALUE'
    smoothing_socket.structure_type = 'AUTO'

    # Socket Paint Name
    paint_name_socket = skin_cutout_2_1.interface.new_socket(name="Paint Name", in_out='INPUT', socket_type='NodeSocketString')
    paint_name_socket.default_value = ""
    paint_name_socket.subtype = 'NONE'
    paint_name_socket.attribute_domain = 'POINT'
    paint_name_socket.default_input = 'VALUE'
    paint_name_socket.structure_type = 'AUTO'

    # Socket Cutout Tolerance
    cutout_tolerance_socket = skin_cutout_2_1.interface.new_socket(name="Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat')
    cutout_tolerance_socket.default_value = 0.0
    cutout_tolerance_socket.min_value = -3.4028234663852886e+38
    cutout_tolerance_socket.max_value = 3.4028234663852886e+38
    cutout_tolerance_socket.subtype = 'NONE'
    cutout_tolerance_socket.attribute_domain = 'POINT'
    cutout_tolerance_socket.default_input = 'VALUE'
    cutout_tolerance_socket.structure_type = 'AUTO'

    # Socket Smooth Sampling
    smooth_sampling_socket = skin_cutout_2_1.interface.new_socket(name="Smooth Sampling", in_out='INPUT', socket_type='NodeSocketInt')
    smooth_sampling_socket.default_value = 10
    smooth_sampling_socket.min_value = 1
    smooth_sampling_socket.max_value = 100000
    smooth_sampling_socket.subtype = 'NONE'
    smooth_sampling_socket.attribute_domain = 'POINT'
    smooth_sampling_socket.default_input = 'VALUE'
    smooth_sampling_socket.structure_type = 'AUTO'

    # Socket Subtraction Paint Name
    subtraction_paint_name_socket = skin_cutout_2_1.interface.new_socket(name="Subtraction Paint Name", in_out='INPUT', socket_type='NodeSocketString')
    subtraction_paint_name_socket.default_value = "Group"
    subtraction_paint_name_socket.subtype = 'NONE'
    subtraction_paint_name_socket.attribute_domain = 'POINT'
    subtraction_paint_name_socket.default_input = 'VALUE'
    subtraction_paint_name_socket.structure_type = 'AUTO'
    subtraction_paint_name_socket.optional_label = True

    # Socket Subtraction Cutout Tolerance
    subtraction_cutout_tolerance_socket = skin_cutout_2_1.interface.new_socket(name="Subtraction Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat')
    subtraction_cutout_tolerance_socket.default_value = 50.0
    subtraction_cutout_tolerance_socket.min_value = 0.0
    subtraction_cutout_tolerance_socket.max_value = 100.0
    subtraction_cutout_tolerance_socket.subtype = 'PERCENTAGE'
    subtraction_cutout_tolerance_socket.attribute_domain = 'POINT'
    subtraction_cutout_tolerance_socket.default_input = 'VALUE'
    subtraction_cutout_tolerance_socket.structure_type = 'AUTO'

    # Socket Subtraction Layer
    subtraction_layer_socket = skin_cutout_2_1.interface.new_socket(name="Subtraction Layer", in_out='INPUT', socket_type='NodeSocketBool')
    subtraction_layer_socket.default_value = False
    subtraction_layer_socket.attribute_domain = 'POINT'
    subtraction_layer_socket.default_input = 'VALUE'
    subtraction_layer_socket.structure_type = 'AUTO'

    # Initialize skin_cutout_2_1 nodes

    # Node Group Output
    group_output = skin_cutout_2_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = skin_cutout_2_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Skin Flat Cutout
    skin_flat_cutout = skin_cutout_2_1.nodes.new("NodeFrame")
    skin_flat_cutout.label = "Skin Flat Cutout"
    skin_flat_cutout.name = "Skin Flat Cutout"
    skin_flat_cutout.use_custom_color = True
    skin_flat_cutout.color = (0.1496679037809372, 0.272470623254776, 0.3146030902862549)
    skin_flat_cutout.show_options = True
    skin_flat_cutout.label_size = 30
    skin_flat_cutout.shrink = True

    # Node Index
    index = skin_cutout_2_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Named Attribute.001
    named_attribute_001 = skin_cutout_2_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'FLOAT'

    # Node Math.002
    math_002 = skin_cutout_2_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.hide = True
    math_002.show_options = True
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False
    # Value_001
    math_002.inputs[1].default_value = 100.0

    # Node Sample Index
    sample_index = skin_cutout_2_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT'
    sample_index.domain = 'POINT'

    # Node Delete Geometry
    delete_geometry = skin_cutout_2_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.show_options = True
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    # Node Compare
    compare = skin_cutout_2_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_EQUAL'

    # Node Math
    math = skin_cutout_2_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.hide = True
    math.show_options = True
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    # Value
    math.inputs[0].default_value = 1.0

    # Node Reroute.001
    reroute_001 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Frame.005
    frame_005 = skin_cutout_2_1.nodes.new("NodeFrame")
    frame_005.label = "Smooth Cutout"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.20436476171016693, 0.5617048144340515, 0.6079999804496765)
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Group.001
    group_001 = skin_cutout_2_1.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.show_options = True
    group_001.node_tree = bpy.data.node_groups[node_tree_names[smooth_mesh_1_node_group]]

    # Node Group.002
    group_002 = skin_cutout_2_1.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.show_options = True
    group_002.node_tree = bpy.data.node_groups[node_tree_names[smooth_mesh_1_node_group]]

    # Node Merge by Distance.002
    merge_by_distance_002 = skin_cutout_2_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_002.name = "Merge by Distance.002"
    merge_by_distance_002.show_options = True
    # Selection
    merge_by_distance_002.inputs[1].default_value = True
    # Mode
    merge_by_distance_002.inputs[2].default_value = 'All'

    # Node Reroute
    reroute = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Reroute.002
    reroute_002 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Mesh to Curve
    mesh_to_curve = skin_cutout_2_1.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.show_options = True
    mesh_to_curve.mode = 'EDGES'
    # Selection
    mesh_to_curve.inputs[1].default_value = True

    # Node Delete Geometry.001
    delete_geometry_001 = skin_cutout_2_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.show_options = True
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'

    # Node Extrude Mesh
    extrude_mesh = skin_cutout_2_1.nodes.new("GeometryNodeExtrudeMesh")
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
    resample_curve = skin_cutout_2_1.nodes.new("GeometryNodeResampleCurve")
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
    reroute_003 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketInt"
    # Node Reroute.004
    reroute_004 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketInt"
    # Node Set Spline Type
    set_spline_type = skin_cutout_2_1.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type.name = "Set Spline Type"
    set_spline_type.show_options = True
    set_spline_type.spline_type = 'CATMULL_ROM'
    # Selection
    set_spline_type.inputs[1].default_value = True

    # Node Sample Nearest
    sample_nearest = skin_cutout_2_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Position.001
    position_001 = skin_cutout_2_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Set Position.001
    set_position_001 = skin_cutout_2_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.show_options = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Sample Index.001
    sample_index_001 = skin_cutout_2_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'

    # Node Position.002
    position_002 = skin_cutout_2_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Sample Index.002
    sample_index_002 = skin_cutout_2_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'

    # Node Index.003
    index_003 = skin_cutout_2_1.nodes.new("GeometryNodeInputIndex")
    index_003.name = "Index.003"
    index_003.show_options = True

    # Node Merge by Distance.001
    merge_by_distance_001 = skin_cutout_2_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.show_options = True
    # Mode
    merge_by_distance_001.inputs[2].default_value = 'All'

    # Node Align Mesh with Spline
    align_mesh_with_spline = skin_cutout_2_1.nodes.new("NodeFrame")
    align_mesh_with_spline.label = "Align Mesh with Spline"
    align_mesh_with_spline.name = "Align Mesh with Spline"
    align_mesh_with_spline.show_options = True
    align_mesh_with_spline.label_size = 20
    align_mesh_with_spline.shrink = True

    # Node Curve to Mesh
    curve_to_mesh = skin_cutout_2_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.show_options = True
    # Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    # Node Reroute.005
    reroute_005 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketGeometry"
    # Node Reroute.006
    reroute_006 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketGeometry"
    # Node Reroute.007
    reroute_007 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketBool"
    # Node Value
    value = skin_cutout_2_1.nodes.new("ShaderNodeValue")
    value.name = "Value"
    value.show_options = True

    value.outputs[0].default_value = 0.0010000000474974513
    # Node Reroute.008
    reroute_008 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketFloat"
    # Node Edge Neighbors
    edge_neighbors = skin_cutout_2_1.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
    edge_neighbors.name = "Edge Neighbors"
    edge_neighbors.show_options = True

    # Node Compare.001
    compare_001 = skin_cutout_2_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.show_options = True
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    # B_INT
    compare_001.inputs[3].default_value = 0

    # Node Delete Geometry.002
    delete_geometry_002 = skin_cutout_2_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.show_options = True
    delete_geometry_002.domain = 'POINT'
    delete_geometry_002.mode = 'ALL'

    # Node Switch
    switch = skin_cutout_2_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'GEOMETRY'

    # Node Reroute.009
    reroute_009 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketBool"
    # Node Reroute.010
    reroute_010 = skin_cutout_2_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketBool"
    # Node Index.001
    index_001 = skin_cutout_2_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Named Attribute.002
    named_attribute_002 = skin_cutout_2_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.show_options = True
    named_attribute_002.data_type = 'FLOAT'

    # Node Sample Index.003
    sample_index_003 = skin_cutout_2_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_003.name = "Sample Index.003"
    sample_index_003.show_options = True
    sample_index_003.clamp = False
    sample_index_003.data_type = 'FLOAT'
    sample_index_003.domain = 'POINT'

    # Node Frame
    frame = skin_cutout_2_1.nodes.new("NodeFrame")
    frame.label = "Inverse Paint"
    frame.name = "Frame"
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Compare.002
    compare_002 = skin_cutout_2_1.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.show_options = True
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'LESS_EQUAL'

    # Node Math.003
    math_003 = skin_cutout_2_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.hide = True
    math_003.show_options = True
    math_003.operation = 'DIVIDE'
    math_003.use_clamp = False
    # Value_001
    math_003.inputs[1].default_value = 100.0

    # Node Math.004
    math_004 = skin_cutout_2_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.hide = True
    math_004.show_options = True
    math_004.operation = 'SUBTRACT'
    math_004.use_clamp = False
    # Value
    math_004.inputs[0].default_value = 1.0

    # Node Boolean Math
    boolean_math = skin_cutout_2_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.show_options = True
    boolean_math.operation = 'OR'

    # Node Viewer
    viewer = skin_cutout_2_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Curve")

    # Node Switch.001
    switch_001 = skin_cutout_2_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'FLOAT'
    # False
    switch_001.inputs[1].default_value = 0.0

    # Node Boolean Math.001
    boolean_math_001 = skin_cutout_2_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.show_options = True
    boolean_math_001.operation = 'NOT'

    # Set parents
    skin_cutout_2_1.nodes["Index"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Named Attribute.001"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Math.002"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Sample Index"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Delete Geometry"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Compare"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Math"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Reroute.001"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Group.001"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Group.002"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Merge by Distance.002"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Reroute"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Reroute.002"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Mesh to Curve"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Delete Geometry.001"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Extrude Mesh"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Resample Curve"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Set Spline Type"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Sample Nearest"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Position.001"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Set Position.001"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Sample Index.001"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Position.002"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Sample Index.002"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Index.003"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Merge by Distance.001"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Curve to Mesh"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Reroute.005"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Reroute.006"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Reroute.007"].parent = skin_cutout_2_1.nodes["Align Mesh with Spline"]
    skin_cutout_2_1.nodes["Edge Neighbors"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Compare.001"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Delete Geometry.002"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Index.001"].parent = skin_cutout_2_1.nodes["Frame"]
    skin_cutout_2_1.nodes["Named Attribute.002"].parent = skin_cutout_2_1.nodes["Frame"]
    skin_cutout_2_1.nodes["Sample Index.003"].parent = skin_cutout_2_1.nodes["Frame"]
    skin_cutout_2_1.nodes["Compare.002"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Math.003"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Math.004"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Boolean Math"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Viewer"].parent = skin_cutout_2_1.nodes["Frame.005"]
    skin_cutout_2_1.nodes["Switch.001"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]
    skin_cutout_2_1.nodes["Boolean Math.001"].parent = skin_cutout_2_1.nodes["Skin Flat Cutout"]

    # Set locations
    skin_cutout_2_1.nodes["Group Output"].location = (3880.0, 400.0)
    skin_cutout_2_1.nodes["Group Input"].location = (-1351.0828857421875, 407.08544921875)
    skin_cutout_2_1.nodes["Skin Flat Cutout"].location = (-1088.9033203125, 803.3226318359375)
    skin_cutout_2_1.nodes["Index"].location = (348.9033203125, -863.3226318359375)
    skin_cutout_2_1.nodes["Named Attribute.001"].location = (250.97900390625, -702.7086181640625)
    skin_cutout_2_1.nodes["Math.002"].location = (41.8917236328125, -540.3829345703125)
    skin_cutout_2_1.nodes["Sample Index"].location = (650.2081298828125, -583.88720703125)
    skin_cutout_2_1.nodes["Delete Geometry"].location = (1448.9033203125, -223.3226318359375)
    skin_cutout_2_1.nodes["Compare"].location = (1088.9033203125, -563.3226318359375)
    skin_cutout_2_1.nodes["Math"].location = (209.94940185546875, -541.6002807617188)
    skin_cutout_2_1.nodes["Reroute.001"].location = (432.49322509765625, -369.1813049316406)
    skin_cutout_2_1.nodes["Frame.005"].location = (901.9323120117188, 395.80645751953125)
    skin_cutout_2_1.nodes["Group.001"].location = (138.06768798828125, -35.80645751953125)
    skin_cutout_2_1.nodes["Group.002"].location = (414.85198974609375, -49.492919921875)
    skin_cutout_2_1.nodes["Merge by Distance.002"].location = (58.5765380859375, -219.026611328125)
    skin_cutout_2_1.nodes["Reroute"].location = (591.0890502929688, -166.79644775390625)
    skin_cutout_2_1.nodes["Reroute.002"].location = (33.8709716796875, -169.7266845703125)
    skin_cutout_2_1.nodes["Mesh to Curve"].location = (639.1122436523438, -365.66082763671875)
    skin_cutout_2_1.nodes["Delete Geometry.001"].location = (443.57830810546875, -296.4813232421875)
    skin_cutout_2_1.nodes["Extrude Mesh"].location = (256.82574462890625, -301.00640869140625)
    skin_cutout_2_1.nodes["Resample Curve"].location = (819.1422729492188, -336.6817626953125)
    skin_cutout_2_1.nodes["Reroute.003"].location = (1412.6131591796875, -231.26043701171875)
    skin_cutout_2_1.nodes["Reroute.004"].location = (-1080.3211669921875, -169.61830139160156)
    skin_cutout_2_1.nodes["Set Spline Type"].location = (999.1427612304688, -328.40472412109375)
    skin_cutout_2_1.nodes["Sample Nearest"].location = (563.147216796875, -424.82525634765625)
    skin_cutout_2_1.nodes["Position.001"].location = (28.884033203125, -532.5821533203125)
    skin_cutout_2_1.nodes["Set Position.001"].location = (964.713134765625, -183.57191467285156)
    skin_cutout_2_1.nodes["Sample Index.001"].location = (768.717529296875, -315.7008056640625)
    skin_cutout_2_1.nodes["Position.002"].location = (375.935302734375, -573.7243041992188)
    skin_cutout_2_1.nodes["Sample Index.002"].location = (391.098388671875, -498.1688232421875)
    skin_cutout_2_1.nodes["Index.003"].location = (38.052490234375, -689.3861083984375)
    skin_cutout_2_1.nodes["Merge by Distance.001"].location = (1167.246826171875, -36.07704162597656)
    skin_cutout_2_1.nodes["Align Mesh with Spline"].location = (2089.935546875, 211.54840087890625)
    skin_cutout_2_1.nodes["Curve to Mesh"].location = (1161.906494140625, -312.6610107421875)
    skin_cutout_2_1.nodes["Reroute.005"].location = (289.754150390625, -275.4189453125)
    skin_cutout_2_1.nodes["Reroute.006"].location = (218.15283203125, -106.71195983886719)
    skin_cutout_2_1.nodes["Reroute.007"].location = (880.727783203125, -121.90650939941406)
    skin_cutout_2_1.nodes["Value"].location = (329.65716552734375, -530.4838256835938)
    skin_cutout_2_1.nodes["Reroute.008"].location = (2985.95849609375, -620.7373657226562)
    skin_cutout_2_1.nodes["Edge Neighbors"].location = (1110.9013671875, -73.18896484375)
    skin_cutout_2_1.nodes["Compare.001"].location = (1314.1181640625, -50.5863037109375)
    skin_cutout_2_1.nodes["Delete Geometry.002"].location = (1666.70361328125, -157.8682861328125)
    skin_cutout_2_1.nodes["Switch"].location = (3480.0, 420.0)
    skin_cutout_2_1.nodes["Reroute.009"].location = (3220.0, 1020.0)
    skin_cutout_2_1.nodes["Reroute.010"].location = (-1060.0, 1000.0)
    skin_cutout_2_1.nodes["Index.001"].location = (189.03228759765625, -295.4193420410156)
    skin_cutout_2_1.nodes["Named Attribute.002"].location = (29.03228759765625, -155.41934204101562)
    skin_cutout_2_1.nodes["Sample Index.003"].location = (429.03228759765625, -35.419342041015625)
    skin_cutout_2_1.nodes["Frame"].location = (-869.0322875976562, -264.5806579589844)
    skin_cutout_2_1.nodes["Compare.002"].location = (1068.9033203125, -1023.3226318359375)
    skin_cutout_2_1.nodes["Math.003"].location = (28.9033203125, -1123.3226318359375)
    skin_cutout_2_1.nodes["Math.004"].location = (188.9033203125, -1123.3226318359375)
    skin_cutout_2_1.nodes["Boolean Math"].location = (1488.9033203125, -723.3226318359375)
    skin_cutout_2_1.nodes["Viewer"].location = (658.0676879882812, -95.80645751953125)
    skin_cutout_2_1.nodes["Switch.001"].location = (888.9033203125, -963.3226318359375)
    skin_cutout_2_1.nodes["Boolean Math.001"].location = (1308.9033203125, -883.3226318359375)

    # Set dimensions
    skin_cutout_2_1.nodes["Group Output"].width  = 140.0
    skin_cutout_2_1.nodes["Group Output"].height = 100.0

    skin_cutout_2_1.nodes["Group Input"].width  = 140.0
    skin_cutout_2_1.nodes["Group Input"].height = 100.0

    skin_cutout_2_1.nodes["Skin Flat Cutout"].width  = 1835.48388671875
    skin_cutout_2_1.nodes["Skin Flat Cutout"].height = 1194.677490234375

    skin_cutout_2_1.nodes["Index"].width  = 140.0
    skin_cutout_2_1.nodes["Index"].height = 100.0

    skin_cutout_2_1.nodes["Named Attribute.001"].width  = 140.0
    skin_cutout_2_1.nodes["Named Attribute.001"].height = 100.0

    skin_cutout_2_1.nodes["Math.002"].width  = 140.0
    skin_cutout_2_1.nodes["Math.002"].height = 100.0

    skin_cutout_2_1.nodes["Sample Index"].width  = 140.0
    skin_cutout_2_1.nodes["Sample Index"].height = 100.0

    skin_cutout_2_1.nodes["Delete Geometry"].width  = 140.0
    skin_cutout_2_1.nodes["Delete Geometry"].height = 100.0

    skin_cutout_2_1.nodes["Compare"].width  = 140.0
    skin_cutout_2_1.nodes["Compare"].height = 100.0

    skin_cutout_2_1.nodes["Math"].width  = 140.0
    skin_cutout_2_1.nodes["Math"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.001"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.001"].height = 100.0

    skin_cutout_2_1.nodes["Frame.005"].width  = 1331.099853515625
    skin_cutout_2_1.nodes["Frame.005"].height = 553.3548583984375

    skin_cutout_2_1.nodes["Group.001"].width  = 200.0
    skin_cutout_2_1.nodes["Group.001"].height = 100.0

    skin_cutout_2_1.nodes["Group.002"].width  = 140.0
    skin_cutout_2_1.nodes["Group.002"].height = 100.0

    skin_cutout_2_1.nodes["Merge by Distance.002"].width  = 140.0
    skin_cutout_2_1.nodes["Merge by Distance.002"].height = 100.0

    skin_cutout_2_1.nodes["Reroute"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.002"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.002"].height = 100.0

    skin_cutout_2_1.nodes["Mesh to Curve"].width  = 140.0
    skin_cutout_2_1.nodes["Mesh to Curve"].height = 100.0

    skin_cutout_2_1.nodes["Delete Geometry.001"].width  = 140.0
    skin_cutout_2_1.nodes["Delete Geometry.001"].height = 100.0

    skin_cutout_2_1.nodes["Extrude Mesh"].width  = 140.0
    skin_cutout_2_1.nodes["Extrude Mesh"].height = 100.0

    skin_cutout_2_1.nodes["Resample Curve"].width  = 140.0
    skin_cutout_2_1.nodes["Resample Curve"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.003"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.003"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.004"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.004"].height = 100.0

    skin_cutout_2_1.nodes["Set Spline Type"].width  = 140.0
    skin_cutout_2_1.nodes["Set Spline Type"].height = 100.0

    skin_cutout_2_1.nodes["Sample Nearest"].width  = 140.0
    skin_cutout_2_1.nodes["Sample Nearest"].height = 100.0

    skin_cutout_2_1.nodes["Position.001"].width  = 140.0
    skin_cutout_2_1.nodes["Position.001"].height = 100.0

    skin_cutout_2_1.nodes["Set Position.001"].width  = 140.0
    skin_cutout_2_1.nodes["Set Position.001"].height = 100.0

    skin_cutout_2_1.nodes["Sample Index.001"].width  = 140.0
    skin_cutout_2_1.nodes["Sample Index.001"].height = 100.0

    skin_cutout_2_1.nodes["Position.002"].width  = 140.0
    skin_cutout_2_1.nodes["Position.002"].height = 100.0

    skin_cutout_2_1.nodes["Sample Index.002"].width  = 140.0
    skin_cutout_2_1.nodes["Sample Index.002"].height = 100.0

    skin_cutout_2_1.nodes["Index.003"].width  = 140.0
    skin_cutout_2_1.nodes["Index.003"].height = 100.0

    skin_cutout_2_1.nodes["Merge by Distance.001"].width  = 140.0
    skin_cutout_2_1.nodes["Merge by Distance.001"].height = 100.0

    skin_cutout_2_1.nodes["Align Mesh with Spline"].width  = 1336.129150390625
    skin_cutout_2_1.nodes["Align Mesh with Spline"].height = 766.2581176757812

    skin_cutout_2_1.nodes["Curve to Mesh"].width  = 140.0
    skin_cutout_2_1.nodes["Curve to Mesh"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.005"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.005"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.006"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.006"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.007"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.007"].height = 100.0

    skin_cutout_2_1.nodes["Value"].width  = 123.92022705078125
    skin_cutout_2_1.nodes["Value"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.008"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.008"].height = 100.0

    skin_cutout_2_1.nodes["Edge Neighbors"].width  = 140.0
    skin_cutout_2_1.nodes["Edge Neighbors"].height = 100.0

    skin_cutout_2_1.nodes["Compare.001"].width  = 140.0
    skin_cutout_2_1.nodes["Compare.001"].height = 100.0

    skin_cutout_2_1.nodes["Delete Geometry.002"].width  = 140.0
    skin_cutout_2_1.nodes["Delete Geometry.002"].height = 100.0

    skin_cutout_2_1.nodes["Switch"].width  = 140.0
    skin_cutout_2_1.nodes["Switch"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.009"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.009"].height = 100.0

    skin_cutout_2_1.nodes["Reroute.010"].width  = 100.0
    skin_cutout_2_1.nodes["Reroute.010"].height = 100.0

    skin_cutout_2_1.nodes["Index.001"].width  = 140.0
    skin_cutout_2_1.nodes["Index.001"].height = 100.0

    skin_cutout_2_1.nodes["Named Attribute.002"].width  = 140.0
    skin_cutout_2_1.nodes["Named Attribute.002"].height = 100.0

    skin_cutout_2_1.nodes["Sample Index.003"].width  = 140.0
    skin_cutout_2_1.nodes["Sample Index.003"].height = 100.0

    skin_cutout_2_1.nodes["Frame"].width  = 598.3226318359375
    skin_cutout_2_1.nodes["Frame"].height = 372.1935729980469

    skin_cutout_2_1.nodes["Compare.002"].width  = 140.0
    skin_cutout_2_1.nodes["Compare.002"].height = 100.0

    skin_cutout_2_1.nodes["Math.003"].width  = 140.0
    skin_cutout_2_1.nodes["Math.003"].height = 100.0

    skin_cutout_2_1.nodes["Math.004"].width  = 140.0
    skin_cutout_2_1.nodes["Math.004"].height = 100.0

    skin_cutout_2_1.nodes["Boolean Math"].width  = 140.0
    skin_cutout_2_1.nodes["Boolean Math"].height = 100.0

    skin_cutout_2_1.nodes["Viewer"].width  = 140.0
    skin_cutout_2_1.nodes["Viewer"].height = 100.0

    skin_cutout_2_1.nodes["Switch.001"].width  = 140.0
    skin_cutout_2_1.nodes["Switch.001"].height = 100.0

    skin_cutout_2_1.nodes["Boolean Math.001"].width  = 140.0
    skin_cutout_2_1.nodes["Boolean Math.001"].height = 100.0


    # Initialize skin_cutout_2_1 links

    # math.Value -> compare.B
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Math"].outputs[0],
        skin_cutout_2_1.nodes["Compare"].inputs[1]
    )
    # index.Index -> sample_index.Index
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Index"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index"].inputs[2]
    )
    # math_002.Value -> math.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Math.002"].outputs[0],
        skin_cutout_2_1.nodes["Math"].inputs[1]
    )
    # named_attribute_001.Attribute -> sample_index.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Named Attribute.001"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index"].inputs[1]
    )
    # reroute_001.Output -> sample_index.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.001"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index"].inputs[0]
    )
    # reroute_001.Output -> delete_geometry.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.001"].outputs[0],
        skin_cutout_2_1.nodes["Delete Geometry"].inputs[0]
    )
    # group_input.Mesh -> reroute_001.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[0],
        skin_cutout_2_1.nodes["Reroute.001"].inputs[0]
    )
    # group_input.Paint Name -> named_attribute_001.Name
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[2],
        skin_cutout_2_1.nodes["Named Attribute.001"].inputs[0]
    )
    # group_input.Cutout Tolerance -> math_002.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[3],
        skin_cutout_2_1.nodes["Math.002"].inputs[0]
    )
    # group_001.Smoothed Surface Cutout -> group_002.Surface Cutout
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group.001"].outputs[0],
        skin_cutout_2_1.nodes["Group.002"].inputs[0]
    )
    # reroute_002.Output -> merge_by_distance_002.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.002"].outputs[0],
        skin_cutout_2_1.nodes["Merge by Distance.002"].inputs[0]
    )
    # group_002.Smoothed Surface Cutout -> reroute.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group.002"].outputs[0],
        skin_cutout_2_1.nodes["Reroute"].inputs[0]
    )
    # merge_by_distance_002.Geometry -> extrude_mesh.Mesh
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Merge by Distance.002"].outputs[0],
        skin_cutout_2_1.nodes["Extrude Mesh"].inputs[0]
    )
    # extrude_mesh.Mesh -> delete_geometry_001.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Extrude Mesh"].outputs[0],
        skin_cutout_2_1.nodes["Delete Geometry.001"].inputs[0]
    )
    # extrude_mesh.Top -> delete_geometry_001.Selection
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Extrude Mesh"].outputs[1],
        skin_cutout_2_1.nodes["Delete Geometry.001"].inputs[1]
    )
    # delete_geometry_001.Geometry -> mesh_to_curve.Mesh
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Delete Geometry.001"].outputs[0],
        skin_cutout_2_1.nodes["Mesh to Curve"].inputs[0]
    )
    # mesh_to_curve.Curve -> resample_curve.Curve
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Mesh to Curve"].outputs[0],
        skin_cutout_2_1.nodes["Resample Curve"].inputs[0]
    )
    # reroute_003.Output -> resample_curve.Count
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.003"].outputs[0],
        skin_cutout_2_1.nodes["Resample Curve"].inputs[3]
    )
    # reroute_004.Output -> reroute_003.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.004"].outputs[0],
        skin_cutout_2_1.nodes["Reroute.003"].inputs[0]
    )
    # group_input.Smooth Sampling -> reroute_004.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[4],
        skin_cutout_2_1.nodes["Reroute.004"].inputs[0]
    )
    # resample_curve.Curve -> set_spline_type.Curve
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Resample Curve"].outputs[0],
        skin_cutout_2_1.nodes["Set Spline Type"].inputs[0]
    )
    # set_position_001.Geometry -> merge_by_distance_001.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Set Position.001"].outputs[0],
        skin_cutout_2_1.nodes["Merge by Distance.001"].inputs[0]
    )
    # index_003.Index -> sample_index_002.Index
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Index.003"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.002"].inputs[2]
    )
    # sample_index_002.Value -> sample_nearest.Sample Position
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Sample Index.002"].outputs[0],
        skin_cutout_2_1.nodes["Sample Nearest"].inputs[1]
    )
    # position_001.Position -> sample_index_002.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Position.001"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.002"].inputs[1]
    )
    # sample_index_001.Value -> set_position_001.Position
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Sample Index.001"].outputs[0],
        skin_cutout_2_1.nodes["Set Position.001"].inputs[2]
    )
    # position_002.Position -> sample_index_001.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Position.002"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.001"].inputs[1]
    )
    # sample_nearest.Index -> sample_index_001.Index
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Sample Nearest"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.001"].inputs[2]
    )
    # set_spline_type.Curve -> curve_to_mesh.Curve
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Set Spline Type"].outputs[0],
        skin_cutout_2_1.nodes["Curve to Mesh"].inputs[0]
    )
    # reroute_005.Output -> sample_nearest.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.005"].outputs[0],
        skin_cutout_2_1.nodes["Sample Nearest"].inputs[0]
    )
    # curve_to_mesh.Mesh -> reroute_005.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Curve to Mesh"].outputs[0],
        skin_cutout_2_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_005.Output -> sample_index_001.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.005"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.001"].inputs[0]
    )
    # reroute_006.Output -> set_position_001.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.006"].outputs[0],
        skin_cutout_2_1.nodes["Set Position.001"].inputs[0]
    )
    # extrude_mesh.Mesh -> reroute_006.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Extrude Mesh"].outputs[0],
        skin_cutout_2_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_007.Output -> set_position_001.Selection
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.007"].outputs[0],
        skin_cutout_2_1.nodes["Set Position.001"].inputs[1]
    )
    # extrude_mesh.Side -> reroute_007.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Extrude Mesh"].outputs[2],
        skin_cutout_2_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_007.Output -> merge_by_distance_001.Selection
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.007"].outputs[0],
        skin_cutout_2_1.nodes["Merge by Distance.001"].inputs[1]
    )
    # value.Value -> merge_by_distance_002.Distance
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Value"].outputs[0],
        skin_cutout_2_1.nodes["Merge by Distance.002"].inputs[3]
    )
    # reroute_008.Output -> merge_by_distance_001.Distance
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.008"].outputs[0],
        skin_cutout_2_1.nodes["Merge by Distance.001"].inputs[3]
    )
    # value.Value -> reroute_008.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Value"].outputs[0],
        skin_cutout_2_1.nodes["Reroute.008"].inputs[0]
    )
    # reroute_006.Output -> sample_index_002.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.006"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.002"].inputs[0]
    )
    # edge_neighbors.Face Count -> compare_001.A
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Edge Neighbors"].outputs[0],
        skin_cutout_2_1.nodes["Compare.001"].inputs[2]
    )
    # delete_geometry.Geometry -> delete_geometry_002.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Delete Geometry"].outputs[0],
        skin_cutout_2_1.nodes["Delete Geometry.002"].inputs[0]
    )
    # compare_001.Result -> delete_geometry_002.Selection
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Compare.001"].outputs[0],
        skin_cutout_2_1.nodes["Delete Geometry.002"].inputs[1]
    )
    # reroute.Output -> reroute_002.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute"].outputs[0],
        skin_cutout_2_1.nodes["Reroute.002"].inputs[0]
    )
    # delete_geometry_002.Geometry -> group_001.Surface Cutout
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Delete Geometry.002"].outputs[0],
        skin_cutout_2_1.nodes["Group.001"].inputs[0]
    )
    # merge_by_distance_001.Geometry -> switch.True
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Merge by Distance.001"].outputs[0],
        skin_cutout_2_1.nodes["Switch"].inputs[2]
    )
    # reroute_009.Output -> switch.Switch
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.009"].outputs[0],
        skin_cutout_2_1.nodes["Switch"].inputs[0]
    )
    # reroute_010.Output -> reroute_009.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.010"].outputs[0],
        skin_cutout_2_1.nodes["Reroute.009"].inputs[0]
    )
    # group_input.Smoothing -> reroute_010.Input
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[1],
        skin_cutout_2_1.nodes["Reroute.010"].inputs[0]
    )
    # delete_geometry_002.Geometry -> switch.False
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Delete Geometry.002"].outputs[0],
        skin_cutout_2_1.nodes["Switch"].inputs[1]
    )
    # switch.Output -> group_output.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Switch"].outputs[0],
        skin_cutout_2_1.nodes["Group Output"].inputs[0]
    )
    # index_001.Index -> sample_index_003.Index
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Index.001"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.003"].inputs[2]
    )
    # named_attribute_002.Attribute -> sample_index_003.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Named Attribute.002"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.003"].inputs[1]
    )
    # reroute_001.Output -> sample_index_003.Geometry
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Reroute.001"].outputs[0],
        skin_cutout_2_1.nodes["Sample Index.003"].inputs[0]
    )
    # group_input.Subtraction Paint Name -> named_attribute_002.Name
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[5],
        skin_cutout_2_1.nodes["Named Attribute.002"].inputs[0]
    )
    # math_003.Value -> math_004.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Math.003"].outputs[0],
        skin_cutout_2_1.nodes["Math.004"].inputs[1]
    )
    # group_input.Subtraction Cutout Tolerance -> math_003.Value
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[6],
        skin_cutout_2_1.nodes["Math.003"].inputs[0]
    )
    # math_004.Value -> compare_002.B
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Math.004"].outputs[0],
        skin_cutout_2_1.nodes["Compare.002"].inputs[1]
    )
    # compare.Result -> boolean_math.Boolean
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Compare"].outputs[0],
        skin_cutout_2_1.nodes["Boolean Math"].inputs[0]
    )
    # boolean_math_001.Boolean -> boolean_math.Boolean
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Boolean Math.001"].outputs[0],
        skin_cutout_2_1.nodes["Boolean Math"].inputs[1]
    )
    # group_001.Smoothed Surface Cutout -> viewer.Curve
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group.001"].outputs[0],
        skin_cutout_2_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Subtraction Layer -> switch_001.Switch
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Group Input"].outputs[7],
        skin_cutout_2_1.nodes["Switch.001"].inputs[0]
    )
    # sample_index_003.Value -> switch_001.True
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Sample Index.003"].outputs[0],
        skin_cutout_2_1.nodes["Switch.001"].inputs[2]
    )
    # switch_001.Output -> compare_002.A
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Switch.001"].outputs[0],
        skin_cutout_2_1.nodes["Compare.002"].inputs[0]
    )
    # sample_index.Value -> compare.A
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Sample Index"].outputs[0],
        skin_cutout_2_1.nodes["Compare"].inputs[0]
    )
    # compare_002.Result -> boolean_math_001.Boolean
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Compare.002"].outputs[0],
        skin_cutout_2_1.nodes["Boolean Math.001"].inputs[0]
    )
    # boolean_math.Boolean -> delete_geometry.Selection
    skin_cutout_2_1.links.new(
        skin_cutout_2_1.nodes["Boolean Math"].outputs[0],
        skin_cutout_2_1.nodes["Delete Geometry"].inputs[1]
    )
    viewer.viewer_items[0].auto_remove = True

    return skin_cutout_2_1


def cutout_thickness_labeled_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Cutout Thickness Labeled node group"""
    cutout_thickness_labeled_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Cutout Thickness Labeled")

    cutout_thickness_labeled_1.color_tag = 'NONE'
    cutout_thickness_labeled_1.description = ""
    cutout_thickness_labeled_1.default_group_node_width = 140
    cutout_thickness_labeled_1.show_modifier_manage_panel = True

    # cutout_thickness_labeled_1 interface

    # Socket Geometry
    geometry_socket = cutout_thickness_labeled_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Top Cut
    top_cut_socket = cutout_thickness_labeled_1.interface.new_socket(name="Top Cut", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    top_cut_socket.attribute_domain = 'POINT'
    top_cut_socket.default_input = 'VALUE'
    top_cut_socket.structure_type = 'AUTO'

    # Socket Extruded Mesh
    extruded_mesh_socket = cutout_thickness_labeled_1.interface.new_socket(name="Extruded Mesh", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    extruded_mesh_socket.attribute_domain = 'POINT'
    extruded_mesh_socket.default_input = 'VALUE'
    extruded_mesh_socket.structure_type = 'AUTO'

    # Socket Bottom Cut
    bottom_cut_socket = cutout_thickness_labeled_1.interface.new_socket(name="Bottom Cut", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    bottom_cut_socket.attribute_domain = 'POINT'
    bottom_cut_socket.default_input = 'VALUE'
    bottom_cut_socket.structure_type = 'AUTO'

    # Socket Side
    side_socket = cutout_thickness_labeled_1.interface.new_socket(name="Side", in_out='OUTPUT', socket_type='NodeSocketBool')
    side_socket.default_value = False
    side_socket.attribute_domain = 'POINT'
    side_socket.default_input = 'VALUE'
    side_socket.structure_type = 'AUTO'

    # Socket Cutout
    cutout_socket = cutout_thickness_labeled_1.interface.new_socket(name="Cutout", in_out='INPUT', socket_type='NodeSocketGeometry')
    cutout_socket.attribute_domain = 'POINT'
    cutout_socket.default_input = 'VALUE'
    cutout_socket.structure_type = 'AUTO'

    # Socket Offset Scale
    offset_scale_socket = cutout_thickness_labeled_1.interface.new_socket(name="Offset Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    offset_scale_socket.default_value = 0.019999999552965164
    offset_scale_socket.min_value = -3.4028234663852886e+38
    offset_scale_socket.max_value = 3.4028234663852886e+38
    offset_scale_socket.subtype = 'NONE'
    offset_scale_socket.attribute_domain = 'POINT'
    offset_scale_socket.default_input = 'VALUE'
    offset_scale_socket.structure_type = 'AUTO'

    # Socket Top Material
    top_material_socket = cutout_thickness_labeled_1.interface.new_socket(name="Top Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    top_material_socket.attribute_domain = 'POINT'
    top_material_socket.default_input = 'VALUE'
    top_material_socket.structure_type = 'AUTO'

    # Socket Side Material
    side_material_socket = cutout_thickness_labeled_1.interface.new_socket(name="Side Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    side_material_socket.attribute_domain = 'POINT'
    side_material_socket.default_input = 'VALUE'
    side_material_socket.structure_type = 'AUTO'

    # Socket Dermis Top Label
    dermis_top_label_socket = cutout_thickness_labeled_1.interface.new_socket(name="Dermis Top Label", in_out='INPUT', socket_type='NodeSocketString')
    dermis_top_label_socket.default_value = ""
    dermis_top_label_socket.subtype = 'NONE'
    dermis_top_label_socket.attribute_domain = 'POINT'
    dermis_top_label_socket.default_input = 'VALUE'
    dermis_top_label_socket.structure_type = 'AUTO'

    # Socket Dermis Full Label
    dermis_full_label_socket = cutout_thickness_labeled_1.interface.new_socket(name="Dermis Full Label", in_out='INPUT', socket_type='NodeSocketString')
    dermis_full_label_socket.default_value = ""
    dermis_full_label_socket.subtype = 'NONE'
    dermis_full_label_socket.attribute_domain = 'POINT'
    dermis_full_label_socket.default_input = 'VALUE'
    dermis_full_label_socket.structure_type = 'AUTO'

    # Socket Dermis Bottom Label
    dermis_bottom_label_socket = cutout_thickness_labeled_1.interface.new_socket(name="Dermis Bottom Label", in_out='INPUT', socket_type='NodeSocketString')
    dermis_bottom_label_socket.default_value = ""
    dermis_bottom_label_socket.subtype = 'NONE'
    dermis_bottom_label_socket.attribute_domain = 'POINT'
    dermis_bottom_label_socket.default_input = 'VALUE'
    dermis_bottom_label_socket.structure_type = 'AUTO'

    # Socket Dermis Side Label
    dermis_side_label_socket = cutout_thickness_labeled_1.interface.new_socket(name="Dermis Side Label", in_out='INPUT', socket_type='NodeSocketString')
    dermis_side_label_socket.default_value = ""
    dermis_side_label_socket.subtype = 'NONE'
    dermis_side_label_socket.attribute_domain = 'POINT'
    dermis_side_label_socket.default_input = 'VALUE'
    dermis_side_label_socket.structure_type = 'AUTO'
    dermis_side_label_socket.optional_label = True

    # Initialize cutout_thickness_labeled_1 nodes

    # Node Group Output
    group_output = cutout_thickness_labeled_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = cutout_thickness_labeled_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Set Material
    set_material = cutout_thickness_labeled_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True

    # Node Set Material.001
    set_material_001 = cutout_thickness_labeled_1.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    set_material_001.show_options = True

    # Node Reroute.010
    reroute_010 = cutout_thickness_labeled_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketGeometry"
    # Node Reroute.003
    reroute_003 = cutout_thickness_labeled_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Set Material.002
    set_material_002 = cutout_thickness_labeled_1.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    set_material_002.show_options = True
    # Selection
    set_material_002.inputs[1].default_value = True

    # Node Join Geometry
    join_geometry = cutout_thickness_labeled_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Frame.007
    frame_007 = cutout_thickness_labeled_1.nodes.new("NodeFrame")
    frame_007.label = "Join Top, Bottom, and Side Cutouts"
    frame_007.name = "Frame.007"
    frame_007.use_custom_color = True
    frame_007.color = (0.4318181574344635, 0.6079999804496765, 0.2556363642215729)
    frame_007.show_options = True
    frame_007.label_size = 30
    frame_007.shrink = True

    # Node Merge by Distance
    merge_by_distance = cutout_thickness_labeled_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.show_options = True
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance.inputs[3].default_value = 0.0010000000474974513

    # Node Extrude Mesh
    extrude_mesh = cutout_thickness_labeled_1.nodes.new("GeometryNodeExtrudeMesh")
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
    flip_faces = cutout_thickness_labeled_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    flip_faces.show_options = True
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Reroute
    reroute = cutout_thickness_labeled_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketMaterial"
    # Node Boolean Math
    boolean_math = cutout_thickness_labeled_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.show_options = True
    boolean_math.operation = 'NOT'

    # Node Viewer
    viewer = cutout_thickness_labeled_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")

    # Node Store Named Attribute
    store_named_attribute = cutout_thickness_labeled_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    # Value
    store_named_attribute.inputs[3].default_value = True

    # Node Store Named Attribute.001
    store_named_attribute_001 = cutout_thickness_labeled_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Value
    store_named_attribute_001.inputs[3].default_value = True

    # Node Reroute.001
    reroute_001 = cutout_thickness_labeled_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketString"
    # Node Store Named Attribute.002
    store_named_attribute_002 = cutout_thickness_labeled_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'BOOLEAN'
    store_named_attribute_002.domain = 'POINT'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Value
    store_named_attribute_002.inputs[3].default_value = True

    # Node Store Named Attribute.003
    store_named_attribute_003 = cutout_thickness_labeled_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.show_options = True
    store_named_attribute_003.data_type = 'BOOLEAN'
    store_named_attribute_003.domain = 'POINT'
    # Value
    store_named_attribute_003.inputs[3].default_value = True

    # Node Reroute.002
    reroute_002 = cutout_thickness_labeled_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketBool"
    # Set parents
    cutout_thickness_labeled_1.nodes["Set Material"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Set Material.001"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Reroute.010"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Reroute.003"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Set Material.002"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Join Geometry"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Merge by Distance"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Extrude Mesh"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Flip Faces"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Reroute"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Boolean Math"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Store Named Attribute"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Reroute.001"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Store Named Attribute.002"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]
    cutout_thickness_labeled_1.nodes["Reroute.002"].parent = cutout_thickness_labeled_1.nodes["Frame.007"]

    # Set locations
    cutout_thickness_labeled_1.nodes["Group Output"].location = (1440.0, 360.0)
    cutout_thickness_labeled_1.nodes["Group Input"].location = (-791.9739990234375, 322.9139099121094)
    cutout_thickness_labeled_1.nodes["Set Material"].location = (395.0, -71.0)
    cutout_thickness_labeled_1.nodes["Set Material.001"].location = (955.0, -391.0)
    cutout_thickness_labeled_1.nodes["Reroute.010"].location = (95.0, -571.0)
    cutout_thickness_labeled_1.nodes["Reroute.003"].location = (35.0, -351.0)
    cutout_thickness_labeled_1.nodes["Set Material.002"].location = (715.0, -471.0)
    cutout_thickness_labeled_1.nodes["Join Geometry"].location = (1175.0, -331.0)
    cutout_thickness_labeled_1.nodes["Frame.007"].location = (-515.0, 371.0)
    cutout_thickness_labeled_1.nodes["Merge by Distance"].location = (1395.0, -291.0)
    cutout_thickness_labeled_1.nodes["Extrude Mesh"].location = (135.0, -211.0)
    cutout_thickness_labeled_1.nodes["Flip Faces"].location = (415.0, -511.0)
    cutout_thickness_labeled_1.nodes["Reroute"].location = (475.0, -211.0)
    cutout_thickness_labeled_1.nodes["Boolean Math"].location = (435.0, -311.0)
    cutout_thickness_labeled_1.nodes["Viewer"].location = (620.0, 140.0)
    cutout_thickness_labeled_1.nodes["Store Named Attribute"].location = (595.0, -51.0)
    cutout_thickness_labeled_1.nodes["Store Named Attribute.001"].location = (1080.0, 100.0)
    cutout_thickness_labeled_1.nodes["Reroute.001"].location = (1355.0, -271.0)
    cutout_thickness_labeled_1.nodes["Store Named Attribute.002"].location = (135.0, -571.0)
    cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].location = (775.0, -251.0)
    cutout_thickness_labeled_1.nodes["Reroute.002"].location = (690.326904296875, -390.40423583984375)

    # Set dimensions
    cutout_thickness_labeled_1.nodes["Group Output"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Group Output"].height = 100.0

    cutout_thickness_labeled_1.nodes["Group Input"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Group Input"].height = 100.0

    cutout_thickness_labeled_1.nodes["Set Material"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Set Material"].height = 100.0

    cutout_thickness_labeled_1.nodes["Set Material.001"].width  = 149.686767578125
    cutout_thickness_labeled_1.nodes["Set Material.001"].height = 100.0

    cutout_thickness_labeled_1.nodes["Reroute.010"].width  = 100.0
    cutout_thickness_labeled_1.nodes["Reroute.010"].height = 100.0

    cutout_thickness_labeled_1.nodes["Reroute.003"].width  = 100.0
    cutout_thickness_labeled_1.nodes["Reroute.003"].height = 100.0

    cutout_thickness_labeled_1.nodes["Set Material.002"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Set Material.002"].height = 100.0

    cutout_thickness_labeled_1.nodes["Join Geometry"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Join Geometry"].height = 100.0

    cutout_thickness_labeled_1.nodes["Frame.007"].width  = 1565.0
    cutout_thickness_labeled_1.nodes["Frame.007"].height = 766.0

    cutout_thickness_labeled_1.nodes["Merge by Distance"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Merge by Distance"].height = 100.0

    cutout_thickness_labeled_1.nodes["Extrude Mesh"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Extrude Mesh"].height = 100.0

    cutout_thickness_labeled_1.nodes["Flip Faces"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Flip Faces"].height = 100.0

    cutout_thickness_labeled_1.nodes["Reroute"].width  = 100.0
    cutout_thickness_labeled_1.nodes["Reroute"].height = 100.0

    cutout_thickness_labeled_1.nodes["Boolean Math"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Boolean Math"].height = 100.0

    cutout_thickness_labeled_1.nodes["Viewer"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Viewer"].height = 100.0

    cutout_thickness_labeled_1.nodes["Store Named Attribute"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Store Named Attribute"].height = 100.0

    cutout_thickness_labeled_1.nodes["Store Named Attribute.001"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Store Named Attribute.001"].height = 100.0

    cutout_thickness_labeled_1.nodes["Reroute.001"].width  = 100.0
    cutout_thickness_labeled_1.nodes["Reroute.001"].height = 100.0

    cutout_thickness_labeled_1.nodes["Store Named Attribute.002"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Store Named Attribute.002"].height = 100.0

    cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].width  = 140.0
    cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].height = 100.0

    cutout_thickness_labeled_1.nodes["Reroute.002"].width  = 100.0
    cutout_thickness_labeled_1.nodes["Reroute.002"].height = 100.0


    # Initialize cutout_thickness_labeled_1 links

    # join_geometry.Geometry -> merge_by_distance.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Join Geometry"].outputs[0],
        cutout_thickness_labeled_1.nodes["Merge by Distance"].inputs[0]
    )
    # extrude_mesh.Top -> set_material.Selection
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].outputs[1],
        cutout_thickness_labeled_1.nodes["Set Material"].inputs[1]
    )
    # set_material_002.Geometry -> join_geometry.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Set Material.002"].outputs[0],
        cutout_thickness_labeled_1.nodes["Join Geometry"].inputs[0]
    )
    # reroute_003.Output -> extrude_mesh.Mesh
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute.003"].outputs[0],
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].inputs[0]
    )
    # store_named_attribute_002.Geometry -> flip_faces.Mesh
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Store Named Attribute.002"].outputs[0],
        cutout_thickness_labeled_1.nodes["Flip Faces"].inputs[0]
    )
    # reroute_003.Output -> reroute_010.Input
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute.003"].outputs[0],
        cutout_thickness_labeled_1.nodes["Reroute.010"].inputs[0]
    )
    # reroute_002.Output -> set_material_001.Selection
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute.002"].outputs[0],
        cutout_thickness_labeled_1.nodes["Set Material.001"].inputs[1]
    )
    # extrude_mesh.Mesh -> set_material.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].outputs[0],
        cutout_thickness_labeled_1.nodes["Set Material"].inputs[0]
    )
    # flip_faces.Mesh -> set_material_002.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Flip Faces"].outputs[0],
        cutout_thickness_labeled_1.nodes["Set Material.002"].inputs[0]
    )
    # group_input.Cutout -> reroute_003.Input
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[0],
        cutout_thickness_labeled_1.nodes["Reroute.003"].inputs[0]
    )
    # group_input.Offset Scale -> extrude_mesh.Offset Scale
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[1],
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].inputs[3]
    )
    # store_named_attribute.Geometry -> group_output.Top Cut
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Store Named Attribute"].outputs[0],
        cutout_thickness_labeled_1.nodes["Group Output"].inputs[1]
    )
    # store_named_attribute_001.Geometry -> group_output.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Store Named Attribute.001"].outputs[0],
        cutout_thickness_labeled_1.nodes["Group Output"].inputs[0]
    )
    # extrude_mesh.Mesh -> group_output.Extruded Mesh
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].outputs[0],
        cutout_thickness_labeled_1.nodes["Group Output"].inputs[2]
    )
    # extrude_mesh.Side -> group_output.Side
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].outputs[2],
        cutout_thickness_labeled_1.nodes["Group Output"].inputs[4]
    )
    # group_input.Top Material -> set_material.Material
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[2],
        cutout_thickness_labeled_1.nodes["Set Material"].inputs[2]
    )
    # reroute.Output -> set_material_001.Material
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute"].outputs[0],
        cutout_thickness_labeled_1.nodes["Set Material.001"].inputs[2]
    )
    # group_input.Side Material -> reroute.Input
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[3],
        cutout_thickness_labeled_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> set_material_002.Material
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute"].outputs[0],
        cutout_thickness_labeled_1.nodes["Set Material.002"].inputs[2]
    )
    # set_material_002.Geometry -> group_output.Bottom Cut
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Set Material.002"].outputs[0],
        cutout_thickness_labeled_1.nodes["Group Output"].inputs[3]
    )
    # extrude_mesh.Side -> boolean_math.Boolean
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].outputs[2],
        cutout_thickness_labeled_1.nodes["Boolean Math"].inputs[0]
    )
    # set_material.Geometry -> store_named_attribute.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Set Material"].outputs[0],
        cutout_thickness_labeled_1.nodes["Store Named Attribute"].inputs[0]
    )
    # store_named_attribute_003.Geometry -> set_material_001.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].outputs[0],
        cutout_thickness_labeled_1.nodes["Set Material.001"].inputs[0]
    )
    # group_input.Dermis Top Label -> store_named_attribute.Name
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[4],
        cutout_thickness_labeled_1.nodes["Store Named Attribute"].inputs[2]
    )
    # extrude_mesh.Top -> store_named_attribute.Selection
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].outputs[1],
        cutout_thickness_labeled_1.nodes["Store Named Attribute"].inputs[1]
    )
    # merge_by_distance.Geometry -> store_named_attribute_001.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Merge by Distance"].outputs[0],
        cutout_thickness_labeled_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # reroute_001.Output -> store_named_attribute_001.Name
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute.001"].outputs[0],
        cutout_thickness_labeled_1.nodes["Store Named Attribute.001"].inputs[2]
    )
    # group_input.Dermis Full Label -> reroute_001.Input
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[5],
        cutout_thickness_labeled_1.nodes["Reroute.001"].inputs[0]
    )
    # set_material_001.Geometry -> viewer.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Set Material.001"].outputs[0],
        cutout_thickness_labeled_1.nodes["Viewer"].inputs[0]
    )
    # reroute_010.Output -> store_named_attribute_002.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute.010"].outputs[0],
        cutout_thickness_labeled_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # group_input.Dermis Bottom Label -> store_named_attribute_002.Name
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[6],
        cutout_thickness_labeled_1.nodes["Store Named Attribute.002"].inputs[2]
    )
    # store_named_attribute.Geometry -> store_named_attribute_003.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Store Named Attribute"].outputs[0],
        cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].inputs[0]
    )
    # extrude_mesh.Side -> reroute_002.Input
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Extrude Mesh"].outputs[2],
        cutout_thickness_labeled_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_002.Output -> store_named_attribute_003.Selection
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Reroute.002"].outputs[0],
        cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].inputs[1]
    )
    # group_input.Dermis Side Label -> store_named_attribute_003.Name
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Group Input"].outputs[7],
        cutout_thickness_labeled_1.nodes["Store Named Attribute.003"].inputs[2]
    )
    # set_material_001.Geometry -> join_geometry.Geometry
    cutout_thickness_labeled_1.links.new(
        cutout_thickness_labeled_1.nodes["Set Material.001"].outputs[0],
        cutout_thickness_labeled_1.nodes["Join Geometry"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True

    return cutout_thickness_labeled_1


def plate_volume_no_ref_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Plate Volume No Ref node group"""
    plate_volume_no_ref_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Plate Volume No Ref")

    plate_volume_no_ref_1.color_tag = 'NONE'
    plate_volume_no_ref_1.description = ""
    plate_volume_no_ref_1.default_group_node_width = 140
    plate_volume_no_ref_1.show_modifier_manage_panel = True

    # plate_volume_no_ref_1 interface

    # Socket Geometry
    geometry_socket = plate_volume_no_ref_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Bottom Plate
    bottom_plate_socket = plate_volume_no_ref_1.interface.new_socket(name="Bottom Plate", in_out='INPUT', socket_type='NodeSocketGeometry')
    bottom_plate_socket.attribute_domain = 'POINT'
    bottom_plate_socket.default_input = 'VALUE'
    bottom_plate_socket.structure_type = 'AUTO'

    # Socket Flat Offset
    flat_offset_socket = plate_volume_no_ref_1.interface.new_socket(name="Flat Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    flat_offset_socket.default_value = 0.5
    flat_offset_socket.min_value = -10000.0
    flat_offset_socket.max_value = 10000.0
    flat_offset_socket.subtype = 'NONE'
    flat_offset_socket.attribute_domain = 'POINT'
    flat_offset_socket.default_input = 'VALUE'
    flat_offset_socket.structure_type = 'AUTO'

    # Socket Limit Thickness
    limit_thickness_socket = plate_volume_no_ref_1.interface.new_socket(name="Limit Thickness", in_out='INPUT', socket_type='NodeSocketBool')
    limit_thickness_socket.default_value = False
    limit_thickness_socket.attribute_domain = 'POINT'
    limit_thickness_socket.default_input = 'VALUE'
    limit_thickness_socket.structure_type = 'AUTO'

    # Socket Layer Offset
    layer_offset_socket = plate_volume_no_ref_1.interface.new_socket(name="Layer Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    layer_offset_socket.default_value = 0.0
    layer_offset_socket.min_value = -3.4028234663852886e+38
    layer_offset_socket.max_value = 3.4028234663852886e+38
    layer_offset_socket.subtype = 'NONE'
    layer_offset_socket.attribute_domain = 'POINT'
    layer_offset_socket.default_input = 'VALUE'
    layer_offset_socket.structure_type = 'AUTO'

    # Socket Top Material
    top_material_socket = plate_volume_no_ref_1.interface.new_socket(name="Top Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    top_material_socket.attribute_domain = 'POINT'
    top_material_socket.default_input = 'VALUE'
    top_material_socket.structure_type = 'AUTO'

    # Socket Dermis Label
    dermis_label_socket = plate_volume_no_ref_1.interface.new_socket(name="Dermis Label", in_out='INPUT', socket_type='NodeSocketString')
    dermis_label_socket.default_value = ""
    dermis_label_socket.subtype = 'NONE'
    dermis_label_socket.attribute_domain = 'POINT'
    dermis_label_socket.hide_value = True
    dermis_label_socket.default_input = 'VALUE'
    dermis_label_socket.structure_type = 'AUTO'

    # Initialize plate_volume_no_ref_1 nodes

    # Node Plate
    plate = plate_volume_no_ref_1.nodes.new("NodeGroupOutput")
    plate.label = "Plate"
    plate.name = "Plate"
    plate.show_options = True
    plate.is_active_output = True

    # Node Group Input
    group_input = plate_volume_no_ref_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Extrude Mesh.002
    extrude_mesh_002 = plate_volume_no_ref_1.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.show_options = True
    extrude_mesh_002.mode = 'FACES'
    # Selection
    extrude_mesh_002.inputs[1].default_value = True
    # Offset
    extrude_mesh_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh_002.inputs[4].default_value = False

    # Node Delete Geometry.002
    delete_geometry_002 = plate_volume_no_ref_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.show_options = True
    delete_geometry_002.domain = 'FACE'
    delete_geometry_002.mode = 'ALL'

    # Node Reroute.024
    reroute_024 = plate_volume_no_ref_1.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.show_options = True
    reroute_024.socket_idname = "NodeSocketFloat"
    # Node Plate\
    plate_ = plate_volume_no_ref_1.nodes.new("NodeFrame")
    plate_.label = "Create a Plate"
    plate_.name = "Plate\\"
    plate_.show_options = True
    plate_.label_size = 20
    plate_.shrink = True

    # Node Math.007
    math_007 = plate_volume_no_ref_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'SUBTRACT'
    math_007.use_clamp = False
    # Value_001
    math_007.inputs[1].default_value = 0.5

    # Node Math.006
    math_006 = plate_volume_no_ref_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'MINIMUM'
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 2.9802322387695312e-08

    # Node Switch
    switch = plate_volume_no_ref_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'FLOAT'

    # Node Reroute
    reroute = plate_volume_no_ref_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketBool"
    # Node Reroute.001
    reroute_001 = plate_volume_no_ref_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketBool"
    # Node Reroute.002
    reroute_002 = plate_volume_no_ref_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketMaterial"
    # Node Cutout Thickness Labeled
    cutout_thickness_labeled = plate_volume_no_ref_1.nodes.new("GeometryNodeGroup")
    cutout_thickness_labeled.name = "Cutout Thickness Labeled"
    cutout_thickness_labeled.show_options = True
    cutout_thickness_labeled.node_tree = bpy.data.node_groups[node_tree_names[cutout_thickness_labeled_1_node_group]]

    # Node Group Input.001
    group_input_001 = plate_volume_no_ref_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Viewer
    viewer = plate_volume_no_ref_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Geometry")

    # Node Join Strings
    join_strings = plate_volume_no_ref_1.nodes.new("GeometryNodeStringJoin")
    join_strings.name = "Join Strings"
    join_strings.show_options = True
    # Delimiter
    join_strings.inputs[0].default_value = "_"

    # Node String
    string = plate_volume_no_ref_1.nodes.new("FunctionNodeInputString")
    string.name = "String"
    string.show_options = True
    string.string = "top"

    # Node String.001
    string_001 = plate_volume_no_ref_1.nodes.new("FunctionNodeInputString")
    string_001.name = "String.001"
    string_001.show_options = True
    string_001.string = "bottom"

    # Node String.002
    string_002 = plate_volume_no_ref_1.nodes.new("FunctionNodeInputString")
    string_002.name = "String.002"
    string_002.show_options = True
    string_002.string = "side"

    # Node Join Strings.001
    join_strings_001 = plate_volume_no_ref_1.nodes.new("GeometryNodeStringJoin")
    join_strings_001.name = "Join Strings.001"
    join_strings_001.show_options = True
    # Delimiter
    join_strings_001.inputs[0].default_value = "_"

    # Node Join Strings.002
    join_strings_002 = plate_volume_no_ref_1.nodes.new("GeometryNodeStringJoin")
    join_strings_002.name = "Join Strings.002"
    join_strings_002.show_options = True
    # Delimiter
    join_strings_002.inputs[0].default_value = "_"

    # Node Reroute.003
    reroute_003 = plate_volume_no_ref_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketString"
    # Set parents
    plate_volume_no_ref_1.nodes["Extrude Mesh.002"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Delete Geometry.002"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Reroute.024"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Math.007"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Math.006"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Switch"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Reroute"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Reroute.001"].parent = plate_volume_no_ref_1.nodes["Plate\\"]
    plate_volume_no_ref_1.nodes["Reroute.002"].parent = plate_volume_no_ref_1.nodes["Plate\\"]

    # Set locations
    plate_volume_no_ref_1.nodes["Plate"].location = (1700.0, 480.0)
    plate_volume_no_ref_1.nodes["Group Input"].location = (-1282.3311767578125, 56.3474235534668)
    plate_volume_no_ref_1.nodes["Extrude Mesh.002"].location = (1240.59033203125, -68.21392822265625)
    plate_volume_no_ref_1.nodes["Delete Geometry.002"].location = (1499.63671875, -35.74273681640625)
    plate_volume_no_ref_1.nodes["Reroute.024"].location = (691.86328125, -237.32037353515625)
    plate_volume_no_ref_1.nodes["Plate\\"].location = (-941.9656372070312, 288.0)
    plate_volume_no_ref_1.nodes["Math.007"].location = (1254.7686767578125, -348.3517150878906)
    plate_volume_no_ref_1.nodes["Math.006"].location = (1486.776611328125, -336.81243896484375)
    plate_volume_no_ref_1.nodes["Switch"].location = (1671.0582275390625, -405.7055969238281)
    plate_volume_no_ref_1.nodes["Reroute"].location = (35.0, -826.1449584960938)
    plate_volume_no_ref_1.nodes["Reroute.001"].location = (1583.4656982421875, -822.3869018554688)
    plate_volume_no_ref_1.nodes["Reroute.002"].location = (1654.518310546875, -253.26968383789062)
    plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].location = (980.0, 600.0)
    plate_volume_no_ref_1.nodes["Group Input.001"].location = (-80.0, 580.0)
    plate_volume_no_ref_1.nodes["Viewer"].location = (1226.6666259765625, 680.6666870117188)
    plate_volume_no_ref_1.nodes["Join Strings"].location = (560.0, 500.0)
    plate_volume_no_ref_1.nodes["String"].location = (280.0, 640.0)
    plate_volume_no_ref_1.nodes["String.001"].location = (280.0, 580.0)
    plate_volume_no_ref_1.nodes["String.002"].location = (280.0, 520.0)
    plate_volume_no_ref_1.nodes["Join Strings.001"].location = (560.0, 600.0)
    plate_volume_no_ref_1.nodes["Join Strings.002"].location = (560.0, 700.0)
    plate_volume_no_ref_1.nodes["Reroute.003"].location = (500.0, 360.0)

    # Set dimensions
    plate_volume_no_ref_1.nodes["Plate"].width  = 140.0
    plate_volume_no_ref_1.nodes["Plate"].height = 100.0

    plate_volume_no_ref_1.nodes["Group Input"].width  = 140.0
    plate_volume_no_ref_1.nodes["Group Input"].height = 100.0

    plate_volume_no_ref_1.nodes["Extrude Mesh.002"].width  = 140.0
    plate_volume_no_ref_1.nodes["Extrude Mesh.002"].height = 100.0

    plate_volume_no_ref_1.nodes["Delete Geometry.002"].width  = 140.0
    plate_volume_no_ref_1.nodes["Delete Geometry.002"].height = 100.0

    plate_volume_no_ref_1.nodes["Reroute.024"].width  = 100.0
    plate_volume_no_ref_1.nodes["Reroute.024"].height = 100.0

    plate_volume_no_ref_1.nodes["Plate\\"].width  = 1840.965576171875
    plate_volume_no_ref_1.nodes["Plate\\"].height = 861.1449584960938

    plate_volume_no_ref_1.nodes["Math.007"].width  = 140.0
    plate_volume_no_ref_1.nodes["Math.007"].height = 100.0

    plate_volume_no_ref_1.nodes["Math.006"].width  = 140.0
    plate_volume_no_ref_1.nodes["Math.006"].height = 100.0

    plate_volume_no_ref_1.nodes["Switch"].width  = 140.0
    plate_volume_no_ref_1.nodes["Switch"].height = 100.0

    plate_volume_no_ref_1.nodes["Reroute"].width  = 100.0
    plate_volume_no_ref_1.nodes["Reroute"].height = 100.0

    plate_volume_no_ref_1.nodes["Reroute.001"].width  = 100.0
    plate_volume_no_ref_1.nodes["Reroute.001"].height = 100.0

    plate_volume_no_ref_1.nodes["Reroute.002"].width  = 100.0
    plate_volume_no_ref_1.nodes["Reroute.002"].height = 100.0

    plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].width  = 220.0
    plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].height = 100.0

    plate_volume_no_ref_1.nodes["Group Input.001"].width  = 140.0
    plate_volume_no_ref_1.nodes["Group Input.001"].height = 100.0

    plate_volume_no_ref_1.nodes["Viewer"].width  = 140.0
    plate_volume_no_ref_1.nodes["Viewer"].height = 100.0

    plate_volume_no_ref_1.nodes["Join Strings"].width  = 140.0
    plate_volume_no_ref_1.nodes["Join Strings"].height = 100.0

    plate_volume_no_ref_1.nodes["String"].width  = 140.0
    plate_volume_no_ref_1.nodes["String"].height = 100.0

    plate_volume_no_ref_1.nodes["String.001"].width  = 140.0
    plate_volume_no_ref_1.nodes["String.001"].height = 100.0

    plate_volume_no_ref_1.nodes["String.002"].width  = 140.0
    plate_volume_no_ref_1.nodes["String.002"].height = 100.0

    plate_volume_no_ref_1.nodes["Join Strings.001"].width  = 140.0
    plate_volume_no_ref_1.nodes["Join Strings.001"].height = 100.0

    plate_volume_no_ref_1.nodes["Join Strings.002"].width  = 140.0
    plate_volume_no_ref_1.nodes["Join Strings.002"].height = 100.0

    plate_volume_no_ref_1.nodes["Reroute.003"].width  = 100.0
    plate_volume_no_ref_1.nodes["Reroute.003"].height = 100.0


    # Initialize plate_volume_no_ref_1 links

    # extrude_mesh_002.Mesh -> delete_geometry_002.Geometry
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Extrude Mesh.002"].outputs[0],
        plate_volume_no_ref_1.nodes["Delete Geometry.002"].inputs[0]
    )
    # extrude_mesh_002.Side -> delete_geometry_002.Selection
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Extrude Mesh.002"].outputs[2],
        plate_volume_no_ref_1.nodes["Delete Geometry.002"].inputs[1]
    )
    # group_input.Layer Offset -> reroute_024.Input
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Group Input"].outputs[3],
        plate_volume_no_ref_1.nodes["Reroute.024"].inputs[0]
    )
    # math_007.Value -> math_006.Value
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Math.007"].outputs[0],
        plate_volume_no_ref_1.nodes["Math.006"].inputs[0]
    )
    # reroute_024.Output -> math_007.Value
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.024"].outputs[0],
        plate_volume_no_ref_1.nodes["Math.007"].inputs[0]
    )
    # reroute_001.Output -> switch.Switch
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.001"].outputs[0],
        plate_volume_no_ref_1.nodes["Switch"].inputs[0]
    )
    # math_006.Value -> switch.True
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Math.006"].outputs[0],
        plate_volume_no_ref_1.nodes["Switch"].inputs[2]
    )
    # group_input.Limit Thickness -> reroute.Input
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Group Input"].outputs[2],
        plate_volume_no_ref_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> reroute_001.Input
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute"].outputs[0],
        plate_volume_no_ref_1.nodes["Reroute.001"].inputs[0]
    )
    # group_input.Bottom Plate -> extrude_mesh_002.Mesh
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Group Input"].outputs[0],
        plate_volume_no_ref_1.nodes["Extrude Mesh.002"].inputs[0]
    )
    # group_input.Top Material -> reroute_002.Input
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Group Input"].outputs[4],
        plate_volume_no_ref_1.nodes["Reroute.002"].inputs[0]
    )
    # delete_geometry_002.Geometry -> cutout_thickness_labeled.Cutout
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Delete Geometry.002"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[0]
    )
    # switch.Output -> cutout_thickness_labeled.Offset Scale
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Switch"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[1]
    )
    # reroute_002.Output -> cutout_thickness_labeled.Top Material
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.002"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[2]
    )
    # reroute_002.Output -> cutout_thickness_labeled.Side Material
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.002"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[3]
    )
    # cutout_thickness_labeled.Geometry -> plate.Geometry
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].outputs[0],
        plate_volume_no_ref_1.nodes["Plate"].inputs[0]
    )
    # reroute_024.Output -> extrude_mesh_002.Offset Scale
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.024"].outputs[0],
        plate_volume_no_ref_1.nodes["Extrude Mesh.002"].inputs[3]
    )
    # group_input.Flat Offset -> switch.False
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Group Input"].outputs[1],
        plate_volume_no_ref_1.nodes["Switch"].inputs[1]
    )
    # cutout_thickness_labeled.Geometry -> viewer.Geometry
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].outputs[0],
        plate_volume_no_ref_1.nodes["Viewer"].inputs[0]
    )
    # group_input_001.Dermis Label -> reroute_003.Input
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Group Input.001"].outputs[5],
        plate_volume_no_ref_1.nodes["Reroute.003"].inputs[0]
    )
    # string.String -> join_strings_002.Strings
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["String"].outputs[0],
        plate_volume_no_ref_1.nodes["Join Strings.002"].inputs[1]
    )
    # string_001.String -> join_strings_001.Strings
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["String.001"].outputs[0],
        plate_volume_no_ref_1.nodes["Join Strings.001"].inputs[1]
    )
    # string_002.String -> join_strings.Strings
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["String.002"].outputs[0],
        plate_volume_no_ref_1.nodes["Join Strings"].inputs[1]
    )
    # join_strings_002.String -> cutout_thickness_labeled.Dermis Top Label
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Join Strings.002"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[4]
    )
    # join_strings_001.String -> cutout_thickness_labeled.Dermis Bottom Label
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Join Strings.001"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[6]
    )
    # reroute_003.Output -> cutout_thickness_labeled.Dermis Full Label
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.003"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[5]
    )
    # join_strings.String -> cutout_thickness_labeled.Dermis Side Label
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Join Strings"].outputs[0],
        plate_volume_no_ref_1.nodes["Cutout Thickness Labeled"].inputs[7]
    )
    # reroute_003.Output -> join_strings.Strings
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.003"].outputs[0],
        plate_volume_no_ref_1.nodes["Join Strings"].inputs[1]
    )
    # reroute_003.Output -> join_strings_001.Strings
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.003"].outputs[0],
        plate_volume_no_ref_1.nodes["Join Strings.001"].inputs[1]
    )
    # reroute_003.Output -> join_strings_002.Strings
    plate_volume_no_ref_1.links.new(
        plate_volume_no_ref_1.nodes["Reroute.003"].outputs[0],
        plate_volume_no_ref_1.nodes["Join Strings.002"].inputs[1]
    )
    viewer.viewer_items[0].auto_remove = True

    return plate_volume_no_ref_1


def dermis_layer__generic__1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Dermis Layer (Generic) node group"""
    dermis_layer__generic__1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Dermis Layer (Generic)")

    dermis_layer__generic__1.color_tag = 'NONE'
    dermis_layer__generic__1.description = ""
    dermis_layer__generic__1.default_group_node_width = 140
    dermis_layer__generic__1.is_modifier = True
    dermis_layer__generic__1.show_modifier_manage_panel = True

    # dermis_layer__generic__1 interface

    # Socket Geometry
    geometry_socket = dermis_layer__generic__1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Dermis
    dermis_socket = dermis_layer__generic__1.interface.new_socket(name="Dermis", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    dermis_socket.attribute_domain = 'POINT'
    dermis_socket.default_input = 'VALUE'
    dermis_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = dermis_layer__generic__1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Include Original Geometry
    include_original_geometry_socket = dermis_layer__generic__1.interface.new_socket(name="Include Original Geometry", in_out='INPUT', socket_type='NodeSocketBool')
    include_original_geometry_socket.default_value = True
    include_original_geometry_socket.attribute_domain = 'POINT'
    include_original_geometry_socket.default_input = 'VALUE'
    include_original_geometry_socket.structure_type = 'AUTO'

    # Socket Paint Name
    paint_name_socket = dermis_layer__generic__1.interface.new_socket(name="Paint Name", in_out='INPUT', socket_type='NodeSocketString')
    paint_name_socket.default_value = "Dermis"
    paint_name_socket.subtype = 'NONE'
    paint_name_socket.attribute_domain = 'POINT'
    paint_name_socket.description = "Weight paint group to include dermis over"
    paint_name_socket.default_input = 'VALUE'
    paint_name_socket.structure_type = 'AUTO'

    # Socket Cutout Tolerance
    cutout_tolerance_socket = dermis_layer__generic__1.interface.new_socket(name="Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat')
    cutout_tolerance_socket.default_value = 50.0
    cutout_tolerance_socket.min_value = 0.0
    cutout_tolerance_socket.max_value = 100.0
    cutout_tolerance_socket.subtype = 'PERCENTAGE'
    cutout_tolerance_socket.attribute_domain = 'POINT'
    cutout_tolerance_socket.default_input = 'VALUE'
    cutout_tolerance_socket.structure_type = 'AUTO'

    # Socket Thickness
    thickness_socket = dermis_layer__generic__1.interface.new_socket(name="Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    thickness_socket.default_value = 0.10000000149011612
    thickness_socket.min_value = 0.0
    thickness_socket.max_value = 3.4028234663852886e+38
    thickness_socket.subtype = 'NONE'
    thickness_socket.attribute_domain = 'POINT'
    thickness_socket.default_input = 'VALUE'
    thickness_socket.structure_type = 'AUTO'

    # Socket Plate Offset
    plate_offset_socket = dermis_layer__generic__1.interface.new_socket(name="Plate Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    plate_offset_socket.default_value = 0.004999999888241291
    plate_offset_socket.min_value = -1.0
    plate_offset_socket.max_value = 1.0
    plate_offset_socket.subtype = 'DISTANCE'
    plate_offset_socket.attribute_domain = 'POINT'
    plate_offset_socket.description = "Percentage of thickness"
    plate_offset_socket.default_input = 'VALUE'
    plate_offset_socket.structure_type = 'AUTO'

    # Socket Smoothing
    smoothing_socket = dermis_layer__generic__1.interface.new_socket(name="Smoothing", in_out='INPUT', socket_type='NodeSocketBool')
    smoothing_socket.default_value = True
    smoothing_socket.attribute_domain = 'POINT'
    smoothing_socket.default_input = 'VALUE'
    smoothing_socket.structure_type = 'AUTO'

    # Socket Smooth Sampling
    smooth_sampling_socket = dermis_layer__generic__1.interface.new_socket(name="Smooth Sampling", in_out='INPUT', socket_type='NodeSocketInt')
    smooth_sampling_socket.default_value = 30
    smooth_sampling_socket.min_value = 1
    smooth_sampling_socket.max_value = 100000
    smooth_sampling_socket.subtype = 'NONE'
    smooth_sampling_socket.attribute_domain = 'POINT'
    smooth_sampling_socket.default_input = 'VALUE'
    smooth_sampling_socket.structure_type = 'AUTO'

    # Panel Customization
    customization_panel = dermis_layer__generic__1.interface.new_panel("Customization", default_closed=True)
    # Socket Top Material
    top_material_socket = dermis_layer__generic__1.interface.new_socket(name="Top Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = customization_panel)
    top_material_socket.attribute_domain = 'POINT'
    top_material_socket.default_input = 'VALUE'
    top_material_socket.structure_type = 'AUTO'


    # Panel Options
    options_panel = dermis_layer__generic__1.interface.new_panel("Options", default_closed=True)
    # Socket Options
    options_socket = dermis_layer__generic__1.interface.new_socket(name="Options", in_out='INPUT', socket_type='NodeSocketMenu', parent = options_panel)
    options_socket.attribute_domain = 'POINT'
    options_socket.default_input = 'VALUE'
    options_socket.structure_type = 'AUTO'
    options_socket.optional_label = True

    # Socket Base Modifier
    base_modifier_socket = dermis_layer__generic__1.interface.new_socket(name="Base Modifier", in_out='INPUT', socket_type='NodeSocketBool', parent = options_panel)
    base_modifier_socket.default_value = True
    base_modifier_socket.attribute_domain = 'POINT'
    base_modifier_socket.default_input = 'VALUE'
    base_modifier_socket.structure_type = 'AUTO'

    # Socket Dermis Label
    dermis_label_socket = dermis_layer__generic__1.interface.new_socket(name="Dermis Label", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    dermis_label_socket.default_value = "dermis"
    dermis_label_socket.subtype = 'NONE'
    dermis_label_socket.attribute_domain = 'POINT'
    dermis_label_socket.default_input = 'VALUE'
    dermis_label_socket.structure_type = 'AUTO'


    # Panel Subtraction Paint
    subtraction_paint_panel = dermis_layer__generic__1.interface.new_panel("Subtraction Paint")
    subtraction_paint_panel.description = "Subtracts a given vertex group from the main vertex group. Used for specific cases like room for wiring."
    # Socket Subtraction Paint
    subtraction_paint_socket = dermis_layer__generic__1.interface.new_socket(name="Subtraction Paint", in_out='INPUT', socket_type='NodeSocketBool', parent = subtraction_paint_panel)
    subtraction_paint_socket.default_value = False
    subtraction_paint_socket.attribute_domain = 'POINT'
    subtraction_paint_socket.default_input = 'VALUE'
    subtraction_paint_socket.is_panel_toggle = True
    subtraction_paint_socket.structure_type = 'AUTO'

    # Socket Subtraction Paint Name
    subtraction_paint_name_socket = dermis_layer__generic__1.interface.new_socket(name="Subtraction Paint Name", in_out='INPUT', socket_type='NodeSocketString', parent = subtraction_paint_panel)
    subtraction_paint_name_socket.default_value = "Dermis Hole"
    subtraction_paint_name_socket.subtype = 'NONE'
    subtraction_paint_name_socket.attribute_domain = 'POINT'
    subtraction_paint_name_socket.default_input = 'VALUE'
    subtraction_paint_name_socket.structure_type = 'AUTO'
    subtraction_paint_name_socket.optional_label = True

    # Socket Subtraction Cutout Tolerance
    subtraction_cutout_tolerance_socket = dermis_layer__generic__1.interface.new_socket(name="Subtraction Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat', parent = subtraction_paint_panel)
    subtraction_cutout_tolerance_socket.default_value = 0.0
    subtraction_cutout_tolerance_socket.min_value = 0.0
    subtraction_cutout_tolerance_socket.max_value = 100.0
    subtraction_cutout_tolerance_socket.subtype = 'PERCENTAGE'
    subtraction_cutout_tolerance_socket.attribute_domain = 'POINT'
    subtraction_cutout_tolerance_socket.default_input = 'VALUE'
    subtraction_cutout_tolerance_socket.structure_type = 'AUTO'


    # Initialize dermis_layer__generic__1 nodes

    # Node Group Input
    group_input = dermis_layer__generic__1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = dermis_layer__generic__1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group.008
    group_008 = dermis_layer__generic__1.nodes.new("GeometryNodeGroup")
    group_008.name = "Group.008"
    group_008.show_options = True
    group_008.node_tree = bpy.data.node_groups[node_tree_names[skin_cutout_2_1_node_group]]

    # Node Menu Switch
    menu_switch = dermis_layer__generic__1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.show_options = True
    menu_switch.active_index = 1
    menu_switch.data_type = 'BOOLEAN'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Default")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Advanced")
    menu_switch.enum_items[1].description = ""
    # Item_2
    menu_switch.inputs[1].default_value = False
    # Item_3
    menu_switch.inputs[2].default_value = True

    # Node Switch
    switch = dermis_layer__generic__1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'STRING'
    # False
    switch.inputs[1].default_value = "dermis"

    # Node Switch.001
    switch_001 = dermis_layer__generic__1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'GEOMETRY'

    # Node Join Geometry
    join_geometry = dermis_layer__generic__1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Store Named Attribute
    store_named_attribute = dermis_layer__generic__1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "thickness"

    # Node Reroute
    reroute = dermis_layer__generic__1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Reroute.001
    reroute_001 = dermis_layer__generic__1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Store Named Attribute.001
    store_named_attribute_001 = dermis_layer__generic__1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "original"
    # Value
    store_named_attribute_001.inputs[3].default_value = True

    # Node Switch.004
    switch_004 = dermis_layer__generic__1.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.show_options = True
    switch_004.input_type = 'GEOMETRY'

    # Node Reroute.002
    reroute_002 = dermis_layer__generic__1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Reroute.003
    reroute_003 = dermis_layer__generic__1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketMaterial"
    # Node Reroute.004
    reroute_004 = dermis_layer__generic__1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketGeometry"
    # Node Reroute.006
    reroute_006 = dermis_layer__generic__1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketGeometry"
    # Node Reroute.007
    reroute_007 = dermis_layer__generic__1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketGeometry"
    # Node Plate Volume Reduced.001
    plate_volume_reduced_001 = dermis_layer__generic__1.nodes.new("GeometryNodeGroup")
    plate_volume_reduced_001.name = "Plate Volume Reduced.001"
    plate_volume_reduced_001.show_options = True
    plate_volume_reduced_001.node_tree = bpy.data.node_groups[node_tree_names[plate_volume_no_ref_1_node_group]]
    # Socket_3
    plate_volume_reduced_001.inputs[2].default_value = False

    # Set locations
    dermis_layer__generic__1.nodes["Group Input"].location = (-1440.0, -20.0)
    dermis_layer__generic__1.nodes["Group Output"].location = (1340.0, 180.0)
    dermis_layer__generic__1.nodes["Group.008"].location = (-580.0, 20.0)
    dermis_layer__generic__1.nodes["Menu Switch"].location = (-1000.0, -460.0)
    dermis_layer__generic__1.nodes["Switch"].location = (-680.0000610351562, -320.0)
    dermis_layer__generic__1.nodes["Switch.001"].location = (40.0, 240.0)
    dermis_layer__generic__1.nodes["Join Geometry"].location = (1120.0, 120.0)
    dermis_layer__generic__1.nodes["Store Named Attribute"].location = (60.0, 0.0)
    dermis_layer__generic__1.nodes["Reroute"].location = (-40.0, -680.0)
    dermis_layer__generic__1.nodes["Reroute.001"].location = (-1020.0, -680.0)
    dermis_layer__generic__1.nodes["Store Named Attribute.001"].location = (-820.0, 240.0)
    dermis_layer__generic__1.nodes["Switch.004"].location = (-600.0, 500.0)
    dermis_layer__generic__1.nodes["Reroute.002"].location = (-279.9999694824219, -320.0)
    dermis_layer__generic__1.nodes["Reroute.003"].location = (-320.0, -339.9999694824219)
    dermis_layer__generic__1.nodes["Reroute.004"].location = (880.3452758789062, 110.21099853515625)
    dermis_layer__generic__1.nodes["Reroute.006"].location = (909.3463745117188, 54.0033073425293)
    dermis_layer__generic__1.nodes["Reroute.007"].location = (1260.0, 40.0)
    dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].location = (-220.0, -240.0)

    # Set dimensions
    dermis_layer__generic__1.nodes["Group Input"].width  = 140.0
    dermis_layer__generic__1.nodes["Group Input"].height = 100.0

    dermis_layer__generic__1.nodes["Group Output"].width  = 140.0
    dermis_layer__generic__1.nodes["Group Output"].height = 100.0

    dermis_layer__generic__1.nodes["Group.008"].width  = 200.0
    dermis_layer__generic__1.nodes["Group.008"].height = 100.0

    dermis_layer__generic__1.nodes["Menu Switch"].width  = 140.0
    dermis_layer__generic__1.nodes["Menu Switch"].height = 100.0

    dermis_layer__generic__1.nodes["Switch"].width  = 220.0
    dermis_layer__generic__1.nodes["Switch"].height = 100.0

    dermis_layer__generic__1.nodes["Switch.001"].width  = 140.0
    dermis_layer__generic__1.nodes["Switch.001"].height = 100.0

    dermis_layer__generic__1.nodes["Join Geometry"].width  = 140.0
    dermis_layer__generic__1.nodes["Join Geometry"].height = 100.0

    dermis_layer__generic__1.nodes["Store Named Attribute"].width  = 140.0
    dermis_layer__generic__1.nodes["Store Named Attribute"].height = 100.0

    dermis_layer__generic__1.nodes["Reroute"].width  = 100.0
    dermis_layer__generic__1.nodes["Reroute"].height = 100.0

    dermis_layer__generic__1.nodes["Reroute.001"].width  = 100.0
    dermis_layer__generic__1.nodes["Reroute.001"].height = 100.0

    dermis_layer__generic__1.nodes["Store Named Attribute.001"].width  = 140.0
    dermis_layer__generic__1.nodes["Store Named Attribute.001"].height = 100.0

    dermis_layer__generic__1.nodes["Switch.004"].width  = 140.0
    dermis_layer__generic__1.nodes["Switch.004"].height = 100.0

    dermis_layer__generic__1.nodes["Reroute.002"].width  = 100.0
    dermis_layer__generic__1.nodes["Reroute.002"].height = 100.0

    dermis_layer__generic__1.nodes["Reroute.003"].width  = 100.0
    dermis_layer__generic__1.nodes["Reroute.003"].height = 100.0

    dermis_layer__generic__1.nodes["Reroute.004"].width  = 100.0
    dermis_layer__generic__1.nodes["Reroute.004"].height = 100.0

    dermis_layer__generic__1.nodes["Reroute.006"].width  = 100.0
    dermis_layer__generic__1.nodes["Reroute.006"].height = 100.0

    dermis_layer__generic__1.nodes["Reroute.007"].width  = 100.0
    dermis_layer__generic__1.nodes["Reroute.007"].height = 100.0

    dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].width  = 200.0
    dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].height = 100.0


    # Initialize dermis_layer__generic__1 links

    # group_input.Geometry -> group_008.Mesh
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[0],
        dermis_layer__generic__1.nodes["Group.008"].inputs[0]
    )
    # group_input.Options -> menu_switch.Menu
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[9],
        dermis_layer__generic__1.nodes["Menu Switch"].inputs[0]
    )
    # menu_switch.Output -> switch.Switch
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Menu Switch"].outputs[0],
        dermis_layer__generic__1.nodes["Switch"].inputs[0]
    )
    # group_input.Paint Name -> group_008.Paint Name
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[2],
        dermis_layer__generic__1.nodes["Group.008"].inputs[2]
    )
    # group_input.Cutout Tolerance -> group_008.Cutout Tolerance
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[3],
        dermis_layer__generic__1.nodes["Group.008"].inputs[3]
    )
    # group_input.Smoothing -> group_008.Smoothing
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[6],
        dermis_layer__generic__1.nodes["Group.008"].inputs[1]
    )
    # group_input.Smooth Sampling -> group_008.Smooth Sampling
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[7],
        dermis_layer__generic__1.nodes["Group.008"].inputs[4]
    )
    # group_input.Include Original Geometry -> switch_001.Switch
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[1],
        dermis_layer__generic__1.nodes["Switch.001"].inputs[0]
    )
    # reroute_006.Output -> join_geometry.Geometry
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute.006"].outputs[0],
        dermis_layer__generic__1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Dermis Label -> switch.True
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[11],
        dermis_layer__generic__1.nodes["Switch"].inputs[2]
    )
    # reroute.Output -> store_named_attribute.Value
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute"].outputs[0],
        dermis_layer__generic__1.nodes["Store Named Attribute"].inputs[3]
    )
    # reroute_001.Output -> reroute.Input
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute.001"].outputs[0],
        dermis_layer__generic__1.nodes["Reroute"].inputs[0]
    )
    # group_input.Thickness -> reroute_001.Input
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[4],
        dermis_layer__generic__1.nodes["Reroute.001"].inputs[0]
    )
    # group_input.Geometry -> store_named_attribute_001.Geometry
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[0],
        dermis_layer__generic__1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # group_input.Geometry -> switch_004.False
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[0],
        dermis_layer__generic__1.nodes["Switch.004"].inputs[1]
    )
    # store_named_attribute_001.Geometry -> switch_004.True
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Store Named Attribute.001"].outputs[0],
        dermis_layer__generic__1.nodes["Switch.004"].inputs[2]
    )
    # switch_004.Output -> switch_001.True
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Switch.004"].outputs[0],
        dermis_layer__generic__1.nodes["Switch.001"].inputs[2]
    )
    # group_input.Base Modifier -> switch_004.Switch
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[10],
        dermis_layer__generic__1.nodes["Switch.004"].inputs[0]
    )
    # group_input.Thickness -> reroute_002.Input
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[4],
        dermis_layer__generic__1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Top Material -> reroute_003.Input
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[8],
        dermis_layer__generic__1.nodes["Reroute.003"].inputs[0]
    )
    # switch_001.Output -> reroute_004.Input
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Switch.001"].outputs[0],
        dermis_layer__generic__1.nodes["Reroute.004"].inputs[0]
    )
    # store_named_attribute.Geometry -> reroute_006.Input
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Store Named Attribute"].outputs[0],
        dermis_layer__generic__1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_007.Output -> group_output.Dermis
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute.007"].outputs[0],
        dermis_layer__generic__1.nodes["Group Output"].inputs[1]
    )
    # reroute_006.Output -> reroute_007.Input
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute.006"].outputs[0],
        dermis_layer__generic__1.nodes["Reroute.007"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Geometry
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Join Geometry"].outputs[0],
        dermis_layer__generic__1.nodes["Group Output"].inputs[0]
    )
    # group_008.Geometry -> plate_volume_reduced_001.Bottom Plate
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group.008"].outputs[0],
        dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].inputs[0]
    )
    # reroute_003.Output -> plate_volume_reduced_001.Top Material
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute.003"].outputs[0],
        dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].inputs[4]
    )
    # group_input.Plate Offset -> plate_volume_reduced_001.Layer Offset
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[5],
        dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].inputs[3]
    )
    # reroute_002.Output -> plate_volume_reduced_001.Flat Offset
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute.002"].outputs[0],
        dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].inputs[1]
    )
    # plate_volume_reduced_001.Geometry -> store_named_attribute.Geometry
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].outputs[0],
        dermis_layer__generic__1.nodes["Store Named Attribute"].inputs[0]
    )
    # switch.Output -> plate_volume_reduced_001.Dermis Label
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Switch"].outputs[0],
        dermis_layer__generic__1.nodes["Plate Volume Reduced.001"].inputs[5]
    )
    # group_input.Subtraction Paint Name -> group_008.Subtraction Paint Name
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[13],
        dermis_layer__generic__1.nodes["Group.008"].inputs[5]
    )
    # group_input.Subtraction Cutout Tolerance -> group_008.Subtraction Cutout Tolerance
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[14],
        dermis_layer__generic__1.nodes["Group.008"].inputs[6]
    )
    # group_input.Subtraction Paint -> group_008.Subtraction Layer
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Group Input"].outputs[12],
        dermis_layer__generic__1.nodes["Group.008"].inputs[7]
    )
    # reroute_004.Output -> join_geometry.Geometry
    dermis_layer__generic__1.links.new(
        dermis_layer__generic__1.nodes["Reroute.004"].outputs[0],
        dermis_layer__generic__1.nodes["Join Geometry"].inputs[0]
    )
    options_socket.default_value = 'Default'

    return dermis_layer__generic__1


def dermis_layer_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Dermis Layer node group"""
    dermis_layer_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Dermis Layer")

    dermis_layer_1.color_tag = 'NONE'
    dermis_layer_1.description = ""
    dermis_layer_1.default_group_node_width = 140
    dermis_layer_1.is_modifier = True
    dermis_layer_1.show_modifier_manage_panel = True

    # dermis_layer_1 interface

    # Socket Geometry
    geometry_socket = dermis_layer_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = dermis_layer_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Include Original Geometry
    include_original_geometry_socket = dermis_layer_1.interface.new_socket(name="Include Original Geometry", in_out='INPUT', socket_type='NodeSocketBool')
    include_original_geometry_socket.default_value = True
    include_original_geometry_socket.attribute_domain = 'POINT'
    include_original_geometry_socket.default_input = 'VALUE'
    include_original_geometry_socket.structure_type = 'AUTO'

    # Socket Paint Name
    paint_name_socket = dermis_layer_1.interface.new_socket(name="Paint Name", in_out='INPUT', socket_type='NodeSocketString')
    paint_name_socket.default_value = "Dermis"
    paint_name_socket.subtype = 'NONE'
    paint_name_socket.attribute_domain = 'POINT'
    paint_name_socket.description = "Weight paint group to include dermis over"
    paint_name_socket.default_input = 'VALUE'
    paint_name_socket.structure_type = 'AUTO'

    # Socket Cutout Tolerance
    cutout_tolerance_socket = dermis_layer_1.interface.new_socket(name="Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat')
    cutout_tolerance_socket.default_value = 50.0
    cutout_tolerance_socket.min_value = 0.0
    cutout_tolerance_socket.max_value = 100.0
    cutout_tolerance_socket.subtype = 'PERCENTAGE'
    cutout_tolerance_socket.attribute_domain = 'POINT'
    cutout_tolerance_socket.default_input = 'VALUE'
    cutout_tolerance_socket.structure_type = 'AUTO'

    # Socket Thickness
    thickness_socket = dermis_layer_1.interface.new_socket(name="Thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    thickness_socket.default_value = 0.10000000149011612
    thickness_socket.min_value = 0.0
    thickness_socket.max_value = 3.4028234663852886e+38
    thickness_socket.subtype = 'DISTANCE'
    thickness_socket.attribute_domain = 'POINT'
    thickness_socket.default_input = 'VALUE'
    thickness_socket.structure_type = 'AUTO'

    # Socket Plate Offset
    plate_offset_socket = dermis_layer_1.interface.new_socket(name="Plate Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    plate_offset_socket.default_value = 0.004999999888241291
    plate_offset_socket.min_value = -1.0
    plate_offset_socket.max_value = 1.0
    plate_offset_socket.subtype = 'DISTANCE'
    plate_offset_socket.attribute_domain = 'POINT'
    plate_offset_socket.description = "Percentage of thickness"
    plate_offset_socket.default_input = 'VALUE'
    plate_offset_socket.structure_type = 'AUTO'

    # Socket Smoothing
    smoothing_socket = dermis_layer_1.interface.new_socket(name="Smoothing", in_out='INPUT', socket_type='NodeSocketBool')
    smoothing_socket.default_value = True
    smoothing_socket.attribute_domain = 'POINT'
    smoothing_socket.default_input = 'VALUE'
    smoothing_socket.structure_type = 'AUTO'

    # Socket Smooth Sampling
    smooth_sampling_socket = dermis_layer_1.interface.new_socket(name="Smooth Sampling", in_out='INPUT', socket_type='NodeSocketInt')
    smooth_sampling_socket.default_value = 30
    smooth_sampling_socket.min_value = 1
    smooth_sampling_socket.max_value = 100000
    smooth_sampling_socket.subtype = 'NONE'
    smooth_sampling_socket.attribute_domain = 'POINT'
    smooth_sampling_socket.default_input = 'VALUE'
    smooth_sampling_socket.structure_type = 'AUTO'

    # Panel Subtraction Hole
    subtraction_hole_panel = dermis_layer_1.interface.new_panel("Subtraction Hole")
    # Socket Subtraction Hole
    subtraction_hole_socket = dermis_layer_1.interface.new_socket(name="Subtraction Hole", in_out='INPUT', socket_type='NodeSocketBool', parent = subtraction_hole_panel)
    subtraction_hole_socket.default_value = False
    subtraction_hole_socket.attribute_domain = 'POINT'
    subtraction_hole_socket.default_input = 'VALUE'
    subtraction_hole_socket.is_panel_toggle = True
    subtraction_hole_socket.structure_type = 'AUTO'

    # Socket Subtraction Paint Name
    subtraction_paint_name_socket = dermis_layer_1.interface.new_socket(name="Subtraction Paint Name", in_out='INPUT', socket_type='NodeSocketString', parent = subtraction_hole_panel)
    subtraction_paint_name_socket.default_value = "Dermis Hole"
    subtraction_paint_name_socket.subtype = 'NONE'
    subtraction_paint_name_socket.attribute_domain = 'POINT'
    subtraction_paint_name_socket.default_input = 'VALUE'
    subtraction_paint_name_socket.structure_type = 'AUTO'
    subtraction_paint_name_socket.optional_label = True

    # Socket Subtraction Cutout Tolerance
    subtraction_cutout_tolerance_socket = dermis_layer_1.interface.new_socket(name="Subtraction Cutout Tolerance", in_out='INPUT', socket_type='NodeSocketFloat', parent = subtraction_hole_panel)
    subtraction_cutout_tolerance_socket.default_value = 0.0
    subtraction_cutout_tolerance_socket.min_value = 0.0
    subtraction_cutout_tolerance_socket.max_value = 100.0
    subtraction_cutout_tolerance_socket.subtype = 'PERCENTAGE'
    subtraction_cutout_tolerance_socket.attribute_domain = 'POINT'
    subtraction_cutout_tolerance_socket.default_input = 'VALUE'
    subtraction_cutout_tolerance_socket.structure_type = 'AUTO'

    # Socket Subtraction Thickness
    subtraction_thickness_socket = dermis_layer_1.interface.new_socket(name="Subtraction Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = subtraction_hole_panel)
    subtraction_thickness_socket.default_value = 50.0
    subtraction_thickness_socket.min_value = 0.0
    subtraction_thickness_socket.max_value = 100.0
    subtraction_thickness_socket.subtype = 'PERCENTAGE'
    subtraction_thickness_socket.attribute_domain = 'POINT'
    subtraction_thickness_socket.default_input = 'VALUE'
    subtraction_thickness_socket.structure_type = 'AUTO'

    # Socket Vertex Merge Distance
    vertex_merge_distance_socket = dermis_layer_1.interface.new_socket(name="Vertex Merge Distance", in_out='INPUT', socket_type='NodeSocketFloat', parent = subtraction_hole_panel)
    vertex_merge_distance_socket.default_value = 0.009999999776482582
    vertex_merge_distance_socket.min_value = 0.0
    vertex_merge_distance_socket.max_value = 3.4028234663852886e+38
    vertex_merge_distance_socket.subtype = 'DISTANCE'
    vertex_merge_distance_socket.attribute_domain = 'POINT'
    vertex_merge_distance_socket.description = "Only modify if there are broken edges inbetween hole and non-hole layers"
    vertex_merge_distance_socket.default_input = 'VALUE'
    vertex_merge_distance_socket.structure_type = 'AUTO'


    # Initialize dermis_layer_1 nodes

    # Node Group Input
    group_input = dermis_layer_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = dermis_layer_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Dermis Layer (Generic)
    dermis_layer__generic_ = dermis_layer_1.nodes.new("GeometryNodeGroup")
    dermis_layer__generic_.name = "Dermis Layer (Generic)"
    dermis_layer__generic_.show_options = True
    dermis_layer__generic_.node_tree = bpy.data.node_groups[node_tree_names[dermis_layer__generic__1_node_group]]
    # Socket_3
    dermis_layer__generic_.inputs[1].default_value = False
    # Socket_13
    dermis_layer__generic_.inputs[9].default_value = 'Default'
    # Socket_14
    dermis_layer__generic_.inputs[10].default_value = True
    # Socket_15
    dermis_layer__generic_.inputs[11].default_value = "dermis"
    # Socket_17
    dermis_layer__generic_.inputs[12].default_value = False
    # Socket_18
    dermis_layer__generic_.inputs[13].default_value = "Dermis Hole"

    # Node Dermis Layer (Generic).001
    dermis_layer__generic__001 = dermis_layer_1.nodes.new("GeometryNodeGroup")
    dermis_layer__generic__001.name = "Dermis Layer (Generic).001"
    dermis_layer__generic__001.show_options = True
    dermis_layer__generic__001.node_tree = bpy.data.node_groups[node_tree_names[dermis_layer__generic__1_node_group]]
    # Socket_3
    dermis_layer__generic__001.inputs[1].default_value = False
    # Socket_7
    dermis_layer__generic__001.inputs[5].default_value = 0.0
    # Socket_13
    dermis_layer__generic__001.inputs[9].default_value = 'Default'
    # Socket_14
    dermis_layer__generic__001.inputs[10].default_value = True
    # Socket_15
    dermis_layer__generic__001.inputs[11].default_value = "dermis"

    # Node Join Geometry
    join_geometry = dermis_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Reroute
    reroute = dermis_layer_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketBool"
    # Node Reroute.001
    reroute_001 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.002
    reroute_002 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.003
    reroute_003 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketString"
    # Node Reroute.004
    reroute_004 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketString"
    # Node Reroute.005
    reroute_005 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.006
    reroute_006 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketBool"
    # Node Reroute.007
    reroute_007 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketInt"
    # Node Reroute.008
    reroute_008 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketFloatDistance"
    # Node Merge by Distance
    merge_by_distance = dermis_layer_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.show_options = True
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'

    # Node Math
    math = dermis_layer_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Math.001
    math_001 = dermis_layer_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'DIVIDE'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 100.0

    # Node Math.002
    math_002 = dermis_layer_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'SUBTRACT'
    math_002.use_clamp = False

    # Node Frame
    frame = dermis_layer_1.nodes.new("NodeFrame")
    frame.label = "Combination of both hole and non-hole layers"
    frame.name = "Frame"
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Switch
    switch = dermis_layer_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'GEOMETRY'

    # Node Math.003
    math_003 = dermis_layer_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'LESS_THAN'
    math_003.use_clamp = False
    # Value_001
    math_003.inputs[1].default_value = 99.9000015258789

    # Node Frame.001
    frame_001 = dermis_layer_1.nodes.new("NodeFrame")
    frame_001.label = "Only include non-hole layer if there is a mix"
    frame_001.name = "Frame.001"
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Switch.001
    switch_001 = dermis_layer_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'GEOMETRY'

    # Node Math.004
    math_004 = dermis_layer_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'GREATER_THAN'
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = 1.0

    # Node Frame.002
    frame_002 = dermis_layer_1.nodes.new("NodeFrame")
    frame_002.label = "Only include non-hole layer if there is a mix"
    frame_002.name = "Frame.002"
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Reroute.009
    reroute_009 = dermis_layer_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloatPercentage"
    # Node Switch.002
    switch_002 = dermis_layer_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.show_options = True
    switch_002.input_type = 'GEOMETRY'

    # Set parents
    dermis_layer_1.nodes["Dermis Layer (Generic)"].parent = dermis_layer_1.nodes["Frame"]
    dermis_layer_1.nodes["Dermis Layer (Generic).001"].parent = dermis_layer_1.nodes["Frame"]
    dermis_layer_1.nodes["Math"].parent = dermis_layer_1.nodes["Frame"]
    dermis_layer_1.nodes["Math.001"].parent = dermis_layer_1.nodes["Frame"]
    dermis_layer_1.nodes["Math.002"].parent = dermis_layer_1.nodes["Frame"]
    dermis_layer_1.nodes["Switch"].parent = dermis_layer_1.nodes["Frame.001"]
    dermis_layer_1.nodes["Math.003"].parent = dermis_layer_1.nodes["Frame.001"]
    dermis_layer_1.nodes["Switch.001"].parent = dermis_layer_1.nodes["Frame.002"]
    dermis_layer_1.nodes["Math.004"].parent = dermis_layer_1.nodes["Frame.002"]

    # Set locations
    dermis_layer_1.nodes["Group Input"].location = (-2060.0, -80.0)
    dermis_layer_1.nodes["Group Output"].location = (820.0, 20.0)
    dermis_layer_1.nodes["Dermis Layer (Generic)"].location = (908.9033203125, -55.806488037109375)
    dermis_layer_1.nodes["Dermis Layer (Generic).001"].location = (908.9033203125, -515.8065185546875)
    dermis_layer_1.nodes["Join Geometry"].location = (340.0, 20.0)
    dermis_layer_1.nodes["Reroute"].location = (-800.0, -240.0)
    dermis_layer_1.nodes["Reroute.001"].location = (-800.0, -180.0)
    dermis_layer_1.nodes["Reroute.002"].location = (-800.0, -120.0)
    dermis_layer_1.nodes["Reroute.003"].location = (-800.0, -40.0)
    dermis_layer_1.nodes["Reroute.004"].location = (-800.0, -260.0)
    dermis_layer_1.nodes["Reroute.005"].location = (-800.0, -80.0)
    dermis_layer_1.nodes["Reroute.006"].location = (-800.0, -140.0)
    dermis_layer_1.nodes["Reroute.007"].location = (-800.0, -160.0)
    dermis_layer_1.nodes["Reroute.008"].location = (-800.0, -100.0)
    dermis_layer_1.nodes["Merge by Distance"].location = (560.0, 20.0)
    dermis_layer_1.nodes["Math"].location = (268.9033203125, -935.8065185546875)
    dermis_layer_1.nodes["Math.001"].location = (28.9033203125, -1055.806396484375)
    dermis_layer_1.nodes["Math.002"].location = (428.9033203125, -735.8065185546875)
    dermis_layer_1.nodes["Frame"].location = (-1568.9033203125, 415.8064880371094)
    dermis_layer_1.nodes["Switch"].location = (249.16128540039062, -176.19354248046875)
    dermis_layer_1.nodes["Math.003"].location = (29.161285400390625, -36.19354248046875)
    dermis_layer_1.nodes["Frame.001"].location = (-289.1612854003906, 576.1935424804688)
    dermis_layer_1.nodes["Switch.001"].location = (248.92214965820312, -175.58087158203125)
    dermis_layer_1.nodes["Math.004"].location = (28.922149658203125, -35.58087158203125)
    dermis_layer_1.nodes["Frame.002"].location = (-258.9677429199219, -328.8387145996094)
    dermis_layer_1.nodes["Reroute.009"].location = (-398.8696594238281, 417.87493896484375)
    dermis_layer_1.nodes["Switch.002"].location = (-143.39479064941406, 116.47321319580078)

    # Set dimensions
    dermis_layer_1.nodes["Group Input"].width  = 140.0
    dermis_layer_1.nodes["Group Input"].height = 100.0

    dermis_layer_1.nodes["Group Output"].width  = 140.0
    dermis_layer_1.nodes["Group Output"].height = 100.0

    dermis_layer_1.nodes["Dermis Layer (Generic)"].width  = 140.0
    dermis_layer_1.nodes["Dermis Layer (Generic)"].height = 100.0

    dermis_layer_1.nodes["Dermis Layer (Generic).001"].width  = 180.0
    dermis_layer_1.nodes["Dermis Layer (Generic).001"].height = 100.0

    dermis_layer_1.nodes["Join Geometry"].width  = 140.0
    dermis_layer_1.nodes["Join Geometry"].height = 100.0

    dermis_layer_1.nodes["Reroute"].width  = 12.5
    dermis_layer_1.nodes["Reroute"].height = 100.0

    dermis_layer_1.nodes["Reroute.001"].width  = 12.5
    dermis_layer_1.nodes["Reroute.001"].height = 100.0

    dermis_layer_1.nodes["Reroute.002"].width  = 12.5
    dermis_layer_1.nodes["Reroute.002"].height = 100.0

    dermis_layer_1.nodes["Reroute.003"].width  = 12.5
    dermis_layer_1.nodes["Reroute.003"].height = 100.0

    dermis_layer_1.nodes["Reroute.004"].width  = 12.5
    dermis_layer_1.nodes["Reroute.004"].height = 100.0

    dermis_layer_1.nodes["Reroute.005"].width  = 12.5
    dermis_layer_1.nodes["Reroute.005"].height = 100.0

    dermis_layer_1.nodes["Reroute.006"].width  = 12.5
    dermis_layer_1.nodes["Reroute.006"].height = 100.0

    dermis_layer_1.nodes["Reroute.007"].width  = 12.5
    dermis_layer_1.nodes["Reroute.007"].height = 100.0

    dermis_layer_1.nodes["Reroute.008"].width  = 12.5
    dermis_layer_1.nodes["Reroute.008"].height = 100.0

    dermis_layer_1.nodes["Merge by Distance"].width  = 140.0
    dermis_layer_1.nodes["Merge by Distance"].height = 100.0

    dermis_layer_1.nodes["Math"].width  = 140.0
    dermis_layer_1.nodes["Math"].height = 100.0

    dermis_layer_1.nodes["Math.001"].width  = 140.0
    dermis_layer_1.nodes["Math.001"].height = 100.0

    dermis_layer_1.nodes["Math.002"].width  = 140.0
    dermis_layer_1.nodes["Math.002"].height = 100.0

    dermis_layer_1.nodes["Frame"].width  = 1117.5484619140625
    dermis_layer_1.nodes["Frame"].height = 1227.5484619140625

    dermis_layer_1.nodes["Switch"].width  = 140.0
    dermis_layer_1.nodes["Switch"].height = 100.0

    dermis_layer_1.nodes["Math.003"].width  = 140.0
    dermis_layer_1.nodes["Math.003"].height = 100.0

    dermis_layer_1.nodes["Frame.001"].width  = 417.93548583984375
    dermis_layer_1.nodes["Frame.001"].height = 344.32257080078125

    dermis_layer_1.nodes["Switch.001"].width  = 140.0
    dermis_layer_1.nodes["Switch.001"].height = 100.0

    dermis_layer_1.nodes["Math.004"].width  = 140.0
    dermis_layer_1.nodes["Math.004"].height = 100.0

    dermis_layer_1.nodes["Frame.002"].width  = 417.93548583984375
    dermis_layer_1.nodes["Frame.002"].height = 342.7742004394531

    dermis_layer_1.nodes["Reroute.009"].width  = 12.5
    dermis_layer_1.nodes["Reroute.009"].height = 100.0

    dermis_layer_1.nodes["Switch.002"].width  = 140.0
    dermis_layer_1.nodes["Switch.002"].height = 100.0


    # Initialize dermis_layer_1 links

    # merge_by_distance.Geometry -> group_output.Geometry
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Merge by Distance"].outputs[0],
        dermis_layer_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Geometry -> dermis_layer__generic_.Geometry
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[0]
    )
    # group_input.Geometry -> dermis_layer__generic__001.Geometry
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[0]
    )
    # reroute_003.Output -> dermis_layer__generic_.Paint Name
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.003"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[2]
    )
    # reroute_005.Output -> dermis_layer__generic_.Cutout Tolerance
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.005"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[3]
    )
    # reroute_006.Output -> dermis_layer__generic_.Smoothing
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.006"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[6]
    )
    # reroute_007.Output -> dermis_layer__generic_.Smooth Sampling
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.007"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[7]
    )
    # reroute_001.Output -> dermis_layer__generic_.Subtraction Cutout Tolerance
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.001"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[14]
    )
    # group_input.Subtraction Hole -> reroute.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[8],
        dermis_layer_1.nodes["Reroute"].inputs[0]
    )
    # group_input.Subtraction Cutout Tolerance -> reroute_001.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[10],
        dermis_layer_1.nodes["Reroute.001"].inputs[0]
    )
    # group_input.Plate Offset -> reroute_002.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[5],
        dermis_layer_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Paint Name -> reroute_003.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[2],
        dermis_layer_1.nodes["Reroute.003"].inputs[0]
    )
    # group_input.Subtraction Paint Name -> reroute_004.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[9],
        dermis_layer_1.nodes["Reroute.004"].inputs[0]
    )
    # group_input.Cutout Tolerance -> reroute_005.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[3],
        dermis_layer_1.nodes["Reroute.005"].inputs[0]
    )
    # group_input.Smoothing -> reroute_006.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[6],
        dermis_layer_1.nodes["Reroute.006"].inputs[0]
    )
    # group_input.Smooth Sampling -> reroute_007.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[7],
        dermis_layer_1.nodes["Reroute.007"].inputs[0]
    )
    # group_input.Thickness -> reroute_008.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[4],
        dermis_layer_1.nodes["Reroute.008"].inputs[0]
    )
    # reroute_003.Output -> dermis_layer__generic__001.Paint Name
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.003"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[2]
    )
    # reroute_005.Output -> dermis_layer__generic__001.Cutout Tolerance
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.005"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[3]
    )
    # reroute_006.Output -> dermis_layer__generic__001.Smoothing
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.006"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[6]
    )
    # reroute_007.Output -> dermis_layer__generic__001.Smooth Sampling
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.007"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[7]
    )
    # reroute_001.Output -> dermis_layer__generic__001.Subtraction Cutout Tolerance
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.001"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[14]
    )
    # reroute.Output -> dermis_layer__generic__001.Subtraction Paint
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[12]
    )
    # reroute_004.Output -> dermis_layer__generic__001.Subtraction Paint Name
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.004"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[13]
    )
    # join_geometry.Geometry -> merge_by_distance.Geometry
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Join Geometry"].outputs[0],
        dermis_layer_1.nodes["Merge by Distance"].inputs[0]
    )
    # group_input.Thickness -> math.Value
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[4],
        dermis_layer_1.nodes["Math"].inputs[0]
    )
    # math_001.Value -> math.Value
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Math.001"].outputs[0],
        dermis_layer_1.nodes["Math"].inputs[1]
    )
    # math.Value -> dermis_layer__generic__001.Thickness
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Math"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].inputs[4]
    )
    # group_input.Subtraction Thickness -> math_001.Value
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[11],
        dermis_layer_1.nodes["Math.001"].inputs[0]
    )
    # group_input.Thickness -> math_002.Value
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[4],
        dermis_layer_1.nodes["Math.002"].inputs[0]
    )
    # math.Value -> math_002.Value
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Math"].outputs[0],
        dermis_layer_1.nodes["Math.002"].inputs[1]
    )
    # math.Value -> dermis_layer__generic_.Plate Offset
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Math"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[5]
    )
    # math_002.Value -> dermis_layer__generic_.Thickness
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Math.002"].outputs[0],
        dermis_layer_1.nodes["Dermis Layer (Generic)"].inputs[4]
    )
    # reroute_009.Output -> math_003.Value
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.009"].outputs[0],
        dermis_layer_1.nodes["Math.003"].inputs[0]
    )
    # math_003.Value -> switch.Switch
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Math.003"].outputs[0],
        dermis_layer_1.nodes["Switch"].inputs[0]
    )
    # dermis_layer__generic_.Dermis -> switch.True
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Dermis Layer (Generic)"].outputs[1],
        dermis_layer_1.nodes["Switch"].inputs[2]
    )
    # math_004.Value -> switch_001.Switch
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Math.004"].outputs[0],
        dermis_layer_1.nodes["Switch.001"].inputs[0]
    )
    # dermis_layer__generic__001.Dermis -> switch_001.True
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Dermis Layer (Generic).001"].outputs[1],
        dermis_layer_1.nodes["Switch.001"].inputs[2]
    )
    # group_input.Subtraction Thickness -> reroute_009.Input
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[11],
        dermis_layer_1.nodes["Reroute.009"].inputs[0]
    )
    # reroute_009.Output -> math_004.Value
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Reroute.009"].outputs[0],
        dermis_layer_1.nodes["Math.004"].inputs[0]
    )
    # group_input.Vertex Merge Distance -> merge_by_distance.Distance
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[12],
        dermis_layer_1.nodes["Merge by Distance"].inputs[3]
    )
    # group_input.Include Original Geometry -> switch_002.Switch
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[1],
        dermis_layer_1.nodes["Switch.002"].inputs[0]
    )
    # group_input.Geometry -> switch_002.True
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Group Input"].outputs[0],
        dermis_layer_1.nodes["Switch.002"].inputs[2]
    )
    # switch_002.Output -> join_geometry.Geometry
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Switch.002"].outputs[0],
        dermis_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # switch_001.Output -> join_geometry.Geometry
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Switch.001"].outputs[0],
        dermis_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # switch.Output -> join_geometry.Geometry
    dermis_layer_1.links.new(
        dermis_layer_1.nodes["Switch"].outputs[0],
        dermis_layer_1.nodes["Join Geometry"].inputs[0]
    )

    return dermis_layer_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    smooth_mesh = smooth_mesh_1_node_group(node_tree_names)
    node_tree_names[smooth_mesh_1_node_group] = smooth_mesh.name

    skin_cutout_2 = skin_cutout_2_1_node_group(node_tree_names)
    node_tree_names[skin_cutout_2_1_node_group] = skin_cutout_2.name

    cutout_thickness_labeled = cutout_thickness_labeled_1_node_group(node_tree_names)
    node_tree_names[cutout_thickness_labeled_1_node_group] = cutout_thickness_labeled.name

    plate_volume_no_ref = plate_volume_no_ref_1_node_group(node_tree_names)
    node_tree_names[plate_volume_no_ref_1_node_group] = plate_volume_no_ref.name

    dermis_layer__generic_ = dermis_layer__generic__1_node_group(node_tree_names)
    node_tree_names[dermis_layer__generic__1_node_group] = dermis_layer__generic_.name

    dermis_layer = dermis_layer_1_node_group(node_tree_names)
    node_tree_names[dermis_layer_1_node_group] = dermis_layer.name

