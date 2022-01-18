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

A kernel module is a :kbd:`.py` file that contains code of your kernel function,
and an associated particle class (if applicable).

Conventions
-----------

* Use one module per kernel.
  :file:`MoaceanParcels/moacean_parcels/kernels/DeleteParticle.py`
  is an example of a kernel module.

* The name of the kernel module is the same as the name of the kernel function it contains.

* `OceanParcels`_ style is to write kernel function names and particle class names in camel-case
  (capitalized words jammed together with no spaces).
  Examples:

  * :py:func:`AdvectionRK4`
  * :py:func:`AdvectionDiffusionM1`
  * :py:func:`DeleteParticle`
  * :py:class:`ScipyParticle`
  * :py:class:`JITParticle`
  * :py:class:`VectorParticle`

  .. _OceanParcels: https://oceanparcels.org/

  Note that this is different to the usual Python convention of using snake-case
  (lower case words separated by underscores)
  for function and module names and camel-case for class names.
  However,
  one of the principle of the `Python style guide`_ is the consistency within
  a project is important.
  So,
  we adopt the OceanParcels style in this package.

  .. _Python style guide: https://www.python.org/dev/peps/pep-0008/


Copyright Notice
-----------------

Please include this copyright notice in a comment block at the top of your module:

.. code-block::

   # Copyright 2021 – present, UBC EOAS MOAD Group and The University of British Columbia
   #
   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at
   #
   #    https://www.apache.org/licenses/LICENSE-2.0
   #
   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.

   # SPDX-License-Identifier: Apache-2.0


Kernel Function Signature
-------------------------

Kernel function definition statements *must* be like:

.. code-block::

   def KernelName(particle, fieldset, time):

That is,
kernel function must accept exactly three arguments.
The conventional names of those arguments are :kbd:`article, fieldset, time`.

As noted above,
the `OceanParcels`_ style is to write kernel function names in camel-case
(capitalized words jammed together with no spaces).


Particle Class Sub-classing
---------------------------

Particle classes must sub-class either :py:class:`parcels.ScipyParticle`:

.. code-block:: python

   class VectorParticle(ScipyParticle):

or :py:class:`parcels.JITParticle`:

.. code-block:: python

   class VectorParticle(JITParticle):

Particle classes that sub-class :py:class:`parcels.JITParticle` generally provide
faster execution.
Those that sub-class :py:class:`parcels.ScipyParticle` are easier to debug so they are generally
faster to develop.
:py:class:`parcels.JITParticle` sub-classes have access to a limited set of Python library modules
while :py:class:`parcels.ScipyParticle` sub-classes are less limited.
A good development strategy may be to start with a :py:class:`parcels.ScipyParticle` sub-class
and then change it to a :py:class:`parcels.JITParticle` once it is debugged and tested.
Please see the `OceanParcels JIT Particles and Scipy particles tutorial`_ for more details.

.. _OceanParcels JIT Particles and Scipy particles tutorial: https://nbviewer.org/github/OceanParcels/parcels/blob/master/parcels/examples/tutorial_jit_vs_scipy.ipynb

Variables defined within particle classes provide the way to pass information
other than :kbd:`fieldset` and :kbd:`time` to a kernel function operating on
a particular particle.

As noted above,
Python and `OceanParcels`_ style is to write particle class names in camel-case
(capitalized words jammed together with no spaces).


.. _KernelFunctionDocstrings:

Kernel Function Docstrings
--------------------------

Docstrings are triple-quoted comment blocks that follow immediately after
function :kbd:`def` statements.
The docstring in your kernel function provides the documentation that is
rendered in the :ref:`MOAD-KernelFunctions` section of these docs
(see :ref:`KernelAndParticleAutoDoc` for details of how that happens).

Your docstring should have for parts:

#. A description of what the kernel does

#. A code example of how to use the kernel

#. A reference to where the :ref:`example notebook <KernelExampleNotebooks>` for your
   kernel is stored

#. Descriptions and type annotations for the three arguments that the kernel function accepts

Here is an example of a complete kernel function docstring:

.. code-block:: python

    """Delete a particle that has been lost during execution
    of the simulation and print its id number as well as information
    about where and when it was lost.

    This kernel is intended for use as an error recovery kernel,
    most likely for the
    :py:exc:`parcels.tools.statuscodes.OutOfBoundsError` or
    :py:exc:`parcels.tools.statuscodes.ThroughSurfaceError`
    error conditions.

    Example usage:

    .. code-block:: python

        from moacean_parcels.kernels import DeleteParticle

        # ...

        pset.execute(
            kernels,
            # ...
            recovery={ErrorCode.ErrorOutOfBounds: DeleteParticle},
            # ...
        )

    For a more detailed usage example,
    please see the example notebook for this kernel in the
    :ref:`RecoveryKernelExampleNotebooks` section.

    :param particle: Particle that has gone out of bounds.
    :type particle: :py:class:`parcels.particle.JITParticle` or
                    :py:class:`parcels.particle.ScipyInteractionParticle`

    :param fieldset: Hydrodynamic fields that is moving the particle.
    :type fieldset: :py:class:`parcels.fieldset.FieldSet`

    :param time: Current time of the particle.
    :type time: :py:attr:`numpy.float64`
    """

.. important:: Indentation is important in docstrings, the same way it is in Python code.

Breaking that down into the four parts:

#. The description of what the kernel does is:

   .. code-block:: restructuredtext

      """Delete a particle that has been lost during execution
      of the simulation and print its id number as well as information
      about where and when it was lost.

      This kernel is intended for use as an error recovery kernel,
      most likely for the
      :py:exc:`parcels.tools.statuscodes.OutOfBoundsError` or
      :py:exc:`parcels.tools.statuscodes.ThroughSurfaceError`
      error conditions.

   This is mostly free text,
   though recovery kernels should probably make reference to the exceptions
   that they provide recovery for as shown here.

#.  The code example of how to use the kernel is mostly a Sphinx :kbd:`code-block` directive
    containing the example code.
    Ellipses in the code block must be marked as comments so that the block is valid Python.
    In the example above,
    the code example part is:

    .. code-block:: restructuredtext

         Example usage:

         .. code-block:: python

            from moacean_parcels.kernels import DeleteParticle

            # ...

            pset.execute(
                kernels,
                # ...
                recovery={ErrorCode.ErrorOutOfBounds: DeleteParticle},
                # ...
            )

#. The reference to where the :ref:`example notebook <KernelExampleNotebooks>` for your
   kernel is stored can be pretty much verbatim:

   .. code-block:: restructuredtext

      For a more detailed usage example,
      please see the example notebook for this kernel in the
      :ref:`RecoveryKernelExampleNotebooks` section.

   For particle behaviour kernels,
   change the reference label to :kbd:`ParticleBehaviourKernelExampleNotebooks`.

#. You can copy and paste the following for the descriptions and type annotations
   of the three arguments that the kernel function accepts:

   .. code-block:: restructuredtext

      :param particle: Particle that has gone out of bounds.
      :type particle: :py:class:`parcels.particle.JITParticle` or
                      :py:class:`parcels.particle.ScipyInteractionParticle`

      :param fieldset: Hydrodynamic fields that is moving the particle.
      :type fieldset: :py:class:`parcels.fieldset.FieldSet`

      :param time: Current time of the particle.
      :type time: :py:attr:`numpy.float64`
      """


Particle Class Documentation
----------------------------

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

We use the `Sphinx autodoc extension`_ pull the documentation for kernel functions
and particle classes from the code docstrings.

.. _Sphinx autodoc extension: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

Provided that you have followed the instruction in the :ref:`KernelModules` section about writing
your docstrings,
adding the documentation of your code to the :ref:`MOAD-KernelFunctions` section is a simple matter
of adding a title and an :kbd:`autofunction` directive to the appropriate section of the
:file:`MoaceanParcels/docs/kernels/kernel_functions.rst` file.
For example:

.. code-block:: restructuredtext

   :py:func:`DeleteParticle`
   -------------------------

   .. autofunction:: moacean_parcels.kernels.DeleteParticle

For a particle class:

* use :kbd:`:py:class:` in the title
* use the :kbd:`autoclass` directive

Please ensure the the underline below your title is at least as long as the title.
It can be longer,
but Sphinx will complain if it is shorter.

If you check the documentation,
either by :ref:`building it locally <MoaceanParcelsBuildingTheDocumentation>`,
or after it has been
`rendered on readthedocs`_,
and find that your kernel or particle class documentation is missing or incomplete,
the likely cause is a reStructuredText syntax error in your docstring.
Check the docstrings of other kernel functions or particle classes or reach out for help on the
:kbd:`#oceanparcels` or :kbd:`#moad-python-notes` Slack channels.

.. _rendered on readthedocs: https://moaceanparcels.readthedocs.io/en/latest/


.. _KernelExampleNotebooks:

Kernel Example Notebooks
========================

We use the `nbsphinx`_ extension for Sphinx to enable Jupyter notebooks to be included as
pages in this documentation.

.. _nbsphinx: https://nbsphinx.readthedocs.io/en/latest/

It is highly recommended that you create a notebook that explains the purpose and features of
your kernels and particle classes,
and provides an example of their use.
To add your notebook to this documentation:

#. Store your notebook in one of the sub-directories of
   :file:`MoaceanParcels/docs/kernels/kernel_example_notebooks/`:

   * :file:`MoaceanParcels/docs/kernels/kernel_example_notebooks/particle_behaviour_kernels/`
     is for particle behaviour kernels and their associated particle classes

   * :file:`MoaceanParcels/docs/kernels/kernel_example_notebooks/recovery_kernels/`
     is for error recovery kernels

   To make it easy for people to find the example notebook associated with a given kernel module
   we use the convention of making the name of the notebook file the same as that of the module
   with :kbd:`-example` appended.
   For example,
   the example notebook for the :file:`MoaceanParcels/moacean_parcels/kernels/DeleteParticle.py`
   recovery kernel is
   :file:`MoaceanParcels/docs/kernels/kernel_example_notebooks/recovery_kernels/DeleteParticle-example.ipynb`.

#. Add the name of your notebook to the :kbd:`toctree` section of the :file:`index.rst` file
   in the directory where you stored it.
   Be sure to include the :kbd:`.ipynb` extension to signal to Sphinx that it should use `nbsphinx`_
   to parse the notebook instead of trying to read it as reStructuredText.
   Example:

   .. code-block:: restructuredtext

      .. toctree::
      :caption: Contents:

      DeleteParticle-example.ipynb

   The title in the first cell of your notebook will be used as the section title in docs
   table of contents.
