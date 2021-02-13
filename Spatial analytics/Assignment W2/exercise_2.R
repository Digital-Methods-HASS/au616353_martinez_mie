##-----------------------------------------------##
##    Author: Mie Arnau Martinez                 ##
##    Institute of Culture and Society           ##
##    Aarhus University, Aarhus, Denmark         ##
##    201806701@post.au.dk                       ##
##-----------------------------------------------##

#### Goals ####

# - Understand the provided datasets
# - Learn how to reproject spatial data
# - Limit your data into an area of interest
# - Create a new map

# We highlighted all parts of the R script in which you are supposed to add your
# own code with: 

# /Start Code/ #

print("Hello World") # This would be your code contribution

# /End Code/ #

#### Required R libraries ####

# We will use the sf, raster, and tmap packages.
# Additionally, we will use the spData and spDataLarge packages that provide new datasets. 
# These packages have been preloaded to the worker2 workspace.

library(sf)
library(raster)
library(tmap)
library(spData)
library(spDataLarge)

#### Data sets #### 

# We will use two data sets: `srtm` and `zion`.
# The first one is an elevation raster object for the Zion National Park area, and the second one is an sf object with polygons representing borders of the Zion National Park.

srtm <- raster(system.file("raster/srtm.tif", package = "spDataLarge"))
zion <- read_sf(system.file("vector/zion.gpkg", package = "spDataLarge"))

# Additionally, the last exercise (IV) will used the masked version of the `lc_data` dataset.

study_area <- read_sf("data/study_area.gpkg")
lc_data <- raster("data/example_landscape.tif")
lc_data_masked <- mask(crop(lc_data, study_area), study_area)

#### Exercise I ####

# 1. Display the `zion` object and view its structure.
head(zion)
plot(st_geometry(zion))
class(zion)
# What can you say about the content of this file?
    # It is a simple feature object with 1 feature of the type polygon.
    # This is also apparent from the plot as evidently there is only one polygon
    # The tibble contains 11 fields (columns) besides the sf object

# What type of data does it store? 
    # It stores the name of the area and different metadata as well as the 
    # geometry of the polygon.

# What is the coordinate system used?
    st_crs(zion) 
    #The CRS value is UTM zone 12N

# How many attributes does it contain?
    # The sf object contains 11 feature attributes (non-geometry fields).
    
# What is its geometry?
    # Polygon


# 2. Display the `srtm` object and view its structure.
    
# /Start Code/ #
class(srtm)
plot(srtm)
srtm
# What can you say about the content of this file? 
    # It is a single-band raster object containing a single layer of raster 
    # values (212.505 cells).

# What type of data does it store?
    # It stores an array of pixels

# What is the coordinate system used?
    crs(srtm)
    # WGS84
    
# How many attributes does it contain?
    # The raster object has 1 attribute (ID)
    
# How many dimensions does it have? 
    length(dim(srtm))
    # 3 dimensions
    
# What is the data resolution?
    res(srtm)
    # 0.0008333333 0.0008333333

# /End Code/ #


    

#### Exercise II ####

# 1. Reproject the `srtm` dataset into the coordinate reference system used in the `zion` object. 
# Create a new object `srtm2`
# Vizualize the results using the `plot()` function.
    
# /Start Code/ #
# Defining the crs of zion as text
crs_1 <- crs(zion, asText = TRUE)

# Projecting srtm to match the crs of Zion and saving as srtm2
srtm2 <- projectRaster(srtm, crs = crs_1)

# Plotting the srtm with the new and old projection to compare
plot(srtm2)
plot(srtm)

# Looking at the CRS to see if they match
st_crs(zion)
crs(srtm2)

# /End Code/ # 
    

# 2. Reproject the `zion` dataset into the coordinate reference system used in the `srtm` object.
# Create a new object `zion2`
# Vizualize the results using the `plot()` function.

# /Start Code/ #
# Defining the crs of zion as text
crs_2 <- crs(srtm, asText = TRUE)

# Project zion to match the CRS of srtm
zion2 <- st_transform(zion, crs = crs_2)

# Plotting zion with the new and old projection to compare
plot(zion2)
plot(zion)

# Looking at the CRS to see if they match
st_crs(zion2)
crs(srtm)


# /End Code/ # 