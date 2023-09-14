To run the code in Google Colab:

1. Upload the `updated_data.csv` file (which was downloaded from the data folder) and `details.csv`:
   - Click on the "Files" icon on the left-hand side of the Colab interface.
   - Click on the "Upload" button and select the name of the file from your local machine.

2. Run the code cells:
   - Go to the "Runtime" menu at the top of the Colab interface.
   - Select "Run all" to run all the code cells in the notebook.
   - Alternatively, you can run each code cell individually by clicking the play button next to each cell or using the keyboard shortcut Shift + Enter.

3. At the end it will ask for the `filename` which is the new merged data file.

Make sure to have the necessary libraries installed, such as `pandas`, `matplotlib`, `seaborn`, and any other libraries mentioned in the code. If any library is missing, you can install it using the command `!pip install <library-name>` in a code cell.

For running the `.py` file locally:

1. Place the `updated_data.csv` file (which was downloaded from the data folder) and `details.csv` file in the same directory as the Python script file (`adappt_intel_merged_eda.py`).

2. Open a command prompt or terminal and navigate to the directory where the Python script file is located.

3. Run the following command to execute the Python script:
   ```
   python adappt_intel_merged_eda.py
   ```
4. At the end it will ask for the `filename` which is the new merged data file.

   Make sure you have Python installed and added to the system's PATH variable.

The code will execute, and you will see the output and visualizations in the console or the Jupyter Notebook interface (make sure you have installed Anaconda packages), depending on the environment you are using.