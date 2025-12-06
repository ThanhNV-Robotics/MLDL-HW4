# Machine Learning and Deep Learning - Homework 4

This repository contains the solutions for Homework 4 in Jupyter Notebook format.

## Repository Structure

```
MLDL-HW4/
├── Q1.ipynb          # Question 1: Support Vector Machines (SVM)
├── Q2.ipynb          # Question 2: Recurrent Neural Networks (RNN) for Time Series
├── Q3.ipynb          # Question 3: Survival Analysis
├── Q4.ipynb          # Question 4: Hierarchical Clustering and Gene Expression Analysis
├── Ch12Ex13.csv      # Dataset for Q4
└── README.md         # This file
```

## Requirements

### Python Environment
- Python 3.10+
- Jupyter Notebook or JupyterLab

### Required Packages
Install the required packages using pip:

```bash
pip install numpy pandas matplotlib scikit-learn scipy torch torchmetrics pytorch-lightning ISLP lifelines torchinfo
```

Or if using conda:

```bash
conda install numpy pandas matplotlib scikit-learn scipy pytorch torchmetrics pytorch-lightning
pip install ISLP lifelines torchinfo
```

## Running the Notebooks

### Option 1: Using Jupyter Notebook
1. Navigate to the repository directory:
   ```bash
   cd "Machine Learning and Deep Learning/MLDL-HW4"
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open any of the question notebooks (Q1.ipynb, Q2.ipynb, Q3.ipynb, or Q4.ipynb) from the browser interface

4. Run the cells sequentially using `Shift + Enter` or click "Run All" from the Cell menu

### Option 2: Using VS Code
1. Open VS Code and install the Jupyter extension if not already installed

2. Open the MLDL-HW4 folder in VS Code

3. Open any notebook file (.ipynb)

4. Select the appropriate Python kernel (Python 3.10+ recommended)

5. Run cells individually or use "Run All" from the toolbar

### Option 3: Using JupyterLab
1. Navigate to the repository directory:
   ```bash
   cd "Machine Learning and Deep Learning/MLDL-HW4"
   ```

2. Launch JupyterLab:
   ```bash
   jupyter lab
   ```

3. Open the desired notebook from the file browser

4. Execute cells sequentially

## Question Descriptions

### Q1.ipynb - Support Vector Machines
- **Part (a)**: Generate 2-class linearly separable data and visualize SVM decision boundaries
- **Part (b)**: Perform cross-validation to find optimal C parameter
- **Part (c)**: Evaluate SVM performance on test set

### Q2.ipynb - Time Series Prediction with RNN
- **Part (a)**: Fit baseline Linear AR model
- **Part (b)**: Implement and train RNN model for NYSE volume prediction
- **Part (c)**: Implement Non-linear AR model
- **Part (d)**: Add temporal features (day_of_week, month) and compare model performances

**Note**: Q2 uses CPU for training by default. Models include:
- Linear Autoregressive (AR) model
- Recurrent Neural Network (RNN)
- Non-linear AR model with ReLU activation

### Q3.ipynb - Survival Analysis
- Kaplan-Meier estimation
- Cox Proportional Hazards model
- Survival curve analysis

### Q4.ipynb - Hierarchical Clustering
- **Part (a)**: Apply hierarchical clustering with correlation-based distance to gene expression data
- **Part (b)**: Identify genes that differ most between two groups using t-statistics

**Required Data**: `Ch12Ex13.csv` (gene expression dataset)

## Notes

- **Q2 Training Time**: The RNN models in Q2 may take several minutes to train depending on your hardware (especially when using CPU)

- **Random Seeds**: All notebooks use fixed random seeds for reproducibility

- **Data Files**: Q4 requires the `Ch12Ex13.csv` file to be in the same directory as the notebook

- **GPU vs CPU**: Q2 is configured to use CPU by default. If you have a compatible GPU and CUDA installed, you can modify the trainer settings in the notebook

## Troubleshooting

### Import Errors
If you encounter import errors, ensure all required packages are installed:
```bash
pip install --upgrade numpy pandas matplotlib scikit-learn scipy torch pytorch-lightning ISLP lifelines torchinfo torchmetrics
```

### CUDA Errors (Q2)
If you see CUDA-related errors in Q2, the notebook is already configured to use CPU. No action needed.

### Missing Data File (Q4)
Ensure `Ch12Ex13.csv` is in the same directory as `Q4.ipynb`.

## Author
Van Thanh Nguyen

## License
This is academic coursework. Please follow your institution's academic integrity policies.
