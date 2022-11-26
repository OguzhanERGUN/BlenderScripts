import bpy

class PanelClassName(bpy.types.Panel):
    bl_idname = "panelname"
    bl_label = "Panelname"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "category"

    def draw(self, context):
        layout = self.layout
        
    