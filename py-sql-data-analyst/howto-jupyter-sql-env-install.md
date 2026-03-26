Let’s do it cleanly; a new env will be way less painful than what you’ve just gone through.

Here’s an end‑to‑end recipe for a **fresh conda env with working `%sql` in Jupyter**, keeping it as short as possible.

## 1. Create and activate the env (terminal)

In a Terminal on your Mac:

```bash
conda create -n jupyter-sql python=3.10 -y
conda activate jupyter-sql
```

Now install the basics:

```bash
conda install -c conda-forge jupyterlab ipykernel -y
conda install -c conda-forge ipython-sql "sqlalchemy<2" sqlparse -y
```

(Using conda-forge avoids the `greenlet` build nightmare and gives you compatible wheels for Python 3.10.) [anaconda](https://anaconda.org/conda-forge/sqlalchemy)

## 2. Register the env as a Jupyter kernel

Still in the activated `jupyter-sql` env:

```bash
python -m ipykernel install --user --name jupyter-sql --display-name "Python (jupyter-sql)"
```

This makes a new selectable kernel in Jupyter called “Python (jupyter-sql)”. [github](https://github.com/jupyter/notebook/issues/4447)

## 3. Use it from Jupyter

1. Start Jupyter (from the same terminal, with the env activated):

   ```bash
   jupyter lab
   ```
   or
   ```bash
   jupyter notebook
   ```

2. In the notebook interface, change the kernel to **Python (jupyter-sql)**.
3. In a new notebook with that kernel, run:

   ```python
   %load_ext sql
   %sql sqlite://
   %%sql
   SELECT 1 AS test;
   ```

You should see a tiny table with `test = 1`.

If anything fails, tell me exactly which command and error, and we’ll fix just that piece.
