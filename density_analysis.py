"""
Script Name: 02_kernel_density_analysis.py
Description: Automates the generation of a Kernel Density raster surface 
             from filtered vector point features using ArcPy.
"""

import os
import arcpy

def check_spatial_license():
    """Validates and checks out the ArcGIS Spatial Analyst extension."""
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
        arcpy.AddMessage("Spatial Analyst extension checked out successfully.")
    else:
        raise arcpy.ExecuteError("Spatial Analyst license is unavailable. Execution halted.")

def run_kernel_density(input_layer, output_raster, search_radius, cell_size):
    """Executes the Kernel Density tool with robust error handling."""
    try:
        # 1. Initialize environment and extension
        check_spatial_license()
        arcpy.env.overwriteOutput = True

        arcpy.AddMessage(f"Initializing Kernel Density for: {input_layer}...")

        # 2. Core Geoprocessing Execution (Using your exact parameters)
        arcpy.gp.KernelDensity_sa(
            input_layer,
            "NONE",               # Population field (assumes point weight = 1)
            output_raster,
            cell_size,
            search_radius,
            "SQUARE_METERS",      # Area units
            "DENSITIES",          # Output values scale
            "PLANAR"              # Method
        )

        arcpy.AddMessage(f"SUCCESS: Density surface saved to {output_raster}")

    except arcpy.ExecuteError:
        # Log specific ArcGIS geoprocessing errors
        arcpy.AddError("ArcPy Geoprocessing Error: " + arcpy.GetMessages(2))
    except Exception as e:
        # Log unexpected Python system/logic errors
        arcpy.AddError(f"Unexpected Script Error: {str(e)}")
    finally:
        # 3. Always ensure the network license is released back to the pool
        arcpy.CheckInExtension("Spatial")
        arcpy.AddMessage("Spatial Analyst extension checked back in.")

if __name__ == "__main__":
    # Standardizing paths dynamically instead of hardcoding absolute C:/ paths
    current_directory = os.path.dirname(os.path.abspath(__file__))
    gdb_path = os.path.join(current_directory, "Data", "Default.gdb")

    # Ensure output directory exists
    if not os.path.exists(os.path.dirname(gdb_path)):
        os.makedirs(os.path.dirname(gdb_path))

    # Parameters mapped from original ArcMap export
    INPUT_LAYER = "feature_point"  # Matches the view created in the SQL script
    OUTPUT_RASTER = os.path.join(gdb_path, "KernelD_shp13")
    CELL_SIZE = "4.32639440857798E-05"
    SEARCH_RADIUS = "200"

    # Execute main workflow
    run_kernel_density(INPUT_LAYER, OUTPUT_RASTER, SEARCH_RADIUS, CELL_SIZE)
