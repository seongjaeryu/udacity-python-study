# udacity-python-study

### How to set up development environment with MiniConda
1. Miniconda Installation
    https://developers.google.com/earth-engine/guides/python_install-conda#install_miniconda
1. Development Environment Setting
    - To create an environment and activate it
        ```
        conda create -n __name-of-environment__ python=__python-version__
        source activate __name-of-environment__
        conda list
        conda install pandas matplotlib notebook # numpy is a dependancy of pandas
        ```
    - To install specific version of a package
        ```
        conda install __package-name__=__version__
        ```
    - To remove a package
        ```
        conda remove __package-name__
        ```
    - To search packages and versions
        ```
        conda search __search-keyword__
        ```
    - To deactivate an environment
        ```
        conda deactivate
        ```
    - To Print current environment
        ```
        conda env export
        ```
    - To Export current environment to a yaml file
        ```
        conda env export > environment.yaml
        ```
    - To create an environment from a yaml file with same name in it
        ```
        conda env create -f environment.yaml
        ```
    - To check environment list
        ```
        conda env list
        ```
    - To delete an specific environment
        ```
        conda env remove -n __name-of-environment__
        ```
    - To check package list of an environment
        ```
        conda list -n __name-of-environment__
        ```
    - To check a specific package of an environment
        ```
        conda list -n __name-of-environment__ __package-name__
        ```
    - EXTRA.
        * pip Environment Export and Application
            ```
            # Export
            pip freeze > requirements.txt
            # Apllication
            pip install -r requirements.txt
            ```