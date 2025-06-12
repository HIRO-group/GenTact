bl_info = {
    "name": "Procedural Skins",
    "author": "Carson Kohlbrenner",
    "version": (1, 18),
    "blender": (2, 80, 0),
    "location": "Object > Skin Import/Export",
    "description": "Export/Import tool for GenTact",
    "warning": "",
    "doc_url": "https://github.com/HIRO-group/GenTact",
    "category": "Object",
}

import bpy
import bpy.props

from .operators.isaac_save_operator import IsaacSaveOperator
from .operators.export_ert_operator import ExportERTOperator
from .operators.skin_vertice_save_operator import SkinVerticeSaveOperator
from .operators.import_heatmap_operator import ImportHeatmapOperator

class MyAddonProperties(bpy.types.PropertyGroup):
    unit_scale: bpy.props.FloatProperty(
        name="Unit Scale",
        description="Scale of the units",
        default=1.0,
        min=0.001,
        max=1000000.0
    )

    group_name_import: bpy.props.StringProperty(
        name="",
        description="Name of the skin vertex group",
        default="Group"
    )

    group_name_export: bpy.props.StringProperty(
        name="",
        description="Name of the skin vertex group",
        default="Group"
    )

class SensorPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Sensor Export"
    bl_idname = "OBJECT_PT_SENSOR_EXPORT"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        unit_prop = scene.my_addon_properties
        obj = context.object

        row = layout.row()
        row.label(text="Save sensors as CSV", icon='FILE_TICK')

        row = layout.row()
        row.label(text="Select root prim for faster processing")

        row = layout.row()
        row.label(text="Selected root prim: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        # String field for identifying the skin vertex group
        row = layout.row()
        row.label(text="Skin Vertex Group")
        row.prop(unit_prop, "group_name_export")

        # Isaac Save Button 
        row = layout.row()
        row.operator("object.isaac_save_operator")

        # Skin Vertice Save Button
        row = layout.row()
        row.operator("object.skin_vertice_save_operator")

        row = layout.row()
        row.label(text="Export Meshes as STLs", icon='EXPORT')

        # Unit Scale Slider
        row = layout.row()
        row.label(text="Unit Scale")
        row.prop(unit_prop, "unit_scale")

        # Export Sensor Button 
        row = layout.row()
        row.operator("object.export_ert_operator")


        # Apply Skin Button
        # row = layout.row()
        # row.operator("object.apply_skin", text="Apply Skin").geo_node_name = "Skin"

class ImportPanel(bpy.types.Panel):
    bl_label = "Sensor Import"
    bl_idname = "OBJECT_PT_SENSOR_IMPORT"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        unit_prop = scene.my_addon_properties

        # Panel Icon
        row = layout.row()
        row.label(text="Apply Heatmaps to Objects", icon='IMPORT')

        # String field for identifying the node placement vertex group
        row = layout.row()
        row.label(text="Sensor Vertex Group")
        row.prop(unit_prop, "group_name_import")

        # Apply Heatmap Button
        row = layout.row()
        row.operator("object.import_heatmap_operator", text="Import Heatmap")


def register():
    bpy.utils.register_class(MyAddonProperties)
    bpy.types.Scene.my_addon_properties = bpy.props.PointerProperty(type=MyAddonProperties)
    bpy.utils.register_class(IsaacSaveOperator)
    bpy.utils.register_class(ExportERTOperator)
    bpy.utils.register_class(SkinVerticeSaveOperator)
    bpy.utils.register_class(ImportHeatmapOperator)
    bpy.utils.register_class(SensorPanel)
    bpy.utils.register_class(ImportPanel)

def unregister():
    bpy.utils.unregister_class(IsaacSaveOperator)
    bpy.utils.unregister_class(ExportERTOperator)
    bpy.utils.unregister_class(SkinVerticeSaveOperator)
    bpy.utils.unregister_class(ImportHeatmapOperator)
    bpy.utils.unregister_class(MyAddonProperties)
    del bpy.types.Scene.my_addon_properties
    bpy.utils.unregister_class(SensorPanel)
    bpy.utils.unregister_class(ImportPanel)
    

if __name__ == "__main__":
    register()
