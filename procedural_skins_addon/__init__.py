import bpy
import os

def register():
    prefs = bpy.context.preferences.filepaths
    lib_path = os.path.join(os.path.dirname(__file__), "assets")
    if "GenTact Toolbox" not in prefs.asset_libraries:
        prefs.asset_libraries.new(name="GenTact Toolbox", directory=lib_path)


def unregister():
    prefs = bpy.context.preferences.filepaths
    if "GenTact Toolbox" in prefs.asset_libraries:
        prefs.asset_libraries.remove(prefs.asset_libraries["GenTact Toolbox"])
    

if __name__ == "__main__":
    register()
