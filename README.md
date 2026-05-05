# Python Journey

🐍 From Zero to Hero, Open Source to Business Applications

1. 程式設計 (Programming)
2. 演算法 (Algorithms)
3. [數值運算 (Numerical Computing - `numpy`)](./numerical-computing/README.md)
4. [資料處理 (Data Processing - `polars`)](./data-processing/README.md)
5. [資料視覺化 (Data Visualization - `matplotlib`)](./data-visualization/README.md)
6. [機器學習 (Machine Learning - `scikit-learn`)](./machine-learning/README.md)
7. [深度學習 (Deep Learning - `torch`)](./deep-learning/README.md)

---

Export marimo notebooks to scripts:

```sh
# Single project
$ uv run export_marimo.py <PROJECT_FOLDER>

# Multiple projects
$ uv run export_marimo.py <PROJECT_FOLDER_1> <PROJECT_FOLDER_2>

# From within project directory
$ cd <PROJECT_FOLDER>
$ uv run ../export_marimo.py
```
