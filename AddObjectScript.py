import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = 'My First Addon'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Add Some Object", icon="MATCUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon='CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cylinder_add", icon='MESH_CYLINDER')
        row = layout.row()
        row.operator("mesh.primitive_monkey_add", icon='MONKEY')
        row = layout.row()
        row.operator("object.text_add", icon='FILE_FONT')
        row = layout.row()
        row.operator("object.delete", icon='X',)






        
def register():
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    
    
if __name__ == "__main__":
    register()