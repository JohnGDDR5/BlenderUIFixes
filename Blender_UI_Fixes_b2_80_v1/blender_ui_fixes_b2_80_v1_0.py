# ##### BEGIN GPL LICENSE BLOCK #####
#
# Iterate Objects is a workflow addon for easily creating duplicates of objects you're working on and sending them to a unique collection. 
# A kind of version-control system where duplicates function as "snapshots" of the object to be able to have a backup when doing destructive modeling on a mesh object.
#
# Copyright (C) 2019 Juan Cardenas
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Blender UI Fixes",
    "description": "General fixes/additions to the UI of Blender, to speed up workflow.",
    "author": "Juan Cardenas (JohnGDDR5)",
    "version": (1, 0), 
    "blender": (2, 80, 0),
    #"location": "3D View > Side Bar > Rig Debugger",
    "location": "Many UI Headers basically",
    "warning": "In Development",
    "support": "COMMUNITY",
    "category": "Scene"
}

import bpy

class SCRIPT_OT_Reload_And_Run(bpy.types.Operator):
    bl_idname = "text.script_reload_and_run"
    bl_label = "Reload and Run Script"
    bl_description = "To rerun the script faster than two button clicks."
    #bl_options = {'UNDO',}
    #type: bpy.props.StringProperty(default="DEFAULT")

    def execute(self, context):
        scene = bpy.context.scene
        
        #Reloads the edited script
        #resolution='RELOAD' is for "Reload from Disk"
        bpy.ops.text.resolve_conflict(resolution='RELOAD')
        
        #Runs the Script
        bpy.ops.text.run_script()
        
        #Removes the button, since it will keep appending a new one every button press
        #bpy.types.TEXT_MT_editor_menus.remove(reload_and_run_script_button)
        
        return {'FINISHED'}
    
def reload_and_run_script_button(self, context):
    #toggle: bpy.props.BoolProperty(default=False)
    layout = self.layout
    
    row = layout.row(align=True)
    #row.prop_enum(inputs, "view_rotate_method", "TRACKBALL", text="", icon="ORIENTATION_GIMBAL")
    
    row.operator("text.script_reload_and_run", text="Reload & Run", icon="FILE_REFRESH")
    
#Classes that are registered
classes = (
    #RIG_DEBUGGER_PreferencesMenu,
    
    SCRIPT_OT_Reload_And_Run,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        #print("Registered: %s" % (cls.__name__) )
    
    #bpy.types.Scene.IM_Collections = bpy.props.CollectionProperty(type=REF_IMAGEAID_Collections)
    #bpy.types.Scene.RD_Props = bpy.props.PointerProperty(type=RIG_DEBUGGER_Props)
    
    bpy.types.TEXT_MT_editor_menus.append(reload_and_run_script_button)
    
def unregister():
    #del bpy.types.Scene.RD_Props
    
    #print("Reversed Classes: %s" % (str(list(reversed(classes))) ) )
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        #print("Unregistered: %s" % (str(cls.__name__)) )
    bpy.types.TEXT_MT_editor_menus.remove(reload_and_run_script_button)
    
    
if __name__ == "__main__":
    register()