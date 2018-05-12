# Biological Activity in the Tijuana River

Photosynthetic active radiation (PAR) is thought to be highly related to predicting algal blooms, which can be detected by Chlorophyll A readings. 


**Data and Tools**<br/>
The data is available online as txt pages and for each site, includes seperate directories for nutritional, metereological, and water quality. I focus on the nutritional and meteorological data sets for the two years that are included, since these two data sets each contain PAR values (in the meteorological data) and CHLA_N values (in the nutritional data). 

The data is quickly scraped and parsed in to DataFrames for easy organization. 

Tools used include:

1. `Matplotlib` 
2. `NumPy`
3.  

**Usage** 

To load and clean your Circuitscape raster file to use for simulation, please follow the 1_Upload_Filter_Circuitscape notebook.

The repository is structured according to the following files:<br/>
_Data:_ This contains the circuitscape raster file. <br/>
_Notebooks:_ This contains the Jupyter notebooks that detail how to use the code.<br/>
_Project:_ This contains the original project proposal. <br/>

**Installation**

Clone the repo and use pip to install it.

git clone https://github.com/cs3425/project.git
cd project/
pip install .

**API Usage**
To use the helloworld Python API:

````
import project
project.project()
````

**Author:** Cecilia Sena<br/>**Email:**  cs3425@columbia.edu


