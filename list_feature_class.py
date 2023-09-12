import arcpy

arcpy.env.workspace = r"C:\Users\shrutika\Downloads\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"

fc_list = arcpy.ListFeatureClasses()

# Creating a list of feature classes in current workspace

for fc_name in fc_list:
    print(fc_name)


print("--------------------------------------------------------------------")

# List of field objects for the specific feature class

field_list = arcpy.ListFields("Freeways")
for field in field_list:
    print(field.name)
    print(field.type)
    print(field.length)
    print("---------------------------------------------------------------------------")