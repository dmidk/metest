# metest
Test, check and compare logs and data from meteorological computations. 

# Prerequisites
*metest* is a script tool based on python. Dependencies is defined in `metest.yml` and a python environment can be made using (mini)conda:

`conda env create -f metest.yml`

# For developers

## Build documentation
```shell
cd doc
sphinx-apidoc -f --private --ext-autodoc --separate -o . ../metest/
make html
```
The html source files goes into `doc/_build/html`