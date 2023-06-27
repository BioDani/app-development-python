# App devolopment in Python #


Create a new enviroment development
```sh
conda create -n- name_project python:3.9
```

To activate this enviroment, use
```sh
conda activate name_project
```
 Or in VScode: use `>python: Select interpreter` and select the environment created previously.

  Now, install some packages that we are going to need
  ```sh
  python -m pip install pygame django fastapi
  ```

Save environment in a `yml` file.
  ```sh
  conda env export > environment.yml
  ```



