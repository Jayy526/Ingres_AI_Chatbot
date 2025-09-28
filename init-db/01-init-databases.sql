-- Create groundwater database
CREATE DATABASE groundwater;

-- Connect to groundwater database
\c groundwater;

-- Enable PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Create groundwater_data table
CREATE TABLE IF NOT EXISTS groundwater_data (
    id SERIAL PRIMARY KEY,
    well_id VARCHAR(50) NOT NULL,
    location_name VARCHAR(100),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    depth_meters DECIMAL(8, 2),
    water_level_meters DECIMAL(8, 2),
    measurement_date DATE,
    quality_ph DECIMAL(4, 2),
    quality_tds DECIMAL(8, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    geom GEOMETRY(POINT, 4326)
);

-- Create spatial index
CREATE INDEX IF NOT EXISTS idx_groundwater_geom ON groundwater_data USING GIST (geom);

-- Create wells table for well information
CREATE TABLE IF NOT EXISTS wells (
    well_id VARCHAR(50) PRIMARY KEY,
    well_name VARCHAR(100) NOT NULL,
    location_name VARCHAR(100),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    depth_meters DECIMAL(8, 2),
    installation_date DATE,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    geom GEOMETRY(POINT, 4326)
);

-- Create spatial index for wells
CREATE INDEX IF NOT EXISTS idx_wells_geom ON wells USING GIST (geom);

-- Create regions table for administrative boundaries
CREATE TABLE IF NOT EXISTS regions (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(100) NOT NULL,
    region_type VARCHAR(50),
    population INTEGER,
    area_sqkm DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    geom GEOMETRY(MULTIPOLYGON, 4326)
);

-- Create spatial index for regions
CREATE INDEX IF NOT EXISTS idx_regions_geom ON regions USING GIST (geom);

-- Insert sample data
INSERT INTO wells (well_id, well_name, location_name, latitude, longitude, depth_meters, installation_date, geom) VALUES
('W001', 'Central Well', 'Downtown Area', 28.6139, 77.2090, 45.5, '2020-01-15', ST_SetSRID(ST_MakePoint(77.2090, 28.6139), 4326)),
('W002', 'North Well', 'North District', 28.7041, 77.1025, 52.3, '2020-03-20', ST_SetSRID(ST_MakePoint(77.1025, 28.7041), 4326)),
('W003', 'South Well', 'South District', 28.5355, 77.3910, 38.7, '2020-05-10', ST_SetSRID(ST_MakePoint(77.3910, 28.5355), 4326)),
('W004', 'East Well', 'East District', 28.6129, 77.2295, 41.2, '2020-07-15', ST_SetSRID(ST_MakePoint(77.2295, 28.6129), 4326)),
('W005', 'West Well', 'West District', 28.6149, 77.1885, 48.9, '2020-09-20', ST_SetSRID(ST_MakePoint(77.1885, 28.6149), 4326));

-- Insert sample groundwater measurements
INSERT INTO groundwater_data (well_id, location_name, latitude, longitude, depth_meters, water_level_meters, measurement_date, quality_ph, quality_tds, geom) VALUES
('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 12.3, '2023-01-15', 7.2, 450.5, ST_SetSRID(ST_MakePoint(77.2090, 28.6139), 4326)),
('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 11.8, '2023-02-15', 7.1, 465.2, ST_SetSRID(ST_MakePoint(77.2090, 28.6139), 4326)),
('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 11.5, '2023-03-15', 7.3, 442.8, ST_SetSRID(ST_MakePoint(77.2090, 28.6139), 4326)),
('W002', 'North District', 28.7041, 77.1025, 52.3, 15.2, '2023-01-15', 6.9, 520.1, ST_SetSRID(ST_MakePoint(77.1025, 28.7041), 4326)),
('W002', 'North District', 28.7041, 77.1025, 52.3, 14.8, '2023-02-15', 7.0, 535.7, ST_SetSRID(ST_MakePoint(77.1025, 28.7041), 4326)),
('W002', 'North District', 28.7041, 77.1025, 52.3, 14.5, '2023-03-15', 7.2, 518.3, ST_SetSRID(ST_MakePoint(77.1025, 28.7041), 4326)),
('W003', 'South District', 28.5355, 77.3910, 38.7, 8.9, '2023-01-15', 7.5, 380.2, ST_SetSRID(ST_MakePoint(77.3910, 28.5355), 4326)),
('W003', 'South District', 28.5355, 77.3910, 38.7, 8.6, '2023-02-15', 7.4, 395.8, ST_SetSRID(ST_MakePoint(77.3910, 28.5355), 4326)),
('W003', 'South District', 28.5355, 77.3910, 38.7, 8.3, '2023-03-15', 7.6, 372.1, ST_SetSRID(ST_MakePoint(77.3910, 28.5355), 4326)),
('W004', 'East District', 28.6129, 77.2295, 41.2, 9.8, '2023-01-15', 7.0, 420.5, ST_SetSRID(ST_MakePoint(77.2295, 28.6129), 4326)),
('W004', 'East District', 28.6129, 77.2295, 41.2, 9.5, '2023-02-15', 6.9, 435.2, ST_SetSRID(ST_MakePoint(77.2295, 28.6129), 4326)),
('W004', 'East District', 28.6129, 77.2295, 41.2, 9.2, '2023-03-15', 7.1, 418.7, ST_SetSRID(ST_MakePoint(77.2295, 28.6129), 4326)),
('W005', 'West District', 28.6149, 77.1885, 48.9, 13.7, '2023-01-15', 7.3, 485.3, ST_SetSRID(ST_MakePoint(77.1885, 28.6149), 4326)),
('W005', 'West District', 28.6149, 77.1885, 48.9, 13.4, '2023-02-15', 7.2, 500.1, ST_SetSRID(ST_MakePoint(77.1885, 28.6149), 4326)),
('W005', 'West District', 28.6149, 77.1885, 48.9, 13.1, '2023-03-15', 7.4, 482.6, ST_SetSRID(ST_MakePoint(77.1885, 28.6149), 4326));

-- Create a view for easy querying
CREATE OR REPLACE VIEW groundwater_summary AS
SELECT 
    gd.well_id,
    w.well_name,
    gd.location_name,
    gd.latitude,
    gd.longitude,
    gd.water_level_meters,
    gd.measurement_date,
    gd.quality_ph,
    gd.quality_tds,
    gd.geom
FROM groundwater_data gd
JOIN wells w ON gd.well_id = w.well_id
ORDER BY gd.measurement_date DESC;

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE groundwater TO postgres;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO postgres;

