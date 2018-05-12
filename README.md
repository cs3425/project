# Biological Activity in the Tijuana River

Photosynthetic active radiation (PAR) is thought to be highly related to predicting algal blooms, which can be detected by Chlorophyll A readings. Visualizing these data together and in relation to each other and their changes over time in one particular area of interest can convey the interactions in complex river systems. 


**Data and Tools**<br/>
The data is available online as txt pages and for each site, includes seperate directories for nutritional, metereological, and water quality. I focus on the nutritional and meteorological data sets for the two years that are included, since these two data sets each contain PAR values (in the meteorological data) and CHLA_N values (in the nutritional data). 

The data is quickly scraped and parsed in to DataFrames for easy organization. 

Tools used include:

1. `Matplotlib` 
2. `NumPy`
3. `Bokeh`

**Organization** 

_Data:_ This is empty since my data comes from the internet</br>
_Documents:_ This contains the proposal, final essay, and code review</br>
_Notebooks:_ This contains a Jupyter notebook that demonstrates the code</br>
_Project:_ This contains the source code</br>

**Installation**

Clone the repo and use pip to install it.

```
git clone https://github.com/cs3425/project.git
cd project/
pip install .
```

**API Usage**
To use the project Python API:

````
import project
newgraph = project.Project.update()
````

**Author:** Cecilia Sena<br/>**Email:**  cs3425@columbia.edu


