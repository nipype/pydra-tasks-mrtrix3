==============================
Pydra task package for mrtrix3
==============================

.. image:: https://github.com/nipype/pydra-tasks-mrtrix3/actions/workflows/ci-cd.yaml/badge.svg
   :target: https://github.com/nipype/pydra-tasks-mrtrix3/actions/workflows/ci-cd.yaml
.. image:: https://codecov.io/gh/nipype/pydra-tasks-mrtrix3/branch/main/graph/badge.svg?token=UIS0OGPST7
   :target: https://codecov.io/gh/nipype/pydra-tasks-mrtrix3
.. image:: https://img.shields.io/pypi/pyversions/pydra-tasks-mrtrix3.svg
   :target: https://pypi.python.org/pypi/pydra-tasks-mrtrix3/
   :alt: Supported Python versions
.. image:: https://img.shields.io/pypi/v/pydra-tasks-mrtrix3.svg
   :target: https://pypi.python.org/pypi/pydra-tasks-mrtrix3/
   :alt: Latest Version


This package contains a collection of Pydra task interfaces for the mrtrix3 toolkit.


Generation of interfaces
------------------------

Task interfaces are automatically generated from the MRtrix3 source code using the
`generate.py` script, with the exception of a few interfaces that are manually
written.

Developer installation
----------------------

First install the package in editable mode

.. code-block::

   $ pip install -e .[test]

This package comes with a battery of automatically generated test modules. They can be launched using

.. code-block::

   $ pytest --doctest-modules pydra/tasks/*
