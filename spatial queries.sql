-- ==============================================================================
-- Script Name: 01_spatial_filter.sql
-- Description: Filters raw sustainability initiatives spatial data to generate a clean target 
--              point feature subset for downstream Kernel Density modeling.
-- ==============================================================================

-- Create a clean, indexed view containing only active, valid point records
CREATE OR REPLACE VIEW feature_point AS
SELECT 
    objectid,
    globalid,
    incident_date,
    shape -- The native geometry column (e.g., ST_Geometry or PostGIS Geometry)
FROM 
    sustainability_initiatives_distributions_raw
WHERE 
    -- 1. Attribute Filtering: Isolate relevant data (e.g., active cases this year)
    status = 'Active'
    AND incident_date >= 'none'
    
    -- 2. Spatial Data Cleaning: Strip out corrupt or missing coordinates
    -- This prevents the ArcPy Kernel Density tool from crashing mid-process
    AND shape IS NOT NULL
    AND ST_IsValid(shape) = 1;

-- Optional: Verify record count prior to exporting to ArcPy
SELECT COUNT(*) as valid_point_count FROM feature_point;
