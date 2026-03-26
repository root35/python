### To close

1. In notebook: Kernel → Shutdown, then Quit Jupyter.
2. In terminal: `Ctrl+C` to stop Jupyter.
3. Optionally: `conda deactivate`.

### To reopen

1. In terminal:
```bash
conda activate jupyter-sql
jupyter notebook     # or: jupyter lab
```

2. In notebook (first cell):

```python
%load_ext sql
%sql sqlite://
%config SqlMagic.style = '_DEPRECATED_DEFAULT'
```

Run SQL cells like:

```sql
%%sql
SELECT 1 AS test;
```
