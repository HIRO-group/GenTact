# Description: This script is used to save the electrode positions in the scene to a CSV file.
# The saves are intented for 3D printing with rigged self-capacitance nodes.

# Author: Carson Kohlbrenner
# Date: 6/20/2024

import bpy
import csv
import re
import os
import bpy.props
import numpy as np
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator

############################################################

class ExportERTOperator(Operator, ExportHelper):
    """Saves the electrodes in the scene"""
    bl_idname = "object.export_ert_operator"
    bl_label = "Export ERT"

    filename_ext = ""
    filter_glob: StringProperty(
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    def execute(self, context):
        self.unit_scale = context.scene.my_addon_properties.unit_scale
        print("ExportERTOperator.execute called\n")
        if self.filepath:  # Check if filepath has been set
            self.save_attributes(context, self.filepath)
        else:
            self.report({'WARNING'}, "No file selected")  # Report a warning if no file was selected
            return {'CANCELLED'}
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)  # Open file explorer
        return {'RUNNING_MODAL'}
    
    def save_attributes(self, context, folder_path, write=True, option=None):
        self.save_attribute_to_csv(context, folder_path, write, option)

    # This function saves the electrode positions to a CSV file
    def save_attribute_to_csv(self, context, folder_path, write=True, option=None):
        # Get the object
        obj = context.object

        # Create a folder at the folder_path to save all exported files 
        os.makedirs(folder_path, exist_ok=True)

        electrode_data = []
        electrode_attribute_name = "electrodes"

        if option is None:
            option = Params([],[], "Default") # Default options, do nothing

        # Check if the object has a geometry nodes modifier
        modifier = None
        for mod in obj.modifiers:
            if re.match(r'ERT(\.\d{3})?$', mod.name):
                modifier = mod
                break

        if modifier is not None:
            # Set the skin parameters as set by options
            for i in range(len(option.names)):
                modifier[option.names[i]] = option.values[i]

            # Update the scene to reflect changes
            bpy.context.view_layer.update()

        # Get the evaluated geometry
        obj.data.update()
        depsgraph = bpy.context.evaluated_depsgraph_get()
        depsgraph.update()
        eval_obj = obj.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()

        # Update the scene to reflect changes
        bpy.context.view_layer.update()

        # Check if the electrode attribute exists
        if electrode_attribute_name not in mesh.attributes:
            print(f"Attribute {electrode_attribute_name} not found in object {obj.name}.")
            print("Available attributes:")
            for attr_name in mesh.attributes.keys():
                print(f"  - {attr_name}")
            return

        # Get the electrode attribute data
        electrode_attribute_data = mesh.attributes[electrode_attribute_name].data
        
        # Extract electrode positions
        for i, electrode in enumerate(electrode_attribute_data):
            if hasattr(electrode, 'vector'):
                electrode_data.append(ElectrodeData(electrode.vector, i))
            elif hasattr(electrode, 'value') and electrode.value:
                # If it's a boolean attribute indicating electrode positions
                # Get position from mesh vertices
                if i < len(mesh.vertices):
                    electrode_data.append(ElectrodeData(mesh.vertices[i].co, i))

        # Check if there are any electrode positions
        if len(electrode_data) == 0:
            print("No electrode positions found.")
            return

        # Save the electrode data to CSV if write is true
        dir_path = os.path.dirname(folder_path) if os.path.isfile(folder_path) else folder_path
        if write:
            csv_filepath = os.path.join(dir_path, 'electrode_config.csv')
            with open(csv_filepath, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Index', 'X (mm)', 'Y (mm)', 'Z (mm)'])
                
                for electrode in electrode_data:
                    pos = electrode.pos
                    csv_writer.writerow([electrode.index, pos.x * self.unit_scale, pos.y * self.unit_scale, pos.z * self.unit_scale])
        
        print(f"Electrode count: {len(electrode_data)}")
        print(f"Electrode positions saved to {csv_filepath if write else 'CSV export skipped'}")

        # Save the electrode data to STL if write is true
        if write:
            self.full_save(context)

     # Saves the selected sensors as an STL file
    def export_object(self, context, file_path, option):

        ob = context.object

        mesh_path = file_path + "/" + option.save_name + ".stl"
        img_path = file_path + "/" + option.save_name + ".png"
        
        modifier = None
        for mod in ob.modifiers:
            if re.match(r'ERT(\.\d{3})?$', mod.name):
                modifier = mod
                break

        # Set the skin parameters as set by options
        for i in range(len(option.names)):
            modifier[option.names[i]] = option.values[i]

        # Ensure the object is in the active view layer
        if ob.name not in bpy.context.view_layer.objects:
            print(f"Object {ob.name} is not in the active view layer.")
            return

        # Ensure the object is not hidden
        if ob.hide_get():
            ob.hide_set(False)

        # Deselect and hide all objects from rendering
        bpy.ops.object.select_all(action='DESELECT')

        # Set the selected object to the active object
        ob.select_set(True)
        bpy.context.view_layer.objects.active = ob

        # Make only the sleected object visible to render
        ob.hide_render = False

        # Set the render output path
        bpy.context.scene.render.filepath = img_path
        
        # Render the scene and save as PNG
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.ops.render.render(write_still=True)

        #bpy.ops.export_mesh.stl(filepath=file_path, use_selection=True)
        bpy.ops.wm.stl_export(filepath=mesh_path, export_selected_objects=True, global_scale=self.unit_scale)

        ob.hide_render = True


    def full_save(self, context):
        # Saves three folders, a unified meshes folder, just the sensors folder, and just the skin folder
        folder_path = self.filepath
        os.makedirs(folder_path, exist_ok=True)

        #Jank solution to input socket naming that could potentially be improved
        # ["Show Original Mesh", "Show Epidermis", "Show Patches", "Show Dermis", "Show Phantom", "Show Electrodes", "Show Wires", "Show Routing"]
        sockets = ["Socket_9", "Socket_39", "Socket_57" "Socket_15", "Socket_14", "Socket_34", "Socket_36", "Socket_25"]

        # Epidermis Layer
        epidermis_params = Params(sockets, [False, True, False, False, False, False, False, False], "Epidermis - Flexible TPU")

        # Patches Layer
        patches_params = Params(sockets, [False, False, True, False, False, False, False, False], "Patches - Flexible Conductive TPU")

        # Phantom Layer
        phantom_params = Params(sockets, [False, False, False, False, True, False, True, False], "Phantom - Conductive PLA")

        # Dermis Layer
        dermis_params = Params(sockets, [False, False, False, True, False, False, False, False], "Dermis - Generic PLA")

        self.export_object(context, folder_path, option=epidermis_params)
        self.export_object(context, folder_path, option=patches_params)
        self.export_object(context, folder_path, option=phantom_params)
        self.export_object(context, folder_path, option=dermis_params)

        # Save copy of blend file to folder
        bpy.ops.wm.save_as_mainfile(filepath=folder_path + '/model.blend', copy=True)
        
    ############################################################
    ##################### Helper Functions #####################
    ############################################################

# This electrode data class is used to store information about each electrode
class ElectrodeData:
    def __init__(self, pos, index):
        self.pos = pos
        self.index = index

    def __str__(self):
        return f"Index: {self.index}, Pos: {self.pos}"

    def __repr__(self):
        return str(self)
    
class Params: # Class to store the parameters for the skin modifier
    def __init__(self, names, values, save_name):
        self.names = names
        self.values = values
        self.save_name = save_name


