# AKTA Visualization
 ---
 
 ## Background
 
AKTA protein purification systems are widely used in biochemistry and molecular biology for the efficient separation and purification of proteins.
These systems utilize liquid chromatography techniques to separate proteins based on their physical and chemical properties, such as size, charge, hydrophobicity, or affinity for specific ligands.
The AKTA equipped with precise pumps, UV detectors and a fraction collectors. During the purification process, fractions of the eluted protein solution are collected into individual wells of a multi-well plate or tubes.
These wells allow for systematic collection and storage of the eluates, which can then be analyzed to determine the protein concentration and purity. The data can be summarized with Excel file and analyzed by the user. 
The Excel file contains data detailing the process progression, correlating absorption levels to the volume (in mL) processed by the AKTA system, with results stratified by well distribution.


---
## Functionality

The code takes the following inputs from the user:
the column and row for mAU (absorbance), fraction (ml), and wells fraction, two well numbers, and an option to select a color.
Based on these inputs, the code generates a graph of absorbance (mAU) vs fraction (ml), highlighting the positions of the specified wells with respect to the ml values.

---
## Required Libraries

- **Pandas**: For data manipulation and reading Excel files.
- **Matplotlib/Seaborn**: For generating plots and graphs.
- **OpenPyXL**: For interacting with Excel files.
- **NumPy**: For efficient numerical operations.
- **Tkinter**: for graphical user interface. 

---
## User-specified parameters

- start and end points (ml) 
- Wells numbers to highlight.
- Color selection for graph highlights.


---
## Visualization

- Plot absorbance (mAU) vs. fraction volume (mL).
- Highlight specified wells fractions with the selected color.

  ---
  ## Benefits

  - speeds up data analysis
  - User-friendly for researchers

  ---

  ## Example

  The needed input to the GUI:
  - Enter starting ml value: 10
  - Enter ending ml value: 20
  - Enter strting fraction name: 5.C.9
  - Enter ending fraction name: 5.D.2
  - Pick fill color: chose color from the list
 
    ![graph example](https://github.com/user-attachments/assets/23f477ab-9501-48c0-bfa9-1cf75d5323fe) 
 
  This Python tool is designed to simplify the manual process of creating graphs from AKTA Excel data. It provides an efficient and user-friendly solution for visualizing absorbance (mAU) vs. fraction volume (mL) graphs, saving time and enhancing data analysis accuracy for researchers.





