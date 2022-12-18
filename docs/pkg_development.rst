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


.. _MoaceanParcelsPackagedDevelopment:

*****************************************
:kbd:`MoaceanParcels` Package Development
*****************************************


.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0
.. image:: https://img.shields.io/badge/Python-3.10-blue?logo=python&label=Python&logoColor=gold
    :target: https://docs.python.org/3.10/
    :alt: Python Version
.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/UBC-MOAD/MoaceanParcels
    :alt: Git on GitHub
.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter
.. image:: https://readthedocs.org/projects/MoaceanParcels/badge/?version=latest
    :target: https://moaceanparcels.readthedocs.io/en/latest/
    :alt: Documentation Status
.. image:: https://github.com/UBC-MOAD/MoaceanParcels/workflows/sphinx-linkcheck/badge.svg
    :target: https://github.com/UBC-MOAD/MoaceanParcels/actions?query=workflow:sphinx-linkcheck
    :alt: Sphinx linkcheck
.. image:: https://img.shields.io/github/issues/UBC-MOAD/MoaceanParcels?logo=github
    :target: https://github.com/UBC-MOAD/MoaceanParcels/issues
    :alt: Issue Tracker

The MoaceanParcels package (:kbd:`moacean_parcels`) contains shared kernels
and other code for OceanParcels developed by the UBC-MOAD group.


.. _MoaceanParcelsPythonVersions:

Python Versions
===============

.. image:: https://img.shields.io/badge/Python-3.10-blue?logo=python&label=Python&logoColor=gold
    :target: https://docs.python.org/3.10/
    :alt: Python Version

The :kbd:`moacean_parcels` package is developed and tested using `Python`_ 3.10.

.. _Python: https://www.python.org/


.. _MoaceanParcelsGettingTheCode:

Getting the Code
================

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


.. _MoaceanParcelsDevelopmentEnvironment:

Development Environment
=======================

Setting up an isolated development environment using `Conda`_ is recommended.
Assuming that you have `Miniconda3`_ installed,
you can create and activate an environment called :kbd:`moacean-parcels` that
will have all of the Python packages necessary for development,
testing,
and building the documentation with the commands below.

.. _Conda: https://conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/en/latest/miniconda.html

.. code-block:: bash

    $ cd MoaceanParcels
    $ conda env create -f envs/environment-dev.yaml
    $ conda activate moacean-parcels
    (moacean-parcels)$ python3 -m pip install --editable .

The :kbd:`--editable` option in the :command:`pip install` command above installs
the package from the cloned repo via symlinks so that the installed package
will be automatically updated as the repo evolves.

To deactivate the environment use:

.. code-block:: bash

    (moacean-parcels)$ conda deactivate


.. _MoaceanParcelsCodingStyle:

Coding Style
============

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter

The :kbd:`MoaceanParcels` package uses Git pre-commit hooks managed by `pre-commit`_ to maintain consistent code style and and other aspects of code,
docs,
and repo QA.

.. _pre-commit: https://pre-commit.com/

To install the :program:`pre-commit` hooks in a newly cloned repo,
activate the conda development environment,
and run :command:`pre-commit install`:

.. code-block:: bash

    $ cd MoaceanParcels
    $ conda activate moacean-parcels
    (moacean-parcels)$ pre-commit install

.. note:: You only need to install the hooks once immediately after you make a new clone of the `MoaceanParcels repository`_ and build your :ref:`MoaceanParcelsDevelopmentEnvironment`.

.. _MoaceanParcels repository: https://github.com/UBC-MOAD/MoaceanParcels


.. _MoaceanParcelsBuildingTheDocumentation:

Building the Documentation
==========================

.. image:: https://readthedocs.org/projects/moaceanparcels/badge/?version=latest
    :target: https://moaceanparcels.readthedocs.io/en/latest/
    :alt: Documentation Status

The documentation for the :kbd:`MoaceanParcels` package is written in
`reStructuredText`_ and converted to HTML using `Sphinx`_.
Creating a :ref:`MoaceanParcelsDevelopmentEnvironment` as described above
includes the installation of Sphinx.
Building the documentation is driven by the :file:`docs/Makefile`.
With your :kbd:`moacean-parcels` development environment activated,
use:

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/

.. code-block:: bash

    (moacean-parcels)$ (cd docs && make clean html)

to do a clean build of the documentation.
The output looks something like:

.. code-block:: text

    Removing everything under '_build'...
    Running Sphinx v4.3.1
    making output directory... done
    loading intersphinx inventory from https://ubc-moad-docs.readthedocs.io/en/latest/objects.inv...
    loading intersphinx inventory from https://numpy.org/doc/stable/objects.inv...
    loading intersphinx inventory from https://oceanparcels.org/gh-pages/html/objects.inv...
    building [mo]: targets for 0 po files that are out of date
    building [html]: targets for 9 source files that are out of date
    updating environment: [new config] 9 added, 0 changed, 0 removed
    reading sources... [100%] pkg_development
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [100%] pkg_development
    generating indices... genindex py-modindex done
    copying notebooks ... [100%] kernels/kernel_example_notebooks/recovery_kernels/DeleteParticle-example.ipynb
    highlighting module code... [100%] moacean_parcels.kernels.DeleteParticle
    writing additional pages... search done
    copying images... [100%] _build/doctrees/nbsphinx/kernels_kernel_example_notebooks_recovery_kernels_DeleteParticle-example_13_0.png
    copying static files... done
    copying extra files... done
    dumping search index in English (code: en)... done
    dumping object inventory... done
    build succeeded.

    The HTML pages are in _build/html.

The HTML rendering of the docs ends up in :file:`docs/_build/html/`.
You can open the :file:`index.html` file in that directory tree in your browser
to preview the results of the build.
If you use Firefox,
you can probably accomplish that with:

.. code-block:: bash

    (moacean-parcels)$ firefox docs/_build/html/index.html


If you have write access to the `repository`_ on GitHub,
whenever you push changes to GitHub the documentation is automatically
re-built and rendered at https://moaceanparcels.readthedocs.io/en/latest/.


.. _MoaceanParcelsLinkCheckingTheDocumentation:

Link Checking the Documentation
-------------------------------

.. image:: https://github.com/UBC-MOAD/MoaceanParcels/workflows/sphinx-linkcheck/badge.svg
    :target: https://github.com/UBC-MOAD/MoaceanParcels/actions?query=workflow:sphinx-linkcheck
    :alt: Sphinx linkcheck

Sphinx also provides a link checker utility which can be run to find
broken or redirected links in the docs.
With your :kbd:`moacean-parcels)` environment activated,
use:

.. code-block:: bash

    (moacean-parcels))$ cd MoaceanParcels/docs/
    (moacean-parcels)) docs$ make linkcheck

The output looks something like:

.. code-block:: text

    Running Sphinx v4.2.0
    loading pickled environment... done
    building [mo]: targets for 0 po files that are out of date
    building [linkcheck]: targets for 2 source files that are out of date
    updating environment: 0 added, 1 changed, 0 removed
    reading sources... [100%] pkg_development
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [100%] pkg_development

    ( pkg_development: line   20) ok        https://black.readthedocs.io/en/stable/
    ( pkg_development: line  261) ok        https://coverage.readthedocs.io/en/latest/
    ( pkg_development: line   20) ok        https://docs.python.org/3.10/
    ( pkg_development: line   62) ok        https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    ( pkg_development: line  241) ok        https://docs.pytest.org/en/latest/
    ( pkg_development: line  298) ok        https://git-scm.com/
    ( pkg_development: line  106) ok        https://conda.io/en/latest/
    ( pkg_development: line  106) ok        https://docs.conda.io/en/latest/miniconda.html
    ( pkg_development: line   93) ok        https://docs.github.com/en/authentication/connecting-to-github-with-ssh
    ( pkg_development: line   20) ok        https://img.shields.io/badge/code%20style-black-000000.svg
    (           index: line   36) ok        https://img.shields.io/badge/license-Apache%202-cb2533.svg
    ( pkg_development: line   20) ok        https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    ( pkg_development: line   20) ok        https://img.shields.io/badge/python-3.10-blue.svg
    ( pkg_development: line   20) ok        https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    ( pkg_development: line  231) ok        https://github.com/UBC-MOAD/MoaceanParcels/actions?query=workflow=sphinx-linkcheck
    ( pkg_development: line   20) ok        https://github.com/UBC-MOAD/MoaceanParcels/issues
    ( pkg_development: line   20) ok        https://moaceanparcels.readthedocs.io/en/latest/
    ( pkg_development: line  261) ok        https://pytest-cov.readthedocs.io/en/latest/
    ( pkg_development: line  307) ok        https://img.shields.io/github/issues/MIDOSS/WWatch3-Cmd?logo=github
    ( pkg_development: line   20) ok        https://github.com/pre-commit/pre-commit
    ( pkg_development: line   20) ok        https://readthedocs.org/projects/MoaceanParcels/badge/?version=latest
    ( pkg_development: line   20) ok        https://github.com/UBC-MOAD/MoaceanParcels
    ( pkg_development: line   93) ok        https://ubc-moad-docs.readthedocs.io/en/latest/ssh_access.html#copyyourpublicsshkeytogithub
    (           index: line   36) ok        https://www.apache.org/licenses/LICENSE-2.0
    ( pkg_development: line   58) ok        https://www.python.org/
    ( pkg_development: line  143) ok        https://www.python.org/dev/peps/pep-0008/
    ( pkg_development: line   93) ok        https://ubc-moad-docs.readthedocs.io/en/latest/ssh_access.html#secureremoteaccess
    ( pkg_development: line  177) ok        https://www.sphinx-doc.org/en/master/
    ( pkg_development: line  177) ok        https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
    ( pkg_development: line   20) ok        https://img.shields.io/github/issues/UBC-MOAD/MoaceanParcels?logo=github
    ( pkg_development: line  171) ok        https://readthedocs.org/projects/moaceanparcels/badge/?version=latest
    build succeeded.

    Look for any errors in the above output or in _build/linkcheck/output.txt

:command:`make linkcheck` is run monthly via a `scheduled GitHub Actions workflow`_

.. _scheduled GitHub Actions workflow: https://github.com/UBC-MOAD/MoaceanParcels/actions?query=workflow=sphinx-linkcheck


.. _MoaceanParcelsRunningTheUnitTests:

Running the Unit Tests
======================

The test suite for the :kbd:`MoaceanParcels` package is in :file:`MoaceanParcels/tests/`.
The `pytest`_ tool is used for test parametrization and as the test runner for the suite.

.. _pytest: https://docs.pytest.org/en/latest/

With your :kbd:`moacean-parcels` development environment activated,
use:

.. code-block:: bash

    (moacean-parcels)$ cd MoaceanParcels/
    (moacean-parcels)$ pytest

to run the test suite.
The output looks something like:

.. code-block:: text

    **add example pytest output**

You can monitor what lines of code the test suite exercises using the
`coverage.py`_ and `pytest-cov`_ tools with the command:

.. _coverage.py: https://coverage.readthedocs.io/en/latest/
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/

.. code-block:: bash

    (moacean-parcels)$ cd MoaceanParcels/
    (moacean-parcels)$ pytest --cov=./

and generate a test coverage report with:

.. code-block:: bash

    (moacean-parcels)$ coverage report

to produce a plain text report,
or

.. code-block:: bash

    (moacean-parcels)$ coverage html

to produce an HTML report that you can view in your browser by opening
:file:`MoaceanParcels/htmlcov/index.html`.


.. _MoaceanParcelsVersionControlRepository:

Version Control Repository
==========================

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/UBC-MOAD/MoaceanParcels
    :alt: Git on GitHub

The :kbd:`MoaceanParcels` package code and documentation source files
are available as a `Git`_ repository at https://github.com/UBC-MOAD/MoaceanParcels.

.. _Git: https://git-scm.com/


.. _MoaceanParcelsIssueTracker:

Issue Tracker
=============

.. image:: https://img.shields.io/github/issues/MIDOSS/WWatch3-Cmd?logo=github
    :target: https://github.com/UBC-MOAD/MoaceanParcels/issues
    :alt: Issue Tracker

Development tasks,
bug reports,
and enhancement ideas are recorded and managed in the issue tracker at
https://github.com/UBC-MOAD/MoaceanParcels/issues.


License
=======

.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0

The code and documentation of the MOAD OceanParcels kernels and utilities project
are copyright 2021 – present by UBC EOAS MOAD Group and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
