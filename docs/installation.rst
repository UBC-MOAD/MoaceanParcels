.. Copyright 2021 – present, UBC EOAS MOAD Group and The University of British Columbia
..
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..    https://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.

.. SPDX-License-Identifier: Apache-2.0

************
Installation
************

The recommended installation workflow for the :kbd:`MoaceanParcels` package is:

#. Clone the code and documentation `repository`_ from GitHub

   .. _repository: https://github.com/UBC-MOAD/MoaceanParcels

#. Create a `conda environment`_

   .. _conda environment: https://docs.conda.io/projects/conda/en/latest/

#. Activate the environment and install the package using the `"editable" install mode`_.

   .. _"editable" install mode: https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs


Details
=======

Getting the Code
----------------

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/UBC-MOAD/MoaceanParcels
    :alt: Git on GitHub

Clone the code and documentation `repository`_ from GitHub with:

.. _repository: https://github.com/UBC-MOAD/MoaceanParcels

.. code-block:: bash

    $ git clone git@github.com:UBC-MOAD/MoaceanParcels.git

or copy the URI
(the stuff after :kbd:`git clone` above)
from the :guilabel:`Code` button on the `repository`_ page.

.. note::

    The :kbd:`git clone` command above assumes that your are `connecting to GitHub using SSH`_.
    If it fails,
    please follow the instructions in our :ref:`moaddocs:SecureRemoteAccess` docs
    to set up your SSH keys and :ref:`moaddocs:CopyYourPublicSshKeyToGitHub`.

    .. _connecting to GitHub using SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh


Create a :program:`conda` Environment
-------------------------------------

Setting up an isolated development environment using `Conda`_ for each of your coding projects
is recommended.
Assuming that you have `Miniconda3`_ installed,
you can create an environment called :kbd:`moacean-parcels` that
will have all of the Python packages necessary for development,
testing,
and building the documentation for the package with the commands below.

.. _Conda: https://conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/en/latest/miniconda.html

.. code-block:: bash

    $ cd MoaceanParcels
    $ conda env create -f envs/environment-dev.yaml

Alternatively,
you can use :file:`envs/environment-dev.yaml` as a guide for creating your own
environment description file.
All of the dependencies above the

.. code-block:: yaml

    # For code style & repo QA

line are required to use :kbd:`MoaceanParcels` with :kbd:`OceanParcels`.
Put them and any other packages you want in your environment file.

The dependencies below that line are required for various parts of
:ref:`MoaceanParcelsPackagedDevelopment`.
You will need them if you are adding new kernel functions and particle classes to
:kbd:`MoaceanParcels`,
but not if you just want to use the stuff that is already in the package.

If you decide that you need to add a package to your environment,
add it to the :kbd:`dependencies:` section of your environment file,
then do:

.. code-block:: bash

    $ conda env update -f envs/environment-dev.yaml

to update your environment.


Activate Environment and Install the Package
--------------------------------------------

Activate your environment:

.. code-block:: bash

    $ cd MoaceanParcels
    $ conda activate moacean-parcels

Here we assume the environment is named :kbd:`moacean-parcels`.
You should substitute whatever name you used for your environment.

In the :kbd:`mocean-parcels` environment :kbd:`MoaceanParcels` is installed in
`editable install mode`_ as part of the conda environment creation process.
That means that the package is installed in a way that it can be updated when new features are
pushed to GitHub by simply doing a :command:`git pull` in the :file:`MoaceanParcels` directory.

.. _editable install mode: https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs

If you are using an environment that you created,
activate your environment,
then install the :kbd:`MoaceanParcels` package with:

.. code-block:: bash

    $ cd MoaceanParcels
    $ conda activate my-environment
    (my-environment)$ python3 -m pip install --editable .

To deactivate the environment use:

.. code-block:: bash

    (moacean-parcels)$ conda deactivate
