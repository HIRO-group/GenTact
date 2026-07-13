import bpy
import mathutils
import os
import typing


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


def sensor_instantiation_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Sensor Instantiation node group"""
    sensor_instantiation_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sensor Instantiation")

    sensor_instantiation_1.color_tag = 'NONE'
    sensor_instantiation_1.description = ""
    sensor_instantiation_1.default_group_node_width = 140
    sensor_instantiation_1.show_modifier_manage_panel = True

    # sensor_instantiation_1 interface

    # Socket Geometry
    geometry_socket = sensor_instantiation_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Instances
    instances_socket = sensor_instantiation_1.interface.new_socket(name="Instances", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    instances_socket.attribute_domain = 'POINT'
    instances_socket.default_input = 'VALUE'
    instances_socket.structure_type = 'AUTO'

    # Socket Shape
    shape_socket = sensor_instantiation_1.interface.new_socket(name="Shape", in_out='INPUT', socket_type='NodeSocketGeometry')
    shape_socket.attribute_domain = 'POINT'
    shape_socket.default_input = 'VALUE'
    shape_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket = sensor_instantiation_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Sensor Material
    sensor_material_socket = sensor_instantiation_1.interface.new_socket(name="Sensor Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    sensor_material_socket.attribute_domain = 'POINT'
    sensor_material_socket.default_input = 'VALUE'
    sensor_material_socket.structure_type = 'AUTO'

    # Socket Node Offset
    node_offset_socket = sensor_instantiation_1.interface.new_socket(name="Node Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    node_offset_socket.default_value = 0.0
    node_offset_socket.min_value = -3.4028234663852886e+38
    node_offset_socket.max_value = 3.4028234663852886e+38
    node_offset_socket.subtype = 'NONE'
    node_offset_socket.attribute_domain = 'POINT'
    node_offset_socket.default_input = 'VALUE'
    node_offset_socket.structure_type = 'AUTO'

    # Socket Scale
    scale_socket = sensor_instantiation_1.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    scale_socket.default_value = 0.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    # Socket Euler Rotation
    euler_rotation_socket = sensor_instantiation_1.interface.new_socket(name="Euler Rotation", in_out='INPUT', socket_type='NodeSocketVector')
    euler_rotation_socket.default_value = (0.0, 0.0, 0.0)
    euler_rotation_socket.min_value = -3.4028234663852886e+38
    euler_rotation_socket.max_value = 3.4028234663852886e+38
    euler_rotation_socket.subtype = 'NONE'
    euler_rotation_socket.attribute_domain = 'POINT'
    euler_rotation_socket.default_input = 'VALUE'
    euler_rotation_socket.structure_type = 'AUTO'

    # Initialize sensor_instantiation_1 nodes

    # Node Group Output
    group_output = sensor_instantiation_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = sensor_instantiation_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Frame.005
    frame_005 = sensor_instantiation_1.nodes.new("NodeFrame")
    frame_005.label = "Cylander Mesh"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.4044908285140991, 0.14717276394367218, 0.17180749773979187)
    frame_005.hide = True
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Instance on Points.001
    instance_on_points_001 = sensor_instantiation_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.show_options = True
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0

    # Node Set Material
    set_material = sensor_instantiation_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Translate Instances
    translate_instances = sensor_instantiation_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances.name = "Translate Instances"
    translate_instances.show_options = True
    # Selection
    translate_instances.inputs[1].default_value = True
    # Local Space
    translate_instances.inputs[3].default_value = True

    # Node Reroute.015
    reroute_015 = sensor_instantiation_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketVector"
    # Node Combine XYZ.001
    combine_xyz_001 = sensor_instantiation_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.show_options = True
    # X
    combine_xyz_001.inputs[0].default_value = 0.0
    # Y
    combine_xyz_001.inputs[1].default_value = 0.0

    # Node Euler to Rotation
    euler_to_rotation = sensor_instantiation_1.nodes.new("FunctionNodeEulerToRotation")
    euler_to_rotation.name = "Euler to Rotation"
    euler_to_rotation.show_options = True

    # Node Reroute.043
    reroute_043 = sensor_instantiation_1.nodes.new("NodeReroute")
    reroute_043.name = "Reroute.043"
    reroute_043.show_options = True
    reroute_043.socket_idname = "NodeSocketFloat"
    # Node Reroute.044
    reroute_044 = sensor_instantiation_1.nodes.new("NodeReroute")
    reroute_044.name = "Reroute.044"
    reroute_044.show_options = True
    reroute_044.socket_idname = "NodeSocketGeometry"
    # Node Realize Instances
    realize_instances = sensor_instantiation_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    realize_instances.realize_to_point_domain = True
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Set parents
    sensor_instantiation_1.nodes["Instance on Points.001"].parent = sensor_instantiation_1.nodes["Frame.005"]
    sensor_instantiation_1.nodes["Set Material"].parent = sensor_instantiation_1.nodes["Frame.005"]
    sensor_instantiation_1.nodes["Translate Instances"].parent = sensor_instantiation_1.nodes["Frame.005"]
    sensor_instantiation_1.nodes["Reroute.015"].parent = sensor_instantiation_1.nodes["Frame.005"]
    sensor_instantiation_1.nodes["Combine XYZ.001"].parent = sensor_instantiation_1.nodes["Frame.005"]
    sensor_instantiation_1.nodes["Euler to Rotation"].parent = sensor_instantiation_1.nodes["Frame.005"]
    sensor_instantiation_1.nodes["Reroute.043"].parent = sensor_instantiation_1.nodes["Frame.005"]
    sensor_instantiation_1.nodes["Reroute.044"].parent = sensor_instantiation_1.nodes["Frame.005"]

    # Set locations
    sensor_instantiation_1.nodes["Group Output"].location = (1200.0, 0.0)
    sensor_instantiation_1.nodes["Group Input"].location = (-880.0, -40.0)
    sensor_instantiation_1.nodes["Frame.005"].location = (-564.3333129882812, 307.8000183105469)
    sensor_instantiation_1.nodes["Instance on Points.001"].location = (869.3333129882812, -35.800018310546875)
    sensor_instantiation_1.nodes["Set Material"].location = (489.33331298828125, -95.80001831054688)
    sensor_instantiation_1.nodes["Translate Instances"].location = (1129.333251953125, -35.800018310546875)
    sensor_instantiation_1.nodes["Reroute.015"].location = (789.3333129882812, -515.800048828125)
    sensor_instantiation_1.nodes["Combine XYZ.001"].location = (29.33331298828125, -495.8000183105469)
    sensor_instantiation_1.nodes["Euler to Rotation"].location = (484.33331298828125, -247.80001831054688)
    sensor_instantiation_1.nodes["Reroute.043"].location = (564.3333129882812, -407.8000183105469)
    sensor_instantiation_1.nodes["Reroute.044"].location = (624.3333129882812, -207.80001831054688)
    sensor_instantiation_1.nodes["Realize Instances"].location = (960.0, 280.0)

    # Set dimensions
    sensor_instantiation_1.nodes["Group Output"].width  = 140.0
    sensor_instantiation_1.nodes["Group Output"].height = 100.0

    sensor_instantiation_1.nodes["Group Input"].width  = 140.0
    sensor_instantiation_1.nodes["Group Input"].height = 100.0

    sensor_instantiation_1.nodes["Frame.005"].width  = 1298.6666259765625
    sensor_instantiation_1.nodes["Frame.005"].height = 638.1333618164062

    sensor_instantiation_1.nodes["Instance on Points.001"].width  = 140.0
    sensor_instantiation_1.nodes["Instance on Points.001"].height = 100.0

    sensor_instantiation_1.nodes["Set Material"].width  = 140.0
    sensor_instantiation_1.nodes["Set Material"].height = 100.0

    sensor_instantiation_1.nodes["Translate Instances"].width  = 140.0
    sensor_instantiation_1.nodes["Translate Instances"].height = 100.0

    sensor_instantiation_1.nodes["Reroute.015"].width  = 14.5
    sensor_instantiation_1.nodes["Reroute.015"].height = 100.0

    sensor_instantiation_1.nodes["Combine XYZ.001"].width  = 140.0
    sensor_instantiation_1.nodes["Combine XYZ.001"].height = 100.0

    sensor_instantiation_1.nodes["Euler to Rotation"].width  = 140.0
    sensor_instantiation_1.nodes["Euler to Rotation"].height = 100.0

    sensor_instantiation_1.nodes["Reroute.043"].width  = 14.5
    sensor_instantiation_1.nodes["Reroute.043"].height = 100.0

    sensor_instantiation_1.nodes["Reroute.044"].width  = 14.5
    sensor_instantiation_1.nodes["Reroute.044"].height = 100.0

    sensor_instantiation_1.nodes["Realize Instances"].width  = 140.0
    sensor_instantiation_1.nodes["Realize Instances"].height = 100.0


    # Initialize sensor_instantiation_1 links

    # reroute_044.Output -> instance_on_points_001.Points
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Reroute.044"].outputs[0],
        sensor_instantiation_1.nodes["Instance on Points.001"].inputs[0]
    )
    # combine_xyz_001.Vector -> reroute_015.Input
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Combine XYZ.001"].outputs[0],
        sensor_instantiation_1.nodes["Reroute.015"].inputs[0]
    )
    # set_material.Geometry -> instance_on_points_001.Instance
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Set Material"].outputs[0],
        sensor_instantiation_1.nodes["Instance on Points.001"].inputs[2]
    )
    # instance_on_points_001.Instances -> translate_instances.Instances
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Instance on Points.001"].outputs[0],
        sensor_instantiation_1.nodes["Translate Instances"].inputs[0]
    )
    # reroute_015.Output -> translate_instances.Translation
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Reroute.015"].outputs[0],
        sensor_instantiation_1.nodes["Translate Instances"].inputs[2]
    )
    # euler_to_rotation.Rotation -> instance_on_points_001.Rotation
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Euler to Rotation"].outputs[0],
        sensor_instantiation_1.nodes["Instance on Points.001"].inputs[5]
    )
    # reroute_043.Output -> instance_on_points_001.Scale
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Reroute.043"].outputs[0],
        sensor_instantiation_1.nodes["Instance on Points.001"].inputs[6]
    )
    # group_input.Sensor Material -> set_material.Material
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Group Input"].outputs[2],
        sensor_instantiation_1.nodes["Set Material"].inputs[2]
    )
    # group_input.Node Offset -> combine_xyz_001.Z
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Group Input"].outputs[3],
        sensor_instantiation_1.nodes["Combine XYZ.001"].inputs[2]
    )
    # group_input.Euler Rotation -> euler_to_rotation.Euler
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Group Input"].outputs[5],
        sensor_instantiation_1.nodes["Euler to Rotation"].inputs[0]
    )
    # group_input.Scale -> reroute_043.Input
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Group Input"].outputs[4],
        sensor_instantiation_1.nodes["Reroute.043"].inputs[0]
    )
    # group_input.Shape -> set_material.Geometry
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Group Input"].outputs[0],
        sensor_instantiation_1.nodes["Set Material"].inputs[0]
    )
    # group_input.Points -> reroute_044.Input
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Group Input"].outputs[1],
        sensor_instantiation_1.nodes["Reroute.044"].inputs[0]
    )
    # translate_instances.Instances -> realize_instances.Geometry
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Translate Instances"].outputs[0],
        sensor_instantiation_1.nodes["Realize Instances"].inputs[0]
    )
    # realize_instances.Geometry -> group_output.Geometry
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Realize Instances"].outputs[0],
        sensor_instantiation_1.nodes["Group Output"].inputs[0]
    )
    # translate_instances.Instances -> group_output.Instances
    sensor_instantiation_1.links.new(
        sensor_instantiation_1.nodes["Translate Instances"].outputs[0],
        sensor_instantiation_1.nodes["Group Output"].inputs[1]
    )

    return sensor_instantiation_1


def cylinder_sensor_distribution_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Cylinder Sensor Distribution node group"""
    cylinder_sensor_distribution_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Cylinder Sensor Distribution")

    cylinder_sensor_distribution_1.color_tag = 'GEOMETRY'
    cylinder_sensor_distribution_1.description = ""
    cylinder_sensor_distribution_1.default_group_node_width = 140
    cylinder_sensor_distribution_1.show_modifier_manage_panel = True

    # cylinder_sensor_distribution_1 interface

    # Socket Sensor Shapes
    sensor_shapes_socket = cylinder_sensor_distribution_1.interface.new_socket(name="Sensor Shapes", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_shapes_socket.attribute_domain = 'POINT'
    sensor_shapes_socket.default_input = 'VALUE'
    sensor_shapes_socket.structure_type = 'AUTO'

    # Socket Nodule Parameters
    nodule_parameters_socket = cylinder_sensor_distribution_1.interface.new_socket(name="Nodule Parameters", in_out='INPUT', socket_type='NodeSocketBundle')
    nodule_parameters_socket.attribute_domain = 'POINT'
    nodule_parameters_socket.default_input = 'VALUE'
    nodule_parameters_socket.structure_type = 'AUTO'

    # Initialize cylinder_sensor_distribution_1 nodes

    # Node Group Input
    group_input = cylinder_sensor_distribution_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = cylinder_sensor_distribution_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Cylinder
    cylinder = cylinder_sensor_distribution_1.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.show_options = True
    cylinder.fill_type = 'NGON'
    # Vertices
    cylinder.inputs[0].default_value = 32
    # Side Segments
    cylinder.inputs[1].default_value = 1
    # Fill Segments
    cylinder.inputs[2].default_value = 1
    # Radius
    cylinder.inputs[3].default_value = 1.0

    # Node Group
    group = cylinder_sensor_distribution_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[sensor_instantiation_1_node_group]]

    # Node Separate Bundle
    separate_bundle = cylinder_sensor_distribution_1.nodes.new("NodeSeparateBundle")
    separate_bundle.name = "Separate Bundle"
    separate_bundle.show_options = True
    separate_bundle.active_index = 5
    separate_bundle.bundle_items.clear()
    separate_bundle.bundle_items.new('GEOMETRY', "Points")
    separate_bundle.bundle_items[0].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('VECTOR', "Euler")
    separate_bundle.bundle_items[1].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('MATERIAL', "Material")
    separate_bundle.bundle_items[2].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Depth")
    separate_bundle.bundle_items[3].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Offset")
    separate_bundle.bundle_items[4].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Base Radii")
    separate_bundle.bundle_items[5].structure_type = 'AUTO'
    separate_bundle.define_signature = False

    # Set locations
    cylinder_sensor_distribution_1.nodes["Group Input"].location = (-520.0, -160.0)
    cylinder_sensor_distribution_1.nodes["Group Output"].location = (760.0, 0.0)
    cylinder_sensor_distribution_1.nodes["Cylinder"].location = (100.0, 380.0)
    cylinder_sensor_distribution_1.nodes["Group"].location = (515.0, 28.0)
    cylinder_sensor_distribution_1.nodes["Separate Bundle"].location = (-280.0, 40.0)

    # Set dimensions
    cylinder_sensor_distribution_1.nodes["Group Input"].width  = 140.0
    cylinder_sensor_distribution_1.nodes["Group Input"].height = 100.0

    cylinder_sensor_distribution_1.nodes["Group Output"].width  = 140.0
    cylinder_sensor_distribution_1.nodes["Group Output"].height = 100.0

    cylinder_sensor_distribution_1.nodes["Cylinder"].width  = 140.0
    cylinder_sensor_distribution_1.nodes["Cylinder"].height = 100.0

    cylinder_sensor_distribution_1.nodes["Group"].width  = 140.0
    cylinder_sensor_distribution_1.nodes["Group"].height = 100.0

    cylinder_sensor_distribution_1.nodes["Separate Bundle"].width  = 140.0
    cylinder_sensor_distribution_1.nodes["Separate Bundle"].height = 100.0


    # Initialize cylinder_sensor_distribution_1 links

    # group_input.Nodule Parameters -> separate_bundle.Bundle
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Group Input"].outputs[0],
        cylinder_sensor_distribution_1.nodes["Separate Bundle"].inputs[0]
    )
    # cylinder.Mesh -> group.Shape
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Cylinder"].outputs[0],
        cylinder_sensor_distribution_1.nodes["Group"].inputs[0]
    )
    # group.Geometry -> group_output.Sensor Shapes
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Group"].outputs[0],
        cylinder_sensor_distribution_1.nodes["Group Output"].inputs[0]
    )
    # separate_bundle.Points -> group.Points
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Separate Bundle"].outputs[0],
        cylinder_sensor_distribution_1.nodes["Group"].inputs[1]
    )
    # separate_bundle.Node Depth -> cylinder.Depth
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Separate Bundle"].outputs[3],
        cylinder_sensor_distribution_1.nodes["Cylinder"].inputs[4]
    )
    # separate_bundle.Base Radii -> group.Scale
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Separate Bundle"].outputs[5],
        cylinder_sensor_distribution_1.nodes["Group"].inputs[4]
    )
    # separate_bundle.Node Offset -> group.Node Offset
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Separate Bundle"].outputs[4],
        cylinder_sensor_distribution_1.nodes["Group"].inputs[3]
    )
    # separate_bundle.Material -> group.Sensor Material
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Separate Bundle"].outputs[2],
        cylinder_sensor_distribution_1.nodes["Group"].inputs[2]
    )
    # separate_bundle.Euler -> group.Euler Rotation
    cylinder_sensor_distribution_1.links.new(
        cylinder_sensor_distribution_1.nodes["Separate Bundle"].outputs[1],
        cylinder_sensor_distribution_1.nodes["Group"].inputs[5]
    )

    return cylinder_sensor_distribution_1


def sphere_sensor_distribution_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Sphere Sensor Distribution node group"""
    sphere_sensor_distribution_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sphere Sensor Distribution")

    sphere_sensor_distribution_1.color_tag = 'GEOMETRY'
    sphere_sensor_distribution_1.description = ""
    sphere_sensor_distribution_1.default_group_node_width = 140
    sphere_sensor_distribution_1.show_modifier_manage_panel = True

    # sphere_sensor_distribution_1 interface

    # Socket Sensor Shapes
    sensor_shapes_socket = sphere_sensor_distribution_1.interface.new_socket(name="Sensor Shapes", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_shapes_socket.attribute_domain = 'POINT'
    sensor_shapes_socket.default_input = 'VALUE'
    sensor_shapes_socket.structure_type = 'AUTO'

    # Socket Nodule Parameters
    nodule_parameters_socket = sphere_sensor_distribution_1.interface.new_socket(name="Nodule Parameters", in_out='INPUT', socket_type='NodeSocketBundle')
    nodule_parameters_socket.attribute_domain = 'POINT'
    nodule_parameters_socket.default_input = 'VALUE'
    nodule_parameters_socket.structure_type = 'AUTO'

    # Initialize sphere_sensor_distribution_1 nodes

    # Node Group Input
    group_input = sphere_sensor_distribution_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = sphere_sensor_distribution_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group
    group = sphere_sensor_distribution_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[sensor_instantiation_1_node_group]]

    # Node Separate Bundle
    separate_bundle = sphere_sensor_distribution_1.nodes.new("NodeSeparateBundle")
    separate_bundle.name = "Separate Bundle"
    separate_bundle.show_options = True
    separate_bundle.active_index = 5
    separate_bundle.bundle_items.clear()
    separate_bundle.bundle_items.new('GEOMETRY', "Points")
    separate_bundle.bundle_items[0].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('VECTOR', "Euler")
    separate_bundle.bundle_items[1].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('MATERIAL', "Material")
    separate_bundle.bundle_items[2].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Depth")
    separate_bundle.bundle_items[3].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Offset")
    separate_bundle.bundle_items[4].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Base Radii")
    separate_bundle.bundle_items[5].structure_type = 'AUTO'
    separate_bundle.define_signature = False

    # Node UV Sphere
    uv_sphere = sphere_sensor_distribution_1.nodes.new("GeometryNodeMeshUVSphere")
    uv_sphere.name = "UV Sphere"
    uv_sphere.show_options = True
    # Segments
    uv_sphere.inputs[0].default_value = 32
    # Rings
    uv_sphere.inputs[1].default_value = 16
    # Radius
    uv_sphere.inputs[2].default_value = 1.0

    # Set locations
    sphere_sensor_distribution_1.nodes["Group Input"].location = (-520.0, -160.0)
    sphere_sensor_distribution_1.nodes["Group Output"].location = (760.0, 0.0)
    sphere_sensor_distribution_1.nodes["Group"].location = (515.0, 28.0)
    sphere_sensor_distribution_1.nodes["Separate Bundle"].location = (-280.0, 40.0)
    sphere_sensor_distribution_1.nodes["UV Sphere"].location = (100.0, 180.0)

    # Set dimensions
    sphere_sensor_distribution_1.nodes["Group Input"].width  = 140.0
    sphere_sensor_distribution_1.nodes["Group Input"].height = 100.0

    sphere_sensor_distribution_1.nodes["Group Output"].width  = 140.0
    sphere_sensor_distribution_1.nodes["Group Output"].height = 100.0

    sphere_sensor_distribution_1.nodes["Group"].width  = 140.0
    sphere_sensor_distribution_1.nodes["Group"].height = 100.0

    sphere_sensor_distribution_1.nodes["Separate Bundle"].width  = 140.0
    sphere_sensor_distribution_1.nodes["Separate Bundle"].height = 100.0

    sphere_sensor_distribution_1.nodes["UV Sphere"].width  = 140.0
    sphere_sensor_distribution_1.nodes["UV Sphere"].height = 100.0


    # Initialize sphere_sensor_distribution_1 links

    # group_input.Nodule Parameters -> separate_bundle.Bundle
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["Group Input"].outputs[0],
        sphere_sensor_distribution_1.nodes["Separate Bundle"].inputs[0]
    )
    # group.Geometry -> group_output.Sensor Shapes
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["Group"].outputs[0],
        sphere_sensor_distribution_1.nodes["Group Output"].inputs[0]
    )
    # separate_bundle.Points -> group.Points
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["Separate Bundle"].outputs[0],
        sphere_sensor_distribution_1.nodes["Group"].inputs[1]
    )
    # separate_bundle.Base Radii -> group.Scale
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["Separate Bundle"].outputs[5],
        sphere_sensor_distribution_1.nodes["Group"].inputs[4]
    )
    # separate_bundle.Node Offset -> group.Node Offset
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["Separate Bundle"].outputs[4],
        sphere_sensor_distribution_1.nodes["Group"].inputs[3]
    )
    # separate_bundle.Material -> group.Sensor Material
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["Separate Bundle"].outputs[2],
        sphere_sensor_distribution_1.nodes["Group"].inputs[2]
    )
    # separate_bundle.Euler -> group.Euler Rotation
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["Separate Bundle"].outputs[1],
        sphere_sensor_distribution_1.nodes["Group"].inputs[5]
    )
    # uv_sphere.Mesh -> group.Shape
    sphere_sensor_distribution_1.links.new(
        sphere_sensor_distribution_1.nodes["UV Sphere"].outputs[0],
        sphere_sensor_distribution_1.nodes["Group"].inputs[0]
    )

    return sphere_sensor_distribution_1


def voronoi_sensor_distribution_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Voronoi Sensor Distribution node group"""
    voronoi_sensor_distribution_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Voronoi Sensor Distribution")

    voronoi_sensor_distribution_1.color_tag = 'GEOMETRY'
    voronoi_sensor_distribution_1.description = ""
    voronoi_sensor_distribution_1.default_group_node_width = 140
    voronoi_sensor_distribution_1.show_modifier_manage_panel = True

    # voronoi_sensor_distribution_1 interface

    # Socket Sensor Shapes
    sensor_shapes_socket = voronoi_sensor_distribution_1.interface.new_socket(name="Sensor Shapes", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_shapes_socket.attribute_domain = 'POINT'
    sensor_shapes_socket.default_input = 'VALUE'
    sensor_shapes_socket.structure_type = 'AUTO'

    # Socket Nodule Parameters
    nodule_parameters_socket = voronoi_sensor_distribution_1.interface.new_socket(name="Nodule Parameters", in_out='INPUT', socket_type='NodeSocketBundle')
    nodule_parameters_socket.attribute_domain = 'POINT'
    nodule_parameters_socket.default_input = 'VALUE'
    nodule_parameters_socket.structure_type = 'AUTO'

    # Socket Bottom Plate
    bottom_plate_socket = voronoi_sensor_distribution_1.interface.new_socket(name="Bottom Plate", in_out='INPUT', socket_type='NodeSocketGeometry')
    bottom_plate_socket.attribute_domain = 'POINT'
    bottom_plate_socket.description = "Geometry to find the closest point on"
    bottom_plate_socket.default_input = 'VALUE'
    bottom_plate_socket.structure_type = 'AUTO'

    # Initialize voronoi_sensor_distribution_1 nodes

    # Node Group Input
    group_input = voronoi_sensor_distribution_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = voronoi_sensor_distribution_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group
    group = voronoi_sensor_distribution_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[sensor_instantiation_1_node_group]]

    # Node Separate Bundle
    separate_bundle = voronoi_sensor_distribution_1.nodes.new("NodeSeparateBundle")
    separate_bundle.name = "Separate Bundle"
    separate_bundle.show_options = True
    separate_bundle.active_index = 5
    separate_bundle.bundle_items.clear()
    separate_bundle.bundle_items.new('GEOMETRY', "Points")
    separate_bundle.bundle_items[0].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('VECTOR', "Euler")
    separate_bundle.bundle_items[1].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('MATERIAL', "Material")
    separate_bundle.bundle_items[2].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Depth")
    separate_bundle.bundle_items[3].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Offset")
    separate_bundle.bundle_items[4].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Base Radii")
    separate_bundle.bundle_items[5].structure_type = 'AUTO'
    separate_bundle.define_signature = False

    # Node Geometry Proximity
    geometry_proximity = voronoi_sensor_distribution_1.nodes.new("GeometryNodeProximity")
    geometry_proximity.name = "Geometry Proximity"
    geometry_proximity.show_options = True
    geometry_proximity.target_element = 'POINTS'
    # Group ID
    geometry_proximity.inputs[1].default_value = 0
    # Sample Group ID
    geometry_proximity.inputs[3].default_value = 0

    # Node Sample Index
    sample_index = voronoi_sensor_distribution_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Index
    index = voronoi_sensor_distribution_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Position
    position = voronoi_sensor_distribution_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Field Min & Max
    field_min___max = voronoi_sensor_distribution_1.nodes.new("GeometryNodeFieldMinAndMax")
    field_min___max.name = "Field Min & Max"
    field_min___max.show_options = True
    field_min___max.data_type = 'FLOAT'
    field_min___max.domain = 'POINT'
    # Group Index
    field_min___max.inputs[1].default_value = 0

    # Node Map Range
    map_range = voronoi_sensor_distribution_1.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.show_options = True
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    # To Min
    map_range.inputs[3].default_value = 0.0
    # To Max
    map_range.inputs[4].default_value = 1.0

    # Node Sample Nearest
    sample_nearest = voronoi_sensor_distribution_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Viewer
    viewer = voronoi_sensor_distribution_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 1
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Points")
    viewer.viewer_items.new('FLOAT', "Distance")

    # Set locations
    voronoi_sensor_distribution_1.nodes["Group Input"].location = (-2320.0, -260.0)
    voronoi_sensor_distribution_1.nodes["Group Output"].location = (760.0, 0.0)
    voronoi_sensor_distribution_1.nodes["Group"].location = (-200.0, 20.0)
    voronoi_sensor_distribution_1.nodes["Separate Bundle"].location = (-2100.0, -40.0)
    voronoi_sensor_distribution_1.nodes["Geometry Proximity"].location = (-1560.0, -440.0)
    voronoi_sensor_distribution_1.nodes["Sample Index"].location = (-1820.0, -560.0)
    voronoi_sensor_distribution_1.nodes["Index"].location = (-2080.0, -700.0)
    voronoi_sensor_distribution_1.nodes["Position"].location = (-2080.0, -640.0)
    voronoi_sensor_distribution_1.nodes["Field Min & Max"].location = (-1340.0, -540.0)
    voronoi_sensor_distribution_1.nodes["Map Range"].location = (-1020.0, -480.0)
    voronoi_sensor_distribution_1.nodes["Sample Nearest"].location = (-1020.0, -320.0)
    voronoi_sensor_distribution_1.nodes["Viewer"].location = (-280.0, -280.0)

    # Set dimensions
    voronoi_sensor_distribution_1.nodes["Group Input"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Group Input"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Group Output"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Group Output"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Group"].width  = 260.0
    voronoi_sensor_distribution_1.nodes["Group"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Separate Bundle"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Separate Bundle"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Geometry Proximity"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Geometry Proximity"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Sample Index"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Sample Index"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Index"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Index"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Position"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Position"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Field Min & Max"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Field Min & Max"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Map Range"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Map Range"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Sample Nearest"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Sample Nearest"].height = 100.0

    voronoi_sensor_distribution_1.nodes["Viewer"].width  = 140.0
    voronoi_sensor_distribution_1.nodes["Viewer"].height = 100.0


    # Initialize voronoi_sensor_distribution_1 links

    # group_input.Nodule Parameters -> separate_bundle.Bundle
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Group Input"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].inputs[0]
    )
    # separate_bundle.Points -> group.Points
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Group"].inputs[1]
    )
    # separate_bundle.Base Radii -> group.Scale
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].outputs[5],
        voronoi_sensor_distribution_1.nodes["Group"].inputs[4]
    )
    # separate_bundle.Node Offset -> group.Node Offset
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].outputs[4],
        voronoi_sensor_distribution_1.nodes["Group"].inputs[3]
    )
    # separate_bundle.Material -> group.Sensor Material
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].outputs[2],
        voronoi_sensor_distribution_1.nodes["Group"].inputs[2]
    )
    # separate_bundle.Euler -> group.Euler Rotation
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].outputs[1],
        voronoi_sensor_distribution_1.nodes["Group"].inputs[5]
    )
    # index.Index -> sample_index.Index
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Index"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Sample Index"].inputs[2]
    )
    # position.Position -> sample_index.Value
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Position"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Sample Index"].inputs[1]
    )
    # sample_index.Value -> geometry_proximity.Sample Position
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Sample Index"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Geometry Proximity"].inputs[2]
    )
    # geometry_proximity.Distance -> field_min___max.Value
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Geometry Proximity"].outputs[1],
        voronoi_sensor_distribution_1.nodes["Field Min & Max"].inputs[0]
    )
    # field_min___max.Min -> map_range.From Min
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Field Min & Max"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Map Range"].inputs[1]
    )
    # field_min___max.Max -> map_range.From Max
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Field Min & Max"].outputs[1],
        voronoi_sensor_distribution_1.nodes["Map Range"].inputs[2]
    )
    # geometry_proximity.Distance -> map_range.Value
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Geometry Proximity"].outputs[1],
        voronoi_sensor_distribution_1.nodes["Map Range"].inputs[0]
    )
    # group_input.Bottom Plate -> sample_index.Geometry
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Group Input"].outputs[1],
        voronoi_sensor_distribution_1.nodes["Sample Index"].inputs[0]
    )
    # separate_bundle.Points -> geometry_proximity.Geometry
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Geometry Proximity"].inputs[0]
    )
    # separate_bundle.Points -> sample_nearest.Geometry
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Separate Bundle"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Sample Nearest"].inputs[0]
    )
    # geometry_proximity.Position -> sample_nearest.Sample Position
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Geometry Proximity"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Sample Nearest"].inputs[1]
    )
    # group_input.Bottom Plate -> viewer.Points
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Group Input"].outputs[1],
        voronoi_sensor_distribution_1.nodes["Viewer"].inputs[0]
    )
    # map_range.Result -> viewer.Distance
    voronoi_sensor_distribution_1.links.new(
        voronoi_sensor_distribution_1.nodes["Map Range"].outputs[0],
        voronoi_sensor_distribution_1.nodes["Viewer"].inputs[1]
    )
    viewer.viewer_items[0].auto_remove = True
    viewer.viewer_items[1].auto_remove = True

    return voronoi_sensor_distribution_1


def ring_sensor_distribution_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Ring Sensor Distribution node group"""
    ring_sensor_distribution_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Ring Sensor Distribution")

    ring_sensor_distribution_1.color_tag = 'GEOMETRY'
    ring_sensor_distribution_1.description = ""
    ring_sensor_distribution_1.default_group_node_width = 140
    ring_sensor_distribution_1.show_modifier_manage_panel = True

    # ring_sensor_distribution_1 interface

    # Socket Sensor Shapes
    sensor_shapes_socket = ring_sensor_distribution_1.interface.new_socket(name="Sensor Shapes", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_shapes_socket.attribute_domain = 'POINT'
    sensor_shapes_socket.default_input = 'VALUE'
    sensor_shapes_socket.structure_type = 'AUTO'

    # Socket Nodule Parameters
    nodule_parameters_socket = ring_sensor_distribution_1.interface.new_socket(name="Nodule Parameters", in_out='INPUT', socket_type='NodeSocketBundle')
    nodule_parameters_socket.attribute_domain = 'POINT'
    nodule_parameters_socket.default_input = 'VALUE'
    nodule_parameters_socket.structure_type = 'AUTO'

    # Socket Center Cut
    center_cut_socket = ring_sensor_distribution_1.interface.new_socket(name="Center Cut", in_out='INPUT', socket_type='NodeSocketFloat')
    center_cut_socket.default_value = 50.0
    center_cut_socket.min_value = 0.0
    center_cut_socket.max_value = 99.5
    center_cut_socket.subtype = 'PERCENTAGE'
    center_cut_socket.attribute_domain = 'POINT'
    center_cut_socket.description = "The percentage of the center radius removed"
    center_cut_socket.default_input = 'VALUE'
    center_cut_socket.structure_type = 'AUTO'

    # Initialize ring_sensor_distribution_1 nodes

    # Node Group Input
    group_input = ring_sensor_distribution_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = ring_sensor_distribution_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Cylinder
    cylinder = ring_sensor_distribution_1.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.show_options = True
    cylinder.fill_type = 'NGON'
    # Vertices
    cylinder.inputs[0].default_value = 32
    # Side Segments
    cylinder.inputs[1].default_value = 1
    # Fill Segments
    cylinder.inputs[2].default_value = 1
    # Radius
    cylinder.inputs[3].default_value = 1.0

    # Node Group
    group = ring_sensor_distribution_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[sensor_instantiation_1_node_group]]

    # Node Separate Bundle
    separate_bundle = ring_sensor_distribution_1.nodes.new("NodeSeparateBundle")
    separate_bundle.name = "Separate Bundle"
    separate_bundle.show_options = True
    separate_bundle.active_index = 5
    separate_bundle.bundle_items.clear()
    separate_bundle.bundle_items.new('GEOMETRY', "Points")
    separate_bundle.bundle_items[0].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('VECTOR', "Euler")
    separate_bundle.bundle_items[1].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('MATERIAL', "Material")
    separate_bundle.bundle_items[2].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Depth")
    separate_bundle.bundle_items[3].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Node Offset")
    separate_bundle.bundle_items[4].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Base Radii")
    separate_bundle.bundle_items[5].structure_type = 'AUTO'
    separate_bundle.define_signature = False

    # Node Cylinder.001
    cylinder_001 = ring_sensor_distribution_1.nodes.new("GeometryNodeMeshCylinder")
    cylinder_001.name = "Cylinder.001"
    cylinder_001.show_options = True
    cylinder_001.fill_type = 'NGON'
    # Vertices
    cylinder_001.inputs[0].default_value = 32
    # Side Segments
    cylinder_001.inputs[1].default_value = 1
    # Fill Segments
    cylinder_001.inputs[2].default_value = 1

    # Node Math
    math = ring_sensor_distribution_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'DIVIDE'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 100.0

    # Node Reroute
    reroute = ring_sensor_distribution_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Math.001
    math_001 = ring_sensor_distribution_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 1.100000023841858

    # Node Mesh Boolean
    mesh_boolean = ring_sensor_distribution_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.show_options = True
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'FLOAT'

    # Node Viewer
    viewer = ring_sensor_distribution_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Mesh")

    # Set locations
    ring_sensor_distribution_1.nodes["Group Input"].location = (-1008.70458984375, -140.00006103515625)
    ring_sensor_distribution_1.nodes["Group Output"].location = (1140.0, -20.0)
    ring_sensor_distribution_1.nodes["Cylinder"].location = (100.0, 380.0)
    ring_sensor_distribution_1.nodes["Group"].location = (900.0, 0.0)
    ring_sensor_distribution_1.nodes["Separate Bundle"].location = (-416.1617431640625, 40.0)
    ring_sensor_distribution_1.nodes["Cylinder.001"].location = (100.0, 660.0)
    ring_sensor_distribution_1.nodes["Math"].location = (-620.0, 460.0)
    ring_sensor_distribution_1.nodes["Reroute"].location = (-124.83334350585938, 74.97879028320312)
    ring_sensor_distribution_1.nodes["Math.001"].location = (-80.00000762939453, 300.0)
    ring_sensor_distribution_1.nodes["Mesh Boolean"].location = (480.0, 460.0)
    ring_sensor_distribution_1.nodes["Viewer"].location = (646.6666870117188, 540.6666870117188)

    # Set dimensions
    ring_sensor_distribution_1.nodes["Group Input"].width  = 140.0
    ring_sensor_distribution_1.nodes["Group Input"].height = 100.0

    ring_sensor_distribution_1.nodes["Group Output"].width  = 140.0
    ring_sensor_distribution_1.nodes["Group Output"].height = 100.0

    ring_sensor_distribution_1.nodes["Cylinder"].width  = 140.0
    ring_sensor_distribution_1.nodes["Cylinder"].height = 100.0

    ring_sensor_distribution_1.nodes["Group"].width  = 140.0
    ring_sensor_distribution_1.nodes["Group"].height = 100.0

    ring_sensor_distribution_1.nodes["Separate Bundle"].width  = 140.0
    ring_sensor_distribution_1.nodes["Separate Bundle"].height = 100.0

    ring_sensor_distribution_1.nodes["Cylinder.001"].width  = 140.0
    ring_sensor_distribution_1.nodes["Cylinder.001"].height = 100.0

    ring_sensor_distribution_1.nodes["Math"].width  = 140.0
    ring_sensor_distribution_1.nodes["Math"].height = 100.0

    ring_sensor_distribution_1.nodes["Reroute"].width  = 14.5
    ring_sensor_distribution_1.nodes["Reroute"].height = 100.0

    ring_sensor_distribution_1.nodes["Math.001"].width  = 140.0
    ring_sensor_distribution_1.nodes["Math.001"].height = 100.0

    ring_sensor_distribution_1.nodes["Mesh Boolean"].width  = 140.0
    ring_sensor_distribution_1.nodes["Mesh Boolean"].height = 100.0

    ring_sensor_distribution_1.nodes["Viewer"].width  = 140.0
    ring_sensor_distribution_1.nodes["Viewer"].height = 100.0


    # Initialize ring_sensor_distribution_1 links

    # group_input.Nodule Parameters -> separate_bundle.Bundle
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Group Input"].outputs[0],
        ring_sensor_distribution_1.nodes["Separate Bundle"].inputs[0]
    )
    # group.Geometry -> group_output.Sensor Shapes
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Group"].outputs[0],
        ring_sensor_distribution_1.nodes["Group Output"].inputs[0]
    )
    # separate_bundle.Points -> group.Points
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Separate Bundle"].outputs[0],
        ring_sensor_distribution_1.nodes["Group"].inputs[1]
    )
    # reroute.Output -> cylinder.Depth
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Reroute"].outputs[0],
        ring_sensor_distribution_1.nodes["Cylinder"].inputs[4]
    )
    # separate_bundle.Base Radii -> group.Scale
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Separate Bundle"].outputs[5],
        ring_sensor_distribution_1.nodes["Group"].inputs[4]
    )
    # separate_bundle.Node Offset -> group.Node Offset
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Separate Bundle"].outputs[4],
        ring_sensor_distribution_1.nodes["Group"].inputs[3]
    )
    # separate_bundle.Material -> group.Sensor Material
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Separate Bundle"].outputs[2],
        ring_sensor_distribution_1.nodes["Group"].inputs[2]
    )
    # separate_bundle.Euler -> group.Euler Rotation
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Separate Bundle"].outputs[1],
        ring_sensor_distribution_1.nodes["Group"].inputs[5]
    )
    # math.Value -> cylinder_001.Radius
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Math"].outputs[0],
        ring_sensor_distribution_1.nodes["Cylinder.001"].inputs[3]
    )
    # group_input.Center Cut -> math.Value
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Group Input"].outputs[1],
        ring_sensor_distribution_1.nodes["Math"].inputs[0]
    )
    # separate_bundle.Node Depth -> reroute.Input
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Separate Bundle"].outputs[3],
        ring_sensor_distribution_1.nodes["Reroute"].inputs[0]
    )
    # math_001.Value -> cylinder_001.Depth
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Math.001"].outputs[0],
        ring_sensor_distribution_1.nodes["Cylinder.001"].inputs[4]
    )
    # reroute.Output -> math_001.Value
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Reroute"].outputs[0],
        ring_sensor_distribution_1.nodes["Math.001"].inputs[0]
    )
    # mesh_boolean.Mesh -> viewer.Mesh
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Mesh Boolean"].outputs[0],
        ring_sensor_distribution_1.nodes["Viewer"].inputs[0]
    )
    # cylinder.Mesh -> mesh_boolean.Mesh 1
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Cylinder"].outputs[0],
        ring_sensor_distribution_1.nodes["Mesh Boolean"].inputs[0]
    )
    # cylinder_001.Mesh -> mesh_boolean.Mesh 2
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Cylinder.001"].outputs[0],
        ring_sensor_distribution_1.nodes["Mesh Boolean"].inputs[1]
    )
    # mesh_boolean.Mesh -> group.Shape
    ring_sensor_distribution_1.links.new(
        ring_sensor_distribution_1.nodes["Mesh Boolean"].outputs[0],
        ring_sensor_distribution_1.nodes["Group"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True

    return ring_sensor_distribution_1


def shape_on_points_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Shape on points node group"""
    shape_on_points_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Shape on points")

    shape_on_points_1.color_tag = 'NONE'
    shape_on_points_1.description = ""
    shape_on_points_1.default_group_node_width = 140
    shape_on_points_1.show_modifier_manage_panel = True

    # shape_on_points_1 interface

    # Socket Uncut Shapes
    uncut_shapes_socket = shape_on_points_1.interface.new_socket(name="Uncut Shapes", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    uncut_shapes_socket.attribute_domain = 'POINT'
    uncut_shapes_socket.default_input = 'VALUE'
    uncut_shapes_socket.structure_type = 'AUTO'

    # Socket Uncut Stems
    uncut_stems_socket = shape_on_points_1.interface.new_socket(name="Uncut Stems", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    uncut_stems_socket.attribute_domain = 'POINT'
    uncut_stems_socket.default_input = 'VALUE'
    uncut_stems_socket.structure_type = 'AUTO'

    # Socket Stem Points
    stem_points_socket = shape_on_points_1.interface.new_socket(name="Stem Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    stem_points_socket.attribute_domain = 'POINT'
    stem_points_socket.default_input = 'VALUE'
    stem_points_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket = shape_on_points_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Bottom Plate
    bottom_plate_socket = shape_on_points_1.interface.new_socket(name="Bottom Plate", in_out='INPUT', socket_type='NodeSocketGeometry')
    bottom_plate_socket.attribute_domain = 'POINT'
    bottom_plate_socket.description = "Geometry to find the closest point on"
    bottom_plate_socket.default_input = 'VALUE'
    bottom_plate_socket.structure_type = 'AUTO'

    # Socket Euler
    euler_socket = shape_on_points_1.interface.new_socket(name="Euler", in_out='INPUT', socket_type='NodeSocketVector')
    euler_socket.default_value = (0.0, 0.0, 0.0)
    euler_socket.min_value = -3.4028234663852886e+38
    euler_socket.max_value = 3.4028234663852886e+38
    euler_socket.subtype = 'EULER'
    euler_socket.attribute_domain = 'POINT'
    euler_socket.default_input = 'VALUE'
    euler_socket.structure_type = 'AUTO'

    # Socket Material
    material_socket = shape_on_points_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    # Socket Node Depth
    node_depth_socket = shape_on_points_1.interface.new_socket(name="Node Depth", in_out='INPUT', socket_type='NodeSocketFloat')
    node_depth_socket.default_value = 1.0
    node_depth_socket.min_value = 0.0
    node_depth_socket.max_value = 3.4028234663852886e+38
    node_depth_socket.subtype = 'DISTANCE'
    node_depth_socket.attribute_domain = 'POINT'
    node_depth_socket.description = "The height of the cylinder"
    node_depth_socket.default_input = 'VALUE'
    node_depth_socket.structure_type = 'AUTO'

    # Socket Node Offset
    node_offset_socket = shape_on_points_1.interface.new_socket(name="Node Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    node_offset_socket.default_value = 0.0
    node_offset_socket.min_value = -10000.0
    node_offset_socket.max_value = 10000.0
    node_offset_socket.subtype = 'NONE'
    node_offset_socket.attribute_domain = 'POINT'
    node_offset_socket.default_input = 'VALUE'
    node_offset_socket.structure_type = 'AUTO'

    # Socket Stem Depth
    stem_depth_socket = shape_on_points_1.interface.new_socket(name="Stem Depth", in_out='INPUT', socket_type='NodeSocketFloat')
    stem_depth_socket.default_value = 1.0
    stem_depth_socket.min_value = 0.0
    stem_depth_socket.max_value = 3.4028234663852886e+38
    stem_depth_socket.subtype = 'DISTANCE'
    stem_depth_socket.attribute_domain = 'POINT'
    stem_depth_socket.description = "The height of the cylinder"
    stem_depth_socket.default_input = 'VALUE'
    stem_depth_socket.structure_type = 'AUTO'

    # Socket Stem Offset
    stem_offset_socket = shape_on_points_1.interface.new_socket(name="Stem Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    stem_offset_socket.default_value = 0.8999999761581421
    stem_offset_socket.min_value = -10000.0
    stem_offset_socket.max_value = 10000.0
    stem_offset_socket.subtype = 'NONE'
    stem_offset_socket.attribute_domain = 'POINT'
    stem_offset_socket.default_input = 'VALUE'
    stem_offset_socket.structure_type = 'AUTO'

    # Socket Base Radii
    base_radii_socket = shape_on_points_1.interface.new_socket(name="Base Radii", in_out='INPUT', socket_type='NodeSocketFloat')
    base_radii_socket.default_value = 0.0
    base_radii_socket.min_value = 0.0
    base_radii_socket.max_value = 3.4028234663852886e+38
    base_radii_socket.subtype = 'NONE'
    base_radii_socket.attribute_domain = 'POINT'
    base_radii_socket.default_input = 'VALUE'
    base_radii_socket.structure_type = 'AUTO'

    # Socket Sensor Shape
    sensor_shape_socket = shape_on_points_1.interface.new_socket(name="Sensor Shape", in_out='INPUT', socket_type='NodeSocketMenu')
    sensor_shape_socket.attribute_domain = 'POINT'
    sensor_shape_socket.default_input = 'VALUE'
    sensor_shape_socket.structure_type = 'AUTO'
    sensor_shape_socket.optional_label = True

    # Socket Center Cut
    center_cut_socket = shape_on_points_1.interface.new_socket(name="Center Cut", in_out='INPUT', socket_type='NodeSocketFloat')
    center_cut_socket.default_value = 2.0
    center_cut_socket.min_value = 0.0
    center_cut_socket.max_value = 99.5
    center_cut_socket.subtype = 'PERCENTAGE'
    center_cut_socket.attribute_domain = 'POINT'
    center_cut_socket.description = "The percentage of the center radius removed"
    center_cut_socket.default_input = 'VALUE'
    center_cut_socket.structure_type = 'AUTO'

    # Initialize shape_on_points_1 nodes

    # Node Group Output
    group_output = shape_on_points_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = shape_on_points_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Frame.010
    frame_010 = shape_on_points_1.nodes.new("NodeFrame")
    frame_010.label = "Cylander Mesh Alternative"
    frame_010.name = "Frame.010"
    frame_010.use_custom_color = True
    frame_010.color = (0.4044908285140991, 0.14717276394367218, 0.17180749773979187)
    frame_010.hide = True
    frame_010.show_options = True
    frame_010.label_size = 20
    frame_010.shrink = True

    # Node Frame.011
    frame_011 = shape_on_points_1.nodes.new("NodeFrame")
    frame_011.label = "Original Mesh"
    frame_011.name = "Frame.011"
    frame_011.show_options = True
    frame_011.label_size = 10
    frame_011.shrink = True

    # Node Instance on Points.002
    instance_on_points_002 = shape_on_points_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    instance_on_points_002.show_options = True
    # Selection
    instance_on_points_002.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_002.inputs[3].default_value = False
    # Instance Index
    instance_on_points_002.inputs[4].default_value = 0

    # Node Set Material.001
    set_material_001 = shape_on_points_1.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    set_material_001.show_options = True
    # Selection
    set_material_001.inputs[1].default_value = True

    # Node Cylinder.001
    cylinder_001 = shape_on_points_1.nodes.new("GeometryNodeMeshCylinder")
    cylinder_001.name = "Cylinder.001"
    cylinder_001.show_options = True
    cylinder_001.fill_type = 'NGON'
    # Vertices
    cylinder_001.inputs[0].default_value = 32
    # Side Segments
    cylinder_001.inputs[1].default_value = 1
    # Fill Segments
    cylinder_001.inputs[2].default_value = 1
    # Radius
    cylinder_001.inputs[3].default_value = 0.10000000149011612

    # Node Translate Instances.001
    translate_instances_001 = shape_on_points_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances_001.name = "Translate Instances.001"
    translate_instances_001.show_options = True
    # Selection
    translate_instances_001.inputs[1].default_value = True
    # Local Space
    translate_instances_001.inputs[3].default_value = True

    # Node Reroute.031
    reroute_031 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_031.name = "Reroute.031"
    reroute_031.show_options = True
    reroute_031.socket_idname = "NodeSocketVector"
    # Node Combine XYZ.002
    combine_xyz_002 = shape_on_points_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.show_options = True
    # X
    combine_xyz_002.inputs[0].default_value = 0.0
    # Y
    combine_xyz_002.inputs[1].default_value = 0.0

    # Node Reroute.032
    reroute_032 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_032.name = "Reroute.032"
    reroute_032.show_options = True
    reroute_032.socket_idname = "NodeSocketVectorEuler"
    # Node Reroute.033
    reroute_033 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_033.name = "Reroute.033"
    reroute_033.show_options = True
    reroute_033.socket_idname = "NodeSocketMaterial"
    # Node Reroute.034
    reroute_034 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_034.name = "Reroute.034"
    reroute_034.show_options = True
    reroute_034.socket_idname = "NodeSocketMaterial"
    # Node Euler to Rotation.001
    euler_to_rotation_001 = shape_on_points_1.nodes.new("FunctionNodeEulerToRotation")
    euler_to_rotation_001.name = "Euler to Rotation.001"
    euler_to_rotation_001.show_options = True

    # Node Reroute.043
    reroute_043 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_043.name = "Reroute.043"
    reroute_043.show_options = True
    reroute_043.socket_idname = "NodeSocketFloat"
    # Node Instances to Points
    instances_to_points = shape_on_points_1.nodes.new("GeometryNodeInstancesToPoints")
    instances_to_points.name = "Instances to Points"
    instances_to_points.show_options = True
    # Selection
    instances_to_points.inputs[1].default_value = True
    # Position
    instances_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    instances_to_points.inputs[3].default_value = 0.05000000074505806

    # Node Frame.012
    frame_012 = shape_on_points_1.nodes.new("NodeFrame")
    frame_012.label = "Store Sensor Stem Positions and Normals"
    frame_012.name = "Frame.012"
    frame_012.use_custom_color = True
    frame_012.color = (0.2452997863292694, 0.4419439136981964, 0.2922254502773285)
    frame_012.show_options = True
    frame_012.label_size = 20
    frame_012.shrink = False

    # Node Store Named Attribute.001
    store_named_attribute_001 = shape_on_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'FLOAT_VECTOR'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True

    # Node Position.003
    position_003 = shape_on_points_1.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    position_003.show_options = True

    # Node String.001
    string_001 = shape_on_points_1.nodes.new("FunctionNodeInputString")
    string_001.name = "String.001"
    string_001.show_options = True
    string_001.string = "sensor_pos_stem"

    # Node Points to Vertices.001
    points_to_vertices_001 = shape_on_points_1.nodes.new("GeometryNodePointsToVertices")
    points_to_vertices_001.name = "Points to Vertices.001"
    points_to_vertices_001.show_options = True
    # Selection
    points_to_vertices_001.inputs[1].default_value = True

    # Node Realize Instances.001
    realize_instances_001 = shape_on_points_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.hide = True
    realize_instances_001.show_options = True
    realize_instances_001.realize_to_point_domain = True
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Reroute
    reroute = shape_on_points_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketVectorEuler"
    # Node Store Named Attribute
    store_named_attribute = shape_on_points_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "wiring_endpoint"
    # Value
    store_named_attribute.inputs[3].default_value = True

    # Node Menu Switch
    menu_switch = shape_on_points_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.show_options = True
    menu_switch.active_index = 1
    menu_switch.data_type = 'GEOMETRY'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Cylinder")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Ring")
    menu_switch.enum_items[1].description = ""
    menu_switch.enum_items.new("Sphere")
    menu_switch.enum_items[2].description = ""
    menu_switch.enum_items.new("Voronoi")
    menu_switch.enum_items[3].description = ""

    # Node Combine Bundle
    combine_bundle = shape_on_points_1.nodes.new("NodeCombineBundle")
    combine_bundle.name = "Combine Bundle"
    combine_bundle.show_options = True
    combine_bundle.active_index = 5
    combine_bundle.bundle_items.clear()
    combine_bundle.bundle_items.new('GEOMETRY', "Points")
    combine_bundle.bundle_items[0].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('VECTOR', "Euler")
    combine_bundle.bundle_items[1].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('MATERIAL', "Material")
    combine_bundle.bundle_items[2].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('FLOAT', "Node Depth")
    combine_bundle.bundle_items[3].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('FLOAT', "Node Offset")
    combine_bundle.bundle_items[4].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('FLOAT', "Base Radii")
    combine_bundle.bundle_items[5].structure_type = 'AUTO'
    combine_bundle.define_signature = False

    # Node Cylinder
    cylinder = shape_on_points_1.nodes.new("GeometryNodeGroup")
    cylinder.name = "Cylinder"
    cylinder.show_options = True
    cylinder.node_tree = bpy.data.node_groups[node_tree_names[cylinder_sensor_distribution_1_node_group]]

    # Node Cylinder.002
    cylinder_002 = shape_on_points_1.nodes.new("GeometryNodeGroup")
    cylinder_002.name = "Cylinder.002"
    cylinder_002.show_options = True
    cylinder_002.node_tree = bpy.data.node_groups[node_tree_names[sphere_sensor_distribution_1_node_group]]

    # Node Reroute.001
    reroute_001 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketBundle"
    # Node Cylinder.003
    cylinder_003 = shape_on_points_1.nodes.new("GeometryNodeGroup")
    cylinder_003.name = "Cylinder.003"
    cylinder_003.show_options = True
    cylinder_003.node_tree = bpy.data.node_groups[node_tree_names[voronoi_sensor_distribution_1_node_group]]

    # Node Reroute.002
    reroute_002 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketMenu"
    # Node Reroute.003
    reroute_003 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketMenu"
    # Node Viewer
    viewer = shape_on_points_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Mesh")

    # Node Reroute.004
    reroute_004 = shape_on_points_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketGeometry"
    # Node Cylinder.004
    cylinder_004 = shape_on_points_1.nodes.new("GeometryNodeGroup")
    cylinder_004.name = "Cylinder.004"
    cylinder_004.show_options = True
    cylinder_004.node_tree = bpy.data.node_groups[node_tree_names[ring_sensor_distribution_1_node_group]]

    # Set parents
    shape_on_points_1.nodes["Frame.011"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Instance on Points.002"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Set Material.001"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Cylinder.001"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Translate Instances.001"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Reroute.031"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Combine XYZ.002"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Reroute.032"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Reroute.033"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Reroute.034"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Euler to Rotation.001"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Instances to Points"].parent = shape_on_points_1.nodes["Frame.012"]
    shape_on_points_1.nodes["Store Named Attribute.001"].parent = shape_on_points_1.nodes["Frame.012"]
    shape_on_points_1.nodes["Position.003"].parent = shape_on_points_1.nodes["Frame.012"]
    shape_on_points_1.nodes["String.001"].parent = shape_on_points_1.nodes["Frame.012"]
    shape_on_points_1.nodes["Points to Vertices.001"].parent = shape_on_points_1.nodes["Frame.012"]
    shape_on_points_1.nodes["Reroute"].parent = shape_on_points_1.nodes["Frame.010"]
    shape_on_points_1.nodes["Store Named Attribute"].parent = shape_on_points_1.nodes["Frame.012"]

    # Set locations
    shape_on_points_1.nodes["Group Output"].location = (700.0, -400.0)
    shape_on_points_1.nodes["Group Input"].location = (-2840.0, 0.0)
    shape_on_points_1.nodes["Frame.010"].location = (-2153.833251953125, -559.3666381835938)
    shape_on_points_1.nodes["Frame.011"].location = (1113.833251953125, -40.63336181640625)
    shape_on_points_1.nodes["Instance on Points.002"].location = (893.833251953125, -60.63336181640625)
    shape_on_points_1.nodes["Set Material.001"].location = (513.833251953125, -100.63336181640625)
    shape_on_points_1.nodes["Cylinder.001"].location = (73.833251953125, -100.63336181640625)
    shape_on_points_1.nodes["Translate Instances.001"].location = (1113.833251953125, -80.63336181640625)
    shape_on_points_1.nodes["Reroute.031"].location = (793.833251953125, -540.6333618164062)
    shape_on_points_1.nodes["Combine XYZ.002"].location = (33.833251953125, -520.6333618164062)
    shape_on_points_1.nodes["Reroute.032"].location = (533.833251953125, -480.63336181640625)
    shape_on_points_1.nodes["Reroute.033"].location = (273.833251953125, -400.63336181640625)
    shape_on_points_1.nodes["Reroute.034"].location = (33.833251953125, -400.63336181640625)
    shape_on_points_1.nodes["Euler to Rotation.001"].location = (673.833251953125, -300.63336181640625)
    shape_on_points_1.nodes["Reroute.043"].location = (-1660.0, -500.0)
    shape_on_points_1.nodes["Instances to Points"].location = (249.6552734375, -82.4349365234375)
    shape_on_points_1.nodes["Frame.012"].location = (-680.0, -600.0)
    shape_on_points_1.nodes["Store Named Attribute.001"].location = (423.5166015625, -114.051025390625)
    shape_on_points_1.nodes["Position.003"].location = (251.9990234375, -355.15478515625)
    shape_on_points_1.nodes["String.001"].location = (252.302734375, -267.08935546875)
    shape_on_points_1.nodes["Points to Vertices.001"].location = (1112.947265625, -115.5533447265625)
    shape_on_points_1.nodes["Realize Instances.001"].location = (-820.0, -600.0)
    shape_on_points_1.nodes["Reroute"].location = (293.833251953125, -40.63336181640625)
    shape_on_points_1.nodes["Store Named Attribute"].location = (772.947265625, -115.5533447265625)
    shape_on_points_1.nodes["Menu Switch"].location = (-1380.0, 220.0)
    shape_on_points_1.nodes["Combine Bundle"].location = (-2380.0, 280.0)
    shape_on_points_1.nodes["Cylinder"].location = (-2000.0, 360.0)
    shape_on_points_1.nodes["Cylinder.002"].location = (-2000.0, 220.0)
    shape_on_points_1.nodes["Reroute.001"].location = (-2119.43505859375, 227.21771240234375)
    shape_on_points_1.nodes["Cylinder.003"].location = (-2000.0, 60.0)
    shape_on_points_1.nodes["Reroute.002"].location = (-1520.0, 640.0)
    shape_on_points_1.nodes["Reroute.003"].location = (-2520.0, 640.0)
    shape_on_points_1.nodes["Viewer"].location = (593.0, -610.5)
    shape_on_points_1.nodes["Reroute.004"].location = (-2601.209716796875, 18.066909790039062)
    shape_on_points_1.nodes["Cylinder.004"].location = (-2000.0, 520.0)

    # Set dimensions
    shape_on_points_1.nodes["Group Output"].width  = 140.0
    shape_on_points_1.nodes["Group Output"].height = 100.0

    shape_on_points_1.nodes["Group Input"].width  = 140.0
    shape_on_points_1.nodes["Group Input"].height = 100.0

    shape_on_points_1.nodes["Frame.010"].width  = 1282.833251953125
    shape_on_points_1.nodes["Frame.010"].height = 662.9667358398438

    shape_on_points_1.nodes["Frame.011"].width  = 122.59814453125
    shape_on_points_1.nodes["Frame.011"].height = 45.0

    shape_on_points_1.nodes["Instance on Points.002"].width  = 140.0
    shape_on_points_1.nodes["Instance on Points.002"].height = 100.0

    shape_on_points_1.nodes["Set Material.001"].width  = 140.0
    shape_on_points_1.nodes["Set Material.001"].height = 100.0

    shape_on_points_1.nodes["Cylinder.001"].width  = 140.0
    shape_on_points_1.nodes["Cylinder.001"].height = 100.0

    shape_on_points_1.nodes["Translate Instances.001"].width  = 140.0
    shape_on_points_1.nodes["Translate Instances.001"].height = 100.0

    shape_on_points_1.nodes["Reroute.031"].width  = 14.5
    shape_on_points_1.nodes["Reroute.031"].height = 100.0

    shape_on_points_1.nodes["Combine XYZ.002"].width  = 140.0
    shape_on_points_1.nodes["Combine XYZ.002"].height = 100.0

    shape_on_points_1.nodes["Reroute.032"].width  = 14.5
    shape_on_points_1.nodes["Reroute.032"].height = 100.0

    shape_on_points_1.nodes["Reroute.033"].width  = 14.5
    shape_on_points_1.nodes["Reroute.033"].height = 100.0

    shape_on_points_1.nodes["Reroute.034"].width  = 14.5
    shape_on_points_1.nodes["Reroute.034"].height = 100.0

    shape_on_points_1.nodes["Euler to Rotation.001"].width  = 140.0
    shape_on_points_1.nodes["Euler to Rotation.001"].height = 100.0

    shape_on_points_1.nodes["Reroute.043"].width  = 14.5
    shape_on_points_1.nodes["Reroute.043"].height = 100.0

    shape_on_points_1.nodes["Instances to Points"].width  = 140.0
    shape_on_points_1.nodes["Instances to Points"].height = 100.0

    shape_on_points_1.nodes["Frame.012"].width  = 1283.0
    shape_on_points_1.nodes["Frame.012"].height = 483.0

    shape_on_points_1.nodes["Store Named Attribute.001"].width  = 140.0
    shape_on_points_1.nodes["Store Named Attribute.001"].height = 100.0

    shape_on_points_1.nodes["Position.003"].width  = 140.0
    shape_on_points_1.nodes["Position.003"].height = 100.0

    shape_on_points_1.nodes["String.001"].width  = 140.0
    shape_on_points_1.nodes["String.001"].height = 100.0

    shape_on_points_1.nodes["Points to Vertices.001"].width  = 140.0
    shape_on_points_1.nodes["Points to Vertices.001"].height = 100.0

    shape_on_points_1.nodes["Realize Instances.001"].width  = 140.0
    shape_on_points_1.nodes["Realize Instances.001"].height = 100.0

    shape_on_points_1.nodes["Reroute"].width  = 14.5
    shape_on_points_1.nodes["Reroute"].height = 100.0

    shape_on_points_1.nodes["Store Named Attribute"].width  = 140.0
    shape_on_points_1.nodes["Store Named Attribute"].height = 100.0

    shape_on_points_1.nodes["Menu Switch"].width  = 140.0
    shape_on_points_1.nodes["Menu Switch"].height = 100.0

    shape_on_points_1.nodes["Combine Bundle"].width  = 140.0
    shape_on_points_1.nodes["Combine Bundle"].height = 100.0

    shape_on_points_1.nodes["Cylinder"].width  = 200.0
    shape_on_points_1.nodes["Cylinder"].height = 100.0

    shape_on_points_1.nodes["Cylinder.002"].width  = 200.0
    shape_on_points_1.nodes["Cylinder.002"].height = 100.0

    shape_on_points_1.nodes["Reroute.001"].width  = 14.5
    shape_on_points_1.nodes["Reroute.001"].height = 100.0

    shape_on_points_1.nodes["Cylinder.003"].width  = 200.0
    shape_on_points_1.nodes["Cylinder.003"].height = 100.0

    shape_on_points_1.nodes["Reroute.002"].width  = 14.5
    shape_on_points_1.nodes["Reroute.002"].height = 100.0

    shape_on_points_1.nodes["Reroute.003"].width  = 14.5
    shape_on_points_1.nodes["Reroute.003"].height = 100.0

    shape_on_points_1.nodes["Viewer"].width  = 140.0
    shape_on_points_1.nodes["Viewer"].height = 100.0

    shape_on_points_1.nodes["Reroute.004"].width  = 14.5
    shape_on_points_1.nodes["Reroute.004"].height = 100.0

    shape_on_points_1.nodes["Cylinder.004"].width  = 200.0
    shape_on_points_1.nodes["Cylinder.004"].height = 100.0


    # Initialize shape_on_points_1 links

    # string_001.String -> store_named_attribute_001.Name
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["String.001"].outputs[0],
        shape_on_points_1.nodes["Store Named Attribute.001"].inputs[2]
    )
    # store_named_attribute.Geometry -> points_to_vertices_001.Points
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Store Named Attribute"].outputs[0],
        shape_on_points_1.nodes["Points to Vertices.001"].inputs[0]
    )
    # reroute_043.Output -> instance_on_points_002.Scale
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.043"].outputs[0],
        shape_on_points_1.nodes["Instance on Points.002"].inputs[6]
    )
    # reroute_032.Output -> euler_to_rotation_001.Euler
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.032"].outputs[0],
        shape_on_points_1.nodes["Euler to Rotation.001"].inputs[0]
    )
    # instance_on_points_002.Instances -> translate_instances_001.Instances
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Instance on Points.002"].outputs[0],
        shape_on_points_1.nodes["Translate Instances.001"].inputs[0]
    )
    # translate_instances_001.Instances -> realize_instances_001.Geometry
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Translate Instances.001"].outputs[0],
        shape_on_points_1.nodes["Realize Instances.001"].inputs[0]
    )
    # set_material_001.Geometry -> instance_on_points_002.Instance
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Set Material.001"].outputs[0],
        shape_on_points_1.nodes["Instance on Points.002"].inputs[2]
    )
    # reroute_031.Output -> translate_instances_001.Translation
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.031"].outputs[0],
        shape_on_points_1.nodes["Translate Instances.001"].inputs[2]
    )
    # combine_xyz_002.Vector -> reroute_031.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Combine XYZ.002"].outputs[0],
        shape_on_points_1.nodes["Reroute.031"].inputs[0]
    )
    # position_003.Position -> store_named_attribute_001.Value
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Position.003"].outputs[0],
        shape_on_points_1.nodes["Store Named Attribute.001"].inputs[3]
    )
    # reroute_034.Output -> reroute_033.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.034"].outputs[0],
        shape_on_points_1.nodes["Reroute.033"].inputs[0]
    )
    # reroute_033.Output -> set_material_001.Material
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.033"].outputs[0],
        shape_on_points_1.nodes["Set Material.001"].inputs[2]
    )
    # cylinder_001.Mesh -> set_material_001.Geometry
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Cylinder.001"].outputs[0],
        shape_on_points_1.nodes["Set Material.001"].inputs[0]
    )
    # instances_to_points.Points -> store_named_attribute_001.Geometry
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Instances to Points"].outputs[0],
        shape_on_points_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # translate_instances_001.Instances -> instances_to_points.Instances
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Translate Instances.001"].outputs[0],
        shape_on_points_1.nodes["Instances to Points"].inputs[0]
    )
    # euler_to_rotation_001.Rotation -> instance_on_points_002.Rotation
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Euler to Rotation.001"].outputs[0],
        shape_on_points_1.nodes["Instance on Points.002"].inputs[5]
    )
    # group_input.Euler -> reroute.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[2],
        shape_on_points_1.nodes["Reroute"].inputs[0]
    )
    # reroute.Output -> reroute_032.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute"].outputs[0],
        shape_on_points_1.nodes["Reroute.032"].inputs[0]
    )
    # group_input.Material -> reroute_034.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[3],
        shape_on_points_1.nodes["Reroute.034"].inputs[0]
    )
    # group_input.Stem Offset -> combine_xyz_002.Z
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[7],
        shape_on_points_1.nodes["Combine XYZ.002"].inputs[2]
    )
    # group_input.Stem Depth -> cylinder_001.Depth
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[6],
        shape_on_points_1.nodes["Cylinder.001"].inputs[4]
    )
    # realize_instances_001.Geometry -> group_output.Uncut Stems
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Realize Instances.001"].outputs[0],
        shape_on_points_1.nodes["Group Output"].inputs[1]
    )
    # points_to_vertices_001.Mesh -> group_output.Stem Points
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Points to Vertices.001"].outputs[0],
        shape_on_points_1.nodes["Group Output"].inputs[2]
    )
    # group_input.Base Radii -> reroute_043.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[8],
        shape_on_points_1.nodes["Reroute.043"].inputs[0]
    )
    # store_named_attribute_001.Geometry -> store_named_attribute.Geometry
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Store Named Attribute.001"].outputs[0],
        shape_on_points_1.nodes["Store Named Attribute"].inputs[0]
    )
    # reroute_002.Output -> menu_switch.Menu
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.002"].outputs[0],
        shape_on_points_1.nodes["Menu Switch"].inputs[0]
    )
    # reroute_004.Output -> combine_bundle.Points
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.004"].outputs[0],
        shape_on_points_1.nodes["Combine Bundle"].inputs[0]
    )
    # group_input.Euler -> combine_bundle.Euler
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[2],
        shape_on_points_1.nodes["Combine Bundle"].inputs[1]
    )
    # group_input.Material -> combine_bundle.Material
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[3],
        shape_on_points_1.nodes["Combine Bundle"].inputs[2]
    )
    # group_input.Node Depth -> combine_bundle.Node Depth
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[4],
        shape_on_points_1.nodes["Combine Bundle"].inputs[3]
    )
    # group_input.Node Offset -> combine_bundle.Node Offset
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[5],
        shape_on_points_1.nodes["Combine Bundle"].inputs[4]
    )
    # group_input.Base Radii -> combine_bundle.Base Radii
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[8],
        shape_on_points_1.nodes["Combine Bundle"].inputs[5]
    )
    # reroute_001.Output -> cylinder.Nodule Parameters
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.001"].outputs[0],
        shape_on_points_1.nodes["Cylinder"].inputs[0]
    )
    # menu_switch.Output -> group_output.Uncut Shapes
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Menu Switch"].outputs[0],
        shape_on_points_1.nodes["Group Output"].inputs[0]
    )
    # cylinder.Sensor Shapes -> menu_switch.Cylinder
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Cylinder"].outputs[0],
        shape_on_points_1.nodes["Menu Switch"].inputs[1]
    )
    # cylinder_002.Sensor Shapes -> menu_switch.Sphere
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Cylinder.002"].outputs[0],
        shape_on_points_1.nodes["Menu Switch"].inputs[3]
    )
    # reroute_001.Output -> cylinder_002.Nodule Parameters
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.001"].outputs[0],
        shape_on_points_1.nodes["Cylinder.002"].inputs[0]
    )
    # combine_bundle.Bundle -> reroute_001.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Combine Bundle"].outputs[0],
        shape_on_points_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_003.Output -> reroute_002.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.003"].outputs[0],
        shape_on_points_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Sensor Shape -> reroute_003.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[9],
        shape_on_points_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_001.Output -> cylinder_003.Nodule Parameters
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.001"].outputs[0],
        shape_on_points_1.nodes["Cylinder.003"].inputs[0]
    )
    # group_input.Bottom Plate -> cylinder_003.Bottom Plate
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[1],
        shape_on_points_1.nodes["Cylinder.003"].inputs[1]
    )
    # points_to_vertices_001.Mesh -> viewer.Mesh
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Points to Vertices.001"].outputs[0],
        shape_on_points_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Points -> reroute_004.Input
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[0],
        shape_on_points_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_004.Output -> instance_on_points_002.Points
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.004"].outputs[0],
        shape_on_points_1.nodes["Instance on Points.002"].inputs[0]
    )
    # reroute_001.Output -> cylinder_004.Nodule Parameters
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Reroute.001"].outputs[0],
        shape_on_points_1.nodes["Cylinder.004"].inputs[0]
    )
    # cylinder_004.Sensor Shapes -> menu_switch.Ring
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Cylinder.004"].outputs[0],
        shape_on_points_1.nodes["Menu Switch"].inputs[2]
    )
    # cylinder_003.Sensor Shapes -> menu_switch.Voronoi
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Cylinder.003"].outputs[0],
        shape_on_points_1.nodes["Menu Switch"].inputs[4]
    )
    # group_input.Center Cut -> cylinder_004.Center Cut
    shape_on_points_1.links.new(
        shape_on_points_1.nodes["Group Input"].outputs[10],
        shape_on_points_1.nodes["Cylinder.004"].inputs[1]
    )
    sensor_shape_socket.default_value = 'Cylinder'
    viewer.viewer_items[0].auto_remove = True

    return shape_on_points_1


def cut_disk_custom_layer_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Cut Disk Custom Layer node group"""
    cut_disk_custom_layer_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Cut Disk Custom Layer")

    cut_disk_custom_layer_1.color_tag = 'NONE'
    cut_disk_custom_layer_1.description = ""
    cut_disk_custom_layer_1.default_group_node_width = 140
    cut_disk_custom_layer_1.show_modifier_manage_panel = True

    # cut_disk_custom_layer_1 interface

    # Socket Geometry
    geometry_socket = cut_disk_custom_layer_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Sensor Geometry
    sensor_geometry_socket = cut_disk_custom_layer_1.interface.new_socket(name="Sensor Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_geometry_socket.attribute_domain = 'POINT'
    sensor_geometry_socket.default_input = 'VALUE'
    sensor_geometry_socket.structure_type = 'AUTO'

    # Socket Stem Points
    stem_points_socket = cut_disk_custom_layer_1.interface.new_socket(name="Stem Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    stem_points_socket.attribute_domain = 'POINT'
    stem_points_socket.default_input = 'VALUE'
    stem_points_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket = cut_disk_custom_layer_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Euler
    euler_socket = cut_disk_custom_layer_1.interface.new_socket(name="Euler", in_out='INPUT', socket_type='NodeSocketVector')
    euler_socket.default_value = (0.0, 0.0, 0.0)
    euler_socket.min_value = -3.4028234663852886e+38
    euler_socket.max_value = 3.4028234663852886e+38
    euler_socket.subtype = 'EULER'
    euler_socket.attribute_domain = 'POINT'
    euler_socket.default_input = 'VALUE'
    euler_socket.structure_type = 'AUTO'

    # Socket Stem Menu
    stem_menu_socket = cut_disk_custom_layer_1.interface.new_socket(name="Stem Menu", in_out='INPUT', socket_type='NodeSocketMenu')
    stem_menu_socket.attribute_domain = 'POINT'
    stem_menu_socket.default_input = 'VALUE'
    stem_menu_socket.structure_type = 'AUTO'
    stem_menu_socket.optional_label = True

    # Socket Base Radii
    base_radii_socket = cut_disk_custom_layer_1.interface.new_socket(name="Base Radii", in_out='INPUT', socket_type='NodeSocketFloat')
    base_radii_socket.default_value = 0.0
    base_radii_socket.min_value = 0.0
    base_radii_socket.max_value = 3.4028234663852886e+38
    base_radii_socket.subtype = 'NONE'
    base_radii_socket.attribute_domain = 'POINT'
    base_radii_socket.default_input = 'VALUE'
    base_radii_socket.structure_type = 'AUTO'

    # Socket Sensor Shape
    sensor_shape_socket = cut_disk_custom_layer_1.interface.new_socket(name="Sensor Shape", in_out='INPUT', socket_type='NodeSocketMenu')
    sensor_shape_socket.attribute_domain = 'POINT'
    sensor_shape_socket.default_input = 'VALUE'
    sensor_shape_socket.structure_type = 'AUTO'
    sensor_shape_socket.optional_label = True

    # Socket Center Cut
    center_cut_socket = cut_disk_custom_layer_1.interface.new_socket(name="Center Cut", in_out='INPUT', socket_type='NodeSocketFloat')
    center_cut_socket.default_value = 2.0
    center_cut_socket.min_value = 0.0
    center_cut_socket.max_value = 99.5
    center_cut_socket.subtype = 'PERCENTAGE'
    center_cut_socket.attribute_domain = 'POINT'
    center_cut_socket.description = "The percentage of the center radius removed"
    center_cut_socket.default_input = 'VALUE'
    center_cut_socket.structure_type = 'AUTO'

    # Panel Shape Settings
    shape_settings_panel = cut_disk_custom_layer_1.interface.new_panel("Shape Settings")
    # Socket Node Offset
    node_offset_socket = cut_disk_custom_layer_1.interface.new_socket(name="Node Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    node_offset_socket.default_value = 0.5
    node_offset_socket.min_value = -10000.0
    node_offset_socket.max_value = 10000.0
    node_offset_socket.subtype = 'NONE'
    node_offset_socket.attribute_domain = 'POINT'
    node_offset_socket.default_input = 'VALUE'
    node_offset_socket.structure_type = 'AUTO'

    # Socket Node Thickness
    node_thickness_socket = cut_disk_custom_layer_1.interface.new_socket(name="Node Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    node_thickness_socket.default_value = 0.5
    node_thickness_socket.min_value = -10000.0
    node_thickness_socket.max_value = 10000.0
    node_thickness_socket.subtype = 'NONE'
    node_thickness_socket.attribute_domain = 'POINT'
    node_thickness_socket.default_input = 'VALUE'
    node_thickness_socket.structure_type = 'AUTO'

    # Socket Node Depth
    node_depth_socket = cut_disk_custom_layer_1.interface.new_socket(name="Node Depth", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    node_depth_socket.default_value = 1.0
    node_depth_socket.min_value = 0.0
    node_depth_socket.max_value = 3.4028234663852886e+38
    node_depth_socket.subtype = 'DISTANCE'
    node_depth_socket.attribute_domain = 'POINT'
    node_depth_socket.description = "The height of the cylinder"
    node_depth_socket.default_input = 'VALUE'
    node_depth_socket.structure_type = 'AUTO'

    # Socket Stem Offset
    stem_offset_socket = cut_disk_custom_layer_1.interface.new_socket(name="Stem Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    stem_offset_socket.default_value = 0.5
    stem_offset_socket.min_value = -10000.0
    stem_offset_socket.max_value = 10000.0
    stem_offset_socket.subtype = 'NONE'
    stem_offset_socket.attribute_domain = 'POINT'
    stem_offset_socket.default_input = 'VALUE'
    stem_offset_socket.structure_type = 'AUTO'

    # Socket Stem Thickness
    stem_thickness_socket = cut_disk_custom_layer_1.interface.new_socket(name="Stem Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    stem_thickness_socket.default_value = 0.5
    stem_thickness_socket.min_value = -10000.0
    stem_thickness_socket.max_value = 10000.0
    stem_thickness_socket.subtype = 'NONE'
    stem_thickness_socket.attribute_domain = 'POINT'
    stem_thickness_socket.default_input = 'VALUE'
    stem_thickness_socket.structure_type = 'AUTO'

    # Socket Stem Depth
    stem_depth_socket = cut_disk_custom_layer_1.interface.new_socket(name="Stem Depth", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    stem_depth_socket.default_value = 1.0
    stem_depth_socket.min_value = 0.0
    stem_depth_socket.max_value = 3.4028234663852886e+38
    stem_depth_socket.subtype = 'DISTANCE'
    stem_depth_socket.attribute_domain = 'POINT'
    stem_depth_socket.description = "The height of the cylinder"
    stem_depth_socket.default_input = 'VALUE'
    stem_depth_socket.structure_type = 'AUTO'

    # Socket Wire Intersect Offset
    wire_intersect_offset_socket = cut_disk_custom_layer_1.interface.new_socket(name="Wire Intersect Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = shape_settings_panel)
    wire_intersect_offset_socket.default_value = 0.8999999761581421
    wire_intersect_offset_socket.min_value = -10000.0
    wire_intersect_offset_socket.max_value = 10000.0
    wire_intersect_offset_socket.subtype = 'NONE'
    wire_intersect_offset_socket.attribute_domain = 'POINT'
    wire_intersect_offset_socket.default_input = 'VALUE'
    wire_intersect_offset_socket.structure_type = 'AUTO'

    # Socket Material
    material_socket = cut_disk_custom_layer_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = shape_settings_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'


    # Panel Dermis Options
    dermis_options_panel = cut_disk_custom_layer_1.interface.new_panel("Dermis Options", default_closed=True)
    # Socket Bottom Plate
    bottom_plate_socket = cut_disk_custom_layer_1.interface.new_socket(name="Bottom Plate", in_out='INPUT', socket_type='NodeSocketGeometry', parent = dermis_options_panel)
    bottom_plate_socket.attribute_domain = 'POINT'
    bottom_plate_socket.default_input = 'VALUE'
    bottom_plate_socket.structure_type = 'AUTO'

    # Socket Reference Thickness
    reference_thickness_socket = cut_disk_custom_layer_1.interface.new_socket(name="Reference Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = dermis_options_panel)
    reference_thickness_socket.default_value = 0.0
    reference_thickness_socket.min_value = 0.0
    reference_thickness_socket.max_value = 3.4028234663852886e+38
    reference_thickness_socket.subtype = 'NONE'
    reference_thickness_socket.attribute_domain = 'POINT'
    reference_thickness_socket.description = "Match this to the dermis"
    reference_thickness_socket.default_input = 'VALUE'
    reference_thickness_socket.structure_type = 'AUTO'


    # Initialize cut_disk_custom_layer_1 nodes

    # Node Group Output
    group_output = cut_disk_custom_layer_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = cut_disk_custom_layer_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Mesh Boolean.005
    mesh_boolean_005 = cut_disk_custom_layer_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_005.name = "Mesh Boolean.005"
    mesh_boolean_005.show_options = True
    mesh_boolean_005.operation = 'INTERSECT'
    mesh_boolean_005.solver = 'FLOAT'

    # Node Plate Volume.002
    plate_volume_002 = cut_disk_custom_layer_1.nodes.new("GeometryNodeGroup")
    plate_volume_002.label = "Plate Volume"
    plate_volume_002.name = "Plate Volume.002"
    plate_volume_002.show_options = True
    plate_volume_002.node_tree = bpy.data.node_groups[node_tree_names[plate_volume_reduced_1_node_group]]
    # Socket_9
    plate_volume_002.inputs[2].default_value = False

    # Node Group.006
    group_006 = cut_disk_custom_layer_1.nodes.new("GeometryNodeGroup")
    group_006.name = "Group.006"
    group_006.show_options = True
    group_006.node_tree = bpy.data.node_groups[node_tree_names[shape_on_points_1_node_group]]
    # Socket_3
    group_006.inputs[5].default_value = 0.0

    # Node Mesh Boolean.006
    mesh_boolean_006 = cut_disk_custom_layer_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_006.name = "Mesh Boolean.006"
    mesh_boolean_006.show_options = True
    mesh_boolean_006.operation = 'INTERSECT'
    mesh_boolean_006.solver = 'FLOAT'

    # Node Plate Volume.003
    plate_volume_003 = cut_disk_custom_layer_1.nodes.new("GeometryNodeGroup")
    plate_volume_003.label = "Plate Volume"
    plate_volume_003.name = "Plate Volume.003"
    plate_volume_003.show_options = True
    plate_volume_003.node_tree = bpy.data.node_groups[node_tree_names[plate_volume_reduced_1_node_group]]
    # Socket_9
    plate_volume_003.inputs[2].default_value = False

    # Node Join Geometry
    join_geometry = cut_disk_custom_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Reroute
    reroute = cut_disk_custom_layer_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Reroute.001
    reroute_001 = cut_disk_custom_layer_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Reroute.006
    reroute_006 = cut_disk_custom_layer_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketString"
    # Node Menu Switch
    menu_switch = cut_disk_custom_layer_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.show_options = True
    menu_switch.active_index = 1
    menu_switch.data_type = 'GEOMETRY'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Stems")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Without Stems")
    menu_switch.enum_items[1].description = ""

    # Node Viewer
    viewer = cut_disk_custom_layer_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Mesh")

    # Node Reroute.002
    reroute_002 = cut_disk_custom_layer_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    # Node Reroute.003
    reroute_003 = cut_disk_custom_layer_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketMaterial"
    # Set locations
    cut_disk_custom_layer_1.nodes["Group Output"].location = (840.0, 180.0)
    cut_disk_custom_layer_1.nodes["Group Input"].location = (-1420.0, 40.0)
    cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].location = (20.0, 180.0)
    cut_disk_custom_layer_1.nodes["Plate Volume.002"].location = (-320.0, 340.0)
    cut_disk_custom_layer_1.nodes["Group.006"].location = (-320.0, 0.0)
    cut_disk_custom_layer_1.nodes["Mesh Boolean.006"].location = (20.0, -200.0)
    cut_disk_custom_layer_1.nodes["Plate Volume.003"].location = (-320.0, -400.0)
    cut_disk_custom_layer_1.nodes["Join Geometry"].location = (540.0, 100.0)
    cut_disk_custom_layer_1.nodes["Reroute"].location = (-640.0, -220.0)
    cut_disk_custom_layer_1.nodes["Reroute.001"].location = (-640.0, -380.0)
    cut_disk_custom_layer_1.nodes["Reroute.006"].location = (-640.0, -240.0)
    cut_disk_custom_layer_1.nodes["Menu Switch"].location = (220.0, 80.0)
    cut_disk_custom_layer_1.nodes["Viewer"].location = (251.30303955078125, -164.47694396972656)
    cut_disk_custom_layer_1.nodes["Reroute.002"].location = (680.0, -120.0)
    cut_disk_custom_layer_1.nodes["Reroute.003"].location = (-379.379150390625, -231.4970245361328)

    # Set dimensions
    cut_disk_custom_layer_1.nodes["Group Output"].width  = 140.0
    cut_disk_custom_layer_1.nodes["Group Output"].height = 100.0

    cut_disk_custom_layer_1.nodes["Group Input"].width  = 140.0
    cut_disk_custom_layer_1.nodes["Group Input"].height = 100.0

    cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].width  = 140.0
    cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].height = 100.0

    cut_disk_custom_layer_1.nodes["Plate Volume.002"].width  = 240.0
    cut_disk_custom_layer_1.nodes["Plate Volume.002"].height = 100.0

    cut_disk_custom_layer_1.nodes["Group.006"].width  = 240.0
    cut_disk_custom_layer_1.nodes["Group.006"].height = 100.0

    cut_disk_custom_layer_1.nodes["Mesh Boolean.006"].width  = 140.0
    cut_disk_custom_layer_1.nodes["Mesh Boolean.006"].height = 100.0

    cut_disk_custom_layer_1.nodes["Plate Volume.003"].width  = 240.0
    cut_disk_custom_layer_1.nodes["Plate Volume.003"].height = 100.0

    cut_disk_custom_layer_1.nodes["Join Geometry"].width  = 140.0
    cut_disk_custom_layer_1.nodes["Join Geometry"].height = 100.0

    cut_disk_custom_layer_1.nodes["Reroute"].width  = 14.5
    cut_disk_custom_layer_1.nodes["Reroute"].height = 100.0

    cut_disk_custom_layer_1.nodes["Reroute.001"].width  = 14.5
    cut_disk_custom_layer_1.nodes["Reroute.001"].height = 100.0

    cut_disk_custom_layer_1.nodes["Reroute.006"].width  = 14.5
    cut_disk_custom_layer_1.nodes["Reroute.006"].height = 100.0

    cut_disk_custom_layer_1.nodes["Menu Switch"].width  = 140.0
    cut_disk_custom_layer_1.nodes["Menu Switch"].height = 100.0

    cut_disk_custom_layer_1.nodes["Viewer"].width  = 140.0
    cut_disk_custom_layer_1.nodes["Viewer"].height = 100.0

    cut_disk_custom_layer_1.nodes["Reroute.002"].width  = 14.5
    cut_disk_custom_layer_1.nodes["Reroute.002"].height = 100.0

    cut_disk_custom_layer_1.nodes["Reroute.003"].width  = 14.5
    cut_disk_custom_layer_1.nodes["Reroute.003"].height = 100.0


    # Initialize cut_disk_custom_layer_1 links

    # plate_volume_003.Geometry -> mesh_boolean_006.Mesh
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Plate Volume.003"].outputs[0],
        cut_disk_custom_layer_1.nodes["Mesh Boolean.006"].inputs[1]
    )
    # group_006.Uncut Shapes -> mesh_boolean_005.Mesh
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group.006"].outputs[0],
        cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].inputs[1]
    )
    # group_input.Points -> group_006.Points
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[0],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[0]
    )
    # group_input.Euler -> group_006.Euler
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[1],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[2]
    )
    # join_geometry.Geometry -> group_output.Geometry
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Join Geometry"].outputs[0],
        cut_disk_custom_layer_1.nodes["Group Output"].inputs[0]
    )
    # reroute.Output -> plate_volume_002.Bottom Plate
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute"].outputs[0],
        cut_disk_custom_layer_1.nodes["Plate Volume.002"].inputs[0]
    )
    # reroute_001.Output -> plate_volume_002.Reference Thickness
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute.001"].outputs[0],
        cut_disk_custom_layer_1.nodes["Plate Volume.002"].inputs[3]
    )
    # group_input.Node Offset -> plate_volume_002.Plate Offset
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[6],
        cut_disk_custom_layer_1.nodes["Plate Volume.002"].inputs[1]
    )
    # group_input.Node Thickness -> plate_volume_002.New Thickness
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[7],
        cut_disk_custom_layer_1.nodes["Plate Volume.002"].inputs[4]
    )
    # group_input.Node Depth -> group_006.Node Depth
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[8],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[4]
    )
    # group_input.Bottom Plate -> reroute.Input
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[14],
        cut_disk_custom_layer_1.nodes["Reroute"].inputs[0]
    )
    # group_input.Reference Thickness -> reroute_001.Input
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[15],
        cut_disk_custom_layer_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute.Output -> plate_volume_003.Bottom Plate
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute"].outputs[0],
        cut_disk_custom_layer_1.nodes["Plate Volume.003"].inputs[0]
    )
    # reroute_001.Output -> plate_volume_003.Reference Thickness
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute.001"].outputs[0],
        cut_disk_custom_layer_1.nodes["Plate Volume.003"].inputs[3]
    )
    # group_input.Stem Offset -> plate_volume_003.Plate Offset
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[9],
        cut_disk_custom_layer_1.nodes["Plate Volume.003"].inputs[1]
    )
    # group_input.Stem Thickness -> plate_volume_003.New Thickness
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[10],
        cut_disk_custom_layer_1.nodes["Plate Volume.003"].inputs[4]
    )
    # group_input.Stem Depth -> group_006.Stem Depth
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[11],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[6]
    )
    # group_input.Wire Intersect Offset -> group_006.Stem Offset
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[12],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[7]
    )
    # reroute_003.Output -> group_006.Material
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute.003"].outputs[0],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[3]
    )
    # mesh_boolean_006.Mesh -> menu_switch.Stems
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Mesh Boolean.006"].outputs[0],
        cut_disk_custom_layer_1.nodes["Menu Switch"].inputs[1]
    )
    # menu_switch.Output -> join_geometry.Geometry
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Menu Switch"].outputs[0],
        cut_disk_custom_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Stem Menu -> menu_switch.Menu
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[2],
        cut_disk_custom_layer_1.nodes["Menu Switch"].inputs[0]
    )
    # mesh_boolean_005.Mesh -> viewer.Mesh
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].outputs[0],
        cut_disk_custom_layer_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Base Radii -> group_006.Base Radii
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[3],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[8]
    )
    # group_input.Sensor Shape -> group_006.Sensor Shape
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[4],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[9]
    )
    # reroute_002.Output -> group_output.Stem Points
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute.002"].outputs[0],
        cut_disk_custom_layer_1.nodes["Group Output"].inputs[2]
    )
    # group_006.Stem Points -> reroute_002.Input
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group.006"].outputs[2],
        cut_disk_custom_layer_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input.Material -> reroute_003.Input
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[13],
        cut_disk_custom_layer_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_003.Output -> plate_volume_002.Top Material
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute.003"].outputs[0],
        cut_disk_custom_layer_1.nodes["Plate Volume.002"].inputs[5]
    )
    # reroute_003.Output -> plate_volume_003.Top Material
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute.003"].outputs[0],
        cut_disk_custom_layer_1.nodes["Plate Volume.003"].inputs[5]
    )
    # reroute.Output -> group_006.Bottom Plate
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Reroute"].outputs[0],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[1]
    )
    # group_input.Center Cut -> group_006.Center Cut
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group Input"].outputs[5],
        cut_disk_custom_layer_1.nodes["Group.006"].inputs[10]
    )
    # mesh_boolean_005.Mesh -> group_output.Sensor Geometry
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].outputs[0],
        cut_disk_custom_layer_1.nodes["Group Output"].inputs[1]
    )
    # plate_volume_002.Geometry -> mesh_boolean_005.Mesh
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Plate Volume.002"].outputs[0],
        cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].inputs[1]
    )
    # group_006.Uncut Stems -> mesh_boolean_006.Mesh
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Group.006"].outputs[1],
        cut_disk_custom_layer_1.nodes["Mesh Boolean.006"].inputs[1]
    )
    # mesh_boolean_005.Mesh -> join_geometry.Geometry
    cut_disk_custom_layer_1.links.new(
        cut_disk_custom_layer_1.nodes["Mesh Boolean.005"].outputs[0],
        cut_disk_custom_layer_1.nodes["Join Geometry"].inputs[0]
    )
    stem_menu_socket.default_value = 'Stems'
    sensor_shape_socket.default_value = 'Cylinder'
    viewer.viewer_items[0].auto_remove = True

    return cut_disk_custom_layer_1


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


def redistributed_points_within_geometry_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Redistributed Points Within Geometry node group"""
    redistributed_points_within_geometry_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Redistributed Points Within Geometry")

    redistributed_points_within_geometry_1.color_tag = 'NONE'
    redistributed_points_within_geometry_1.description = ""
    redistributed_points_within_geometry_1.default_group_node_width = 140
    redistributed_points_within_geometry_1.show_modifier_manage_panel = True

    # redistributed_points_within_geometry_1 interface

    # Socket Points
    points_socket = redistributed_points_within_geometry_1.interface.new_socket(name="Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Socket Mesh
    mesh_socket = redistributed_points_within_geometry_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    mesh_socket.description = "Mesh to convert the inner volume to a fog volume geometry"
    mesh_socket.default_input = 'VALUE'
    mesh_socket.structure_type = 'AUTO'

    # Socket Volume Density
    volume_density_socket = redistributed_points_within_geometry_1.interface.new_socket(name="Volume Density", in_out='INPUT', socket_type='NodeSocketFloat')
    volume_density_socket.default_value = 10000.0
    volume_density_socket.min_value = 0.009999999776482582
    volume_density_socket.max_value = 3.4028234663852886e+38
    volume_density_socket.subtype = 'NONE'
    volume_density_socket.attribute_domain = 'POINT'
    volume_density_socket.default_input = 'VALUE'
    volume_density_socket.structure_type = 'AUTO'

    # Socket Voxel Size
    voxel_size_socket = redistributed_points_within_geometry_1.interface.new_socket(name="Voxel Size", in_out='INPUT', socket_type='NodeSocketFloat')
    voxel_size_socket.default_value = 0.0010000000474974513
    voxel_size_socket.min_value = 0.009999999776482582
    voxel_size_socket.max_value = 3.4028234663852886e+38
    voxel_size_socket.subtype = 'DISTANCE'
    voxel_size_socket.attribute_domain = 'POINT'
    voxel_size_socket.default_input = 'VALUE'
    voxel_size_socket.structure_type = 'AUTO'

    # Socket Point Density
    point_density_socket = redistributed_points_within_geometry_1.interface.new_socket(name="Point Density", in_out='INPUT', socket_type='NodeSocketFloat')
    point_density_socket.default_value = 1000.0
    point_density_socket.min_value = 0.0
    point_density_socket.max_value = 100000.0
    point_density_socket.subtype = 'NONE'
    point_density_socket.attribute_domain = 'POINT'
    point_density_socket.description = "Number of points to sample per unit volume"
    point_density_socket.default_input = 'VALUE'
    point_density_socket.structure_type = 'AUTO'

    # Socket Point Random Seed
    point_random_seed_socket = redistributed_points_within_geometry_1.interface.new_socket(name="Point Random Seed", in_out='INPUT', socket_type='NodeSocketInt')
    point_random_seed_socket.default_value = 0
    point_random_seed_socket.min_value = -10000
    point_random_seed_socket.max_value = 10000
    point_random_seed_socket.subtype = 'NONE'
    point_random_seed_socket.attribute_domain = 'POINT'
    point_random_seed_socket.description = "Seed used by the random number generator to generate random points"
    point_random_seed_socket.default_input = 'VALUE'
    point_random_seed_socket.structure_type = 'AUTO'

    # Socket Name
    name_socket = redistributed_points_within_geometry_1.interface.new_socket(name="Name", in_out='INPUT', socket_type='NodeSocketString')
    name_socket.default_value = ""
    name_socket.subtype = 'NONE'
    name_socket.attribute_domain = 'POINT'
    name_socket.default_input = 'VALUE'
    name_socket.structure_type = 'AUTO'
    name_socket.optional_label = True

    # Socket Points
    points_socket_1 = redistributed_points_within_geometry_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry')
    points_socket_1.attribute_domain = 'POINT'
    points_socket_1.description = "Mesh or point cloud to find the nearest point on"
    points_socket_1.default_input = 'VALUE'
    points_socket_1.structure_type = 'AUTO'

    # Initialize redistributed_points_within_geometry_1 nodes

    # Node Group Output
    group_output = redistributed_points_within_geometry_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group Input
    group_input = redistributed_points_within_geometry_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Mesh to Volume
    mesh_to_volume = redistributed_points_within_geometry_1.nodes.new("GeometryNodeMeshToVolume")
    mesh_to_volume.name = "Mesh to Volume"
    mesh_to_volume.show_options = True
    # Resolution Mode
    mesh_to_volume.inputs[2].default_value = 'Size'
    # Voxel Amount
    mesh_to_volume.inputs[4].default_value = 64.0
    # Interior Band Width
    mesh_to_volume.inputs[5].default_value = 0.20000000298023224

    # Node Distribute Points in Volume
    distribute_points_in_volume = redistributed_points_within_geometry_1.nodes.new("GeometryNodeDistributePointsInVolume")
    distribute_points_in_volume.name = "Distribute Points in Volume"
    distribute_points_in_volume.show_options = True
    # Mode
    distribute_points_in_volume.inputs[1].default_value = 'Random'
    # Spacing
    distribute_points_in_volume.inputs[4].default_value = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)
    # Threshold
    distribute_points_in_volume.inputs[5].default_value = 0.10000000149011612

    # Node Viewer
    viewer = redistributed_points_within_geometry_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Volume")

    # Node Store Named Attribute.001
    store_named_attribute_001 = redistributed_points_within_geometry_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'POINT'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Value
    store_named_attribute_001.inputs[3].default_value = True

    # Node Sample Nearest
    sample_nearest = redistributed_points_within_geometry_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.show_options = True
    sample_nearest.domain = 'POINT'

    # Node Position
    position = redistributed_points_within_geometry_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Sample Index
    sample_index = redistributed_points_within_geometry_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Index
    index = redistributed_points_within_geometry_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Store Named Attribute
    store_named_attribute = redistributed_points_within_geometry_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'INT'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "sensor_idx"

    # Node Math
    math = redistributed_points_within_geometry_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'ADD'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # Node Points to Vertices
    points_to_vertices = redistributed_points_within_geometry_1.nodes.new("GeometryNodePointsToVertices")
    points_to_vertices.name = "Points to Vertices"
    points_to_vertices.show_options = True
    # Selection
    points_to_vertices.inputs[1].default_value = True

    # Set locations
    redistributed_points_within_geometry_1.nodes["Group Output"].location = (1080.0, -20.0)
    redistributed_points_within_geometry_1.nodes["Group Input"].location = (-780.0, -180.0)
    redistributed_points_within_geometry_1.nodes["Mesh to Volume"].location = (-375.0, 10.0)
    redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].location = (-120.0, -60.0)
    redistributed_points_within_geometry_1.nodes["Viewer"].location = (-8.666666984558105, 116.66666412353516)
    redistributed_points_within_geometry_1.nodes["Store Named Attribute.001"].location = (500.0, -20.0)
    redistributed_points_within_geometry_1.nodes["Sample Nearest"].location = (380.0, -240.0)
    redistributed_points_within_geometry_1.nodes["Position"].location = (-200.0, -480.0)
    redistributed_points_within_geometry_1.nodes["Sample Index"].location = (120.0, -400.0)
    redistributed_points_within_geometry_1.nodes["Index"].location = (-200.0, -560.0)
    redistributed_points_within_geometry_1.nodes["Store Named Attribute"].location = (740.0, -140.0)
    redistributed_points_within_geometry_1.nodes["Math"].location = (560.0, -240.0)
    redistributed_points_within_geometry_1.nodes["Points to Vertices"].location = (200.0, -40.0)

    # Set dimensions
    redistributed_points_within_geometry_1.nodes["Group Output"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Group Output"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Group Input"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Group Input"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Mesh to Volume"].width  = 200.0
    redistributed_points_within_geometry_1.nodes["Mesh to Volume"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].width  = 170.0
    redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Viewer"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Viewer"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Store Named Attribute.001"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Store Named Attribute.001"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Sample Nearest"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Sample Nearest"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Position"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Position"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Sample Index"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Sample Index"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Index"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Index"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Store Named Attribute"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Store Named Attribute"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Math"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Math"].height = 100.0

    redistributed_points_within_geometry_1.nodes["Points to Vertices"].width  = 140.0
    redistributed_points_within_geometry_1.nodes["Points to Vertices"].height = 100.0


    # Initialize redistributed_points_within_geometry_1 links

    # mesh_to_volume.Volume -> distribute_points_in_volume.Volume
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Mesh to Volume"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].inputs[0]
    )
    # group_input.Mesh -> mesh_to_volume.Mesh
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Group Input"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Mesh to Volume"].inputs[0]
    )
    # mesh_to_volume.Volume -> viewer.Volume
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Mesh to Volume"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Viewer"].inputs[0]
    )
    # group_input.Volume Density -> mesh_to_volume.Density
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Group Input"].outputs[1],
        redistributed_points_within_geometry_1.nodes["Mesh to Volume"].inputs[1]
    )
    # group_input.Voxel Size -> mesh_to_volume.Voxel Size
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Group Input"].outputs[2],
        redistributed_points_within_geometry_1.nodes["Mesh to Volume"].inputs[3]
    )
    # group_input.Point Random Seed -> distribute_points_in_volume.Seed
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Group Input"].outputs[4],
        redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].inputs[3]
    )
    # group_input.Point Density -> distribute_points_in_volume.Density
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Group Input"].outputs[3],
        redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].inputs[2]
    )
    # group_input.Name -> store_named_attribute_001.Name
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Group Input"].outputs[5],
        redistributed_points_within_geometry_1.nodes["Store Named Attribute.001"].inputs[2]
    )
    # group_input.Points -> sample_nearest.Geometry
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Group Input"].outputs[6],
        redistributed_points_within_geometry_1.nodes["Sample Nearest"].inputs[0]
    )
    # distribute_points_in_volume.Points -> sample_index.Geometry
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Sample Index"].inputs[0]
    )
    # position.Position -> sample_index.Value
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Position"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Sample Index"].inputs[1]
    )
    # index.Index -> sample_index.Index
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Index"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Sample Index"].inputs[2]
    )
    # sample_index.Value -> sample_nearest.Sample Position
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Sample Index"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Sample Nearest"].inputs[1]
    )
    # math.Value -> store_named_attribute.Value
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Math"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Store Named Attribute"].inputs[3]
    )
    # store_named_attribute_001.Geometry -> store_named_attribute.Geometry
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Store Named Attribute.001"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Store Named Attribute"].inputs[0]
    )
    # store_named_attribute.Geometry -> group_output.Points
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Store Named Attribute"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Group Output"].inputs[0]
    )
    # sample_nearest.Index -> math.Value
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Sample Nearest"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Math"].inputs[0]
    )
    # distribute_points_in_volume.Points -> points_to_vertices.Points
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Distribute Points in Volume"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Points to Vertices"].inputs[0]
    )
    # points_to_vertices.Mesh -> store_named_attribute_001.Geometry
    redistributed_points_within_geometry_1.links.new(
        redistributed_points_within_geometry_1.nodes["Points to Vertices"].outputs[0],
        redistributed_points_within_geometry_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    viewer.viewer_items[0].auto_remove = True

    return redistributed_points_within_geometry_1


def self_cap_layer_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Self-Cap Layer node group"""
    self_cap_layer_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Self-Cap Layer")

    self_cap_layer_1.color_tag = 'NONE'
    self_cap_layer_1.description = ""
    self_cap_layer_1.default_group_node_width = 140
    self_cap_layer_1.is_modifier = True
    self_cap_layer_1.show_modifier_manage_panel = True

    # self_cap_layer_1 interface

    # Socket Geometry
    geometry_socket = self_cap_layer_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Redistributed Points
    redistributed_points_socket = self_cap_layer_1.interface.new_socket(name="Redistributed Points", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    redistributed_points_socket.attribute_domain = 'POINT'
    redistributed_points_socket.default_input = 'VALUE'
    redistributed_points_socket.structure_type = 'AUTO'

    # Socket Sensor Geometry
    sensor_geometry_socket = self_cap_layer_1.interface.new_socket(name="Sensor Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    sensor_geometry_socket.attribute_domain = 'POINT'
    sensor_geometry_socket.default_input = 'VALUE'
    sensor_geometry_socket.structure_type = 'AUTO'

    # Socket Point Name
    point_name_socket = self_cap_layer_1.interface.new_socket(name="Point Name", in_out='OUTPUT', socket_type='NodeSocketString')
    point_name_socket.default_value = ""
    point_name_socket.subtype = 'NONE'
    point_name_socket.attribute_domain = 'POINT'
    point_name_socket.default_input = 'VALUE'
    point_name_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = self_cap_layer_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Isolate
    isolate_socket = self_cap_layer_1.interface.new_socket(name="Isolate", in_out='INPUT', socket_type='NodeSocketBool')
    isolate_socket.default_value = False
    isolate_socket.attribute_domain = 'POINT'
    isolate_socket.default_input = 'VALUE'
    isolate_socket.structure_type = 'AUTO'

    # Socket Sensor Shape
    sensor_shape_socket = self_cap_layer_1.interface.new_socket(name="Sensor Shape", in_out='INPUT', socket_type='NodeSocketMenu')
    sensor_shape_socket.attribute_domain = 'POINT'
    sensor_shape_socket.default_input = 'VALUE'
    sensor_shape_socket.structure_type = 'AUTO'
    sensor_shape_socket.optional_label = True

    # Socket Radius
    radius_socket = self_cap_layer_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    radius_socket.default_value = 0.4000000059604645
    radius_socket.min_value = 0.0
    radius_socket.max_value = 2.0
    radius_socket.subtype = 'FACTOR'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    # Socket Wire Intersect Offset
    wire_intersect_offset_socket = self_cap_layer_1.interface.new_socket(name="Wire Intersect Offset", in_out='INPUT', socket_type='NodeSocketFloat')
    wire_intersect_offset_socket.default_value = 0.0
    wire_intersect_offset_socket.min_value = -10000.0
    wire_intersect_offset_socket.max_value = 10000.0
    wire_intersect_offset_socket.subtype = 'NONE'
    wire_intersect_offset_socket.attribute_domain = 'POINT'
    wire_intersect_offset_socket.default_input = 'VALUE'
    wire_intersect_offset_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = self_cap_layer_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket.default_value = 128
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Panel Point Distribution
    point_distribution_panel = self_cap_layer_1.interface.new_panel("Point Distribution")
    # Socket Point distribution
    point_distribution_socket = self_cap_layer_1.interface.new_socket(name="Point distribution", in_out='INPUT', socket_type='NodeSocketMenu', parent = point_distribution_panel)
    point_distribution_socket.attribute_domain = 'POINT'
    point_distribution_socket.description = "Choose if the sensor points should be redistributed within the volume to preserve space and wiring length. Requires careful tuning, easy to crash computer"
    point_distribution_socket.default_input = 'VALUE'
    point_distribution_socket.structure_type = 'AUTO'
    point_distribution_socket.optional_label = True

    # Socket Isolate Points
    isolate_points_socket = self_cap_layer_1.interface.new_socket(name="Isolate Points", in_out='INPUT', socket_type='NodeSocketBool', parent = point_distribution_panel)
    isolate_points_socket.default_value = False
    isolate_points_socket.attribute_domain = 'POINT'
    isolate_points_socket.default_input = 'VALUE'
    isolate_points_socket.structure_type = 'AUTO'

    # Socket Point Name
    point_name_socket_1 = self_cap_layer_1.interface.new_socket(name="Point Name", in_out='INPUT', socket_type='NodeSocketString', parent = point_distribution_panel)
    point_name_socket_1.default_value = "redist_points"
    point_name_socket_1.subtype = 'NONE'
    point_name_socket_1.attribute_domain = 'POINT'
    point_name_socket_1.description = "Specific name of the points for the other layers to find"
    point_name_socket_1.default_input = 'VALUE'
    point_name_socket_1.structure_type = 'AUTO'

    # Socket Volume Density
    volume_density_socket = self_cap_layer_1.interface.new_socket(name="Volume Density", in_out='INPUT', socket_type='NodeSocketFloat', parent = point_distribution_panel)
    volume_density_socket.default_value = 10000.0
    volume_density_socket.min_value = 0.009999999776482582
    volume_density_socket.max_value = 3.4028234663852886e+38
    volume_density_socket.subtype = 'NONE'
    volume_density_socket.attribute_domain = 'POINT'
    volume_density_socket.default_input = 'VALUE'
    volume_density_socket.structure_type = 'AUTO'

    # Socket Voxel Size
    voxel_size_socket = self_cap_layer_1.interface.new_socket(name="Voxel Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = point_distribution_panel)
    voxel_size_socket.default_value = 0.0010000000474974513
    voxel_size_socket.min_value = 0.009999999776482582
    voxel_size_socket.max_value = 3.4028234663852886e+38
    voxel_size_socket.subtype = 'DISTANCE'
    voxel_size_socket.attribute_domain = 'POINT'
    voxel_size_socket.default_input = 'VALUE'
    voxel_size_socket.structure_type = 'AUTO'

    # Socket Point Density
    point_density_socket = self_cap_layer_1.interface.new_socket(name="Point Density", in_out='INPUT', socket_type='NodeSocketFloat', parent = point_distribution_panel)
    point_density_socket.default_value = 1000.0
    point_density_socket.min_value = 0.0
    point_density_socket.max_value = 100000.0
    point_density_socket.subtype = 'NONE'
    point_density_socket.attribute_domain = 'POINT'
    point_density_socket.description = "Number of points to sample per unit volume"
    point_density_socket.default_input = 'VALUE'
    point_density_socket.structure_type = 'AUTO'

    # Socket Point Random Seed
    point_random_seed_socket = self_cap_layer_1.interface.new_socket(name="Point Random Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = point_distribution_panel)
    point_random_seed_socket.default_value = 0
    point_random_seed_socket.min_value = -10000
    point_random_seed_socket.max_value = 10000
    point_random_seed_socket.subtype = 'NONE'
    point_random_seed_socket.attribute_domain = 'POINT'
    point_random_seed_socket.description = "Seed used by the random number generator to generate random points"
    point_random_seed_socket.default_input = 'VALUE'
    point_random_seed_socket.structure_type = 'AUTO'


    # Panel Node Shape
    node_shape_panel = self_cap_layer_1.interface.new_panel("Node Shape")
    # Socket Node Offset
    node_offset_socket = self_cap_layer_1.interface.new_socket(name="Node Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = node_shape_panel)
    node_offset_socket.default_value = 50.0
    node_offset_socket.min_value = 0.0
    node_offset_socket.max_value = 200.0
    node_offset_socket.subtype = 'PERCENTAGE'
    node_offset_socket.attribute_domain = 'POINT'
    node_offset_socket.default_input = 'VALUE'
    node_offset_socket.structure_type = 'AUTO'

    # Socket Node Thickness
    node_thickness_socket = self_cap_layer_1.interface.new_socket(name="Node Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = node_shape_panel)
    node_thickness_socket.default_value = 50.0
    node_thickness_socket.min_value = 0.0
    node_thickness_socket.max_value = 200.0
    node_thickness_socket.subtype = 'PERCENTAGE'
    node_thickness_socket.attribute_domain = 'POINT'
    node_thickness_socket.default_input = 'VALUE'
    node_thickness_socket.structure_type = 'AUTO'

    # Socket Node Depth
    node_depth_socket = self_cap_layer_1.interface.new_socket(name="Node Depth", in_out='INPUT', socket_type='NodeSocketFloat', parent = node_shape_panel)
    node_depth_socket.default_value = 1.0
    node_depth_socket.min_value = 0.0
    node_depth_socket.max_value = 3.4028234663852886e+38
    node_depth_socket.subtype = 'DISTANCE'
    node_depth_socket.attribute_domain = 'POINT'
    node_depth_socket.description = "The height of the cylinder"
    node_depth_socket.default_input = 'VALUE'
    node_depth_socket.structure_type = 'AUTO'

    # Socket Center Cut
    center_cut_socket = self_cap_layer_1.interface.new_socket(name="Center Cut", in_out='INPUT', socket_type='NodeSocketFloat', parent = node_shape_panel)
    center_cut_socket.default_value = 2.0
    center_cut_socket.min_value = 0.0
    center_cut_socket.max_value = 99.5
    center_cut_socket.subtype = 'PERCENTAGE'
    center_cut_socket.attribute_domain = 'POINT'
    center_cut_socket.description = "The percentage of the center radius removed"
    center_cut_socket.default_input = 'VALUE'
    center_cut_socket.structure_type = 'AUTO'


    # Panel Stem Shape
    stem_shape_panel = self_cap_layer_1.interface.new_panel("Stem Shape")
    # Socket Modifiers
    modifiers_socket = self_cap_layer_1.interface.new_socket(name="Modifiers", in_out='INPUT', socket_type='NodeSocketMenu', parent = stem_shape_panel)
    modifiers_socket.attribute_domain = 'POINT'
    modifiers_socket.default_input = 'VALUE'
    modifiers_socket.structure_type = 'AUTO'
    modifiers_socket.optional_label = True

    # Socket Stem Offset
    stem_offset_socket = self_cap_layer_1.interface.new_socket(name="Stem Offset", in_out='INPUT', socket_type='NodeSocketFloat', parent = stem_shape_panel)
    stem_offset_socket.default_value = 50.0
    stem_offset_socket.min_value = 0.0
    stem_offset_socket.max_value = 200.0
    stem_offset_socket.subtype = 'PERCENTAGE'
    stem_offset_socket.attribute_domain = 'POINT'
    stem_offset_socket.default_input = 'VALUE'
    stem_offset_socket.structure_type = 'AUTO'

    # Socket Stem Thickness
    stem_thickness_socket = self_cap_layer_1.interface.new_socket(name="Stem Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = stem_shape_panel)
    stem_thickness_socket.default_value = 50.0
    stem_thickness_socket.min_value = 0.0
    stem_thickness_socket.max_value = 200.0
    stem_thickness_socket.subtype = 'PERCENTAGE'
    stem_thickness_socket.attribute_domain = 'POINT'
    stem_thickness_socket.default_input = 'VALUE'
    stem_thickness_socket.structure_type = 'AUTO'

    # Socket Stem Depth
    stem_depth_socket = self_cap_layer_1.interface.new_socket(name="Stem Depth", in_out='INPUT', socket_type='NodeSocketFloat', parent = stem_shape_panel)
    stem_depth_socket.default_value = 1.0
    stem_depth_socket.min_value = 0.0
    stem_depth_socket.max_value = 3.4028234663852886e+38
    stem_depth_socket.subtype = 'DISTANCE'
    stem_depth_socket.attribute_domain = 'POINT'
    stem_depth_socket.description = "The height of the cylinder"
    stem_depth_socket.default_input = 'VALUE'
    stem_depth_socket.structure_type = 'AUTO'


    # Panel Customization
    customization_panel = self_cap_layer_1.interface.new_panel("Customization", default_closed=True)
    # Socket Material
    material_socket = self_cap_layer_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = customization_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'


    # Panel Options
    options_panel = self_cap_layer_1.interface.new_panel("Options", default_closed=True)
    # Socket Options
    options_socket = self_cap_layer_1.interface.new_socket(name="Options", in_out='INPUT', socket_type='NodeSocketMenu', parent = options_panel)
    options_socket.attribute_domain = 'POINT'
    options_socket.default_input = 'VALUE'
    options_socket.structure_type = 'AUTO'
    options_socket.optional_label = True

    # Socket Dermis
    dermis_socket = self_cap_layer_1.interface.new_socket(name="Dermis", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    dermis_socket.default_value = "dermis"
    dermis_socket.subtype = 'NONE'
    dermis_socket.attribute_domain = 'POINT'
    dermis_socket.default_input = 'VALUE'
    dermis_socket.structure_type = 'AUTO'

    # Socket Application Surface
    application_surface_socket = self_cap_layer_1.interface.new_socket(name="Application Surface", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    application_surface_socket.default_value = "dermis_top"
    application_surface_socket.subtype = 'NONE'
    application_surface_socket.attribute_domain = 'POINT'
    application_surface_socket.default_input = 'VALUE'
    application_surface_socket.structure_type = 'AUTO'

    # Socket Dermis Bottom
    dermis_bottom_socket = self_cap_layer_1.interface.new_socket(name="Dermis Bottom", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    dermis_bottom_socket.default_value = "dermis_bottom"
    dermis_bottom_socket.subtype = 'NONE'
    dermis_bottom_socket.attribute_domain = 'POINT'
    dermis_bottom_socket.default_input = 'VALUE'
    dermis_bottom_socket.structure_type = 'AUTO'

    # Socket Sensor Point Label
    sensor_point_label_socket = self_cap_layer_1.interface.new_socket(name="Sensor Point Label", in_out='INPUT', socket_type='NodeSocketString', parent = options_panel)
    sensor_point_label_socket.default_value = ""
    sensor_point_label_socket.subtype = 'NONE'
    sensor_point_label_socket.attribute_domain = 'POINT'
    sensor_point_label_socket.default_input = 'VALUE'
    sensor_point_label_socket.structure_type = 'AUTO'


    # Initialize self_cap_layer_1 nodes

    # Node Group Input
    group_input = self_cap_layer_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = self_cap_layer_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Group.005
    group_005 = self_cap_layer_1.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.show_options = True
    group_005.node_tree = bpy.data.node_groups[node_tree_names[cut_disk_custom_layer_1_node_group]]

    # Node Join Geometry
    join_geometry = self_cap_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Switch
    switch = self_cap_layer_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'GEOMETRY'

    # Node Menu Switch
    menu_switch = self_cap_layer_1.nodes.new("GeometryNodeMenuSwitch")
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

    # Node Switch.001
    switch_001 = self_cap_layer_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'STRING'
    # False
    switch_001.inputs[1].default_value = "dermis_top"

    # Node Reroute
    reroute = self_cap_layer_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Switch.002
    switch_002 = self_cap_layer_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.show_options = True
    switch_002.input_type = 'STRING'
    # False
    switch_002.inputs[1].default_value = "dermis_bottom"

    # Node Named Attribute.002
    named_attribute_002 = self_cap_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.show_options = True
    named_attribute_002.data_type = 'FLOAT'
    # Name
    named_attribute_002.inputs[0].default_value = "thickness"

    # Node Sample Index
    sample_index = self_cap_layer_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT'
    sample_index.domain = 'POINT'
    # Index
    sample_index.inputs[2].default_value = 0

    # Node Reroute.001
    reroute_001 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.002
    reroute_002 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.003
    reroute_003 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.004
    reroute_004 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketFloat"
    # Node Reroute.005
    reroute_005 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.006
    reroute_006 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.007
    reroute_007 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.008
    reroute_008 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.009
    reroute_009 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.010
    reroute_010 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.011
    reroute_011 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketFloatPercentage"
    # Node Reroute.012
    reroute_012 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.013
    reroute_013 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketFloatDistance"
    # Node Reroute.014
    reroute_014 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    reroute_014.socket_idname = "NodeSocketFloat"
    # Node Reroute.015
    reroute_015 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketGeometry"
    # Node Flip Faces
    flip_faces = self_cap_layer_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    flip_faces.show_options = True
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Store Named Attribute
    store_named_attribute = self_cap_layer_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "wiring_endpoint"
    # Value
    store_named_attribute.inputs[3].default_value = True

    # Node Separate and Remove Att
    separate_and_remove_att = self_cap_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att.name = "Separate and Remove Att"
    separate_and_remove_att.show_options = True
    separate_and_remove_att.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]

    # Node Separate and Remove Att.001
    separate_and_remove_att_001 = self_cap_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att_001.name = "Separate and Remove Att.001"
    separate_and_remove_att_001.show_options = True
    separate_and_remove_att_001.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]

    # Node Viewer
    viewer = self_cap_layer_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.active_index = 0
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    viewer.viewer_items.clear()
    viewer.viewer_items.new('GEOMETRY', "Selection")

    # Node Switch.003
    switch_003 = self_cap_layer_1.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.show_options = True
    switch_003.input_type = 'STRING'
    # False
    switch_003.inputs[1].default_value = "dermis"

    # Node Reroute.016
    reroute_016 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    reroute_016.socket_idname = "NodeSocketGeometry"
    # Node Switch.005
    switch_005 = self_cap_layer_1.nodes.new("GeometryNodeSwitch")
    switch_005.name = "Switch.005"
    switch_005.show_options = True
    switch_005.input_type = 'STRING'
    # False
    switch_005.inputs[1].default_value = "sensor_point"

    # Node Sample Index.001
    sample_index_001 = self_cap_layer_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'

    # Node Named Attribute
    named_attribute = self_cap_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'FLOAT_VECTOR'
    # Name
    named_attribute.inputs[0].default_value = "eulers"

    # Node Index.001
    index_001 = self_cap_layer_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Sample Index.002
    sample_index_002 = self_cap_layer_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT'
    sample_index_002.domain = 'POINT'

    # Node Named Attribute.001
    named_attribute_001 = self_cap_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'FLOAT'
    # Name
    named_attribute_001.inputs[0].default_value = "radii"

    # Node Math
    math = self_cap_layer_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Group
    group = self_cap_layer_1.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.show_options = True
    group.node_tree = bpy.data.node_groups[node_tree_names[redistributed_points_within_geometry_1_node_group]]

    # Node Menu Switch.001
    menu_switch_001 = self_cap_layer_1.nodes.new("GeometryNodeMenuSwitch")
    menu_switch_001.name = "Menu Switch.001"
    menu_switch_001.show_options = True
    menu_switch_001.active_index = 1
    menu_switch_001.data_type = 'GEOMETRY'
    menu_switch_001.enum_items.clear()
    menu_switch_001.enum_items.new("Redistribute Points")
    menu_switch_001.enum_items[0].description = ""
    menu_switch_001.enum_items.new("Keep Points")
    menu_switch_001.enum_items[1].description = ""

    # Node Separate Bundle
    separate_bundle = self_cap_layer_1.nodes.new("NodeSeparateBundle")
    separate_bundle.name = "Separate Bundle"
    separate_bundle.show_options = True
    separate_bundle.active_index = 5
    separate_bundle.bundle_items.clear()
    separate_bundle.bundle_items.new('FLOAT', "Volume Density")
    separate_bundle.bundle_items[0].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Voxel Size")
    separate_bundle.bundle_items[1].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('FLOAT', "Point Density")
    separate_bundle.bundle_items[2].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('INT', "Point Random Seed")
    separate_bundle.bundle_items[3].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('BOOLEAN', "Isolate Points")
    separate_bundle.bundle_items[4].structure_type = 'AUTO'
    separate_bundle.bundle_items.new('STRING', "Point Name")
    separate_bundle.bundle_items[5].structure_type = 'AUTO'
    separate_bundle.define_signature = False

    # Node Reroute.017
    reroute_017 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.show_options = True
    reroute_017.socket_idname = "NodeSocketBundle"
    # Node Combine Bundle
    combine_bundle = self_cap_layer_1.nodes.new("NodeCombineBundle")
    combine_bundle.name = "Combine Bundle"
    combine_bundle.show_options = True
    combine_bundle.active_index = 5
    combine_bundle.bundle_items.clear()
    combine_bundle.bundle_items.new('FLOAT', "Volume Density")
    combine_bundle.bundle_items[0].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('FLOAT', "Voxel Size")
    combine_bundle.bundle_items[1].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('FLOAT', "Point Density")
    combine_bundle.bundle_items[2].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('INT', "Point Random Seed")
    combine_bundle.bundle_items[3].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('BOOLEAN', "Isolate Points")
    combine_bundle.bundle_items[4].structure_type = 'AUTO'
    combine_bundle.bundle_items.new('STRING', "Point Name")
    combine_bundle.bundle_items[5].structure_type = 'AUTO'
    combine_bundle.define_signature = False

    # Node Reroute.018
    reroute_018 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    reroute_018.socket_idname = "NodeSocketGeometry"
    # Node Reroute.019
    reroute_019 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    reroute_019.socket_idname = "NodeSocketGeometry"
    # Node Reroute.020
    reroute_020 = self_cap_layer_1.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.show_options = True
    reroute_020.socket_idname = "NodeSocketGeometry"
    # Node Named Attribute.003
    named_attribute_003 = self_cap_layer_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.show_options = True
    named_attribute_003.data_type = 'INT'
    # Name
    named_attribute_003.inputs[0].default_value = "sensor_idx"

    # Node Join Geometry.001
    join_geometry_001 = self_cap_layer_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Switch.004
    switch_004 = self_cap_layer_1.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.show_options = True
    switch_004.input_type = 'STRING'
    # False
    switch_004.inputs[1].default_value = "wiring_endpoint"

    # Node Separate and Remove Att.002
    separate_and_remove_att_002 = self_cap_layer_1.nodes.new("GeometryNodeGroup")
    separate_and_remove_att_002.name = "Separate and Remove Att.002"
    separate_and_remove_att_002.show_options = True
    separate_and_remove_att_002.node_tree = bpy.data.node_groups[node_tree_names[separate_and_remove_att_1_node_group]]
    # Socket_6
    separate_and_remove_att_002.inputs[2].default_value = ""
    # Socket_7
    separate_and_remove_att_002.inputs[3].default_value = ""

    # Set locations
    self_cap_layer_1.nodes["Group Input"].location = (-1760.0, 20.0)
    self_cap_layer_1.nodes["Group Output"].location = (2780.0, 20.0)
    self_cap_layer_1.nodes["Group.005"].location = (210.0, 300.0)
    self_cap_layer_1.nodes["Join Geometry"].location = (2300.0, -40.0)
    self_cap_layer_1.nodes["Switch"].location = (380.0, -480.0)
    self_cap_layer_1.nodes["Menu Switch"].location = (-1549.9998779296875, 626.8682250976562)
    self_cap_layer_1.nodes["Switch.001"].location = (-1229.9998779296875, 725.4033813476562)
    self_cap_layer_1.nodes["Reroute"].location = (-950.0, 560.0)
    self_cap_layer_1.nodes["Switch.002"].location = (-1229.9998779296875, 520.0)
    self_cap_layer_1.nodes["Named Attribute.002"].location = (-329.9999694824219, -320.0)
    self_cap_layer_1.nodes["Sample Index"].location = (-89.99999237060547, -160.0)
    self_cap_layer_1.nodes["Reroute.001"].location = (70.00000762939453, -820.0)
    self_cap_layer_1.nodes["Reroute.002"].location = (70.00000762939453, -780.0)
    self_cap_layer_1.nodes["Reroute.003"].location = (70.00000762939453, -760.0)
    self_cap_layer_1.nodes["Reroute.004"].location = (70.00000762939453, -860.0)
    self_cap_layer_1.nodes["Reroute.005"].location = (70.00000762939453, -740.0)
    self_cap_layer_1.nodes["Reroute.006"].location = (70.00000762939453, -840.0)
    self_cap_layer_1.nodes["Reroute.007"].location = (70.00000762939453, -800.0)
    self_cap_layer_1.nodes["Reroute.008"].location = (-1469.9998779296875, -840.0)
    self_cap_layer_1.nodes["Reroute.009"].location = (-1469.9998779296875, -780.0)
    self_cap_layer_1.nodes["Reroute.010"].location = (-1469.9998779296875, -820.0)
    self_cap_layer_1.nodes["Reroute.011"].location = (-1469.9998779296875, -760.0)
    self_cap_layer_1.nodes["Reroute.012"].location = (-1469.9998779296875, -800.0)
    self_cap_layer_1.nodes["Reroute.013"].location = (-1469.9998779296875, -860.0)
    self_cap_layer_1.nodes["Reroute.014"].location = (-1469.9998779296875, -880.0)
    self_cap_layer_1.nodes["Reroute.015"].location = (-69.99999237060547, -100.0)
    self_cap_layer_1.nodes["Flip Faces"].location = (-89.99999237060547, -60.0)
    self_cap_layer_1.nodes["Store Named Attribute"].location = (560.0, 0.0)
    self_cap_layer_1.nodes["Separate and Remove Att"].location = (-640.0, 760.0)
    self_cap_layer_1.nodes["Separate and Remove Att.001"].location = (-830.0, 540.0)
    self_cap_layer_1.nodes["Viewer"].location = (1440.0, 520.0)
    self_cap_layer_1.nodes["Switch.003"].location = (-1229.9998779296875, 320.0)
    self_cap_layer_1.nodes["Reroute.016"].location = (-148.1590576171875, -76.98004150390625)
    self_cap_layer_1.nodes["Switch.005"].location = (-1240.0, 140.0)
    self_cap_layer_1.nodes["Sample Index.001"].location = (-369.9999694824219, 140.0)
    self_cap_layer_1.nodes["Named Attribute"].location = (-600.0, 40.0)
    self_cap_layer_1.nodes["Index.001"].location = (-550.0, 160.0)
    self_cap_layer_1.nodes["Sample Index.002"].location = (-349.9999694824219, 480.0)
    self_cap_layer_1.nodes["Named Attribute.001"].location = (-650.0, 360.0)
    self_cap_layer_1.nodes["Math"].location = (-89.99999237060547, 440.0)
    self_cap_layer_1.nodes["Group"].location = (1400.0001220703125, 400.0)
    self_cap_layer_1.nodes["Menu Switch.001"].location = (1940.0, 180.0)
    self_cap_layer_1.nodes["Separate Bundle"].location = (1160.0001220703125, 280.0)
    self_cap_layer_1.nodes["Reroute.017"].location = (860.0, -660.0)
    self_cap_layer_1.nodes["Combine Bundle"].location = (-1439.9998779296875, -580.0)
    self_cap_layer_1.nodes["Reroute.018"].location = (67.1259765625, 182.3778533935547)
    self_cap_layer_1.nodes["Reroute.019"].location = (1320.0, 380.0)
    self_cap_layer_1.nodes["Reroute.020"].location = (200.0, 360.0)
    self_cap_layer_1.nodes["Named Attribute.003"].location = (1940.0, 320.0)
    self_cap_layer_1.nodes["Join Geometry.001"].location = (2300.0, -140.0)
    self_cap_layer_1.nodes["Switch.004"].location = (2500.0, 220.0)
    self_cap_layer_1.nodes["Separate and Remove Att.002"].location = (-859.9999389648438, 280.0)

    # Set dimensions
    self_cap_layer_1.nodes["Group Input"].width  = 140.0
    self_cap_layer_1.nodes["Group Input"].height = 100.0

    self_cap_layer_1.nodes["Group Output"].width  = 140.0
    self_cap_layer_1.nodes["Group Output"].height = 100.0

    self_cap_layer_1.nodes["Group.005"].width  = 200.0
    self_cap_layer_1.nodes["Group.005"].height = 100.0

    self_cap_layer_1.nodes["Join Geometry"].width  = 140.0
    self_cap_layer_1.nodes["Join Geometry"].height = 100.0

    self_cap_layer_1.nodes["Switch"].width  = 140.0
    self_cap_layer_1.nodes["Switch"].height = 100.0

    self_cap_layer_1.nodes["Menu Switch"].width  = 140.0
    self_cap_layer_1.nodes["Menu Switch"].height = 100.0

    self_cap_layer_1.nodes["Switch.001"].width  = 180.0
    self_cap_layer_1.nodes["Switch.001"].height = 100.0

    self_cap_layer_1.nodes["Reroute"].width  = 12.5
    self_cap_layer_1.nodes["Reroute"].height = 100.0

    self_cap_layer_1.nodes["Switch.002"].width  = 180.0
    self_cap_layer_1.nodes["Switch.002"].height = 100.0

    self_cap_layer_1.nodes["Named Attribute.002"].width  = 140.0
    self_cap_layer_1.nodes["Named Attribute.002"].height = 100.0

    self_cap_layer_1.nodes["Sample Index"].width  = 140.0
    self_cap_layer_1.nodes["Sample Index"].height = 100.0

    self_cap_layer_1.nodes["Reroute.001"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.001"].height = 100.0

    self_cap_layer_1.nodes["Reroute.002"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.002"].height = 100.0

    self_cap_layer_1.nodes["Reroute.003"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.003"].height = 100.0

    self_cap_layer_1.nodes["Reroute.004"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.004"].height = 100.0

    self_cap_layer_1.nodes["Reroute.005"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.005"].height = 100.0

    self_cap_layer_1.nodes["Reroute.006"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.006"].height = 100.0

    self_cap_layer_1.nodes["Reroute.007"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.007"].height = 100.0

    self_cap_layer_1.nodes["Reroute.008"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.008"].height = 100.0

    self_cap_layer_1.nodes["Reroute.009"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.009"].height = 100.0

    self_cap_layer_1.nodes["Reroute.010"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.010"].height = 100.0

    self_cap_layer_1.nodes["Reroute.011"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.011"].height = 100.0

    self_cap_layer_1.nodes["Reroute.012"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.012"].height = 100.0

    self_cap_layer_1.nodes["Reroute.013"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.013"].height = 100.0

    self_cap_layer_1.nodes["Reroute.014"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.014"].height = 100.0

    self_cap_layer_1.nodes["Reroute.015"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.015"].height = 100.0

    self_cap_layer_1.nodes["Flip Faces"].width  = 140.0
    self_cap_layer_1.nodes["Flip Faces"].height = 100.0

    self_cap_layer_1.nodes["Store Named Attribute"].width  = 140.0
    self_cap_layer_1.nodes["Store Named Attribute"].height = 100.0

    self_cap_layer_1.nodes["Separate and Remove Att"].width  = 140.0
    self_cap_layer_1.nodes["Separate and Remove Att"].height = 100.0

    self_cap_layer_1.nodes["Separate and Remove Att.001"].width  = 140.0
    self_cap_layer_1.nodes["Separate and Remove Att.001"].height = 100.0

    self_cap_layer_1.nodes["Viewer"].width  = 140.0
    self_cap_layer_1.nodes["Viewer"].height = 100.0

    self_cap_layer_1.nodes["Switch.003"].width  = 180.0
    self_cap_layer_1.nodes["Switch.003"].height = 100.0

    self_cap_layer_1.nodes["Reroute.016"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.016"].height = 100.0

    self_cap_layer_1.nodes["Switch.005"].width  = 180.0
    self_cap_layer_1.nodes["Switch.005"].height = 100.0

    self_cap_layer_1.nodes["Sample Index.001"].width  = 140.0
    self_cap_layer_1.nodes["Sample Index.001"].height = 100.0

    self_cap_layer_1.nodes["Named Attribute"].width  = 140.0
    self_cap_layer_1.nodes["Named Attribute"].height = 100.0

    self_cap_layer_1.nodes["Index.001"].width  = 140.0
    self_cap_layer_1.nodes["Index.001"].height = 100.0

    self_cap_layer_1.nodes["Sample Index.002"].width  = 140.0
    self_cap_layer_1.nodes["Sample Index.002"].height = 100.0

    self_cap_layer_1.nodes["Named Attribute.001"].width  = 140.0
    self_cap_layer_1.nodes["Named Attribute.001"].height = 100.0

    self_cap_layer_1.nodes["Math"].width  = 140.0
    self_cap_layer_1.nodes["Math"].height = 100.0

    self_cap_layer_1.nodes["Group"].width  = 320.0
    self_cap_layer_1.nodes["Group"].height = 100.0

    self_cap_layer_1.nodes["Menu Switch.001"].width  = 140.0
    self_cap_layer_1.nodes["Menu Switch.001"].height = 100.0

    self_cap_layer_1.nodes["Separate Bundle"].width  = 140.0
    self_cap_layer_1.nodes["Separate Bundle"].height = 100.0

    self_cap_layer_1.nodes["Reroute.017"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.017"].height = 100.0

    self_cap_layer_1.nodes["Combine Bundle"].width  = 140.0
    self_cap_layer_1.nodes["Combine Bundle"].height = 100.0

    self_cap_layer_1.nodes["Reroute.018"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.018"].height = 100.0

    self_cap_layer_1.nodes["Reroute.019"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.019"].height = 100.0

    self_cap_layer_1.nodes["Reroute.020"].width  = 12.5
    self_cap_layer_1.nodes["Reroute.020"].height = 100.0

    self_cap_layer_1.nodes["Named Attribute.003"].width  = 140.0
    self_cap_layer_1.nodes["Named Attribute.003"].height = 100.0

    self_cap_layer_1.nodes["Join Geometry.001"].width  = 140.0
    self_cap_layer_1.nodes["Join Geometry.001"].height = 100.0

    self_cap_layer_1.nodes["Switch.004"].width  = 140.0
    self_cap_layer_1.nodes["Switch.004"].height = 100.0

    self_cap_layer_1.nodes["Separate and Remove Att.002"].width  = 140.0
    self_cap_layer_1.nodes["Separate and Remove Att.002"].height = 100.0


    # Initialize self_cap_layer_1 links

    # group_input.Isolate -> switch.Switch
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[1],
        self_cap_layer_1.nodes["Switch"].inputs[0]
    )
    # group_input.Geometry -> switch.False
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[0],
        self_cap_layer_1.nodes["Switch"].inputs[1]
    )
    # switch.Output -> join_geometry.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch"].outputs[0],
        self_cap_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Options -> menu_switch.Menu
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[22],
        self_cap_layer_1.nodes["Menu Switch"].inputs[0]
    )
    # menu_switch.Output -> switch_001.Switch
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Menu Switch"].outputs[0],
        self_cap_layer_1.nodes["Switch.001"].inputs[0]
    )
    # group_input.Application Surface -> switch_001.True
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[24],
        self_cap_layer_1.nodes["Switch.001"].inputs[2]
    )
    # group_input.Modifiers -> group_005.Stem Menu
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[17],
        self_cap_layer_1.nodes["Group.005"].inputs[2]
    )
    # group_input.Geometry -> reroute.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[0],
        self_cap_layer_1.nodes["Reroute"].inputs[0]
    )
    # group_input.Dermis Bottom -> switch_002.True
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[25],
        self_cap_layer_1.nodes["Switch.002"].inputs[2]
    )
    # menu_switch.Output -> switch_002.Switch
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Menu Switch"].outputs[0],
        self_cap_layer_1.nodes["Switch.002"].inputs[0]
    )
    # sample_index.Value -> group_005.Reference Thickness
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Sample Index"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[15]
    )
    # reroute_005.Output -> group_005.Node Offset
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.005"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[6]
    )
    # reroute_003.Output -> group_005.Node Thickness
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.003"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[7]
    )
    # reroute_002.Output -> group_005.Node Depth
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.002"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[8]
    )
    # reroute_007.Output -> group_005.Stem Offset
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.007"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[9]
    )
    # reroute_001.Output -> group_005.Stem Thickness
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.001"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[10]
    )
    # reroute_006.Output -> group_005.Stem Depth
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.006"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[11]
    )
    # reroute_004.Output -> group_005.Wire Intersect Offset
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.004"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[12]
    )
    # reroute_008.Output -> reroute_001.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.008"].outputs[0],
        self_cap_layer_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_012.Output -> reroute_002.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.012"].outputs[0],
        self_cap_layer_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_009.Output -> reroute_003.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.009"].outputs[0],
        self_cap_layer_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_014.Output -> reroute_004.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.014"].outputs[0],
        self_cap_layer_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_011.Output -> reroute_005.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.011"].outputs[0],
        self_cap_layer_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_013.Output -> reroute_006.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.013"].outputs[0],
        self_cap_layer_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_010.Output -> reroute_007.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.010"].outputs[0],
        self_cap_layer_1.nodes["Reroute.007"].inputs[0]
    )
    # group_input.Stem Thickness -> reroute_008.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[19],
        self_cap_layer_1.nodes["Reroute.008"].inputs[0]
    )
    # group_input.Node Thickness -> reroute_009.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[14],
        self_cap_layer_1.nodes["Reroute.009"].inputs[0]
    )
    # group_input.Stem Offset -> reroute_010.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[18],
        self_cap_layer_1.nodes["Reroute.010"].inputs[0]
    )
    # group_input.Node Offset -> reroute_011.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[13],
        self_cap_layer_1.nodes["Reroute.011"].inputs[0]
    )
    # group_input.Node Depth -> reroute_012.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[15],
        self_cap_layer_1.nodes["Reroute.012"].inputs[0]
    )
    # group_input.Stem Depth -> reroute_013.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[20],
        self_cap_layer_1.nodes["Reroute.013"].inputs[0]
    )
    # group_input.Wire Intersect Offset -> reroute_014.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[4],
        self_cap_layer_1.nodes["Reroute.014"].inputs[0]
    )
    # flip_faces.Mesh -> group_005.Bottom Plate
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Flip Faces"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[14]
    )
    # reroute_016.Output -> reroute_015.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.016"].outputs[0],
        self_cap_layer_1.nodes["Reroute.015"].inputs[0]
    )
    # named_attribute_002.Attribute -> sample_index.Value
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Named Attribute.002"].outputs[0],
        self_cap_layer_1.nodes["Sample Index"].inputs[1]
    )
    # reroute_015.Output -> flip_faces.Mesh
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.015"].outputs[0],
        self_cap_layer_1.nodes["Flip Faces"].inputs[0]
    )
    # group_input.Sensor Shape -> group_005.Sensor Shape
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[2],
        self_cap_layer_1.nodes["Group.005"].inputs[4]
    )
    # group_005.Stem Points -> store_named_attribute.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group.005"].outputs[2],
        self_cap_layer_1.nodes["Store Named Attribute"].inputs[0]
    )
    # reroute.Output -> separate_and_remove_att.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att"].inputs[0]
    )
    # switch_001.Output -> separate_and_remove_att.Attribute
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.001"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att"].inputs[1]
    )
    # switch_002.Output -> separate_and_remove_att_001.Attribute
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.002"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att.001"].inputs[1]
    )
    # reroute.Output -> separate_and_remove_att_001.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att.001"].inputs[0]
    )
    # menu_switch.Output -> switch_003.Switch
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Menu Switch"].outputs[0],
        self_cap_layer_1.nodes["Switch.003"].inputs[0]
    )
    # group_input.Dermis -> switch_003.True
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[23],
        self_cap_layer_1.nodes["Switch.003"].inputs[2]
    )
    # switch_002.Output -> separate_and_remove_att.Additional Remove
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.002"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att"].inputs[2]
    )
    # switch_003.Output -> separate_and_remove_att.Additional Remove
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.003"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att"].inputs[3]
    )
    # switch_001.Output -> separate_and_remove_att_001.Additional Remove
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.001"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att.001"].inputs[2]
    )
    # switch_003.Output -> separate_and_remove_att_001.Additional Remove
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.003"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att.001"].inputs[3]
    )
    # separate_and_remove_att_001.Selection -> reroute_016.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate and Remove Att.001"].outputs[0],
        self_cap_layer_1.nodes["Reroute.016"].inputs[0]
    )
    # reroute_016.Output -> sample_index.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.016"].outputs[0],
        self_cap_layer_1.nodes["Sample Index"].inputs[0]
    )
    # group_input.Material -> group_005.Material
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[21],
        self_cap_layer_1.nodes["Group.005"].inputs[13]
    )
    # named_attribute.Attribute -> sample_index_001.Value
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Named Attribute"].outputs[0],
        self_cap_layer_1.nodes["Sample Index.001"].inputs[1]
    )
    # index_001.Index -> sample_index_001.Index
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Index.001"].outputs[0],
        self_cap_layer_1.nodes["Sample Index.001"].inputs[2]
    )
    # reroute_018.Output -> group_005.Points
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.018"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[0]
    )
    # sample_index_001.Value -> group_005.Euler
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Sample Index.001"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[1]
    )
    # menu_switch.Output -> switch_005.Switch
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Menu Switch"].outputs[0],
        self_cap_layer_1.nodes["Switch.005"].inputs[0]
    )
    # group_input.Sensor Point Label -> switch_005.True
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[26],
        self_cap_layer_1.nodes["Switch.005"].inputs[2]
    )
    # index_001.Index -> sample_index_002.Index
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Index.001"].outputs[0],
        self_cap_layer_1.nodes["Sample Index.002"].inputs[2]
    )
    # named_attribute_001.Attribute -> sample_index_002.Value
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Named Attribute.001"].outputs[0],
        self_cap_layer_1.nodes["Sample Index.002"].inputs[1]
    )
    # math.Value -> group_005.Base Radii
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Math"].outputs[0],
        self_cap_layer_1.nodes["Group.005"].inputs[3]
    )
    # sample_index_002.Value -> math.Value
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Sample Index.002"].outputs[0],
        self_cap_layer_1.nodes["Math"].inputs[0]
    )
    # group_input.Radius -> math.Value
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[3],
        self_cap_layer_1.nodes["Math"].inputs[1]
    )
    # group_input.Center Cut -> group_005.Center Cut
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[16],
        self_cap_layer_1.nodes["Group.005"].inputs[5]
    )
    # reroute_019.Output -> viewer.Selection
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.019"].outputs[0],
        self_cap_layer_1.nodes["Viewer"].inputs[0]
    )
    # group_005.Sensor Geometry -> group.Mesh
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group.005"].outputs[1],
        self_cap_layer_1.nodes["Group"].inputs[0]
    )
    # group_input.Point distribution -> menu_switch_001.Menu
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[6],
        self_cap_layer_1.nodes["Menu Switch.001"].inputs[0]
    )
    # reroute_017.Output -> separate_bundle.Bundle
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.017"].outputs[0],
        self_cap_layer_1.nodes["Separate Bundle"].inputs[0]
    )
    # group_input.Volume Density -> combine_bundle.Volume Density
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[9],
        self_cap_layer_1.nodes["Combine Bundle"].inputs[0]
    )
    # group_input.Voxel Size -> combine_bundle.Voxel Size
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[10],
        self_cap_layer_1.nodes["Combine Bundle"].inputs[1]
    )
    # group_input.Point Density -> combine_bundle.Point Density
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[11],
        self_cap_layer_1.nodes["Combine Bundle"].inputs[2]
    )
    # group_input.Point Random Seed -> combine_bundle.Point Random Seed
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[12],
        self_cap_layer_1.nodes["Combine Bundle"].inputs[3]
    )
    # combine_bundle.Bundle -> reroute_017.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Combine Bundle"].outputs[0],
        self_cap_layer_1.nodes["Reroute.017"].inputs[0]
    )
    # separate_bundle.Volume Density -> group.Volume Density
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate Bundle"].outputs[0],
        self_cap_layer_1.nodes["Group"].inputs[1]
    )
    # separate_bundle.Voxel Size -> group.Voxel Size
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate Bundle"].outputs[1],
        self_cap_layer_1.nodes["Group"].inputs[2]
    )
    # separate_bundle.Point Density -> group.Point Density
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate Bundle"].outputs[2],
        self_cap_layer_1.nodes["Group"].inputs[3]
    )
    # separate_bundle.Point Random Seed -> group.Point Random Seed
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate Bundle"].outputs[3],
        self_cap_layer_1.nodes["Group"].inputs[4]
    )
    # group_input.Isolate Points -> combine_bundle.Isolate Points
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[7],
        self_cap_layer_1.nodes["Combine Bundle"].inputs[4]
    )
    # group_input.Point Name -> combine_bundle.Point Name
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group Input"].outputs[8],
        self_cap_layer_1.nodes["Combine Bundle"].inputs[5]
    )
    # separate_bundle.Point Name -> group.Name
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate Bundle"].outputs[5],
        self_cap_layer_1.nodes["Group"].inputs[5]
    )
    # group.Points -> menu_switch_001.Redistribute Points
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group"].outputs[0],
        self_cap_layer_1.nodes["Menu Switch.001"].inputs[1]
    )
    # reroute_019.Output -> group.Points
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.019"].outputs[0],
        self_cap_layer_1.nodes["Group"].inputs[6]
    )
    # reroute_020.Output -> reroute_019.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.020"].outputs[0],
        self_cap_layer_1.nodes["Reroute.019"].inputs[0]
    )
    # reroute_018.Output -> reroute_020.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute.018"].outputs[0],
        self_cap_layer_1.nodes["Reroute.020"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Join Geometry"].outputs[0],
        self_cap_layer_1.nodes["Group Output"].inputs[0]
    )
    # menu_switch_001.Output -> group_output.Redistributed Points
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Menu Switch.001"].outputs[0],
        self_cap_layer_1.nodes["Group Output"].inputs[1]
    )
    # join_geometry_001.Geometry -> group_output.Sensor Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Join Geometry.001"].outputs[0],
        self_cap_layer_1.nodes["Group Output"].inputs[2]
    )
    # store_named_attribute.Geometry -> join_geometry_001.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Store Named Attribute"].outputs[0],
        self_cap_layer_1.nodes["Join Geometry.001"].inputs[0]
    )
    # menu_switch_001.Redistribute Points -> switch_004.Switch
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Menu Switch.001"].outputs[1],
        self_cap_layer_1.nodes["Switch.004"].inputs[0]
    )
    # separate_bundle.Point Name -> switch_004.True
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate Bundle"].outputs[5],
        self_cap_layer_1.nodes["Switch.004"].inputs[2]
    )
    # switch_004.Output -> group_output.Point Name
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.004"].outputs[0],
        self_cap_layer_1.nodes["Group Output"].inputs[3]
    )
    # switch_005.Output -> separate_and_remove_att_002.Attribute
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Switch.005"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att.002"].inputs[1]
    )
    # reroute.Output -> separate_and_remove_att_002.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Reroute"].outputs[0],
        self_cap_layer_1.nodes["Separate and Remove Att.002"].inputs[0]
    )
    # separate_and_remove_att_002.Selection -> sample_index_002.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate and Remove Att.002"].outputs[0],
        self_cap_layer_1.nodes["Sample Index.002"].inputs[0]
    )
    # separate_and_remove_att_002.Selection -> sample_index_001.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate and Remove Att.002"].outputs[0],
        self_cap_layer_1.nodes["Sample Index.001"].inputs[0]
    )
    # separate_and_remove_att_002.Selection -> reroute_018.Input
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Separate and Remove Att.002"].outputs[0],
        self_cap_layer_1.nodes["Reroute.018"].inputs[0]
    )
    # store_named_attribute.Geometry -> join_geometry.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Store Named Attribute"].outputs[0],
        self_cap_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # group_005.Geometry -> join_geometry_001.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group.005"].outputs[0],
        self_cap_layer_1.nodes["Join Geometry.001"].inputs[0]
    )
    # group_005.Geometry -> join_geometry.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Group.005"].outputs[0],
        self_cap_layer_1.nodes["Join Geometry"].inputs[0]
    )
    # menu_switch_001.Output -> join_geometry.Geometry
    self_cap_layer_1.links.new(
        self_cap_layer_1.nodes["Menu Switch.001"].outputs[0],
        self_cap_layer_1.nodes["Join Geometry"].inputs[0]
    )
    sensor_shape_socket.default_value = 'Cylinder'
    point_distribution_socket.default_value = 'Keep Points'
    modifiers_socket.default_value = 'Stems'
    options_socket.default_value = 'Default'
    viewer.viewer_items[0].auto_remove = True

    return self_cap_layer_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    cutout_thickness = cutout_thickness_1_node_group(node_tree_names)
    node_tree_names[cutout_thickness_1_node_group] = cutout_thickness.name

    plate_volume_reduced = plate_volume_reduced_1_node_group(node_tree_names)
    node_tree_names[plate_volume_reduced_1_node_group] = plate_volume_reduced.name

    sensor_instantiation = sensor_instantiation_1_node_group(node_tree_names)
    node_tree_names[sensor_instantiation_1_node_group] = sensor_instantiation.name

    cylinder_sensor_distribution = cylinder_sensor_distribution_1_node_group(node_tree_names)
    node_tree_names[cylinder_sensor_distribution_1_node_group] = cylinder_sensor_distribution.name

    sphere_sensor_distribution = sphere_sensor_distribution_1_node_group(node_tree_names)
    node_tree_names[sphere_sensor_distribution_1_node_group] = sphere_sensor_distribution.name

    voronoi_sensor_distribution = voronoi_sensor_distribution_1_node_group(node_tree_names)
    node_tree_names[voronoi_sensor_distribution_1_node_group] = voronoi_sensor_distribution.name

    ring_sensor_distribution = ring_sensor_distribution_1_node_group(node_tree_names)
    node_tree_names[ring_sensor_distribution_1_node_group] = ring_sensor_distribution.name

    shape_on_points = shape_on_points_1_node_group(node_tree_names)
    node_tree_names[shape_on_points_1_node_group] = shape_on_points.name

    cut_disk_custom_layer = cut_disk_custom_layer_1_node_group(node_tree_names)
    node_tree_names[cut_disk_custom_layer_1_node_group] = cut_disk_custom_layer.name

    separate_and_remove_att = separate_and_remove_att_1_node_group(node_tree_names)
    node_tree_names[separate_and_remove_att_1_node_group] = separate_and_remove_att.name

    redistributed_points_within_geometry = redistributed_points_within_geometry_1_node_group(node_tree_names)
    node_tree_names[redistributed_points_within_geometry_1_node_group] = redistributed_points_within_geometry.name

    self_cap_layer = self_cap_layer_1_node_group(node_tree_names)
    node_tree_names[self_cap_layer_1_node_group] = self_cap_layer.name

