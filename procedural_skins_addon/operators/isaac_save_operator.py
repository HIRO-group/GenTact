# Description: This script is used to save the sensor positions in the scene to a CSV file.
# The saves are intented for import in the Isaac Sim "Contact Extension" plugin.

# Author: Carson Kohlbrenner
# Date: 6/20/2024

import bpy
import csv
import re
import bpy.props
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty
from bpy.types import Operator

############################################################

class IsaacSaveOperator(Operator, ExportHelper):
    """Saves the sensors in the scene"""
    bl_idname = "object.isaac_save_operator"
    bl_label = "Isaac Save"

    filename_ext = ".csv"
    filter_glob: StringProperty(
        default="*.csv",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    def execute(self, context):
        print("IsaacSaveOperator.execute called\n")
        if self.filepath:  # Check if filepath has been set
            save_attribute_to_csv(context, self.filepath)
        else:
            self.report({'WARNING'}, "No file selected")  # Report a warning if no file was selected
            return {'CANCELLED'}
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)  # Open file explorer
        return {'RUNNING_MODAL'}
    
############################################################
##################### Helper Functions #####################
############################################################

class SensorData:
    def __init__(self, pos, normal, radius, parent, obj_name):
        self.pos = pos
        self.normal = normal
        self.radius = radius
        self.parent = parent
        self.obj_name = obj_name

    def __str__(self):
        return f"Pos: {self.pos}, Radius: {self.radius}, Parent: {self.parent}"

    def __repr__(self):
        return str(self)

def check_children_for_sensors(obj, parent_path):

    sensor_data = {}
    sensor_data_all = []

    # Get the parent path from the root object
    parent_path = parent_path + "/" + obj.name

    is_sensor_attribute_name = "is_sensor"
    pos_attribute_name = "position"
    norm_attribute_name = "sensor_normal"
    rad_attribute_name = "radii"
    alligator_clip_attribute_name = "is_clip"
    default_radius = False

    # Loop through all of the children objects and search for GeometryNodes modifier
    for child in obj.children:
        sensor_data[child.name] = False
        pos_attribute_data = []
        normal_attribute_data = []

        # Recursively check the children for sensors
        child_sensor_data = check_children_for_sensors(child, parent_path)

        # Ensure the object has geometry nodes modifier
        if child.modifiers.get('Skin') is None:
            #print(f"{child.name} does not have a Skin modifier.")
            # Add the child sensor data to the sensor data list
            sensor_data[child.name] = child_sensor_data
            continue

        #print(f"Found Skin modifier in object {child.name}.")

        # Get the evaluated geometry
        depsgraph = bpy.context.evaluated_depsgraph_get()
        eval_obj = child.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()
        
        # Check if the position data exists
        if pos_attribute_name not in mesh.attributes:
            #print(f"Attribute {attribute_name} not found in object {child.name}.")
            # for other_name in mesh.attributes:
            #     print(f"Found attribute: {other_name}.")
            # Add the child sensor data to the sensor data list
            sensor_data[child.name] = child_sensor_data
            continue

        if is_sensor_attribute_name not in mesh.attributes:
            #print(f"Attribute {is_sensor_attribtue_name} not found in object {child.name}.")
            # Add the child sensor data to the sensor data list
            sensor_data[child.name] = child_sensor_data
            continue

        if norm_attribute_name not in mesh.attributes:
            #print(f"Attribute {norm_attribute_name} not found in object {child.name}.")
            # Add the child sensor data to the sensor data list
            sensor_data[child.name] = child_sensor_data
            continue

        if rad_attribute_name not in mesh.attributes:
            #Set a default radius value if the radii attribute is not found
            print(f"Attribute {rad_attribute_name} not found in object {child.name}. Setting default radius of 0.1.")
            default_radius = True

        if alligator_clip_attribute_name in mesh.attributes:
            is_clip_data = mesh.attributes[alligator_clip_attribute_name].data
            # Get the position data of the alligator clip
            for i in range(len(is_clip_data)):
                if is_clip_data[i].value:
                    clip_pos = mesh.attributes[pos_attribute_name].data[i].vector
        
            print("\n\n ############################################## \n\n")
            print(f"    Alligator clip position found at {clip_pos} in object {child.name}.")
            print("\n\n ############################################## \n\n")
    
        # Get the attribute data

        pos_attribute_data = mesh.attributes[pos_attribute_name].data
        normal_attribute_data = mesh.attributes[norm_attribute_name].data

        # Get the radii attribute data
        rad_attribute_data = []
        if not default_radius:
            rad_attribute_data = mesh.attributes[rad_attribute_name].data

        is_sensor_data = mesh.attributes[is_sensor_attribute_name].data

        # Get path to object
        parent_path = parent_path + "/" + child.name
        # Remove any triple digit numbers from the parent path
        parent_path = re.sub(r'\.\d{3,}', '', parent_path)

        # Add the attribute data to the sensor data list
        sensor_counter = 0
        for i in range(len(pos_attribute_data)):
            if is_sensor_data[i].value:
                if default_radius:
                    child_sensor_data.append(SensorData(pos_attribute_data[i].vector, normal_attribute_data[i].vector, 0.1, parent_path, child.name))
                else:
                    child_sensor_data.append(SensorData(pos_attribute_data[i].vector, normal_attribute_data[i].vector, rad_attribute_data[i].value, parent_path, child.name))

                sensor_counter = sensor_counter + 1

        #print(f"Found {sensor_counter} sensor positions in object {child.name} under {parent_path}.")

        # Clean up
        #eval_obj.to_mesh_clear()

        # Add the child sensor data to the sensor data list
        sensor_data[child.name] = child_sensor_data

    # Print the sensor data
    if len(obj.children) == 0:
        return sensor_data_all
    else:
        print(f"\nObject {obj.name} has {len(obj.children)} child(ren):")
        for child in obj.children:
            if sensor_data[child.name] == False:
                print(f"        Child: {child.name} has no sensors.")
            else:
                print(f"        Child: {child.name} has {len(sensor_data[child.name])} sensors.")

                for sensor in sensor_data[child.name]:
                    sensor_data_all.append(sensor)

        print(f"Returning {len(sensor_data_all)} sensor positions in object {obj.name} under {parent_path}.")
    return sensor_data_all


def save_attribute_to_csv(context, file_path):
    # Get the object
    obj = context.object

    # Expand the ~ symbol into the path of the home directory
    #file_path = os.path.expanduser(file_path)

    # Make an array of all sensor positions,radii, and parent paths
    sensor_data = []
    
    # Check the children for sensors
    sensor_data = check_children_for_sensors(obj, "")

    # Check if there are any sensor positions
    if len(sensor_data) == 0:
        print("No sensor positions found.")
        return

    # Save the attribute data to CSV
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Index', 'X', 'Y', 'Z', 'NormX', 'NormY', 'NormZ', 'Radius', 'Parent', 'Object Name in Blender'])
        
        for i, element in enumerate(sensor_data):
            pos = element.pos
            norm = element.normal
            csv_writer.writerow([i, pos.x, pos.y, pos.z, norm.x, norm.y, norm.z, element.radius, element.parent, element.obj_name])
    
    # print(f"\nAttribute {attribute_name} saved to {file_path}")
    print(f"Sensor count: {len(sensor_data)}")

