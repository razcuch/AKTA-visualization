 **AKTA Visualization**
 ---
 *Background*
 ---
AKTA protein purification systems are widely used in biochemistry and molecular biology for the efficient separation and purification of proteins. These systems utilize liquid chromatography techniques to separate proteins based on their physical and chemical properties, such as size, charge, hydrophobicity, or affinity for specific ligands. The AKTA equipped with precise pumps, UV detectors and a fraction collectors. During the purification process, fractions of the eluted protein solution are collected into individual wells of a multi-well plate or tubes. These wells allow for systematic collection and storage of the eluates, which can then be analyzed to determine the protein concentration and purity. The data can be summarized with Excel file and analyzed by the user. The Excel file contains data detailing the process progression, correlating absorption levels to the volume (in mL) processed by the AKTA system, with results stratified by well distribution.
Functionality:
The code takes the following inputs from the user: the column and row for mAU (absorbance), fraction (ml), and wells fraction, two well numbers, and an option to select a color. Based on these inputs, the code generates a graph of absorbance (mAU) vs fraction (ml), highlighting the positions of the specified wells with respect to the ml values.
Required Libraries:
Pandas: For data manipulation and reading Excel files.
Matplotlib/Seaborn: For generating plots and graphs.
OpenPyXL: For interacting with Excel files.
NumPy: For efficient numerical operations.
Tkinter: for graphical user interface. 
User-specified parameters:
Columns and rows for mAU, fraction, and well data.
Well numbers to highlight.
Color selection for graph highlights.
Visualization:
Plot absorbance (mAU) vs. fraction volume (mL).
Highlight specified well fractions with the selected color.
