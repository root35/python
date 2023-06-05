#### Set Jupyter password
https://jupyter-notebook.readthedocs.io/en/stable/public_server.html


#### Launch notebook in Chrome
- Set Chrome as default browser in the Chrome settings
- Open terminal and type
$ jupyter notebook


#### Add environment to Jupyter Notebook with specific Python version
# Ref:
# https://sites.northwestern.edu/researchcomputing/resources/adding-python-3-to-jupyter-notebook/

$ conda create -n py39 python=3.9 ipykernel jupyter anaconda
$ source activate py39
(OR: $ conda activate py39)
$ ipython kernel install --name py39 --user
# Close terminal and open a new one

# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#setting-environment-variables
$ conda env config vars set OPENAI_API_KEY=...
$ conda activate py39  # restart env
$ echo $OPENAI_API_KEY

$ (base) macbook nltk_data >> jupyter notebook   # -> py39
$ (base) macbook ~ >> jupyter notebook           # -> default


$ source activate py39
(OR: $ conda activate py39)
$ pip install pip_search
$ pip_search langchain

