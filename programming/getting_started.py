import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 起手式 (Getting Started)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. 安裝 Python

    Windows：

    ```powershell
    >_ winget install --id=astral-sh.uv  -e
    ```

    macOS：

    ```sh
    $ brew install uv
    ```

    指定版本：

    ```sh
    $ uv python install 3.14
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. 下載 VS Code 編輯器

    https://code.visualstudio.com/download
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. 初始化專案

    ```sh
    $ uv init <PROJECT_NAME>
    $ cd <PROJECT_NAME>

    # e.g.
    $ uv init my-project
    $ cd my-project
    ```

    安裝 Marimo Notebook：

    ```sh
    $ uv add marimo
    ```

    在 VS Code 編輯器內安裝 Marimo 的擴充功能：

    https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. 安裝 Ruff 工具鏈

    全域環境：

    ```sh
    $ uv tool install ruff
    ```

    專案下：

    ```sh
    $ uv add ruff --dev
    ```

    `pyproject.toml` 內：

    ```toml
    [tool.ruff]
    line-length = 100

    [tool.ruff.lint]
    select = ["I"]
    ```

    執行格式化：

    ```sh
    $ uv run ruff format
    ```

    執行靜態分析：

    ```sh
    $ uv run ruff check --fix
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
