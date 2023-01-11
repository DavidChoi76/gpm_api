# Welcome to GPM-API

[![DOI](https://zenodo.org/badge/DOI/XXX)](https://doi.org/10.5281/zenodo.XXXX)
[![PyPI version](https://badge.fury.io/py/gpm_api.svg)](https://badge.fury.io/py/gpm_api)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/gpm_api.svg)](https://anaconda.org/conda-forge/gpm_api)
[![Build Status](https://github.com/ghiggi/gpm_api/workflows/Continuous%20Integration/badge.svg?branch=main)](https://github.com/ghiggi/gpm_api/actions)
[![Coverage Status](https://coveralls.io/repos/github/ghiggi/gpm_api/badge.svg?branch=main)](https://coveralls.io/github/ghiggi/gpm_api?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gpm_api/badge/?version=latest)](https://gpm_api.readthedocs.io/projects/gpm_api/en/stable/?badge=stable)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/github/license/ghiggi/gpm_api)(https://github.com/ghiggi/gpm_api/blob/master/LICENSE)

The GPM-API is still in development. Feel free to try it out and to report issues or to suggest changes.

## Purpose
GPM-API provides an easy-to-use python interface to download, read, process and visualize most of the products of the Global Precipitation Measurement Mission (GPM) data archive. The available products can be retrieved by: 

```python
import gpm_api
gpm_api.available_products(product_type="RS")  # research products
gpm_api.available_products(product_type="NRT") # near-real-time products

```

The gpm-api enable to:
- TODO: list all gpm_api utility


## Installation

### conda [NOT YET AVAILABLE]

GPM-API can be installed via [conda][conda_link] on Linux, Mac, and Windows.
Install the package by typing the following command in a command terminal:

    conda install gpm_api

In case conda forge is not set up for your system yet, see the easy to follow
instructions on [conda forge][conda_forge_link].

### pip

GPM-API can be installed via [pip][pip_link] on Linux, Mac, and Windows.
On Windows you can install [WinPython][winpy_link] to get Python and pip
running. Install the package by typing the following command in a command terminal:

    pip install gpm_api

To install the latest development version via pip, see the
[documentation][doc_install_link].


## Citation

If you are using GPM-API in your publication please cite our paper:

TODO: GMD

You can cite the Zenodo code publication of GPM-API by:

> Ghiggi Gionata & XXXX . ghiggi/gpm_api. Zenodo. https://doi.org/10.5281/zenodo.XXXXX

If you want to cite a specific version, have a look at the [Zenodo site](https://doi.org/10.5281/zenodo.XXXXX).

## Documentation for GPM-API

You can find the documentation under [gpm_api.readthedocs.io][doc_link]

### Tutorials and Examples

The documentation also includes some [tutorials][tut_link], showing the most important use cases of GPM-API.
These tutorial are also available as Jupyter Notebooks and in Google Colab:

- GPM Product Download [Notebook][tut1_link][Colab][colab1_link]
- [GPM Products Reading][tut2_link]
- [GPM Product Visualization ][tut3_link]
- [Exploratory data analysis of the IMERG dataset][tut8_link]
- [Exploratory data analysis of PMW 1B and 1C products][tut4_link]
- [Exploratory data analysis of the DPR 1A product][tut4_link
- [Exploratory data analysis of the DPR 2A product][tut5_link]
- [Exploratory data analysis of the CORRA 2B product][tut6_link]
- [Exploratory data analysis of the Latent Heating products][tut7_link]
- [Area Labeling][tut10_link]
- [Patch Data Extraction][tut9_link]

The associated python scripts are also provided in the `tutorial` folder.
 
## Requirements:

- [xarray](https://docs.xarray.dev/en/stable/)
- [dask](https://www.dask.org/)
- [cartopy](https://scitools.org.uk/cartopy/docs/latest/)
- [pyresample](https://pyresample.readthedocs.io/en/latest/)
- [h5py](https://github.com/h5py/h5py)
- [curl](https://curl.se/)
- [wget](https://www.gnu.org/software/wget/)

### Optional

- [zarr](https://zarr.readthedocs.io/en/stable/)
- [dask_image](https://image.dask.org/en/latest/)
- [skimage](https://scikit-image.org/)

## License

[MIT][license_link] © 2021-2023


[pip_link]: https://pypi.org/project/gstools
[conda_link]: https://docs.conda.io/en/latest/miniconda.html
[conda_forge_link]: https://github.com/conda-forge/gpm_api-feedstock#installing-gpm_api
[conda_pip]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#installing-non-conda-packages
[pipiflag]: https://pip-python3.readthedocs.io/en/latest/reference/pip_install.html?highlight=i#cmdoption-i
[winpy_link]: https://winpython.github.io/

[license_link]: https://github.com/ghiggi/gpm_api/blob/main/LICENSE
 
[doc_link]: https://gpm_api.readthedocs.io/projects/gpm_api/en/stable/
[doc_install_link]: https://gpm_api.readthedocs.io/projects/gpm_api/en/stable/#pip
[tut_link]: https://gpm_api.readthedocs.io/projects/gpm_api/en/stable/tutorials.html
[tut1_link]: https://gpm_api.readthedocs.io/projects/gpm_api/en/stable/examples/XXX/index.html
 
 
