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

*****************************************************
How to Add a Kernel to :kbd:`moacean_parcels.kernels`
*****************************************************

In summary,
the steps you need to follow to add a kernel to this package are:

#. Put your kernel function and related particle class code in a module in the
   :file:`MoaceanParcels/moacean_parcels/kernels/` directory.
   Please see :ref:`KernelModules` for details.

#. Register your kernel function and particle class in the
   :file:`MoaceanParcels/moacean_parcels/kernels/__init__.py` file.
   Please see :ref:`KernelAndParticleRegistration` for details.

#. Add your kernel function and particle class to the automatic documentation generator in the
   :file:`MoaceanParcels/docs/kernel_functions.rst` file.
   Please see :ref:`KernelAndParticleAutoDoc` for details.

#. Add a notebook that explain the design of your kernel function and particle class to the
   :file:`MoaceanParcels/docs/kernels/kernel_example_notebooks/particle_behaviour_kernels/`
   directory and :file:`index.html` file therein,
   or the
   :file:`MoaceanParcels/docs/kernels/kernel_example_notebooks/recovery_kernels/` directory
   and :file:`index.html` file.
   Please see :ref:`KernelExampleNotebooks` for details.

The details of what to do and how to do it for each of those steps are provided in the sections 
below:


.. _KernelModules:

Kernel Modules
==============

Coming soon...


.. _KernelAndParticleRegistration:

Kernel Function and Particle Class Registration
===============================================

One of the design goals of this package is to enable kernel functions and particle classes
to be imported from it using clean,
intuitive import statement like:

.. code-block::  python

   from moacean_parcels.kernels import DeleteParticle

To make that possible with the naming convention we have adopted for kernel modules and the  
functions they contain,
it is necessary to "register" kernel functions and particle classes in the
:file:`MoaceanParcels/moacean_parcels/kernels/__init__.py` file.
The :py:func:`moacean_parcels.kernels.DeleteParticle` function is registered with the line:

.. code-block:: python

   from .DeleteParticle import DeleteParticle

That line is using Python relative import syntax to import the function called
:py:func:`~moacean_parcels.kernels.DeleteParticle` from the module called
:py:mod:`moacean_parcels.kernels.DeleteParticle` in the 
:file:`MoaceanParcels/moacean_parcels/kernels/` directory.
It has the effect of putting the :py:func:`~moacean_parcels.kernels.DeleteParticle` function into
the :py:obj:`moacean_parcels.kernels` namespace so that import statement like:

.. code-block::  python

   from moacean_parcels.kernels import DeleteParticle

just work.

If you have defined a particle class in your kernel module,
it also needs to have a registration line in the
:file:`MoaceanParcels/moacean_parcels/kernels/__init__.py` file.
   

.. _KernelAndParticleAutoDoc:

Kernel Function and Particle Class Auto-Documentation
=====================================================

Coming soon...
      

.. _KernelExampleNotebooks:

Kernel Example Notebooks
========================

Coming soon...
   