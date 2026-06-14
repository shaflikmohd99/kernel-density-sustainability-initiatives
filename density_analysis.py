# GIS Automation: Kernel Density Analysis using ArcPy

This repository contains a reusable Python script that automates the generation of a **Kernel Density** surface raster from point feature classes using the ArcGIS `arcpy` site package. 

Automating this process removes the manual overhead of the ArcMap/ArcGIS Pro GUI, enabling batch processing and reproducible spatial analysis workflows.

## 🛠️ Tool Configuration
The script utilizes the `KernelDensity_sa` geoprocessing tool with the following specific configurations:
* **Population Field:** `NONE` (Shapes are evaluated based on geometry density only)
* **Search Radius (Bandwidth):** `200`
* **Area Units:** `SQUARE_METERS`
* **Output Values:** `DENSITIES`
* **Method:** `PLANAR`

## 🚀 How to Use
1. Clone this repository to your local machine.
2. Ensure you have an active **ArcGIS Spatial Analyst** extension license.
3. Open the script and modify the `INPUT_LAYER` and `OUTPUT_PATH` variables in the `__main__` block to match your local data structure.
4. Run the script via your ArcGIS Python environment:
   ```bash
   python kernel_density_tool.py
